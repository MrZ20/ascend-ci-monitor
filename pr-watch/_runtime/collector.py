"""Read-only incremental PR Watch collector. An Agent must service its file queue.

No direct network, credentials, job logs, PR writes or report publishing here.
"""
from __future__ import annotations
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone, timedelta
import fcntl
import json
import os
from pathlib import Path
import re
import time
import uuid
from urllib.parse import urlencode, urlsplit
from engine import WatchDB, aggregate_ci, iso, instant

REPO='vllm-project/vllm-ascend'
ROOT=f'https://api.github.com/repos/{REPO}'

class CoverageError(RuntimeError): pass
class BudgetError(CoverageError): pass


def atomic_json(path, value):
    path=Path(path);path.parent.mkdir(parents=True, exist_ok=True)
    tmp=path.with_name(path.name+'.tmp-'+uuid.uuid4().hex)
    tmp.write_text(json.dumps(value, ensure_ascii=False))
    os.replace(tmp,path)

@contextmanager
def round_lock(directory):
    directory=Path(directory);directory.mkdir(parents=True,exist_ok=True)
    with open(directory/'watch.lock','a+') as lock:
        try: fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError: raise CoverageError('another PR Watch phase is active')
        try: yield
        finally: fcntl.flock(lock,fcntl.LOCK_UN)


def safe_url(url):
    u=urlsplit(url)
    prefix=f'/repos/{REPO}/'
    if u.scheme!='https' or u.netloc!='api.github.com' or not u.path.startswith(prefix):
        raise ValueError('source GET outside allowlist')
    rel=u.path[len(prefix):]
    if not (re.fullmatch(r'pulls(?:/\d+(?:/files)?)?',rel) or
            re.fullmatch(r'commits/[A-Za-z0-9._-]+(?:/(?:check-runs|status))?',rel) or
            re.fullmatch(r'git/commits/[A-Za-z0-9._-]+',rel) or
            re.fullmatch(r'issues/\d+/timeline',rel) or rel=='actions/runs'):
        raise ValueError('source GET endpoint outside allowlist')
    return url


def is_transient(response):
    status=response.get('status')
    error=str(response.get('error','')).lower()
    prohibited=('bad credentials','expired credential','permission denied','resource not accessible','organization access','saml','security policy','human denial','invalid credential')
    if any(w in error for w in prohibited): return False
    return status in (429,500,502,503,504) or (status==403) or any(w in error for w in ('temporary','timeout','connection reset','network error'))

class Bridge:
    def __init__(self, queue, budget_seconds=720, request_timeout=90):
        self.queue=Path(queue);self.queue.mkdir(parents=True,exist_ok=True)
        self.budget_seconds=budget_seconds
        self.deadline=time.monotonic()+budget_seconds
        self.phase_deadline=None
        self.request_timeout=request_timeout
        self.metrics={'rest_requests':0,'requests_queued':0,'graphql_queries':0,'graphql_cost':None,'response_bytes':0,'file_list_bytes':0}
        self.events=[]
    def left(self):
        return min(self.deadline,self.phase_deadline if self.phase_deadline is not None else float('inf'))-time.monotonic()
    def get(self,url):
        safe_url(url)
        for attempt in range(3):
            if self.left()<=0: raise BudgetError('round time budget exhausted')
            seq=self.metrics['requests_queued']+1
            self.metrics['requests_queued']=seq
            request=self.queue/f'request-{seq:06d}.json';response=self.queue/f'response-{seq:06d}.json'
            atomic_json(request,{'id':seq,'method':'GET','url':url,'requested_at':iso(),'expires_at_epoch':time.time()+min(self.request_timeout,self.left())})
            until=time.monotonic()+min(self.request_timeout,self.left())
            while not response.exists():
                if time.monotonic()>=until:
                    # A queued request is not proof of an actual GitHub attempt.
                    marker=self.queue/f'dispatch-{seq:06d}.json'
                    if marker.exists():
                        dispatched=json.loads(marker.read_text())
                        if dispatched.get('id')==seq and dispatched.get('attempted') is True:self.metrics['rest_requests']+=1
                    raise BudgetError('connector response not received before request/phase deadline')
                time.sleep(.15)
            data=json.loads(response.read_text())
            if data.get('id',seq)!=seq: raise CoverageError('bridge response ID mismatch')
            if data.get('attempted',True):self.metrics['rest_requests']+=1
            self.metrics['response_bytes']+=response.stat().st_size
            if '/files?' in url:self.metrics['file_list_bytes']+=response.stat().st_size
            # Raw API responses and unrelated patches are transient, never persistent caches.
            response.unlink();request.unlink(missing_ok=True)
            (self.queue/f'dispatch-{seq:06d}.json').unlink(missing_ok=True)
            if data.get('budget_expired') and not data.get('attempted',True):
                raise BudgetError('Agent skipped an expired undispatched GET')
            if data.get('ok'):
                return data['data']
            status=data.get('status');error=str(data.get('error','connector GET failed'))[:300]
            self.events.append({'at':iso(),'url':url,'status':status,'attempt':attempt+1,'error':error})
            if attempt==2 or not is_transient(data):raise CoverageError(f'GET failed: HTTP {status or "unknown"}; {error}')
            delay=(30,90)[attempt]
            delay=max(delay,float(data.get('retry_after_seconds') or 0))
            reset=data.get('rate_reset_epoch')
            if reset:delay=max(delay,float(reset)-time.time())
            if delay>=self.left():raise BudgetError('retry delay exceeds remaining round budget')
            time.sleep(delay)
        raise AssertionError('unreachable')


