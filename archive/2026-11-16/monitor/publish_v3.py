#!/usr/bin/env python3
"""V3.2 reconstructed target-only publisher; connector bridge keeps credentials external."""
import argparse,contextlib,datetime as dt,fcntl,hashlib,json,pathlib,re,time,uuid
from zoneinfo import ZoneInfo
TARGET='MrZ20/ascend-ci-monitor'
CANONICAL={'v31:infra:main_shared:runner.temp_script_missing','v31:infra:main_shared:kubernetes.kubelet_exec_timeout'}
CATS=[('infra','infra','基础设施'),('insufficient_evidence','unknown','证据不足'),('pr_caused','pr','PR 导致'),('other_non_infra','other','其他')]
JOB=re.compile(r'https://github\.com/vllm-project/vllm-ascend/actions/runs/\d+/job/\d+');SHA=re.compile(r'^[0-9a-f]{40}$')
class PublishError(Exception):pass
def now():return dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00','Z')
def stamp(s):return dt.datetime.fromisoformat(s.replace('Z','+00:00'))
def day_for(s):return (stamp(s).astimezone(ZoneInfo('Asia/Shanghai'))-dt.timedelta(hours=9)).date().isoformat()
def display(s):return stamp(s).astimezone(ZoneInfo('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')+'（上海）' if s else '未知'
def key(s):return s if re.fullmatch('[0-9a-f]{64}',s) else hashlib.sha256(s.encode()).hexdigest()
def save(p,v):
 p=pathlib.Path(p);p.parent.mkdir(parents=True,exist_ok=True);q=p.with_suffix(p.suffix+'.tmp');q.write_text(json.dumps(v,ensure_ascii=False,indent=2));q.replace(p)
def safe(s):
 patterns=[r'(?i)\b(?:gh[pousr]_[a-zA-Z0-9]{15,}|github_pat_[a-zA-Z0-9_]{15,})',r'-----BEGIN [A-Z ]*PRIVATE KEY-----',r'(?im)^\s*Authorization\s*:',r'https?://[^\s/@:]+:[^\s/@]+@',r'(?i)[?&](?:access_token|token|password|client_secret|signature|sig|x-amz-signature)=[^\s&]+',r'(?i)\b(?:password|client_secret|api_key)\s*[:=]\s*["\']?[^\s"\']{8,}']
 if any(re.search(p,s) for p in patterns):raise PublishError('public_secret_scan_blocked')
 return s

def jobs(f):
 out={}
 for j in f['verified_jobs']:
  j={'job_url':j} if isinstance(j,str) else j;u=j.get('job_url') or j.get('url');t=j.get('first_error_at')
  if not u or not JOB.fullmatch(u):raise PublishError('invalid_verified_job_url')
  if t:stamp(t)
  if u not in out or (t and (not out[u] or t<out[u])):out[u]=t
 return out

def validate(f):
 for n in ['fingerprint','classification','cause','first_error_at','job_url','verified_jobs','evidence','raw_error','collected_day','discovered_at']:
  if n not in f:raise PublishError('missing_finding_'+n)
 if f['classification'] not in [c[0] for c in CATS]:raise PublishError('invalid_classification')
 if not f['cause'] or not f['evidence'] or not f['raw_error']:raise PublishError('empty_evidence')
 if len(f['raw_error'])>24000:raise PublishError('excerpt_too_large')
 js=jobs(f)
 if not js or f['job_url'] not in js:raise PublishError('representative_not_verified')
 if f['first_error_at']:stamp(f['first_error_at'])
 dt.date.fromisoformat(f['collected_day']);stamp(f['discovered_at'])
 if f['classification'] in ('infra','pr_caused'):
  cc=f.get('causation_checks');by={x.get('job_url'):x for x in cc} if isinstance(cc,list) else {}
  for u in js:
   c=by.get(u,{});b=c.get('main_baseline',{})
   if not SHA.fullmatch(str(b.get('sha',''))) or not b.get('evidence') or not b.get('relationship'):raise PublishError('missing_exact_main_baseline')
   for n in ['failure_sha','workflow_ref','runner','evidence']:
    if not c.get(n):raise PublishError('missing_causation_'+n)
   if not SHA.fullmatch(c['failure_sha']):raise PublishError('invalid_failure_sha')
  if f['classification']=='pr_caused' and not f.get('pr_evidence'):raise PublishError('missing_pr_evidence')
 safe(json.dumps(f,ensure_ascii=False));return f

def parse(text):
 entries={};aliases={};gaps={};bounds=list(re.finditer(r'<a id="(infra|unknown|pr|other)"></a>',text));cmap={x[1]:x[0] for x in CATS}
 for i,b in enumerate(bounds):
  block=text[b.end():bounds[i+1].start() if i+1<len(bounds) else len(text)];ms=list(re.finditer(r'^### (F-\d+)\s*$',block,re.M))
  for k,m in enumerate(ms):
   raw=block[m.start():ms[k+1].start() if k+1<len(ms) else len(block)];end=raw.rfind('\n---')
   if end>=0:raw=raw[:end+4]
   meta=re.search(r'<!-- finding (F-\d+) key=(\S+) discovered=(\S+) source=(\S+) -->',raw)
   if not meta:raise PublishError('unrecognized_remote_finding')
   fid,fp,discovered,source=meta.groups()
   if fp in entries or any(x['id']==fid for x in entries.values()):raise PublishError('remote_identity_conflict')
   first=re.search(r'<!-- first-error finding='+fid+r' at=(\S+) -->',raw);times={jid:t for jid,t in re.findall(r'<!-- job-time finding='+fid+r' job=(\d+) at=(\S+) -->',raw)}
   entries[fp]={'id':fid,'key':fp,'discovered':discovered,'source':source,'first_error_at':first[1] if first else None,'jobs':{u:times.get(u.rsplit('/',1)[1]) for u in set(JOB.findall(raw))},'classification':cmap[b[1]],'raw':raw.strip()}
 for primary,fp in re.findall(r'<!-- fingerprint-alias primary=(F-\d+) key=([a-f0-9]+) -->',text):
  target=next((k for k,v in entries.items() if v['id']==primary),None)
  if not target:raise PublishError('orphan_alias')
  if fp in aliases and aliases[fp]!=target:raise PublishError('alias_conflict')
  aliases[fp]=target
 for fp,at,desc in re.findall(r'<!-- coverage-gap key=(\S+) observed=(\S+) -->\s*\n- ([^\n]+)',text):gaps[fp]={'gap_id':fp,'observed_at':at,'description':desc,'rendered':True}
 if re.search(r'<!-- finding ',text) and not entries:raise PublishError('unrecognized_remote_report')
 return entries,aliases,gaps

def fenced(s):
 fence='`'*max(3,1+max([len(x) for x in re.findall(r'`+',s)]+[0]));return fence+'text\n'+s.rstrip()+'\n'+fence
def evidence_text(f):
 es=f['evidence'] if isinstance(f['evidence'],list) else [f['evidence']];out=['**原因分析**','',f['cause'],'','**证据与基线**','']
 out+=['- '+(e if isinstance(e,str) else json.dumps(e,ensure_ascii=False)) for e in es]
 if f.get('pr_evidence'):out+=['','PR 证据：'+json.dumps(f['pr_evidence'],ensure_ascii=False)]
 for c in f.get('causation_checks',[]):out+=['','逐 Job 因果核对：'+json.dumps(c,ensure_ascii=False)]
 return '\n'.join(out)
def jobs_block(e):
 out=[f'<details>\n<summary>所有 Job（{len(e["jobs"])}）</summary>','']
 out+=['- '+u+' · 首次报错：'+display(t) for u,t in sorted(e['jobs'].items(),key=lambda x:(x[1] is None,x[1] or '',x[0]))]
 return '\n'.join(out+['','</details>'])
def new_raw(e,f):
 out=[f"### {e['id']}",'',f"<!-- finding {e['id']} key={e['key']} discovered={e['discovered']} source={e['source']} -->"]
 if e['first_error_at']:out += [f"<!-- first-error finding={e['id']} at={e['first_error_at']} -->"]
 out += [f"<!-- job-time finding={e['id']} job={u.rsplit('/',1)[1]} at={t} -->" for u,t in e['jobs'].items() if t]
 out+=['','**关键原始错误**','',fenced(f['raw_error']),'',evidence_text(f),'',f"- **首次报错：** {display(e['first_error_at'])}",f"- **已核实 Job：** {len(e['jobs'])} 个",'- **代表 Job：** '+f['job_url'],'',jobs_block(e),'','---'];return '\n'.join(out)

def merge(text,findings,coverage,at):
 entries,aliases,gaps=parse(text);new=0
 for f in findings:
  validate(f);fp=key(f['fingerprint']);fp=aliases.get(fp,fp)
  if fp not in entries:
   num=max([int(v['id'][2:]) for v in entries.values()]+[0])+1;e={'id':f'F-{num:03d}','key':fp,'discovered':f['discovered_at'],'source':f['collected_day'],'first_error_at':f['first_error_at'],'jobs':jobs(f),'classification':f['classification']};e['raw']=new_raw(e,f);entries[fp]=e;new+=1
  else:
   e=entries[fp];raw=e['raw'];added=jobs(f);known=e['jobs']
   changed=any(u not in known or (t and (not known[u] or t<known[u])) for u,t in added.items()) or f['classification']!=e['classification'] or f['cause'] not in raw or f['raw_error'].rstrip() not in raw
   if not changed:continue
   for u,t in added.items():
    if u not in known or (t and (not known[u] or t<known[u])):known[u]=t
   ts=[t for t in known.values() if t];e['first_error_at']=min(ts) if ts else e['first_error_at'];e['classification']=f['classification']
   raw=re.sub(r'<details>\s*<summary>所有 Job（\d+）</summary>.*?</details>',lambda m:jobs_block(e),raw,flags=re.S);raw=re.sub(r'\*\*已核实 Job：\*\* \d+ 个',f"**已核实 Job：** {len(known)} 个",raw)
   if e['first_error_at']:
    meta=f"<!-- first-error finding={e['id']} at={e['first_error_at']} -->";pat=r'<!-- first-error finding='+e['id']+r' at=\S+ -->'
    raw=re.sub(pat,meta,raw) if re.search(pat,raw) else raw.replace('\n\n**关键原始错误**','\n'+meta+'\n\n**关键原始错误**',1)
    raw=re.sub(r'- \*\*首次报错：\*\* [^\n]+','- **首次报错：** '+display(e['first_error_at']),raw);earliest=min((t,u) for u,t in known.items() if t);raw=re.sub(r'- \*\*代表 Job：\*\* [^\n]+','- **代表 Job：** '+earliest[1],raw)
   extra='\n\n**本轮补充核实（保留以上历史证据）**\n\n'+fenced(f['raw_error'])+'\n\n'+evidence_text(f)+'\n';extra+='\n'.join(f"<!-- job-time finding={e['id']} job={u.rsplit('/',1)[1]} at={t} -->" for u,t in added.items() if t);e['raw']=raw.rstrip().removesuffix('---').rstrip()+extra+'\n\n---'
 for g in coverage:
  if not all(g.get(x) for x in ['gap_id','observed_at','description']):raise PublishError('invalid_gap')
  stamp(g['observed_at']);safe(g['description']);gaps.setdefault(key(g['gap_id']),g)
 return entries,aliases,gaps,new

def render(day,entries,aliases,gaps,at,note,finalized=False):
 end=(dt.date.fromisoformat(day)+dt.timedelta(days=1)).isoformat();n=len(set(u for e in entries.values() for u in e['jobs']))
 out=[f'# vllm-ascend CI 监测 · {day}','',f'<!-- monitor-v3 day={day} updated={at} finalized={int(finalized)} format=3.2 -->',f'**统计窗口：** {day} 09:00 ~ {end} 09:00（上海）','',f'**最近巡检：** {display(at)}','',f'**本日分析：** {n} 个唯一 Job','',' · '.join(f'[{label}（{sum(e["classification"]==cat for e in entries.values())}）](#{anchor})' for cat,anchor,label in CATS),'','---','']
 if gaps:
  out+=['**覆盖缺口：**','']
  for fp,g in sorted(gaps.items(),key=lambda x:x[1]['observed_at']):out += [f'<!-- coverage-gap key={fp} observed={g["observed_at"]} -->','- '+(g['description'] if g.get('rendered') else display(g['observed_at'])+'：'+g['description']),'']
 for cat,anchor,label in CATS:
  es=sorted([e for e in entries.values() if e['classification']==cat],key=lambda e:(not e['first_error_at'],e['first_error_at'] or '',e['id']));out += [f'<a id="{anchor}"></a>','', '<details open>' if cat=='infra' else '<details>',f'<summary><strong>{label}（{len(es)}）</strong></summary>','']
  for e in es:out += [e['raw'],'']
  out += ['</details>','']
 for fp,target in sorted(aliases.items()):out += [f'<!-- fingerprint-alias primary={entries[target]["id"]} key={fp} -->']
 out+=['','本报告为分层抽样，不代表所有 CI 或 main 全部健康；仅发现过去 24 小时创建的失败运行，旧创建运行重跑可能遗漏。','',safe(note),'',f'更新时间：{display(at)}',''];return safe('\n'.join(out))

class Bridge:
 def __init__(self,d):self.path=pathlib.Path(d)/('publish-bridge-'+uuid.uuid4().hex);self.path.mkdir();self.seq=0;print(json.dumps({'bridge':str(self.path)}),flush=True)
 def __call__(self,op,payload):
  self.seq+=1;save(self.path/'request.json',{'id':self.seq,'operation':op,'payload':payload});p=self.path/f'response-{self.seq}.json';deadline=time.monotonic()+180
  while not p.exists():
   if time.monotonic()>deadline:raise PublishError('connector_bridge_timeout_'+op)
   time.sleep(.1)
  r=json.loads(p.read_text())
  if r.get('error'):raise PublishError('connector_'+op+'_failed')
  return r.get('body',r)
@contextlib.contextmanager
def lock(d):
 p=pathlib.Path(d)/'collector.lock';p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('a') as f:
  try:fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
  except BlockingIOError:raise PublishError('collection_active')
  yield

def publish(directory,findings,round_id,note,coverage_gaps,transport,at=None):
 at=at or now();today=day_for(at)
 with lock(directory):
  for f in findings:validate(f)
  days={today}|{day_for(f['discovered_at']) for f in findings}|{day_for(g['observed_at']) for g in coverage_gaps};required=['README.md']+[f'reports/{d[:4]}/{d[5:7]}/{d}.md' for d in sorted(days)]
  intent_path=pathlib.Path(directory)/'publication-intent.json'
  if intent_path.exists():
   old=json.loads(intent_path.read_text())
   if old.get('status')=='outcome_unknown':required=list(set(required)|set(old['files']))
  snap=transport('target_snapshot',{'repository':TARGET,'branch':'main','required_paths':required})
  if not SHA.fullmatch(snap.get('commit','')):raise PublishError('invalid_remote_head')
  if snap.get('repository')!=TARGET or snap.get('public') is not True or snap.get('branch')!='main':raise PublishError('target_identity_or_visibility_unverified')
  files=snap.get('files',{});manifest=snap.get('manifest');absent=snap.get('absent_paths',[])
  if snap.get('complete') is not True or not isinstance(manifest,list) or set(manifest)!=set(files):raise PublishError('snapshot_incomplete')
  if any(p not in files and p not in absent for p in required):raise PublishError('required_path_not_read_or_absence_unverified')
  if set(files)&set(absent):raise PublishError('snapshot_presence_conflict')
  historical={}
  for path,content in files.items():
   if path.startswith('reports/'):
    for fp,e in parse(content)[0].items():historical.setdefault(fp,[]).append(e)
  for f in findings:
   if f['fingerprint'] in CANONICAL:
    matches=historical.get(key(f['fingerprint']),[])
    if not matches or any(e['classification']!='infra' for e in matches):raise PublishError('canonical_identity_not_verified')
  if intent_path.exists():
   previous=json.loads(intent_path.read_text())
   if previous.get('status')=='outcome_unknown':
    if all(files.get(p)==t for p,t in previous['files'].items()):
     previous.update(status='verified_from_remote',commit=snap['commit']);save(intent_path,previous)
     if previous.get('round_id')==round_id:
      result={'status':'published','commit':snap['commit'],'new_findings':previous.get('new_findings',0),'round_id':round_id};save(pathlib.Path(directory)/'last_publication.json',result);return result
    else:raise PublishError('previous_write_outcome_unknown_requires_remote_history_check')
  changes={};totalnew=0;by={today:[]};gapby={}
  for f in findings:by.setdefault(day_for(f['discovered_at']),[]).append(f)
  for g in coverage_gaps:gapby.setdefault(day_for(g['observed_at']),[]).append(g);by.setdefault(day_for(g['observed_at']),[])
  for day,fs in by.items():
   path=f'reports/{day[:4]}/{day[5:7]}/{day}.md';e,a,g,n=merge(files.get(path,''),fs,gapby.get(day,[]),at);totalnew+=n;changes[path]=render(day,e,a,g,at,note if day==today else '历史覆盖缺口补记。',day<today)
  for path,text in files.items():
   m=re.match(r'reports/\d{4}/\d{2}/(\d{4}-\d{2}-\d{2})\.md$',path)
   if m and m[1]<today and 'finalized=0' in text and path not in changes:changes[path]=text.replace('finalized=0','finalized=1',1)
  link=f'reports/{today[:4]}/{today[5:7]}/{today}.md';readme=files.get('README.md','');marker='<!-- latest-report:start -->';end='<!-- latest-report:end -->';block=f'{marker}\n最新日报：[上海统计日 {today}]({link})\n{end}'
  readme=re.sub(re.escape(marker)+'.*?'+re.escape(end),lambda m:block,readme,flags=re.S) if marker in readme and end in readme else block+'\n\n'+readme;changes['README.md']=readme
  for path,text in changes.items():
   if path!='README.md' and not re.fullmatch(r'reports/\d{4}/\d{2}/\d{4}-\d{2}-\d{2}\.md',path):raise PublishError('path_not_allowed')
   safe(text)
  plan={'repository':TARGET,'branch':'main','expected_sha':snap['commit'],'files':changes,'message':f'CI report: {totalnew} new findings ({round_id})'};save(pathlib.Path(directory)/'publication-plan.json',plan);save(intent_path,dict(status='outcome_unknown',round_id=round_id,expected_sha=snap['commit'],files=changes,new_findings=totalnew,prepared_at=at))
  r=transport('target_commit',plan);commit=r.get('commit')
  if not commit or not SHA.fullmatch(commit):raise PublishError('commit_outcome_uncertain')
  v=transport('target_verify',{'repository':TARGET,'branch':'main','commit':commit,'files':changes})
  if not v.get('verified') or v.get('remote_commit')!=commit:raise PublishError('remote_readback_unverified')
  save(intent_path,{'status':'verified','round_id':round_id,'commit':commit});result={'status':'published','commit':commit,'new_findings':totalnew,'round_id':round_id};save(pathlib.Path(directory)/'last_publication.json',result);return result

def main():
 p=argparse.ArgumentParser();p.add_argument('--directory',required=True);p.add_argument('--findings',required=True);p.add_argument('--round-id',required=True);p.add_argument('--note',default='');p.add_argument('--coverage-gaps');p.add_argument('--credential-file',help='Compatibility only; connector credentials stay external.');a=p.parse_args()
 try:
  fs=json.loads(pathlib.Path(a.findings).read_text());gs=json.loads(pathlib.Path(a.coverage_gaps).read_text()) if a.coverage_gaps else [];print(json.dumps(publish(a.directory,fs,a.round_id,a.note,gs,Bridge(a.directory))))
 except Exception as e:print(json.dumps({'status':'blocked','reason':str(e) if isinstance(e,PublishError) else type(e).__name__}));raise SystemExit(1)
if __name__=='__main__':main()
