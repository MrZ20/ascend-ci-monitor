import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from collector import *

RULES=Path(__file__).with_name('exclude.yaml')
NOW='2026-11-12T09:00:00Z'

def pr(n=1,sha='a',path=None):
    return {'number':n,'title':'Title','html_url':f'https://github.com/{REPO}/pull/{n}',
      'created_at':'2026-11-11T00:00:00Z','updated_at':NOW,'draft':False,'state':'open',
      'head':{'sha':sha},'base':{'ref':'main'},'merge_commit_sha':None,'additions':5,'deletions':2,'body':'change'}

class Fake:
    def __init__(self, prs, overrides=None):
        self.prs=prs;self.overrides=overrides or {};self.calls=[]
        self.metrics={'rest_requests':0,'graphql_queries':0,'graphql_cost':None,'response_bytes':0,'file_list_bytes':0}
    def get(self,url):
        safe_url(url);self.calls.append(url);self.metrics['rest_requests']+=1
        rel=url[len(ROOT)+1:]
        for key,v in self.overrides.items():
            if rel.startswith(key):
                if isinstance(v,Exception):raise v
                return v
        if rel.startswith('pulls?'):return self.prs
        if re.fullmatch(r'pulls/\d+',rel):return next(p for p in self.prs if p['number']==int(rel.split('/')[1]))
        if '/files?' in rel:return [{'filename':'.github/workflows/a.yml','patch':'+hello','status':'modified'}]
        if '/check-runs?' in rel:return {'check_runs':[{'id':2,'name':'test','status':'completed','conclusion':'success','app':{'id':1}}]}
        if '/status?' in rel:return {'statuses':[]}
        if rel.startswith('git/commits/'):return {'committer':{'date':'2026-11-11T03:00:00Z'},'parents':[]}
        if rel.startswith('actions/runs?'):return {'workflow_runs':[]}
        if '/timeline?' in rel:return []
        raise AssertionError(url)

class FakeTimed(Fake):
    def __init__(self,prs,clock,budget=100,cost=10,overrides=None):
        super().__init__(prs,overrides);self.clock=clock;self.budget_seconds=budget
        self.deadline=clock[0]+budget;self.phase_deadline=None;self.cost=cost
    def get(self,url):
        left=budget_left(self)
        if left<=0:raise BudgetError('no phase budget; no request issued')
        data=super().get(url)
        cost=self.cost(url) if callable(self.cost) else self.cost
        self.clock[0]+=min(cost,left)
        if cost>left:raise BudgetError('issued GET interrupted by phase deadline')
        return data