def pages(api,path,key=None,cap=200):
    out=[]
    for page in range(1,cap+1):
        sep='&' if '?' in path else '?'
        data=api.get(f'{ROOT}/{path}{sep}per_page=100&page={page}')
        values=data[key] if key else data
        if not isinstance(values,list):raise CoverageError('unexpected paginated response')
        out.extend(values)
        if len(values)<100:return out
    raise CoverageError(f'pagination limit reached: {path.split("?")[0]}')


def strip_files(files):
    return [{k:f[k] for k in ('filename','previous_filename','status','additions','deletions','changes') if k in f} for f in files]


def check_run_id(check):
    m=re.search(r'/actions/runs/(\d+)',check.get('details_url') or '')
    return int(m.group(1)) if m else None


def latest_checks(checks,runs):
    """Select latest logical check per workflow/app/name, retaining different workflows.

    A run index supplies workflow identity. Missing identity on duplicates is explicitly
    marked uncertain rather than treating old cancelled checks as current failure.
    """
    by_id={int(r['id']):r for r in runs}
    groups={};ambiguous=False
    for c in checks:
        rid=check_run_id(c);run=by_id.get(rid)
        app=(c.get('app') or {}).get('id') or (c.get('app') or {}).get('slug') or 'unknown'
        workflow=run.get('workflow_id') or run.get('path') if run else None
        if workflow is None:
            # External integrations often have no Actions run; exact check name/app is
            # their stable identity. For unresolved Actions URLs retain a distinct key.
            workflow=('unresolved',rid) if rid else ('external',)
            if rid:ambiguous=True
        key=(str(workflow),str(app),c.get('name',''))
        rank=((run or {}).get('run_number',0),(run or {}).get('run_attempt',0),
              c.get('started_at') or c.get('completed_at') or '',int(c.get('id',0)))
        if key not in groups or rank>groups[key][0]:groups[key]=(rank,c)
    return [v[1] for v in groups.values()],not ambiguous


def latest_statuses(statuses):
    groups={}
    for s in statuses:
        key=s.get('context','');rank=(s.get('updated_at') or s.get('created_at') or '',int(s.get('id',0)))
        if key not in groups or rank>groups[key][0]:groups[key]=(rank,s)
    return [v[1] for v in groups.values()]


