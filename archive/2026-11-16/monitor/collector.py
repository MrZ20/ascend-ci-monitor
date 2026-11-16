#!/usr/bin/env python3
"""Reconstructed source-read-only collector. An agent services its JSON bridge."""
import argparse,contextlib,datetime as dt,fcntl,json,os,pathlib,re,sqlite3,time,uuid
from urllib.parse import urlencode
from zoneinfo import ZoneInfo
REPO='vllm-project/vllm-ascend'; API='repos/'+REPO; FAIL={'failure','timed_out'}
SCHEMA={'meta':['key','value'],'jobs':['key','collected_day','reviewed','payload'],'runs':['key','collected_day','payload']}
class ReadFailure(RuntimeError):pass
class Busy(RuntimeError):pass
def now():return dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00','Z')
def instant(s):return dt.datetime.fromisoformat(s.replace('Z','+00:00'))
def day(s=None):return instant(s or now()).astimezone(ZoneInfo('Asia/Shanghai')).date().isoformat()
def save(p,v):
 p=pathlib.Path(p);p.parent.mkdir(parents=True,exist_ok=True);t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n');os.replace(t,p)
def capture_id():return 'capture-'+now()[:19].replace(':','').replace('T','-')+'-'+uuid.uuid4().hex[:8]
@contextlib.contextmanager
def round_lock(directory):
 with open(pathlib.Path(directory)/'collector.lock','a') as f:
  try:fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
  except BlockingIOError:raise Busy('collection_active')
  try:yield
  finally:fcntl.flock(f,fcntl.LOCK_UN)
def validate_database(c):
 if c.execute('PRAGMA integrity_check').fetchone()[0]!='ok':raise ReadFailure('database_integrity_failure')
 for table,columns in SCHEMA.items():
  if [r[1] for r in c.execute('PRAGMA table_info('+table+')')]!=columns:raise ReadFailure('database_schema_mismatch')
 if c.execute("SELECT value FROM meta WHERE key='schema_version'").fetchone()!=('1',):raise ReadFailure('database_version_mismatch')
def database(directory):
 p=pathlib.Path(directory)/'collector.sqlite3'
 if p.exists():
  c=sqlite3.connect('file:'+str(p)+'?mode=rw',uri=True)
  try:validate_database(c)
  except Exception:c.close();raise
  return c
 c=sqlite3.connect(p)
 try:
  c.executescript('CREATE TABLE meta(key TEXT PRIMARY KEY,value TEXT); CREATE TABLE jobs(key TEXT PRIMARY KEY,collected_day TEXT NOT NULL,reviewed INTEGER NOT NULL DEFAULT 0,payload TEXT NOT NULL); CREATE TABLE runs(key TEXT PRIMARY KEY,collected_day TEXT NOT NULL,payload TEXT NOT NULL);')
  c.executemany('INSERT INTO meta VALUES(?,?)',[('schema_version','1'),('new_baseline_started_at',now())]);c.commit();return c
 except Exception:c.close();raise

def mark_reviewed(directory,job_keys):
 with round_lock(directory):
  c=database(directory)
  try:
   for key in job_keys:
    row=c.execute('SELECT payload FROM jobs WHERE key=?',(key,)).fetchone()
    if not row or not json.loads(row[0]).get('log_collected'):raise ValueError('not_an_actual_log_sample')
   with c:
    for key in job_keys:c.execute('UPDATE jobs SET reviewed=1 WHERE key=?',(key,))
  finally:c.close()

class Bridge:
 def __init__(self,path,deadline):self.path=path;self.deadline=deadline;self.seq=0
 def __call__(self,req):
  self.seq+=1;save(self.path/'request.json',dict(req,id=self.seq));p=self.path/f'response-{self.seq}.json';until=min(self.deadline,time.monotonic()+120)
  while not p.exists():
   if time.monotonic()>=until:raise ReadFailure('connector_bridge_timeout')
   time.sleep(.05)
  try:r=json.loads(p.read_text())
  except (ValueError,OSError):raise ReadFailure('invalid_bridge_response')
  if not isinstance(r,dict) or r.get('error') or 'body' not in r:raise ReadFailure('connector_error_requires_inspection')
  return r.get('status',200),r.get('headers',{}),r['body']

