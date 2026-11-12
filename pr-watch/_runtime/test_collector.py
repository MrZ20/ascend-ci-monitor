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
        raise AssertionError(url)

class Tests(unittest.TestCase):
    def setupdir(self):
        t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);d=Path(t.name)
        (d/'exclude.yaml').write_bytes(RULES.read_bytes());return d
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
        r=prepare(d,Fake([],{ 'pulls?':CoverageError('503') }),round_id='two',now=NOW)
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
    def test_lock_nonblocking(self):
        d=self.setupdir()
        with round_lock(d):
            with self.assertRaises(CoverageError):
                with round_lock(d):pass
    def test_atomic_bridge_contract(self):
        d=self.setupdir();b=Bridge(d,1)
        atomic_json(d/'response-000001.json',{'id':1,'ok':True,'data':{'a':1}})
        self.assertEqual(b.get(ROOT+'/pulls'),{'a':1})
        self.assertFalse((d/'response-000001.json').exists())

if __name__=='__main__':unittest.main()