def collect_ci(api,pr):
    head=pr['head']['sha'];merge=pr.get('merge_commit_sha')
    refs=[head]
    if merge and merge!=head:
        # Ensure synthetic merge actually contains this PR head before using it.
        mc=api.get(f'{ROOT}/git/commits/{merge}')
        if head in [p.get('sha') for p in mc.get('parents',[])]:refs.append(merge)
    checks=[];statuses=[];runs=[]
    for sha in refs:
        checks.extend(pages(api,f'commits/{sha}/check-runs?filter=latest','check_runs'))
        statuses.extend(pages(api,f'commits/{sha}/status','statuses'))
        # Only request lightweight workflow-run metadata when there are Actions checks.
        if any(check_run_id(c) for c in checks):
            runs.extend(pages(api,'actions/runs?'+urlencode({'head_sha':sha}),'workflow_runs'))
    selected,identity_complete=latest_checks(checks,runs)
    result=aggregate_ci(selected,latest_statuses(statuses),complete=identity_complete)
    times=[c.get(k) for c in selected for k in ('started_at','completed_at')]
    times += [s.get(k) for s in latest_statuses(statuses) for k in ('created_at','updated_at')]
    activity_at=max((iso(t) for t in times if t),default=None)
    return dict(result,complete=identity_complete,refs=refs,checks=len(selected),statuses=len(latest_statuses(statuses)),activity_at=activity_at)


def selection(db,needs,batch_limit,now=None):
    """No whole-history backlog: only PRs with proven activity in the last 30d."""
    if batch_limit<=0:return []
    active=set(db.scope_active(now))
    rows=[db.row(n) for n in set(needs) if n in active]
    # Source/observed code activity, never first discovery or comment updated_at.
    rows.sort(key=lambda r:(r['activity_at'] or r['created_at'],r['created_at'],r['number']),reverse=True)
    return [r['number'] for r in rows[:batch_limit]]



def activity_probe_candidates(db,now,limit=20):
    """updated_at is only a cheap candidate hint, never activity evidence."""
    cutoff=instant(now)-timedelta(days=30);active=set(db.scope_active(now));candidates=[]
    known=db._last_complete_open_ids()
    for rec in db.conn.execute("SELECT number FROM prs WHERE state='open'"):
        row=db.row(rec[0])
        if known is not None and row['number'] not in known:continue
        if row['number'] in active or instant(row['created_at'])>=cutoff:continue
        if instant(row['updated_at'])<cutoff:continue
        result=row.get('activity_probe_result');at=row.get('activity_probe_at')
        if result=='inactive':continue
        if at and instant(now)-instant(at)<timedelta(hours=1):continue
        candidates.append(row)
    candidates.sort(key=lambda r:(bool(r.get('activity_probe_at')),r.get('activity_probe_at') or '',-instant(r['updated_at']).timestamp(),-r['number']))
    return [r['number'] for r in candidates[:limit]]


def probe_activity(db,api,pr,now):
    """Prove activity from actual commit, check/status or Draft transition dates.

    Complete old data proves inactivity only for the observed head and list version.
    An API failure/ambiguous CI remains unknown, not silently outside the scope.
    """
    n=pr['number'];row=db.row(n);cutoff=instant(now)-timedelta(days=30)
    commit=api.get(f'{ROOT}/git/commits/{row["head_sha"]}')
    at=commit.get('committer',{}).get('date') or commit.get('author',{}).get('date')
    if not at:raise CoverageError('latest commit timestamp unavailable for activity probe')
    db.record_activity(n,at,'commit',f'Git commit {row["head_sha"]} committer/author date')
    if instant(at)>=cutoff:
        db.record_activity_probe(n,'active',now);return 'active'
    ci=collect_ci(api,pr)
    if ci['activity_at']:
        db.record_activity(n,ci['activity_at'],'ci','Latest selected head/verified-merge check or commit-status event timestamp')
        if instant(ci['activity_at'])>=cutoff:
            db.record_activity_probe(n,'active',now);return 'active'
    events=pages(api,f'issues/{n}/timeline')
    drafts=[e.get('created_at') for e in events if e.get('event') in ('ready_for_review','converted_to_draft') and e.get('created_at')]
    if drafts:
        at=max(drafts,key=instant)
        db.record_activity(n,at,'draft',f'Issue timeline ready_for_review/converted_to_draft event at {at}')
        if instant(at)>=cutoff:
            db.record_activity_probe(n,'active',now);return 'active'
    if not ci['complete']:raise CoverageError('CI identity incomplete; absence of recent activity not established')
    final=api.get(f'{ROOT}/pulls/{n}')
    if final['head']['sha']!=row['head_sha'] or final['base']['ref']!=row['base_ref'] or bool(final.get('draft'))!=bool(row['draft']) or final.get('updated_at')!=row['updated_at']:
        raise CoverageError('PR changed during activity probe; inactivity not established')
    db.record_activity_probe(n,'inactive',now);return 'inactive'


