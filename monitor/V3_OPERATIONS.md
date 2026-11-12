# Reconstructed v3.2 monitor operations

This source backup is authorized by the owner after loss of the previous local workspace. It is not evidence of a completed monitoring run. Existing public reports remain the historical record.

Source repository: vllm-project/vllm-ascend (read-only). Report repository: MrZ20/ascend-ci-monitor, public main. No source edits, CI reruns, PR/issue comments, Gmail, email or Excel in this workflow. Keep the existing hourly automation; do not create duplicates.

## Run
1. Read REVIEW_POLICY.md and the current code.
2. Run python3 cleanup_v2.py and inspect real exit and JSON errors. skipped=collection_active is not success. Never delete locks.
3. Run python3 collector.py collect --directory <local-directory> --sample-limit 20 --budget-seconds 720.
4. Service the printed local bridge sequentially through the already authorized GitHub connector. GET request paths are source-only. job_logs is a read-only log fetch. Return parsed JSON or decoded log text in response-ID.json, or explicit error. Do not turn tool errors into empty successful data.
5. Wait for the real process exit. Review actual sampled jobs against exact main/PR evidence. Save original dates and actual job times; mark_reviewed only after review.
6. Run publish_v3.py --directory <local-directory> --findings <reviewed-json> --round-id <stable-capture> --note <actual-coverage>; include --coverage-gaps for real exceptional gaps. The optional old credential-file argument does not restore a missing token; connector credentials stay outside this code.
7. Service target_snapshot with complete current README and all daily report Markdown, exact main head, target repository/public/main metadata, complete manifest and explicit verified absent paths. Service target_commit through a tree based on the remote tree, commit parented to expected head, then force=false expected_sha guarded main update. Service target_verify by reading remote ref and changed content. Unknown writes must first reconcile their persistent intent with remote content; never blindly resend.

## Safety and recovery
Only useful finite error excerpts are public. No raw logs, SQLite, credentials, Authorization contents, auth-bearing URLs, secrets, or sensitive private data in backups. Normal report commits contain README and daily Markdown only. Separately authorized source backups live in monitor/ and contain reviewed code, tests and policy/docs only.

Local collection files and corresponding SQLite rows retain their original Shanghai collection day and next day. Do not reset damaged/unknown state. Public reports are the long-term record; preserve existing identities/aliases and links on recovery.

After workspace replacement, restore monitor/ files from a verified remote commit, run tests, read public historical reports, and begin an explicitly new local collection baseline if old state is unavailable. Do not claim that source backup or restored reports mean collection completed.

## Known reconstruction limits
The original exact exclusion list was lost. Do not invent or broaden it. Stream logs remain excluded by explicit instruction. A bounded recovery sample is not full equivalence to the lost policy; persist a coverage gap. The connector may omit Link/rate headers; use total_count and terminal pages and disclose limitations. Discover runs created in the past 24 hours; older-created reruns can be missed.

On 2026-11-12 the first reconstructed capture (07:48:27 UTC) was interrupted by a second executor replacement before a result or done record existed. It did not publish a CI report or advance a complete baseline.
