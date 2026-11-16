#!/usr/bin/env python3
"""Clean reconstructed collection data only; retain original Shanghai day plus next."""
import argparse,datetime as dt,json,pathlib,shutil,sqlite3
from collector import round_lock,Busy,day,validate_database

def cleanup(directory,today=None):
 d=pathlib.Path(directory);result={'deleted_days':[],'errors':[]};cutoff=(dt.date.fromisoformat(today or day())-dt.timedelta(days=1)).isoformat()
 try:
  with round_lock(d):
   db=d/'collector.sqlite3'
   if db.exists():
    c=sqlite3.connect('file:'+str(db)+'?mode=rw',uri=True)
    try:
     validate_database(c)
     with c:
      c.execute('DELETE FROM jobs WHERE collected_day<?',(cutoff,));c.execute('DELETE FROM runs WHERE collected_day<?',(cutoff,))
    finally:c.close()
   root=d/'data'
   if root.exists():
    for p in sorted(root.iterdir()):
     if p.is_symlink() or not p.is_dir():continue
     try:date=dt.date.fromisoformat(p.name).isoformat()
     except ValueError:continue
     if date<cutoff:shutil.rmtree(p);result['deleted_days'].append(date)
 except Busy:result['skipped']='collection_active'
 except Exception as e:result['errors'].append(type(e).__name__+':cleanup_incomplete')
 return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--directory',default=str(pathlib.Path(__file__).parent));a=p.parse_args();r=cleanup(a.directory);print(json.dumps(r));raise SystemExit(1 if r.get('errors') or r.get('skipped') else 0)