def budget_left(api):
    """Both GET/retry waits and loop scheduling honor the current phase deadline."""
    end=min(getattr(api,'deadline',float('inf')),getattr(api,'phase_deadline',None) or float('inf'))
    return end-time.monotonic()


@contextmanager
def phase_limit(api,deadline):
    old=getattr(api,'phase_deadline',None)
    api.phase_deadline=deadline
    try:yield
    finally:api.phase_deadline=old



def prepare(directory,api,batch_limit=60,round_id=None,now=None):
    directory=Path(directory);now=iso(now);round_id=round_id or ('round-'+now.replace(':','').replace('-','')+'-'+uuid.uuid4().hex[:6])
    work=directory/'work'/round_id;work.mkdir(parents=True,exist_ok=True)
    db=WatchDB(directory/'pr_watch.db',directory/'exclude.yaml')
    result={'round_id':round_id,'started_at':now,'discovery_complete':False,'gaps':[],'deferrals':[],
            'summary_requests':0,'file_prs':0,'ci_prs':0,'closed':0,'activity_probes':0,
            'activity_probes_completed':0,'init_processed':0,'ci_due':0,'ci_existing_refreshed':0,
            'ci_existing_attempted':0,'ci_new_refreshed':0,'ci_new_attempted':0,'ci_deferred':0,'finished_at':None}
    requests=[];prs=[];index={};start=time.monotonic();attempted_ci=set();deferred_ci=set()
    def gap(scope,err):
        result['gaps'].append({'scope':scope,'at':iso(),'description':str(err)[:400]})
    def defer(phase,numbers,reason='phase_budget_exhausted',ci=False):
        numbers=list(dict.fromkeys(numbers))
        if not numbers:return
        result['deferrals'].append({'phase':phase,'reason':reason,'at':iso(),'count':len(numbers),'pr_numbers':numbers})
        gap(phase,f'{len(numbers)} PRs deferred: {reason}; not treated as checked')
        if ci:
            deferred_ci.update(numbers)
            db.mark_ci_deferred(numbers,now,reason=reason)
    def checked_ci(numbers,kind):
        numbers=list(numbers)
        for i,n in enumerate(numbers):
            if budget_left(api)<=0:
                defer(kind+' CI',numbers[i:],ci=True);break
            before=api.metrics['rest_requests'];budget_failure=False
            try:
                row=db.row(n);pr=index.get(n) or api.get(f'{ROOT}/pulls/{n}')
                if pr.get('state')=='closed' and pr.get('closed_at'):
                    db.confirm_closed(n,'merged' if pr.get('merged_at') else 'closed',pr['closed_at'],pr.get('merged_at'));result['closed']+=1
                    continue
                db.ingest_discovery([pr],complete=False,now=now);index[n]=pr;row=db.row(n)
                result['tracked_metadata_checked']+=1
                if pr['head']['sha']!=row['head_sha'] or pr['base']['ref']!=row['base_ref']:
                    raise CoverageError('head/base changed during CI collection')
                ci=collect_ci(api,pr)
                final=api.get(f'{ROOT}/pulls/{n}')
                if final['head']['sha']!=row['head_sha'] or final['base']['ref']!=row['base_ref'] or final.get('state')!='open':
                    raise CoverageError('head/base/state changed during CI collection; deferred')
                if final.get('merge_commit_sha')!=pr.get('merge_commit_sha'):
                    raise CoverageError('merge reference changed during CI collection; deferred')
                db.update_ci(n,ci['state'],ci['ci_gate'],now=now,complete=ci['complete'],head_sha=row['head_sha'],base_ref=row['base_ref'],activity_at=ci['activity_at'])
                if ci['complete']:
                    result['ci_prs']+=1;result['ci_'+kind+'_refreshed']+=1
                else:gap(f'PR {n} CI','Actions workflow identity unavailable; status unknown')
            except (CoverageError,KeyError,ValueError) as e:
                budget_failure=isinstance(e,BudgetError)
                if api.metrics['rest_requests']>before:
                    db.update_ci(n,'unknown',now=now,complete=False)
                    if not budget_failure:gap(f'PR {n} CI',e)
                elif not budget_failure:gap(f'PR {n} CI',e)
            finally:
                if api.metrics['rest_requests']>before:
                    attempted_ci.add(n);result['ci_'+kind+'_attempted']+=1
            if budget_failure:
                defer(kind+' CI',numbers[i:],ci=True);break
    try:
        # Existing tracked PRs are independent of candidate discovery.
        tracked=[r[0] for r in db.conn.execute("SELECT number FROM prs WHERE state='open' AND matched=1")]
        result['tracked_before']=tracked
        result['tracked_metadata_checked']=0
        existing_due=[n for n in db.ci_due(now) if n in tracked]
        result['ci_due']=len(existing_due);result['ci_due_existing']=len(existing_due)
        round_end=getattr(api,'deadline',float('inf'))
        remaining=max(0,round_end-time.monotonic())
        # User-authorized lightweight priority: bounded candidate discovery and
        # current changed-file evidence first, independent CI rotation afterwards.
        reserve=min(300,remaining*.45)
        result['initialization_reserve_seconds']=round(reserve,3)
        candidate_ids=set();cutoff=instant(now)-timedelta(days=30)
        discovery_end=min(round_end,time.monotonic()+min(60,remaining*.10))
        with phase_limit(api,discovery_end):
            for sort in ('created','updated'):
                if budget_left(api)<=0:break
                try:
                    values=api.get(f'{ROOT}/pulls?state=open&sort={sort}&direction=desc&per_page=30&page=1')
                    if not isinstance(values,list):raise CoverageError('invalid candidate list')
                    recent=[p for p in values if instant(p['updated_at'])>=cutoff]
                    for pr in recent:
                        if pr['number'] not in candidate_ids:
                            candidate_ids.add(pr['number']);prs.append(pr)
                except (CoverageError,KeyError,ValueError) as e:
                    gap('recent PR candidate discovery',e)
        # Discovery remains intentionally bounded, never a closure snapshot.
        discovery=db.ingest_discovery(prs,complete=False,now=now)
        index.update({p['number']:p for p in prs})
        db._meta('bounded_discovery',True);db.conn.commit()
        result['candidate_prs']=len(prs);result['open_prs']=None
        if not result['discovery_complete']:
            result['coverage_limit']='Bounded recent candidates (30 newest + 30 updated); no complete open snapshot or forced history initialization.'
        if budget_left(api)>0:
            # Backlog is bounded even if all old tracked CI finishes early. Unused
            # round time can then check newly matched PRs rather than disappear.
            backlog_end=min(round_end,time.monotonic()+reserve)
            with phase_limit(api,backlog_end):
                missing=[n for n in discovery['missing'] if db.row(n)['matched']]
                for i,n in enumerate(missing):
                    if budget_left(api)<=0:defer('final state',missing[i:]);break
                    try:
                        pr=api.get(f'{ROOT}/pulls/{n}')
                        if pr.get('state')=='closed' and pr.get('closed_at'):
                            db.confirm_closed(n,'merged' if pr.get('merged_at') else 'closed',pr['closed_at'],pr.get('merged_at'));result['closed']+=1
                    except BudgetError:defer('final state',missing[i:]);break
                    except CoverageError as e:gap(f'PR {n} final state',e)

                # Probes cannot eat the whole initialization tail: leave most of it
                # for confirmed recent PR file screening and summary recovery.
                probes=[n for n in activity_probe_candidates(db,now,limit=5) if n in candidate_ids]
                probe_end=min(backlog_end,time.monotonic()+max(0,budget_left(api))*.15)
                with phase_limit(api,probe_end):
                    for i,n in enumerate(probes):
                        if budget_left(api)<=0:defer('activity probes',probes[i:]);break
                        before=api.metrics['rest_requests']
                        try:
                            probe_activity(db,api,index[n],now);result['activity_probes_completed']+=1
                        except BudgetError:
                            if api.metrics['rest_requests']>before:db.record_activity_probe(n,'unknown',now)
                            defer('activity probes',probes[i:]);break
                        except (CoverageError,KeyError,ValueError) as e:
                            if api.metrics['rest_requests']>before:db.record_activity_probe(n,'unknown',now)
                            gap(f'PR {n} 30-day activity',e)
                        finally:
                            if api.metrics['rest_requests']>before:result['activity_probes']+=1
                scope=set(db.scope_active(now))
                needs=[n for n in scope if n in candidate_ids or n in tracked]
                needs=[n for n in needs if n in index and (db.row(n)['changed_files'] is None or db.row(n)['files_sha']!=db.row(n)['head_sha'] or db.row(n)['files_base']!=db.row(n)['base_ref'])]
                selected=selection(db,needs,batch_limit,now);result['init_selected']=len(selected)
                for i,n in enumerate(selected):
                    if budget_left(api)<=0:defer('files/detail',selected[i:]);break
                    try:
                        row=db.row(n);files=pages(api,f'pulls/{n}/files',cap=30)
                        result['file_prs']+=1
                        pr=api.get(f'{ROOT}/pulls/{n}')
                        if pr['head']['sha']!=row['head_sha'] or pr['base']['ref']!=row['base_ref'] or pr.get('state')!='open':
                            raise CoverageError('head/base/state changed during collection; deferred')
                        if not db.rules.matches(files):
                            db.update_detail(n,strip_files(files),head_sha=row['head_sha'],base_ref=row['base_ref']);result['init_processed']+=1;continue
                        commit=api.get(f'{ROOT}/git/commits/{row["head_sha"]}')
                        latest=commit.get('committer',{}).get('date') or commit.get('author',{}).get('date')
                        if not latest:raise CoverageError('latest commit time missing')
                        db.record_activity(n,latest,'commit',f'Git commit {row["head_sha"]} committer/author date')
                        db.update_detail(n,strip_files(files),pr['additions'],pr['deletions'],latest,head_sha=row['head_sha'],base_ref=row['base_ref'])
                        result['init_processed']+=1;index[n]=pr
                        if not db.cached_summary(n):
                            requests.append({'number':n,'head_sha':row['head_sha'],'base_ref':row['base_ref'],'title':pr['title'],'body':pr.get('body') or '',
                                             'relevant_files':[f for f in files if db.rules.matches([f])]})
                    except BudgetError:defer('files/detail',selected[i:]);break
                    except (CoverageError,KeyError,ValueError) as e:gap(f'PR {n} files/detail',e)
                rematched=[]
                for r in db.conn.execute("SELECT number FROM prs WHERE state='open' AND matched=1 AND (detail_sha IS NULL OR detail_sha!=head_sha OR detail_base!=base_ref)"):
                    n=r[0];row=db.row(n)
                    if n in selected or n not in scope:continue
                    if row['files_sha']==row['head_sha'] and row['files_base']==row['base_ref']:rematched.append(n)
                for i,n in enumerate(rematched):
                    if budget_left(api)<=0:defer('rematched detail',rematched[i:]);break
                    try:
                        row=db.row(n);pr=api.get(f'{ROOT}/pulls/{n}')
                        if pr['head']['sha']!=row['head_sha'] or pr['base']['ref']!=row['base_ref']:raise CoverageError('head/base changed; deferred')
                        commit=api.get(f'{ROOT}/git/commits/{row["head_sha"]}')
                        latest=commit['committer']['date']
                        db.record_activity(n,latest,'commit',f'Git commit {row["head_sha"]} committer date')
                        db.update_detail(n,row['changed_files'],pr['additions'],pr['deletions'],latest,head_sha=row['head_sha'],base_ref=row['base_ref']);index[n]=pr
                    except BudgetError:defer('rematched detail',rematched[i:]);break
                    except (CoverageError,KeyError,ValueError) as e:gap(f'PR {n} rematched detail',e)
                known={r['number'] for r in requests};missing_summaries=[]
                for r in db.conn.execute("SELECT number FROM prs WHERE state='open' AND matched=1"):
                    n=r[0];row=db.row(n)
                    if n not in scope or n in known or db.cached_summary(n):continue
                    if row['detail_sha']==row['head_sha'] and row['detail_base']==row['base_ref']:missing_summaries.append(n)
                for i,n in enumerate(missing_summaries):
                    if budget_left(api)<=0:defer('summary evidence',missing_summaries[i:]);break
                    try:
                        row=db.row(n);files=pages(api,f'pulls/{n}/files',cap=30)
                        pr=index.get(n) or api.get(f'{ROOT}/pulls/{n}')
                        requests.append({'number':n,'head_sha':row['head_sha'],'base_ref':row['base_ref'],'title':pr['title'],'body':pr.get('body') or '',
                                         'relevant_files':[f for f in files if db.rules.matches([f])]})
                    except BudgetError:defer('summary evidence',missing_summaries[i:]);break
                    except CoverageError as e:gap(f'PR {n} summary evidence',e)

        # Discovery or one PR failure never prevents independent tracked CI.
        with phase_limit(api,round_end):
            checked_ci(existing_due,'existing')
            for n in tracked:
                if n in existing_due or n in index:continue
                if budget_left(api)<=0:break
                try:
                    pr=api.get(f'{ROOT}/pulls/{n}')
                    if pr.get('state')=='closed' and pr.get('closed_at'):
                        db.confirm_closed(n,'merged' if pr.get('merged_at') else 'closed',pr['closed_at'],pr.get('merged_at'));result['closed']+=1
                    elif pr.get('state')=='open':
                        db.ingest_discovery([pr],complete=False,now=now);index[n]=pr
                        if n in db.ci_due(now):checked_ci([n],'existing')
                    result['tracked_metadata_checked']+=1
                except (CoverageError,KeyError,ValueError) as e:gap(f'PR {n} metadata',e)
            scope=set(db.scope_active(now));existing_ids=set(existing_due)
            new_due=[n for n in db.ci_due(now) if n in scope and n in index and n not in existing_ids and n not in attempted_ci]
            result['ci_due_new']=len(new_due);result['ci_due']+=len(new_due)
            checked_ci(new_due,'new')
        if db.rules.policy_version >= 2:
            known={r['number'] for r in requests}
            for row in db.semantic_pending(now):
                if row['number'] not in known:
                    requests.append(dict(number=row['number'],head_sha=row['head_sha'],base_ref=row['base_ref'],
                        title=row['title'],cached_summary=db.cached_summary(row['number']),semantic_only=True,
                        relevant_files=[f for f in row['changed_files'] if db.rules.matches([f])]))
        result['new_related_prs']=sum(1 for n in candidate_ids if n not in tracked and db.row(n)['matched'])
        result['existing_details_updated']=sum(1 for r in requests if r['number'] in tracked and not r.get('semantic_only'))
        result['summary_requests']=len(requests);result['ci_deferred']=len(deferred_ci)
        scoped=[db.row(n) for n in db.scope_active(now)]
        result['scope_active_open']=len(scoped);result['matched_open']=sum(bool(r['matched']) for r in scoped)
        result['pending_files']=sum(r['changed_files'] is None or r['files_sha']!=r['head_sha'] or r['files_base']!=r['base_ref'] for r in scoped if r['number'] in candidate_ids or r['number'] in tracked)
        cutoff=instant(now)-timedelta(days=30);active_numbers={r['number'] for r in scoped};known_open=db._last_complete_open_ids()
        result['activity_unconfirmed']=sum((known_open is None or r[0] in known_open) and instant(db.row(r[0])['updated_at'])>=cutoff and r[0] not in active_numbers and db.row(r[0]).get('activity_probe_result')!='inactive' for r in db.conn.execute("SELECT number FROM prs WHERE state='open'"))
        result['coverage_limit']='Recent new/updated PR file evidence first; independent CI rotation; candidates capped at 60; no full-open snapshot or forced historical backlog. Old CI-only reruns may be missed.'
        result['metrics']=dict(api.metrics);result['metrics']['elapsed_seconds']=round(time.monotonic()-start,3)
        result['finished_at']=iso();result['status']='partial' if result['gaps'] else 'collected'
        db._meta('prepared_round',round_id);db.conn.commit()
        atomic_json(work/'summary_requests.json',requests);atomic_json(work/'result.json',result);atomic_json(directory/'latest-round.json',result)
        return result
    finally:db.close()