class Tests(unittest.TestCase):
    def setupdir(self):
        t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);d=Path(t.name)
        (d/'exclude.yaml').write_text('# PR Watch V1: explicit keep rules take precedence over exclusions.\n# Unmatched paths are included; do not expand exclusions automatically.\nversion: 1\nkeep:\n  - .github/**\n  - tests/e2e/common/**\n  - tests/e2e/doctests/**\n  - tests/e2e/nightly/**/scripts/**\n  - tests/ut/_tools/**\n  - tests/ut/tools/**\nexclude:\n  - vllm_ascend/**\n  - docs/source/tutorials/models/**\n  - docs/source/user_guide/feature_guide/**\n  - docs/source/user_guide/support_matrix/**\n  - tests/SIT/cases/models/**\n  - tests/SIT/cases/features/**\n  - tests/e2e/pull_request/**\n  - tests/e2e/nightly/**\n  - tests/ut/**/test_*.py\n');return d
    def test_allowlist(self):
        safe_url(ROOT+'/pulls/1/files?per_page=100&page=1')
        for u in ('https://api.github.com/repos/x/y/pulls','https://api.github.com/repos/'+REPO+'/actions/jobs/1/logs',ROOT+'/pulls/1/comments',ROOT+'/contents/a'):
            with self.assertRaises(ValueError):safe_url(u)
    def test_complete_prepare_finish(self):
        d=self.setupdir();api=Fake([pr()]);r=prepare(d,api,round_id='one',now=NOW)
        self.assertEqual(r['matched_open'],1);self.assertEqual(r['summary_requests'],1)
        self.assertEqual(r['status'],'collected')
        req=json.loads((d/'work/one/summary_requests.json').read_text())
        self.assertEqual(req[0]['relevant_files'][0]['patch'],'+hello')
        r=finish(d,'one',{'1':{'head_sha':'a','summary':'修改工作流。'}},now=NOW)
        self.assertEqual(r['metrics']['ai_summaries_applied'],1)
        self.assertIn('修改工作流',(d/'active.md').read_text())
        self.assertFalse((d/'work/one/summary_requests.json').exists())
        db=WatchDB(d/'pr_watch.db',d/'exclude.yaml');self.addCleanup(db.close)
        self.assertNotIn('patch',db.row(1)['changed_files'][0])
    def test_discovery_failure_does_not_block_existing_ci(self):
        d=self.setupdir();ps,old=self.seed_tracked(d,2)
        api=Fake(ps,{'pulls?':CoverageError('503 discovery unavailable')})
        result=prepare(d,api,batch_limit=0,round_id='discovery-fault',now=NOW)
        self.assertEqual(result['ci_existing_refreshed'],2)
        self.assertFalse(result['discovery_complete'])
        self.assertLess(next(i for i,u in enumerate(api.calls) if '/check-runs?' in u),next(i for i,u in enumerate(api.calls) if '/pulls?' in u))
        db=WatchDB(d/'pr_watch.db',d/'exclude.yaml');self.addCleanup(db.close)
        self.assertEqual(db.row(1)['ci_success_at'],NOW)
    def test_bounded_candidates_deduplicate_and_cancel_old_backlog(self):
        d=self.setupdir();ps,old=self.seed_tracked(d,1)
        db=WatchDB(d/'pr_watch.db',d/'exclude.yaml')
        db.ingest_discovery([pr(n) for n in range(2,1003)],False,NOW);db.close()
        api=Fake([pr(2000)]*100)
        api.overrides['pulls/1']=ps[0]
        result=prepare(d,api,batch_limit=0,round_id='bounded',now=NOW)
        self.assertEqual(sum('/pulls?' in u for u in api.calls),3)
        self.assertEqual(result['candidate_prs'],1)
        self.assertEqual(result['pending_files'],1)
        db=WatchDB(d/'pr_watch.db',d/'exclude.yaml');self.addCleanup(db.close)
        self.assertNotIn('1001',db.render(NOW)[0])
    def test_summary_sha_reject(self):
        d=self.setupdir();prepare(d,Fake([pr()]),round_id='one',now=NOW)
        with self.assertRaises(CoverageError):finish(d,'one',{'1':{'head_sha':'wrong','summary':'x'}},now=NOW)
    def test_unchanged_round_reuses_files_summary(self):
        d=self.setupdir();prepare(d,Fake([pr()]),round_id='one',now=NOW)
        finish(d,'one',{'1':{'head_sha':'a','summary':'summary'}},now=NOW)
        api=Fake([pr()]);r=prepare(d,api,round_id='two',now='2026-11-12T10:00:00Z')
        self.assertEqual(r['file_prs'],0);self.assertEqual(r['summary_requests'],0)
        self.assertFalse(any('/files?' in u for u in api.calls))
    def test_failed_discovery_no_archive(self):
        d=self.setupdir();prepare(d,Fake([pr()]),round_id='one',now=NOW)
        r=prepare(d,Fake([pr()],{ 'pulls?':CoverageError('503') }),round_id='two',now=NOW)
        self.assertFalse(r['discovery_complete']);self.assertEqual(r['closed'],0)
        db=WatchDB(d/'pr_watch.db',d/'exclude.yaml');self.addCleanup(db.close)
        self.assertEqual(db.row(1)['state'],'open')
    def test_files_race_does_not_cache_wrong_sha(self):
        d=self.setupdir();r=prepare(d,Fake([pr()],{'pulls/1':pr(1,'b')}),round_id='one',now=NOW)
        db=WatchDB(d/'pr_watch.db',d/'exclude.yaml');self.addCleanup(db.close)
        self.assertIsNone(db.row(1)['files_sha']);self.assertTrue(r['gaps'])
    def test_empty_ci_is_unknown(self):
        p=pr();p['merge_commit_sha']='m'
        api=Fake([p],{'commits/m':{'parents':[{'sha':'a'}]},'commits/a/check-runs':{'check_runs':[]},'commits/a/status':{'statuses':[]}})
        # Exact fake m prefix overrides every merge route, so test with no merge first.
        p['merge_commit_sha']=None
        r=collect_ci(api,p);self.assertEqual(r['state'],'unknown')
    def test_dedup_old_cancelled_latest_pass(self):
        checks=[{'id':1,'name':'test','app':{'id':1},'details_url':'https://github.com/x/y/actions/runs/11/job/1','conclusion':'cancelled','status':'completed'},
                {'id':2,'name':'test','app':{'id':1},'details_url':'https://github.com/x/y/actions/runs/12/job/2','conclusion':'success','status':'completed'}]
        runs=[{'id':11,'workflow_id':3,'run_number':1},{'id':12,'workflow_id':3,'run_number':2}]
        selected,complete=latest_checks(checks,runs)
        self.assertTrue(complete);self.assertEqual(len(selected),1);self.assertEqual(aggregate_ci(selected)['state'],'passed')
    def test_workflow_names_not_cross_merged(self):
        checks=[{'id':i,'name':'test','details_url':f'https://github.com/x/y/actions/runs/{i}/job/{i}'} for i in (1,2)]
        selected,complete=latest_checks(checks,[{'id':1,'workflow_id':1},{'id':2,'workflow_id':2}])
        self.assertEqual(len(selected),2);self.assertTrue(complete)
    def test_unknown_workflow_not_false_pass(self):
        selected,complete=latest_checks([{'name':'test','details_url':'https://github.com/x/y/actions/runs/1/job/1','conclusion':'success'}],[])
        self.assertFalse(complete);self.assertEqual(aggregate_ci(selected,complete=complete)['state'],'unknown')
    def test_transient_not_permission(self):
        self.assertTrue(is_transient({'status':403,'error':'Forbidden'}))
        self.assertFalse(is_transient({'status':403,'error':'Resource not accessible by integration'}))
        self.assertTrue(is_transient({'status':503}))
    def test_priority_reserves_pending(self):
        d=self.setupdir();db=WatchDB(d/'pr_watch.db',d/'exclude.yaml');self.addCleanup(db.close)
        db.ingest_discovery([pr(i) for i in range(1,10)],True,NOW)
        for n in range(1,5):db.update_detail(n,[{'filename':'vllm_ascend/foo.py'}])
        db.ingest_discovery([pr(i,'b') for i in range(1,10)],True,NOW)
        chosen=selection(db,list(range(1,10)),4)
        self.assertEqual(len(chosen),4);self.assertEqual(sum(n>=5 for n in chosen),2)
    def test_new_pr_not_behind_old_initial_backlog(self):
        d=self.setupdir();db=WatchDB(d/'pr_watch.db',d/'exclude.yaml');self.addCleanup(db.close)
        db.ingest_discovery([pr(i) for i in range(1,10)],True,NOW)
        later='2026-11-12T10:00:00Z'
        db.ingest_discovery([pr(i) for i in range(1,11)],True,later)
        chosen=selection(db,list(range(1,11)),4,later)
        self.assertIn(10,chosen);self.assertEqual(len(chosen),4)
    def test_batch_zero_no_stale_files_promoted(self):
        d=self.setupdir();prepare(d,Fake([pr()]),round_id='one',now=NOW)
        finish(d,'one',{'1':{'head_sha':'a','summary':'old summary'}},now=NOW)
        later='2026-11-12T10:00:00Z'
        api=Fake([pr(1,'b')]);r=prepare(d,api,batch_limit=0,round_id='two',now=later)
        db=WatchDB(d/'pr_watch.db',d/'exclude.yaml');self.addCleanup(db.close)
        self.assertEqual(r['file_prs'],0);self.assertEqual(r['pending_files'],1)
        self.assertEqual(db.row(1)['files_sha'],'a');self.assertEqual(db.row(1)['detail_sha'],'a')
        self.assertFalse(any('/files?' in u for u in api.calls))
    def old_pr(self,n=1):
        p=pr(n);p['created_at']='2026-05-01T00:00:00Z';return p
    def test_old_comment_only_not_in_scope(self):
        d=self.setupdir();p=self.old_pr()
        api=Fake([p],{'git/commits/':{'committer':{'date':'2026-05-01T00:00:00Z'},'parents':[]},
                     'issues/1/timeline':[{'event':'commented','created_at':NOW}]})
        r=prepare(d,api,round_id='one',now=NOW)
        self.assertEqual(r['file_prs'],0);self.assertEqual(r['pending_files'],0);self.assertEqual(r['activity_unconfirmed'],0)
        db=WatchDB(d/'pr_watch.db',d/'exclude.yaml');self.addCleanup(db.close)
        self.assertEqual(db.row(1)['activity_probe_result'],'inactive');self.assertEqual(db.scope_active(NOW),[])
    def test_old_recent_commit_qualifies(self):
        d=self.setupdir();p=self.old_pr();r=prepare(d,Fake([p]),round_id='one',now=NOW)
        self.assertEqual(r['file_prs'],1);self.assertEqual(r['activity_probes'],1);self.assertEqual(r['scope_active_open'],1)
    def test_old_recent_draft_qualifies_not_comment(self):
        d=self.setupdir();p=self.old_pr();api=Fake([p],{'git/commits/':{'committer':{'date':'2026-05-01T00:00:00Z'},'parents':[]},
                  'issues/1/timeline':[{'event':'ready_for_review','created_at':'2026-11-11T00:00:00Z'}]})
        r=prepare(d,api,round_id='one',now=NOW)
        self.assertEqual(r['scope_active_open'],1);self.assertEqual(r['file_prs'],1)
    def test_old_recent_ci_timestamp_qualifies(self):
        d=self.setupdir();p=self.old_pr();api=Fake([p],{'git/commits/':{'committer':{'date':'2026-05-01T00:00:00Z'},'parents':[]},
            'commits/a/check-runs':{'check_runs':[{'id':1,'name':'test','conclusion':'success','status':'completed','completed_at':'2026-11-11T00:00:00Z'}]}})
        r=prepare(d,api,round_id='one',now=NOW)
        self.assertEqual(r['scope_active_open'],1)
    def test_activity_failure_unknown_not_inactive(self):
        d=self.setupdir();p=self.old_pr();api=Fake([p],{'git/commits/':CoverageError('unavailable')})
        r=prepare(d,api,round_id='one',now=NOW)
        self.assertEqual(r['file_prs'],0);self.assertEqual(r['activity_unconfirmed'],1);self.assertTrue(r['gaps'])
        db=WatchDB(d/'pr_watch.db',d/'exclude.yaml');self.addCleanup(db.close)
        self.assertEqual(db.row(1)['activity_probe_result'],'unknown')
    def test_activity_probe_cap20_and_cached(self):
        d=self.setupdir();ps=[self.old_pr(n) for n in range(1,26)]
        overrides={'git/commits/':{'committer':{'date':'2026-05-01T00:00:00Z'},'parents':[]}}
        first=prepare(d,Fake(ps,overrides),round_id='one',now=NOW)
        self.assertEqual(first['activity_probes'],20);self.assertEqual(first['activity_unconfirmed'],5)
        second=prepare(d,Fake(ps,overrides),round_id='two',now=NOW)
        self.assertEqual(second['activity_probes'],5);self.assertEqual(second['activity_unconfirmed'],0)
    def test_ci_activity_uses_actual_timestamp_not_poll(self):
        p=pr();api=Fake([p],{'commits/a/status':{'statuses':[{'context':'docs','state':'success','created_at':'2026-11-01T00:00:00Z','updated_at':'2026-11-02T00:00:00Z'}]}})
        self.assertEqual(collect_ci(api,p)['activity_at'],'2026-11-02T00:00:00Z')
    def seed_tracked(self,d,count=4):
        ps=[pr(n,'a'+str(n)) for n in range(1,count+1)]
        db=WatchDB(d/'pr_watch.db',d/'exclude.yaml')
        old='2026-11-12T07:00:00Z';db.ingest_discovery(ps,True,old)
        for p in ps:
            n=p['number'];db.update_detail(n,[{'filename':'.github/a.yml'}],1,0,old,summary='cached',summary_sha=p['head']['sha'])
            db.update_ci(n,'passed',now=old)
        db.close();return ps,old
    def test_existing_ci_before_backlog_with_reserve(self):
        d=self.setupdir();ps,old=self.seed_tracked(d,4);ps.append(pr(10,'a10'))
        clock=[0.0];api=FakeTimed(ps,clock,cost=lambda u:1 if '/pulls?' in u else 10)
        with patch('collector.time.monotonic',side_effect=lambda:clock[0]):
            r=prepare(d,api,round_id='timed',now=NOW)
        file_index=next(i for i,u in enumerate(api.calls) if '/files?' in u)
        check_index=next(i for i,u in enumerate(api.calls) if '/check-runs?' in u)
        self.assertLess(check_index,file_index)
        self.assertGreaterEqual(r['ci_existing_refreshed'],1)
        self.assertGreaterEqual(r['file_prs'],1)
        self.assertGreater(r['ci_deferred'],0)
        db=WatchDB(d/'pr_watch.db',d/'exclude.yaml');self.addCleanup(db.close)
        # The fourth old PR had no request and must retain its successful/attempt clocks.
        self.assertEqual(db.row(4)['ci_checked_at'],old)
        self.assertEqual(db.row(4)['ci_success_at'],old)
        self.assertEqual(db.row(4)['ci_attempted_at'],old)
    def test_zero_remaining_budget_does_not_touch_ci_clock(self):
        d=self.setupdir();ps,old=self.seed_tracked(d,2);clock=[0.0]
        api=FakeTimed(ps,clock,budget=100,cost=100)
        with patch('collector.time.monotonic',side_effect=lambda:clock[0]):
            r=prepare(d,api,round_id='zero',now=NOW)
        self.assertEqual(r['ci_existing_attempted'],1);self.assertEqual(r['ci_deferred'],2)
        self.assertEqual(len(api.calls),2)
        db=WatchDB(d/'pr_watch.db',d/'exclude.yaml');self.addCleanup(db.close)
        for n in (1,2):
            self.assertEqual(db.row(n)['ci_success_at'],old)
            self.assertEqual(db.row(n)['ci_attempted_at'],NOW if n==1 else old)
    def test_failed_ci_attempt_rotates_next_round(self):
        d=self.setupdir();ps,old=self.seed_tracked(d,3)
        clock=[0.0];api=FakeTimed(ps,clock,cost=lambda u:1 if '/pulls' in u else 100)
        with patch('collector.time.monotonic',side_effect=lambda:clock[0]):
            one=prepare(d,api,batch_limit=0,round_id='one',now=NOW)
        self.assertEqual(one['ci_existing_attempted'],1);self.assertEqual(one['ci_existing_refreshed'],0)
        clock=[0.0];second=FakeTimed(ps,clock,cost=lambda u:1 if '/pulls' in u else 100)
        with patch('collector.time.monotonic',side_effect=lambda:clock[0]):
            two=prepare(d,second,batch_limit=0,round_id='two',now='2026-11-12T10:00:00Z')
        first_check=next(u for u in api.calls if '/check-runs?' in u)
        second_check=next(u for u in second.calls if '/check-runs?' in u)
        self.assertIn('/a1/',first_check);self.assertIn('/a2/',second_check)
    def test_probe_phase_leaves_time_for_files(self):
        d=self.setupdir();old=self.old_pr(20);new=pr(10,'a10');clock=[0.0]
        api=FakeTimed([old,new],clock,budget=300,cost=lambda u:1 if '/pulls?' in u else (60 if '/git/commits/a' in u and 'a10' not in u else 10))
        with patch('collector.time.monotonic',side_effect=lambda:clock[0]):
            r=prepare(d,api,round_id='probe',now=NOW)
        self.assertTrue(any(x['phase']=='activity probes' for x in r['deferrals']))
        self.assertGreaterEqual(r['file_prs'],1)
    def test_lock_nonblocking(self):
        d=self.setupdir()
        with round_lock(d):
            with self.assertRaises(CoverageError):
                with round_lock(d):pass
    def test_queued_timeout_is_not_actual_attempt(self):
        d=self.setupdir();b=Bridge(d,budget_seconds=1,request_timeout=0)
        with self.assertRaises(BudgetError):b.get(ROOT+'/pulls')
        self.assertEqual(b.metrics['requests_queued'],1);self.assertEqual(b.metrics['rest_requests'],0)
    def test_dispatch_marker_proves_attempt_on_timeout(self):
        d=self.setupdir();b=Bridge(d,budget_seconds=1,request_timeout=0)
        atomic_json(d/'dispatch-000001.json',{'id':1,'attempted':True})
        with self.assertRaises(BudgetError):b.get(ROOT+'/pulls')
        self.assertEqual(b.metrics['rest_requests'],1)
    def test_expired_skipped_response_not_actual_attempt(self):
        d=self.setupdir();b=Bridge(d,budget_seconds=1)
        atomic_json(d/'response-000001.json',{'id':1,'ok':False,'attempted':False,'budget_expired':True})
        with self.assertRaises(BudgetError):b.get(ROOT+'/pulls')
        self.assertEqual(b.metrics['rest_requests'],0)
    def test_atomic_bridge_contract(self):
        d=self.setupdir();b=Bridge(d,1)
        atomic_json(d/'response-000001.json',{'id':1,'ok':True,'data':{'a':1}})
        self.assertEqual(b.get(ROOT+'/pulls'),{'a':1})
        self.assertFalse((d/'response-000001.json').exists())

if __name__=='__main__':unittest.main()
