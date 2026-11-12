"""Prepare a strictly isolated pr-watch publication; Agent performs leased Git writes."""
from pathlib import Path
import re,json,hashlib

RUNTIME=('engine.py','collector.py','publication.py','test_engine.py','test_collector.py','test_publication.py','operations.txt')
def archive_sections(text):
    chunks=re.split(r'(?=<a id="pr-\d+"></a>)',text)
    out={}
    for c in chunks:
        m=re.match(r'<a id="pr-(\d+)"></a>',c)
        if not m:continue
        d=re.search(r'\*\*(?:已合入|已关闭)：\*\* (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})',c)
        if not d:raise ValueError('remote archive section missing final timestamp')
        out[int(m[1])]=(d[1],c.strip())
    if '<a id=' in text and not out:raise ValueError('unrecognized archive format')
    return out

def merge_archive(local,remote):
    sections=archive_sections(remote);sections.update(archive_sections(local))
    pruned=set()
    for text in (local,remote):
        for raw in re.findall(r'<!-- pr-watch-pruned: (\[[^\n]*\]) -->',text):
            pruned.update(int(n) for n in json.loads(raw))
    for n in pruned:sections.pop(n,None)
    head=local.split('<a id=',1)[0].replace('暂无归档。','').strip()
    head=re.sub(r'<!-- pr-watch-pruned: \[[^\n]*\] -->','',head).strip()
    if pruned:head+='\n\n<!-- pr-watch-pruned: '+json.dumps(sorted(pruned))+' -->'
    if not sections:return head+'\n\n暂无归档。\n'
    return head+'\n\n'+'\n\n'.join(c for _,c in sorted(sections.values(),reverse=True))+'\n'

def manifest(directory,remote_archive=''):
    p=Path(directory)
    files={'pr-watch/active.md':(p/'active.md').read_text(),'pr-watch/archive.md':merge_archive((p/'archive.md').read_text(),remote_archive),'pr-watch/exclude.yaml':(p/'exclude.yaml').read_text()}
    for f in RUNTIME:
        if (p/f).exists():files['pr-watch/_runtime/'+f]=(p/f).read_text()
    for path,content in files.items():
        if not path.startswith('pr-watch/') or '..' in path.split('/'):raise ValueError('path outside scope')
        if re.search(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----|https?://[^/\s]+:[^/\s]+@',content):raise ValueError('possible secret')
    return files

if __name__=='__main__':
    import argparse
    a=argparse.ArgumentParser();a.add_argument('--directory',required=True);a.add_argument('--remote-archive');args=a.parse_args()
    print(json.dumps(manifest(args.directory,Path(args.remote_archive).read_text() if args.remote_archive else ''),ensure_ascii=False))