class Collector:
 def __init__(self,directory,transport,budget=720,sample_limit=20,capture=None,observed=None):
  self.d=pathlib.Path(directory);self.started=observed or now();self.capture=capture or capture_id();self.out=self.d/'data'/day(self.started)/self.capture;self.out.mkdir(parents=True,exist_ok=True)
  self.deadline=time.monotonic()+budget;self.transport=transport;self.limit=min(20,max(0,sample_limit));self.gaps=[];self.http=[];self.pages=[];self.samples=[];self.runs=[];self.candidates=[];self.safety_count=0;self.sample_phase_done=False;self.runs_processed=0
  p=self.d/'exclusions.json'
  try:self.config=json.loads(p.read_text()) if p.exists() else {'rules':[],'recovered':False}
  except (ValueError,OSError):raise ReadFailure('invalid_exclusions_configuration')
  if not isinstance(self.config,dict) or not isinstance(self.config.get('rules',[]),list):raise ReadFailure('invalid_exclusions_configuration')
  for rule in self.config.get('rules',[]):
   if not isinstance(rule,dict) or not rule or any(k not in ('workflow','job','step') or not isinstance(v,str) for k,v in rule.items()):raise ReadFailure('invalid_exact_exclusion')
  self.c=database(self.d)
 def gap(self,key,description):
  v={'gap_id':self.capture+':'+key,'observed_at':now(),'description':description}
  if not any(x['gap_id']==v['gap_id'] for x in self.gaps):self.gaps.append(v);save(self.out/'gaps.json',self.gaps)
 def request(self,req):
  if req.get('op') not in ('get','job_logs'):raise ReadFailure('non_read_operation_rejected')
  for attempt in range(3):
   if time.monotonic()>=self.deadline:raise ReadFailure('round_budget_exhausted')
   try:status,headers,body=self.transport(req)
   except (ConnectionError,TimeoutError):status,headers,body=None,{},''
   self.http.append({'op':req['op'],'path':req.get('path'),'job_id':req.get('job_id'),'attempt':attempt+1,'status':status,'observed_at':now()});save(self.out/'http.json',self.http)
   if isinstance(status,int) and 200<=status<300:return body
   hard=any(x in str(body).lower() for x in ['bad credentials','resource not accessible','requires authentication','organization access','saml','security policy','permission denied','access denied','manual denial','not permitted','insufficient permission'])
   if hard or status not in (None,403,408,425,429,500,502,503,504) or attempt==2:raise ReadFailure('http_failure_'+str(status))
   try:
    h={k.lower():v for k,v in headers.items()};delay=(30,90)[attempt]
    if h.get('retry-after'):
     from email.utils import parsedate_to_datetime
     try:delay=max(delay,float(h['retry-after']))
     except ValueError:delay=max(delay,parsedate_to_datetime(h['retry-after']).timestamp()-time.time())
    if str(h.get('x-ratelimit-remaining'))=='0' and h.get('x-ratelimit-reset'):delay=max(delay,float(h['x-ratelimit-reset'])-time.time())
   except (ValueError,TypeError,AttributeError,OverflowError):raise ReadFailure('invalid_retry_headers')
   if time.monotonic()+delay>=self.deadline:raise ReadFailure('retry_wait_exceeds_budget')
   time.sleep(delay)
 def get(self,path):return self.request({'op':'get','path':path})
 def paged(self,path,field):
  out=[];seen=set()
  for page in range(1,101):
   body=self.get(path+('&' if '?' in path else '?')+urlencode({'per_page':100,'page':page}))
   if not isinstance(body,dict) or not isinstance(body.get(field),list):raise ReadFailure('invalid_page')
   rows=body[field];total=body.get('total_count');ids=[r.get('id') for r in rows if isinstance(r,dict)]
   if len(ids)!=len(rows) or None in ids or len(set(ids))!=len(ids) or any(i in seen for i in ids):raise ReadFailure('duplicate_or_invalid_page')
   seen.update(ids);out+=rows;self.pages.append({'path':path,'page':page,'rows':len(rows)})
   if total is not None and (not isinstance(total,int) or total<0):raise ReadFailure('invalid_total')
   if total is not None and len(out)>=total:return out
   if len(rows)<100:
    if total is not None and len(out)<total:raise ReadFailure('pagination_total_mismatch')
    return out
  raise ReadFailure('pagination_limit')
 def excluded(self,row):
  vals={'workflow':row['run'].get('name'),'job':row['job'].get('name'),'step':row.get('failed_step')}
  return any(all(vals[k]==v for k,v in rule.items()) for rule in self.config.get('rules',[]))
 def sample_key(self,row):
  r,j=row['run'],row['job'];return (r.get('workflow_id'),j.get('name'),row.get('failed_step'),tuple(j.get('labels',[])),(j.get('started_at') or '')[:13])
 def choose(self,rows,limit):
  groups={}
  for row in sorted(rows,key=lambda r:r['job'].get('started_at') or '',reverse=True):groups.setdefault(self.sample_key(row),[]).append(row)
  picked=[]
  while groups and len(picked)<limit:
   for k in list(groups):
    picked.append(groups[k].pop(0))
    if not groups[k]:del groups[k]
    if len(picked)>=limit:break
  return picked
 def fetch_log(self,row):
  body=self.request({'op':'job_logs','repository_full_name':REPO,'job_id':row['job']['id']})
  if isinstance(body,dict):body=body.get('content',body.get('logs',body.get('text')))
  if not isinstance(body,str):raise ReadFailure('invalid_log_response')
  source_day=dt.date.fromisoformat(row['collected_day']).isoformat();root=self.d/'data'/source_day/'samples';root.mkdir(parents=True,exist_ok=True)
  p=root/('job-'+str(row['job']['id'])+'.log');p.write_text(body)
  row=dict(row,log_path=str(p),log_collected=True);save(root/('job-'+str(row['job']['id'])+'.json'),row);self.samples.append(row)
  self.c.execute('UPDATE jobs SET payload=? WHERE key=?',(json.dumps(row),row['key']));self.c.commit();self.save_manifest()
 def anomaly(self,excluded,limit=3):
  selected=[];cutoff=instant(self.started)-dt.timedelta(hours=1);diagnostic=[]
  for wid in sorted({x['run']['workflow_id'] for x in excluded}):
   if len(selected)>=limit:break
   try:
    body=self.get(f'{API}/actions/workflows/{wid}/runs?status=completed&per_page=100&page=1')
    if not isinstance(body,dict) or not isinstance(body.get('workflow_runs'),list):raise ReadFailure('invalid_workflow_status')
    runs=body['workflow_runs'];ids=[r.get('id') for r in runs]
    if len(set(ids))!=len(ids):raise ReadFailure('duplicate_workflow_status')
    # created_at and updated_at are NOT completion timestamps. Never invent
    # completion ordering from either. No historical paging or state machine.
    timed=[]
    for r in runs:
     if not r.get('completed_at'):continue
     try:t=instant(r['completed_at'])
     except (ValueError,TypeError):continue
     if t>instant(self.started):continue
     timed.append((t,r))
    complete=len(timed)==len(runs) and isinstance(body.get('total_count'),int) and len(runs)>=body['total_count']
    ordered=sorted(timed,key=lambda x:x[0],reverse=True)
    a=complete and len(ordered)>=10 and all(r.get('conclusion')=='failure' for _,r in ordered[:10])
    # B covers only observed completed samples, but unknown timestamps can
    # conceal an observed nonfailure in this hour, so any unknown skips B.
    recent=[r for t,r in timed if t>=cutoff]
    b=len(timed)==len(runs) and len(recent)>=2 and all(r.get('conclusion')=='failure' for r in recent)
    diagnostic.append({'workflow_id':wid,'observed_runs':len(runs),'exact_completion_times':len(timed),'A':a,'B':b,'skipped_insufficient_status':not(a or b) and len(timed)<len(runs)})
    if a or b:
     seen=set()
     for row in sorted([r for r in excluded if r['run']['workflow_id']==wid],key=lambda r:r['run'].get('created_at',''),reverse=True):
      if row['run']['id'] in seen:continue
      selected.append(dict(row,anomaly_trigger='A' if a else 'B'));seen.add(row['run']['id'])
      if len(selected)>=limit:break
   except ReadFailure:self.gap('anomaly-'+str(wid),'可选 Workflow 异常状态查询未完成；正常采集继续。')
  save(self.out/'anomaly-diagnostics.json',diagnostic);return selected
 def collect(self):
  if not self.config.get('recovered'):self.gap('missing-exclusion-policy','原精确排除配置未恢复，未虚构旧排除。恢复期最多20份普通日志及额外最多3份必要测试日志；不是V3.2异常触发。')
  cutoff=(instant(self.started)-dt.timedelta(hours=24)).isoformat().replace('+00:00','Z')
  try:
   byid={}
   for status in ('failure','timed_out'):
    for r in self.paged(f'{API}/actions/runs?'+urlencode({'status':status,'created':'>='+cutoff}),'workflow_runs'):byid[r['id']]=r
   self.runs=sorted(byid.values(),key=lambda r:r.get('created_at',''),reverse=True)
  except ReadFailure as e:self.gap('run-discovery','过去24小时失败运行发现/分页未完成：'+str(e));return self.finish()
  save(self.out/'discovered-runs.json',[{'id':r['id'],'run_attempt':r.get('run_attempt',1),'head_sha':r.get('head_sha')} for r in self.runs])
  for run in self.runs:
   if time.monotonic()+180>=self.deadline:self.gap('jobs-budget-reserve','Jobs采集提前终止，为有限日志保留最多180秒；剩余运行未覆盖。');break
   k=f"{run['id']}:{run.get('run_attempt',1)}"
   if self.c.execute('SELECT 1 FROM runs WHERE key=?',(k,)).fetchone():continue
   try:
    jobs=self.paged(f"{API}/actions/runs/{run['id']}/attempts/{run.get('run_attempt',1)}/jobs",'jobs');fresh=self.get(f"{API}/actions/runs/{run['id']}")
    if fresh.get('run_attempt',1)!=run.get('run_attempt',1) or fresh.get('head_sha')!=run.get('head_sha'):raise ReadFailure('run_changed_during_collection')
    with self.c:
     for job in jobs:
      if job.get('conclusion') not in FAIL:continue
      failed=[s['name'] for s in job.get('steps',[]) if s.get('conclusion') in FAIL]
      row={'key':k+':'+str(job['id']),'run':run,'job':job,'failed_step':failed[0] if failed else None,'collected_day':day(self.started),'log_collected':False}
      self.c.execute('INSERT OR IGNORE INTO jobs(key,collected_day,payload) VALUES(?,?,?)',(row['key'],row['collected_day'],json.dumps(row)))
     self.c.execute('INSERT OR IGNORE INTO runs VALUES(?,?,?)',(k,day(self.started),json.dumps(run)))
   except ReadFailure as e:self.gap('jobs-'+k,'运行 '+k+' Jobs/复核未完成：'+str(e))
   self.runs_processed+=1
   save(self.out/'coverage-progress.json',{'observed_at':now(),'runs_discovered':len(self.runs),'runs_processed_this_round':self.runs_processed,'samples_persisted':len(self.samples),'complete':False})
   if not self.sample_phase_done:
    rows=[json.loads(r[0]) for r in self.c.execute('SELECT payload FROM jobs WHERE reviewed=0')]
    groups={self.sample_key(r) for r in rows if (r.get('failed_step') or '')!='Stream logs' and not self.excluded(r) and not (not self.config.get('recovered') and re.search(r'\b(pytest|tests?|benchmark|accuracy|performance)\b',r.get('failed_step') or '',re.I))}
    if len(groups)>=self.limit or self.runs_processed>=40:self.collect_samples();self.sample_phase_done=True
  if not self.sample_phase_done:self.collect_samples()
  return self.finish()
 def collect_samples(self):
  self.candidates=[json.loads(r[0]) for r in self.c.execute('SELECT payload FROM jobs WHERE reviewed=0')];normal=[];excluded=[];safety=[]
  save(self.out/'sampling-scope.json',{'observed_at':now(),'runs_discovered':len(self.runs),'runs_processed_before_sampling':self.runs_processed,'candidate_jobs_at_sampling':len(self.candidates),'policy':'Bounded grouping over jobs available at sampling time; remaining run jobs continue after logs. Unread group jobs are not verified.'})
  for row in self.candidates:
   step=row.get('failed_step') or ''
   if step=='Stream logs':continue
   if self.excluded(row):excluded.append(row);continue
   if not self.config.get('recovered') and re.search(r'\b(pytest|tests?|benchmark|accuracy|performance)\b',step,re.I):safety.append(row);continue
   normal.append(row)
  chosen=self.choose(normal,self.limit);extras=self.anomaly(excluded) if excluded else []
  # Reconstruction-only bounded exception, not a broad saved exclusion and not
  # an anomaly claim. Extras share the total cap of three, never displace 20.
  extras+= [dict(r,recovery_test_exception=True) for r in self.choose(safety,3-len(extras))];chosen+=extras;self.safety_count=max(0,len(safety)-sum(bool(r.get('recovery_test_exception')) for r in extras))
  for row in chosen:
   if row.get('log_collected') and pathlib.Path(row.get('log_path','')).is_file():self.samples.append(row);continue
   try:self.fetch_log(row)
   except ReadFailure as e:self.gap('log-'+row['key'],'Job '+str(row['job']['id'])+' 日志未获取：'+str(e))
  self.save_manifest()
 def save_manifest(self):
  # Capture manifest references original-day sample records, never copies old
  # full payload/log into today's retention directory.
  manifest=[]
  for row in self.samples:
   p=self.d/'data'/row['collected_day']/'samples'/('job-'+str(row['job']['id'])+'.json')
   save(p,row);manifest.append({'key':row['key'],'collected_day':row['collected_day'],'sample_path':str(p)})
  save(self.out/'samples.json',manifest)
 def finish(self):
  self.save_manifest();save(self.out/'gaps.json',self.gaps);save(self.out/'pages.json',self.pages)
  result={'capture_id':self.capture,'observed_at':self.started,'collected_day':day(self.started),'status':'partial' if self.gaps else 'collected','runs_observed':len(self.runs),'unreviewed_candidates':len(self.candidates),'samples':len(self.samples),'safety_deferred':self.safety_count,'samples_file':str(self.out/'samples.json'),'coverage_gaps_file':str(self.out/'gaps.json'),'new_baseline_started_at':self.c.execute("SELECT value FROM meta WHERE key='new_baseline_started_at'").fetchone()[0],'limitations':['仅过去24小时创建的运行，旧运行重跑可能遗漏。','有限分层抽样，未读取Job不当已核实。','连接器无HTTP Link/限流响应头；按total_count及末页分页。','异常规则无确切完成时间时跳过，不用创建/更新时间冒充。']}
  save(self.out/'result.json',result);self.c.close();return result

