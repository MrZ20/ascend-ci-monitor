# Review policy

Use exactly one classification per reviewed job:
- infra: direct error plus independent exact main/shared-environment evidence.
- pr_caused: exact failure SHA/workflow/ref, PR diff, main/base configuration and actual runner/labels/step demonstrate the PR change. A PR-only environment failing there qualifies without pretending its deep root cause is known.
- other_non_infra: demonstrated code/config issue without proven PR attribution.
- insufficient_evidence: the causal/environment relationship is not established.

Timeout/OOM/exit code alone is not infrastructure attribution. Read each actual sampled job before grouping; unread jobs are never verified. Findings require fingerprint, classification, cause, first_error_at (null when unknown), job_url, verified_jobs, evidence, raw_error, collected_day and original discovered_at. New infra/pr findings also require per-job causation_checks with exact main_baseline.sha, evidence, relationship, failure_sha, workflow_ref, actual runner and evidence; PR findings require pr_evidence.

Group observable operation/service/error/environment scope, not random script UUID, pod suffix, node IP or run/job number. Preserve canonical aliases, oldest time and all actual links. Main shared temporary shell script missing uses v31:infra:main_shared:runner.temp_script_missing; main shared kubelet 10250 exec timeout uses v31:infra:main_shared:kubernetes.kubelet_exec_timeout. Do not group API443 or PR-only environments with these. Daily F numbers are not global pattern IDs. Grouping is not proof of a common deep cause.

Normal stratified sample limit20. Stream logs default excluded; no bulk testing logs. V3.2 exact-excluded test exceptions only: A latest10 completed workflow runs all failure; B at least2 observed completed runs within past hour, all failure with no nonfailure. Jobs within a matrix are not separate workflow runs. Inadequate time/status evidence means skip, not guess. Extra cap3, preferably distinct run/PR. Missing original exclusion policy is explicit degraded coverage, not permission to invent exclusions.

Public excerpts must preserve useful IP/port/path/host/node/module/variable diagnostics but exclude real credentials, passwords, private keys, Authorization values, auth URL secrets and private sensitive data. Do not upload full raw logs. Block publication if unsafe. Keep code fences unescaped.

Discovery/pagination/log errors, exhausted budget or unfinished review require persistent {gap_id,observed_at,description} using true observation time and stable capture identity. Do not advance a complete watermark or erase earlier gaps. Shanghai09:00 determines report day; later success never retroactively fills an old gap.
