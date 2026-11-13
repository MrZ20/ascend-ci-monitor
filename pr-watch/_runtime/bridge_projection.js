/* Lossless-for-consumer PR projection. Never project checks, files, commits or runs. */
function projectResponse(url, data) {
  if (!/^https:\/\/api\.github\.com\/repos\/vllm-project\/vllm-ascend\/pulls(?:\/\d+)?(?:\?|$)/.test(url)) return data;
  const required = ['number','title','created_at','updated_at','draft','state','merge_commit_sha'];
  function one(p) {
    if (!p || required.some(k => !Object.hasOwn(p,k)) || !p.head?.sha || !p.base?.ref) return p;
    const result={};
    for (const k of [...required,'html_url','additions','deletions','closed_at','merged_at']) if(Object.hasOwn(p,k)) result[k]=p[k];
    result.head={sha:p.head.sha};result.base={ref:p.base.ref};
    // Body is intentionally unused for summaries; actual relevant file patches are used.
    return result;
  }
  return Array.isArray(data) ? data.map(one) : one(data);
}
if (typeof module !== 'undefined') module.exports={projectResponse};