def main(argv=None):
 p=argparse.ArgumentParser();p.add_argument('command',choices=['collect']);p.add_argument('--directory',default=str(pathlib.Path(__file__).parent));p.add_argument('--sample-limit',type=int,default=20);p.add_argument('--budget-seconds',type=int,default=720);a=p.parse_args(argv);d=pathlib.Path(a.directory);d.mkdir(parents=True,exist_ok=True);cap=capture_id();started=now();out=d/'data'/day(started)/cap
 try:
  with round_lock(d):
   try:c=Collector(d,None,a.budget_seconds,a.sample_limit,cap,started)
   except Exception as e:
    gap={'gap_id':cap+':startup','observed_at':started,'description':'采集启动失败：'+type(e).__name__+'；未重建已有数据库。'}
    save(out/'gaps.json',[gap]);result={'capture_id':cap,'status':'blocked','coverage_gaps_file':str(out/'gaps.json'),'reason':'collector_startup_failed'};save(out/'result.json',result);save(out/'done.json',{'done':True});print(json.dumps(result));return 1
   c.transport=Bridge(c.out,c.deadline);print(json.dumps({'bridge':str(c.out),'capture_id':c.capture}),flush=True)
   try:result=c.collect()
   except Exception as e:c.gap('unexpected','采集未完成，错误类型 '+type(e).__name__+'；未视为零故障。');result=c.finish()
   save(c.out/'done.json',{'done':True});print(json.dumps(result,ensure_ascii=False),flush=True);return 0 if result['status']=='collected' else 1
 except Busy:print(json.dumps({'skipped':'collection_active'}));return 2
if __name__=='__main__':raise SystemExit(main())