def finish(directory,round_id,summaries,now=None):
    directory=Path(directory);work=directory/'work'/round_id
    result=json.loads((work/'result.json').read_text());requests=json.loads((work/'summary_requests.json').read_text())
    db=WatchDB(directory/'pr_watch.db',directory/'exclude.yaml')
    try:
        prepared=db.conn.execute("SELECT value FROM metadata WHERE key='prepared_round'").fetchone()
        if not prepared or json.loads(prepared[0])!=round_id:raise CoverageError('another round has replaced this prepared result')
        applied=0
        for req in requests:
            n=req['number'];value=summaries.get(str(n),summaries.get(n))
            if not value:continue
            row=db.row(n)
            if row['head_sha']!=req['head_sha'] or row['base_ref']!=req['base_ref']:raise CoverageError('summary request is stale')
            if value.get('head_sha')!=req['head_sha']:raise CoverageError('summary SHA mismatch')
            if value.get('base_ref',req['base_ref'])!=req['base_ref']:raise CoverageError('summary base mismatch')
            db.update_detail(n,row['changed_files'],row['additions'],row['deletions'],row['latest_commit_at'],
                             summary=value.get('summary') or db.cached_summary(n),summary_sha=req['head_sha'],head_sha=req['head_sha'],base_ref=req['base_ref'])
            if value.get('scope_decision'):
                db.apply_scope_decision(n,value['scope_decision'],value['scope_reason'],req['head_sha'],req['base_ref'])
            applied+=1
        active,archive=db.render(now)
        # Detailed diagnostics remain local; per-PR last-known times show staleness.
        (directory/'active.md').write_text(active);(directory/'archive.md').write_text(archive)
        result['metrics']['ai_summaries_applied']=applied;result['rendered_at']=iso(now)
        result['new_related_prs_final']=sum(1 for r in requests if db.row(r['number'])['matched'] and r['number'] not in result.get('tracked_before',[]))
        result['summaries_remaining']=len(requests)-applied
        atomic_json(work/'result.json',result);atomic_json(directory/'latest-round.json',result)
        # Do not retain patch bodies beyond review. Diagnostic counters/gaps survive.
        (work/'summary_requests.json').unlink(missing_ok=True)
        for p in (work/'bridge').glob('response-*.json'):p.unlink()
        return result
    finally:db.close()


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('action',choices=['prepare','finish']);p.add_argument('--directory',required=True)
    p.add_argument('--batch-limit',type=int,default=60);p.add_argument('--budget-seconds',type=float,default=720)
    p.add_argument('--round-id');p.add_argument('--summaries');p.add_argument('--now');a=p.parse_args();d=Path(a.directory)
    try:
        with round_lock(d):
            if a.action=='prepare':
                rid=a.round_id or 'round-'+iso().replace(':','').replace('-','')+'-'+uuid.uuid4().hex[:6]
                api=Bridge(d/'work'/rid/'bridge',a.budget_seconds)
                result=prepare(d,api,a.batch_limit,rid,a.now)
            else:
                if not a.round_id or not a.summaries:raise ValueError('finish needs --round-id and --summaries')
                result=finish(d,a.round_id,json.loads(Path(a.summaries).read_text()),a.now)
        print(json.dumps(result,ensure_ascii=False))
    except Exception as e:
        print(json.dumps({'status':'blocked','error':str(e)[:400]},ensure_ascii=False));raise SystemExit(2)

if __name__=='__main__':main()
