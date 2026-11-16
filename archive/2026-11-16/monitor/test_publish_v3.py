import pathlib,tempfile,unittest
import publish_v3 as p
U='https://github.com/vllm-project/vllm-ascend/actions/runs/1/job/2'
AT='2026-11-12T08:00:00Z'
def finding():return dict(fingerprint='test:pattern',classification='insufficient_evidence',cause='Exact relationship unknown.',first_error_at=None,job_url=U,verified_jobs=[U],evidence=['Observed failure.'],raw_error='error: unavailable',collected_day='2026-11-12',discovered_at=AT)
def snapshot(files=None):
 files=files or {};return dict(commit='a'*40,repository=p.TARGET,public=True,branch='main',complete=True,manifest=list(files),files=files,absent_paths=['README.md','reports/2026/11/2026-11-12.md'] if not files else [])
def report():
 e,a,g,n=p.merge('',[finding()],[],AT);return p.render('2026-11-12',e,a,g,AT,'test')
class Tests(unittest.TestCase):
 def test_statistical_boundary(self):self.assertEqual(p.day_for('2026-11-12T00:59:59Z'),'2026-11-11');self.assertEqual(p.day_for('2026-11-12T01:00:00Z'),'2026-11-12')
 def test_roundtrip(self):
  e,a,g=p.parse(report());self.assertEqual(p.parse(p.render('2026-11-12',e,a,g,AT,'')),(e,a,g))
 def test_dedup(self):self.assertEqual(p.merge(report(),[finding()],[],AT)[3],0)
 def test_requires_baseline(self):
  f=finding();f['classification']='infra'
  with self.assertRaises(p.PublishError):p.validate(f)
 def test_secret_scan(self):
  for text in ['ghp_'+'x'*30,'Authorization: Bearer secret','https://x/?token=secret','-----BEGIN PRIVATE KEY-----']:
   with self.assertRaises(p.PublishError):p.safe(text)
  p.safe('connect 10.0.0.1:10250 /tmp/script.sh failed')
 def test_fences(self):self.assertTrue(p.fenced('```\nerror').startswith('````text'))
 def test_add_job_preserves_history(self):
  f=finding();f['verified_jobs']+=[U.replace('/2','/3')];e,a,g,n=p.merge(report(),[f],[],AT);self.assertEqual(n,0);self.assertEqual(len(next(iter(e.values()))['jobs']),2);self.assertIn('所有 Job（2）',p.render('2026-11-12',e,a,g,AT,''))
 def test_gap_dedup(self):
  g=dict(gap_id='a',observed_at=AT,description='Missing page.');self.assertEqual(len(p.merge('',[],[g,g],AT)[2]),1)
 def test_publish_verify(self):
  calls=[]
  def tr(op,payload):
   calls.append(op)
   return snapshot() if op=='target_snapshot' else {'commit':'b'*40} if op=='target_commit' else {'verified':True,'remote_commit':'b'*40}
  with tempfile.TemporaryDirectory() as d:r=p.publish(d,[finding()],'t','',[],tr,AT)
  self.assertEqual(r['commit'],'b'*40);self.assertEqual(calls,['target_snapshot','target_commit','target_verify'])
 def test_never_success_unverified(self):
  def tr(op,payload):return snapshot() if op=='target_snapshot' else {'commit':'b'*40} if op=='target_commit' else {'verified':False}
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaises(p.PublishError):p.publish(d,[],'t','',[],tr,AT)
 def test_lock(self):
  with tempfile.TemporaryDirectory() as d:
   with p.lock(d):
    with self.assertRaises(p.PublishError):
     with p.lock(d):pass
 def test_requires_original_date(self):
  f=finding();del f['discovered_at']
  with self.assertRaises(p.PublishError):p.validate(f)
 def test_snapshot_incomplete(self):
  def tr(op,payload):s=snapshot();s['complete']=False;return s
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaisesRegex(p.PublishError,'snapshot_incomplete'):p.publish(d,[],'t','',[],tr,AT)
 def test_absence_unverified(self):
  def tr(op,payload):s=snapshot();s['absent_paths']=[];return s
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaisesRegex(p.PublishError,'absence_unverified'):p.publish(d,[],'t','',[],tr,AT)
 def test_unknown_write_never_blind_retry(self):
  calls=[]
  def tr(op,payload):
   calls.append(op)
   if op=='target_snapshot':return snapshot()
   raise p.PublishError('timeout')
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaises(p.PublishError):p.publish(d,[],'t','',[],tr,AT)
   with self.assertRaisesRegex(p.PublishError,'previous_write'):p.publish(d,[],'t','',[],tr,AT)
  self.assertEqual(calls.count('target_commit'),1)
 def test_unknown_write_remote_recovery(self):
  state={}
  def tr(op,payload):
   if op=='target_snapshot':return snapshot(state.get('files'))
   if op=='target_commit':state['files']=payload['files'];raise p.PublishError('timeout')
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaises(p.PublishError):p.publish(d,[],'t','',[],tr,AT)
   self.assertEqual(p.publish(d,[],'t','',[],tr,AT)['status'],'published')
 def test_no_identity_merge_by_daily_number(self):
  e,a,g=p.parse(report());f=finding();f['fingerprint']='different:pattern';ee,_,_,n=p.merge(report(),[f],[],AT);self.assertEqual(n,1);self.assertEqual(len(ee),2);self.assertNotEqual(p.key(f['fingerprint']),p.key('test:pattern'))
if __name__=='__main__':unittest.main()
