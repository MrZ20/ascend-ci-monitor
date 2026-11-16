import contextlib,io,json,pathlib,sqlite3,tempfile,unittest
from unittest.mock import patch
from collector import *
from cleanup_v2 import cleanup
class Tests(unittest.TestCase):
 def setUp(self):self.tmp=tempfile.TemporaryDirectory();self.d=pathlib.Path(self.tmp.name)
 def tearDown(self):self.tmp.cleanup()
 def collector(self,body=None):return Collector(self.d,lambda req:(200,{},body))
 def test_lock(self):
  with round_lock(self.d):self.assertEqual(cleanup(self.d).get('skipped'),'collection_active')
 def test_retention(self):
  for day in ['2026-11-09','2026-11-10','2026-11-11','2026-11-12']:(self.d/'data'/day).mkdir(parents=True)
  (self.d/'recovery').mkdir();database(self.d).close()
  self.assertEqual(cleanup(self.d,'2026-11-12')['deleted_days'],['2026-11-09','2026-11-10']);self.assertTrue((self.d/'recovery').exists())
 def test_corrupt_no_rebuild(self):
  p=self.d/'collector.sqlite3';p.write_bytes(b'bad');self.assertTrue(cleanup(self.d)['errors']);self.assertEqual(p.read_bytes(),b'bad')
 def test_missing_table_not_recreated(self):
  c=database(self.d);c.execute('DROP TABLE jobs');c.close()
  with self.assertRaises(ReadFailure):database(self.d)
  c=sqlite3.connect(self.d/'collector.sqlite3');self.assertFalse(c.execute("SELECT 1 FROM sqlite_master WHERE name='jobs'").fetchone());c.close()
 def test_bad_version(self):
  c=database(self.d);c.execute("UPDATE meta SET value='9' WHERE key='schema_version'");c.commit();c.close()
  with self.assertRaises(ReadFailure):database(self.d)
 def test_startup_gap(self):
  (self.d/'exclusions.json').write_text('{bad')
  with contextlib.redirect_stdout(io.StringIO()):code=main(['collect','--directory',str(self.d)])
  self.assertEqual(code,1);g=list((self.d/'data').glob('*/*/gaps.json'));self.assertEqual(len(g),1);self.assertIn('startup',json.loads(g[0].read_text())[0]['gap_id'])
 def test_page_duplicates(self):
  c=self.collector({'jobs':[{'id':1},{'id':1}],'total_count':2})
  with self.assertRaises(ReadFailure):c.paged('x','jobs')
  c.c.close()
 def test_invalid_page(self):
  c=self.collector({'oops':[]})
  with self.assertRaises(ReadFailure):c.paged('x','jobs')
  c.c.close()
 def test_exact_exclude(self):
  c=self.collector();c.config={'rules':[{'step':'Run tests'}]};r={'run':{},'job':{},'failed_step':'Run tests'};self.assertTrue(c.excluded(r));r['failed_step']='Run tests extra';self.assertFalse(c.excluded(r));c.c.close()
 def test_mark_unread(self):
  c=database(self.d);c.execute('INSERT INTO jobs VALUES(?,?,?,?)',('1','2026-11-12',0,'{}'));c.commit();c.close()
  with self.assertRaises(ValueError):mark_reviewed(self.d,['1'])
 def test_original_log_day(self):
  c=self.collector('raw log');r={'key':'1','collected_day':'2026-11-11','run':{},'job':{'id':1}};c.c.execute('INSERT INTO jobs VALUES(?,?,?,?)',('1',r['collected_day'],0,json.dumps(r)));c.c.commit();c.fetch_log(r);result=c.finish();manifest=json.loads(pathlib.Path(result['samples_file']).read_text());self.assertIn('/2026-11-11/',manifest[0]['sample_path']);self.assertNotIn('job',manifest[0]);self.assertTrue((self.d/'data/2026-11-11/samples/job-1.log').exists())
 def anomaly(self,runs):
  c=self.collector({'workflow_runs':runs,'total_count':len(runs)});c.started='2026-11-12T07:00:00Z';rows=[{'run':{'id':r['id'],'workflow_id':1},'job':{'id':r['id']}} for r in runs];x=c.anomaly(rows);c.c.close();return x
 def test_unknown_completion_skip(self):
  self.assertEqual(self.anomaly([{'id':i,'conclusion':'failure','created_at':'2026-11-12T06:30:00Z','updated_at':'2026-11-12T06:40:00Z'} for i in range(10)]),[])
 def test_b_exact_completion(self):
  self.assertEqual(len(self.anomaly([{'id':i,'conclusion':'failure','completed_at':'2026-11-12T06:30:00Z'} for i in (1,2)])),2)
 def test_b_success_blocks(self):
  self.assertEqual(self.anomaly([{'id':1,'conclusion':'failure','completed_at':'2026-11-12T06:30:00Z'},{'id':2,'conclusion':'success','completed_at':'2026-11-12T06:40:00Z'}]),[])
 def test_a_completion_order(self):
  runs=[{'id':i,'conclusion':'failure','completed_at':'2026-11-11T06:30:00Z'} for i in range(10)]+[{'id':11,'conclusion':'success','created_at':'2026-01-01T00:00:00Z','completed_at':'2026-11-12T06:40:00Z'}]
  self.assertEqual(self.anomaly(runs),[])
 def test_no_write_ops(self):
  c=self.collector()
  with self.assertRaises(ReadFailure):c.request({'op':'post'})
  c.c.close()
 def test_retries_max_and_delays(self):
  c=self.collector();n=[];s=[]
  def transport(req):n.append(req);return 503,{},'temporary'
  c.transport=transport
  with patch('collector.time.sleep',side_effect=lambda d:s.append(d)):
   with self.assertRaises(ReadFailure):c.get('repos/x')
  self.assertEqual(len(n),3);self.assertEqual(s,[30,90]);c.c.close()
 def test_permission_no_retry(self):
  c=self.collector();n=[]
  def t(req):n.append(req);return 403,{},'Resource not accessible'
  c.transport=t
  with self.assertRaises(ReadFailure):c.get('repos/x')
  self.assertEqual(len(n),1);c.c.close()
 def test_retry_after(self):
  c=self.collector();n=[];s=[]
  def t(req):n.append(req);return (503,{'Retry-After':'100'},'temporary') if len(n)==1 else (200,{}, {})
  c.transport=t
  with patch('collector.time.sleep',side_effect=lambda d:s.append(d)):c.get('repos/x')
  self.assertEqual(s,[100]);c.c.close()
 def test_logs_before_remaining_jobs(self):
  (self.d/'exclusions.json').write_text('{"rules":[],"recovered":true}')
  seen=[];runs=[{'id':i,'run_attempt':1,'head_sha':'s','workflow_id':i,'created_at':f'2026-11-12T06:{i:02}:00Z'} for i in range(25)]
  def t(req):
   seen.append(req)
   if req['op']=='job_logs':return 200,{},'log'
   path=req['path']
   if 'status=failure' in path:return 200,{}, {'workflow_runs':runs,'total_count':25}
   if 'status=timed_out' in path:return 200,{}, {'workflow_runs':[],'total_count':0}
   rid=int(path.split('/runs/')[1].split('/')[0])
   if '/jobs?' in path:return 200,{}, {'jobs':[{'id':rid,'name':'j','conclusion':'failure','steps':[{'name':'setup','conclusion':'failure'}]}],'total_count':1}
   return 200,{},runs[rid]
  c=Collector(self.d,t);r=c.collect();self.assertEqual(r['samples'],20)
  first_log=next(i for i,x in enumerate(seen) if x['op']=='job_logs');last_job=max(i for i,x in enumerate(seen) if '/jobs?' in x.get('path',''))
  self.assertLess(first_log,last_job);self.assertEqual(len(json.loads((c.out/'samples.json').read_text())),20)
if __name__=='__main__':unittest.main()
