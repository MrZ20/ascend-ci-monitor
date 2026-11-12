import json
from pathlib import Path
import tempfile
import unittest
import sqlite3

from engine import WatchDB, Rules, aggregate_ci, glob_match, instant

RULES = Path(__file__).with_name("exclude.yaml")
T = "2026-11-12T01:00:00Z"


def pr(n=1, head="a", draft=False, created="2026-11-01T00:00:00Z", updated=T, base="main", title="Engineering PR"):
    return dict(number=n, title=title, createdAt=created, updatedAt=updated, headRefOid=head, baseRefName=base, isDraft=draft)


class MatchTests(unittest.TestCase):
    def setUp(self):
        self.rules = Rules(RULES)

    def test_glob_zero_and_many_segments(self):
        self.assertTrue(glob_match("tests/ut/test_x.py", "tests/ut/**/test_*.py"))
        self.assertTrue(glob_match("tests/ut/x/y/test_x.py", "tests/ut/**/test_*.py"))
        self.assertFalse(glob_match("tests/ut/x/helper.py", "tests/ut/**/test_*.py"))

    def test_keep_precedence(self):
        for path in [".github/workflows/x.yaml", "tests/e2e/common/x.py", "tests/e2e/doctests/test.py", "tests/e2e/nightly/scripts/a.sh", "tests/e2e/nightly/a/scripts/a.sh", "tests/ut/tools/test_a.py", "tests/ut/_tools/test_a.py"]:
            self.assertTrue(self.rules.included(path), path)

    def test_exclusions(self):
        for path in ["vllm_ascend/a.py", "docs/source/tutorials/models/a.md", "docs/source/user_guide/feature_guide/a.md", "docs/source/user_guide/support_matrix/a.md", "tests/SIT/cases/models/a.yaml", "tests/SIT/cases/features/a.yaml", "tests/e2e/pull_request/a.py", "tests/e2e/nightly/x/a.py", "tests/ut/test_a.py"]:
            self.assertFalse(self.rules.included(path), path)

    def test_rename_both_directions(self):
        self.assertTrue(self.rules.matches([{"filename": "vllm_ascend/a.py", "previous_filename": "tools/a.py"}]))
        self.assertTrue(self.rules.matches([{"filename": "tools/a.py", "previous_filename": "vllm_ascend/a.py"}]))

    def test_new_directory_default(self):
        self.assertTrue(self.rules.included("future-engineering/tool.py"))
        self.assertFalse(self.rules.matches(["vllm_ascend/a.py", "tests/ut/test_a.py"]))


class DBTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        fixture=Path(self.tmp.name)/"legacy.yaml"
        fixture.write_text('# PR Watch V1: explicit keep rules take precedence over exclusions.\n# Unmatched paths are included; do not expand exclusions automatically.\nversion: 1\nkeep:\n  - .github/**\n  - tests/e2e/common/**\n  - tests/e2e/doctests/**\n  - tests/e2e/nightly/**/scripts/**\n  - tests/ut/_tools/**\n  - tests/ut/tools/**\nexclude:\n  - vllm_ascend/**\n  - docs/source/tutorials/models/**\n  - docs/source/user_guide/feature_guide/**\n  - docs/source/user_guide/support_matrix/**\n  - tests/SIT/cases/models/**\n  - tests/SIT/cases/features/**\n  - tests/e2e/pull_request/**\n  - tests/e2e/nightly/**\n  - tests/ut/**/test_*.py\n')
        self.db = WatchDB(Path(self.tmp.name) / "watch.db", fixture)

    def tearDown(self):
        self.db.close()
        self.tmp.cleanup()

    def add(self, n=1, **kwargs):
        self.db.ingest_discovery([pr(n, **kwargs)], True, T)
        self.db.update_detail(n, ["tools/a.py"], 10, 2, "2026-11-11T23:00:00Z", "更新构建工具。", kwargs.get("head", "a"), T)

    def test_new_pr_and_cache(self):
        result = self.db.ingest_discovery([pr()], True, T)
        self.assertEqual(result, {"needs_files": [1], "missing": []})
        self.db.update_detail(1, ["tools/a.py"], 10, 2, T, "更新工具。", "a", T)
        result = self.db.ingest_discovery([pr(updated="2026-11-12T03:00:00Z")], True, "2026-11-12T03:00:00Z")
        self.assertEqual(result["needs_files"], [])
        self.assertEqual(self.db.cached_summary(1), "更新工具。")
        self.assertEqual(self.db.row(1)["meaningful_updated_at"], pr()["createdAt"])

    def test_head_and_base_changes(self):
        self.add()
        later = "2026-11-12T02:00:00Z"
        result = self.db.ingest_discovery([pr(head="b")], True, later)
        self.assertEqual(result["needs_files"], [1])
        self.assertEqual(self.db.row(1)["meaningful_updated_at"], later)
        self.assertIsNone(self.db.cached_summary(1))
        active, _ = self.db.render(later)
        self.assertIn("摘要待补齐", active)
        self.assertIn("改动：** 待更新", active)
        result = self.db.ingest_discovery([pr(head="b", base="release")], True, later)
        self.assertEqual(result["needs_files"], [1])

    def test_draft_change_without_files_query(self):
        self.add()
        later = "2026-11-12T02:00:00Z"
        result = self.db.ingest_discovery([pr(draft=True)], True, later)
        self.assertFalse(result["needs_files"])
        self.assertEqual(self.db.row(1)["meaningful_updated_at"], later)
        self.assertIn("**Draft**", self.db.render(later)[0])

    def test_no_archive_incomplete_discovery(self):
        self.add()
        self.assertEqual(self.db.ingest_discovery([], False, T)["missing"], [])
        self.assertEqual(self.db.row(1)["state"], "open")
        self.assertEqual(self.db.ingest_discovery([], True, T)["missing"], [1])
        self.assertEqual(self.db.row(1)["state"], "open")
        self.db.confirm_closed(1, "merged", "2026-11-12T05:00:00Z")
        active, archived = self.db.render(T)
        self.assertNotIn("pr-1", active)
        self.assertIn("已合入", archived)
        with self.assertRaises(ValueError):
            self.db.update_ci(1, "failed", now=T)

    def test_ci_changes_bump_only_real_observation(self):
        self.add()
        self.db.update_ci(1, "passed", now=T)
        self.db.update_ci(1, "passed", now="2026-11-12T02:00:00Z", activity_at="2026-11-12T02:00:00Z")
        self.assertEqual(self.db.row(1)["meaningful_updated_at"], T)
        self.db.update_ci(1, "failed", True, "2026-11-12T03:00:00Z")
        self.assertEqual(self.db.row(1)["meaningful_updated_at"], "2026-11-12T03:00:00Z")
        self.assertIn("失败（ci-gate）", self.db.render(T)[0])
        self.db.update_ci(1, "passed", now="2026-11-12T04:00:00Z", complete=False)
        self.assertEqual(self.db.row(1)["ci_state"], "unknown")
        self.assertEqual(self.db.row(1)["meaningful_updated_at"], "2026-11-12T03:00:00Z")
        self.db.update_ci(1, "failed", True, "2026-11-12T05:00:00Z")
        self.assertEqual(self.db.row(1)["meaningful_updated_at"], "2026-11-12T03:00:00Z")

    def test_stale_sha_rejected(self):
        self.add()
        with self.assertRaises(ValueError):
            self.db.update_ci(1, "passed", head_sha="old")
        with self.assertRaises(ValueError):
            self.db.update_detail(1, [], head_sha="old")
        with self.assertRaises(ValueError):
            self.db.update_detail(1, ["tools/a.py"], summary="bad", summary_sha="old")

    def test_incomplete_files_preserve_previous(self):
        self.add()
        self.db.update_detail(1, ["vllm_ascend/a.py"], files_complete=False)
        self.assertEqual(self.db.row(1)["matched"], 1)
        self.assertEqual(self.db.row(1)["changed_files"], ["tools/a.py"])

    def test_invalid_detail_does_not_mutate_cache(self):
        self.add()
        before = self.db.row(1)
        with self.assertRaises(ValueError):
            self.db.update_detail(1, ["tools/b.py"], 999, 999, T, "wrong", "old")
        self.assertEqual(self.db.row(1), before)

    def test_summary_reused_on_same_sha_detail_refresh(self):
        self.add()
        self.db.update_detail(1, ["tools/a.py"], 10, 2, T)
        self.assertEqual(self.db.cached_summary(1), "更新构建工具。")
        self.assertEqual(self.db.row(1)["summary"], "更新构建工具。")

    def test_active_and_stable_frequency(self):
        self.add()
        self.db.update_ci(1, "passed", now=T)
        self.assertEqual(self.db.ci_due("2026-11-12T01:30:00Z"), [])
        self.assertEqual(self.db.ci_due("2026-11-12T02:00:00Z"), [1])
        self.assertEqual(self.db.ci_due("2026-11-16T00:59:00Z"), [])
        self.assertEqual(self.db.ci_due("2026-11-16T01:00:00Z"), [1])
        self.db.update_ci(1, "passed", now="2026-11-16T01:00:00Z")
        self.assertEqual(self.db.ci_due("2026-11-16T02:00:00Z"), [])
        self.assertEqual(self.db.ci_due("2026-11-17T01:00:00Z"), [1])

    def test_pending_is_always_active(self):
        self.add()
        self.db.update_ci(1, "pending", now=T)
        self.assertEqual(self.db.ci_due("2026-11-20T00:30:00Z"), [1])

    def test_rule_change_rematches_cache(self):
        self.add()
        custom = Path(self.tmp.name) / "rules.yaml"
        custom.write_text("keep: []\nexclude: ['tools/**']\n")
        self.db.rules = Rules(custom)
        result = self.db.ingest_discovery([pr()], True, T)
        self.assertEqual(result["needs_files"], [])
        self.assertFalse(self.db.row(1)["matched"])

    def test_body_created_order_index_meaningful_order(self):
        prs = [pr(1, created="2026-11-10T00:00:00Z"), pr(2, created="2026-11-11T00:00:00Z")]
        self.db.ingest_discovery(prs, True, T)
        for n in (1, 2):
            self.db.update_detail(n, ["tools/a.py"], 1, 0, T, f"摘要{n}", "a", T)
        self.db.update_ci(1, "passed", now="2026-11-12T02:00:00Z", activity_at="2026-11-12T02:00:00Z")
        active, _ = self.db.render("2026-11-12T02:00:00Z")
        self.assertLess(active.index("· #1"), active.index("· #2"))
        self.assertLess(active.index('<a id="pr-2">'), active.index('<a id="pr-1">'))
        self.assertIn("(#pr-1)", active)

    def test_comments_do_not_keep_72h_index_alive(self):
        self.add()
        self.db.update_ci(1, "passed", now=T)
        self.db.ingest_discovery([pr(updated="2026-11-20T00:00:00Z")], True, "2026-11-20T00:00:00Z")
        active, _ = self.db.render("2026-11-20T00:00:00Z")
        self.assertIn("暂无近期更新", active)
        self.assertIn('<a id="pr-1">', active)

    def test_duplicate_discovery_rejected(self):
        with self.assertRaises(ValueError):
            self.db.ingest_discovery([pr(), pr()], True, T)
        self.assertIsNone(self.db.row(1))

    def test_title_is_escaped(self):
        self.add(title="a [b] <script>\n*oops*")
        active, _ = self.db.render(T)
        self.assertNotIn("<script>", active)
        self.assertIn("\\[b\\]", active)

    def test_scope_does_not_use_discovery_or_updated(self):
        self.db.ingest_discovery([pr(created="2025-01-01T00:00:00Z", updated=T)], True, T)
        self.assertEqual(self.db.scope_active(T), [])
        self.assertEqual(self.db.row(1)["activity_at"], "2025-01-01T00:00:00Z")
        active, _ = self.db.render(T)
        self.assertIn("活动待确认：1", active)
        self.assertNotIn("文件范围或详情待补齐", active)
        self.db.record_activity_probe(1, "inactive", T)
        self.assertNotIn("活动待确认", self.db.render(T)[0])

    def test_old_ci_first_observation_not_now_activity(self):
        self.db.ingest_discovery([pr(created="2025-01-01T00:00:00Z")], True, T)
        self.db.update_ci(1, "failed", True, T)
        self.assertEqual(self.db.scope_active(T), [])
        self.db.update_ci(1, "failed", True, T, activity_at="2025-01-02T00:00:00Z")
        self.assertEqual(self.db.scope_active(T), [])
        self.db.update_ci(1, "failed", True, T, activity_at="2026-11-11T00:00:00Z")
        self.assertEqual(self.db.scope_active(T), [1])
        self.assertEqual(self.db.row(1)["activity_kind"], "ci")

    def test_commit_evidence_enters_scope_and_expires(self):
        self.db.ingest_discovery([pr(created="2025-01-01T00:00:00Z")], True, T)
        self.db.record_activity(1, "2026-11-11T00:00:00Z", "commit", "head SHA a commit timestamp")
        self.assertEqual(self.db.scope_active(T), [1])
        self.assertEqual(self.db.scope_active("2026-12-12T00:00:00Z"), [])
        self.assertEqual(self.db.ci_due("2026-12-12T00:00:00Z"), [])

    def test_observed_head_change_is_real_activity(self):
        self.db.ingest_discovery([pr(created="2025-01-01T00:00:00Z")], True, T)
        later = "2026-11-12T02:00:00Z"
        self.db.ingest_discovery([pr(created="2025-01-01T00:00:00Z", head="b")], True, later)
        self.assertEqual(self.db.scope_active(later), [1])
        self.assertEqual(self.db.row(1)["activity_kind"], "head")

    def test_activity_probe_reset_on_updated_only_no_scope_change(self):
        self.db.ingest_discovery([pr(created="2025-01-01T00:00:00Z")], True, T)
        self.db.record_activity_probe(1, "inactive", T)
        later = "2026-11-12T02:00:00Z"
        self.db.ingest_discovery([pr(created="2025-01-01T00:00:00Z", updated=later)], True, later)
        self.assertIsNone(self.db.row(1)["activity_probe_result"])
        self.assertEqual(self.db.scope_active(later), [])

    def test_activity_migration_ignores_fake_meaningful_time(self):
        self.db.ingest_discovery([pr(created="2025-01-01T00:00:00Z")], True, T)
        self.db.conn.execute("UPDATE prs SET activity_at=NULL,latest_commit_at='2025-02-01T00:00:00Z',meaningful_updated_at=?", (T,))
        self.db.conn.commit()
        self.db.close()
        fixture=Path(self.tmp.name)/"legacy.yaml"
        fixture.write_text('# PR Watch V1: explicit keep rules take precedence over exclusions.\n# Unmatched paths are included; do not expand exclusions automatically.\nversion: 1\nkeep:\n  - .github/**\n  - tests/e2e/common/**\n  - tests/e2e/doctests/**\n  - tests/e2e/nightly/**/scripts/**\n  - tests/ut/_tools/**\n  - tests/ut/tools/**\nexclude:\n  - vllm_ascend/**\n  - docs/source/tutorials/models/**\n  - docs/source/user_guide/feature_guide/**\n  - docs/source/user_guide/support_matrix/**\n  - tests/SIT/cases/models/**\n  - tests/SIT/cases/features/**\n  - tests/e2e/pull_request/**\n  - tests/e2e/nightly/**\n  - tests/ut/**/test_*.py\n')
        self.db = WatchDB(Path(self.tmp.name) / "watch.db", fixture)
        self.assertEqual(self.db.row(1)["activity_at"], "2025-02-01T00:00:00Z")
        self.assertEqual(self.db.scope_active(T), [])

    def test_missing_unmatched_not_selected_or_pending(self):
        self.db.ingest_discovery([pr()], True, T)
        later = "2026-11-12T02:00:00Z"
        self.db.ingest_discovery([], True, later)
        self.assertEqual(self.db.scope_active(later), [])
        self.assertEqual(self.db.row(1)["state"], "open")
        self.assertNotIn("文件范围或详情待补齐", self.db.render(later)[0])
        self.db.ingest_discovery([], False, "2026-11-12T03:00:00Z")
        self.assertEqual(self.db.scope_active(later), [])

    def test_missing_matched_retained_pending_final_confirmation(self):
        self.add()
        later = "2026-11-12T02:00:00Z"
        self.db.ingest_discovery([], True, later)
        self.assertEqual(self.db.scope_active(later), [1])
        self.assertIn("最终状态待确认：1", self.db.render(later)[0])
        self.db.confirm_closed(1, "merged", later)
        self.assertIn("已合入", self.db.render("2027-01-01T00:00:00Z")[1])

    def test_newer_partial_proves_presence_not_absence(self):
        self.db.ingest_discovery([], True, T)
        later = "2026-11-12T02:00:00Z"
        self.db.ingest_discovery([pr()], False, later)
        self.assertEqual(self.db.scope_active(later), [1])
        self.assertIn("1 个近 30 天范围内的 PR 文件范围或详情待补齐", self.db.render(later)[0])

    def test_failed_refresh_does_not_reset_success_clock(self):
        self.add()
        self.db.update_ci(1, "passed", now=T)
        failed_at = "2026-11-12T01:30:00Z"
        self.db.update_ci(1, "unknown", now=failed_at, complete=False)
        row = self.db.row(1)
        self.assertEqual(row["ci_success_at"], T)
        self.assertEqual(row["ci_checked_at"], T)
        self.assertEqual(row["ci_attempted_at"], failed_at)
        self.assertEqual(self.db.ci_due("2026-11-12T01:31:00Z"), [1])
        self.db.update_ci(1, "passed", now="2026-11-12T02:00:00Z", activity_at="2026-11-12T02:00:00Z")
        self.assertEqual(self.db.row(1)["ci_success_at"], "2026-11-12T02:00:00Z")

    def test_due_fair_rotation_uses_actual_attempt_not_number(self):
        self.db.ingest_discovery([pr(1), pr(2), pr(3)], True, T)
        for number in (1, 2, 3):
            self.db.update_detail(number, ["tools/a.py"], 1, 0, T, "改动。", "a", T)
        self.assertEqual(self.db.ci_due(T), [1, 2, 3])
        self.db.update_ci(1, "unknown", complete=False, now=T)
        self.assertEqual(self.db.ci_due(T), [2, 3, 1])
        self.db.update_ci(2, "passed", now="2026-11-12T01:10:00Z")
        self.db.update_ci(3, "unknown", complete=False, now="2026-11-12T01:20:00Z")
        self.assertEqual(self.db.ci_due("2026-11-12T02:30:00Z"), [1, 2, 3])
        self.db.update_ci(1, "unknown", complete=False, now="2026-11-12T02:30:00Z")
        self.assertEqual(self.db.ci_due("2026-11-12T02:31:00Z"), [2, 3, 1])

    def test_unattempted_budget_deferral_preserves_clocks_and_order(self):
        self.add()
        self.db.update_ci(1, "passed", now=T)
        before = self.db.row(1)
        later = "2026-11-12T02:00:00Z"
        self.db.mark_ci_deferred([1], later)
        after = self.db.row(1)
        for key in ("ci_state", "ci_checked_at", "ci_success_at", "ci_attempted_at", "meaningful_updated_at"):
            self.assertEqual(after[key], before[key])
        report = self.db.render(later)[0]
        self.assertIn("CI 待刷新：1", report)
        self.assertIn("**CI：** 未知（待刷新", report)
        self.assertIn("上次完整检查：11-12 09:00 · 通过", report)
        self.db.update_ci(1, "passed", now=later)
        self.assertIsNone(self.db.row(1)["ci_deferred_at"])
        self.assertNotIn("CI 待刷新", self.db.render(later)[0])

    def test_ci_success_migration_does_not_invent_failed_success(self):
        self.db.ingest_discovery([pr(1), pr(2)], True, T)
        self.db.update_ci(1, "passed", now=T)
        self.db.update_ci(2, "unknown", complete=False, now=T)
        # Reproduce old version: ci_checked_at was overwritten by failed attempts.
        self.db.conn.execute("UPDATE prs SET ci_checked_at=? WHERE number=2", (T,))
        for col in ("ci_success_at", "ci_attempted_at", "ci_deferred_at", "ci_deferred_reason"):
            self.db.conn.execute(f"ALTER TABLE prs DROP COLUMN {col}")
        self.db.conn.commit()
        self.db.close()
        fixture=Path(self.tmp.name)/"legacy.yaml"
        fixture.write_text('# PR Watch V1: explicit keep rules take precedence over exclusions.\n# Unmatched paths are included; do not expand exclusions automatically.\nversion: 1\nkeep:\n  - .github/**\n  - tests/e2e/common/**\n  - tests/e2e/doctests/**\n  - tests/e2e/nightly/**/scripts/**\n  - tests/ut/_tools/**\n  - tests/ut/tools/**\nexclude:\n  - vllm_ascend/**\n  - docs/source/tutorials/models/**\n  - docs/source/user_guide/feature_guide/**\n  - docs/source/user_guide/support_matrix/**\n  - tests/SIT/cases/models/**\n  - tests/SIT/cases/features/**\n  - tests/e2e/pull_request/**\n  - tests/e2e/nightly/**\n  - tests/ut/**/test_*.py\n')
        self.db = WatchDB(Path(self.tmp.name) / "watch.db", fixture)
        self.assertEqual(self.db.row(1)["ci_success_at"], T)
        self.assertEqual(self.db.row(1)["ci_attempted_at"], T)
        self.assertIsNone(self.db.row(2)["ci_success_at"])
        self.assertIsNone(self.db.row(2)["ci_checked_at"])
        self.assertIsNone(self.db.row(2)["ci_attempted_at"])


class CITests(unittest.TestCase):
    def test_states(self):
        self.assertEqual(aggregate_ci([])["state"], "unknown")
        self.assertEqual(aggregate_ci([{"status": "completed", "conclusion": "success"}])["state"], "passed")
        self.assertEqual(aggregate_ci([{"status": "queued", "conclusion": None}])["state"], "pending")
        self.assertEqual(aggregate_ci([{"status": "completed", "conclusion": "failure", "name": "ci-gate"}]), {"state": "failed", "ci_gate": True})
        self.assertEqual(aggregate_ci([{"status": "completed", "conclusion": "success"}], complete=False)["state"], "unknown")
        self.assertEqual(aggregate_ci([], [{"state": "success"}])["state"], "passed")

    def test_failure_dominates_pending(self):
        self.assertEqual(aggregate_ci([{"conclusion": "failure"}, {"status": "queued"}])["state"], "failed")

    def test_naive_time_rejected(self):
        with self.assertRaises(ValueError):
            instant("2026-11-12T01:00:00")


if __name__ == "__main__":
    unittest.main()

class ScopeV2Tests(unittest.TestCase):
    def test_root_glob_and_semantic_cache(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t);r=p/'rules';r.write_text('version: 2\nkeep: [".github/**", "tests/ut/_tools/**"]\nexclude: ["/*.patch", "vllm_ascend/**", "tests/ut/**/test_*.py"]\n')
            db=WatchDB(p/'db',r)
            self.assertFalse(db.rules.included('a.patch'));self.assertTrue(db.rules.included('nested/a.patch'))
            db.ingest_discovery([pr()],True,T);db.update_detail(1,['tests/ut/_tools/test_model.py'],now=T)
            self.assertFalse(db.row(1)['matched']);self.assertEqual(len(db.semantic_pending(T)),1)
            db.apply_scope_decision(1,'include','通用mock工具', 'a','main');self.assertTrue(db.row(1)['matched'])
            db.update_detail(1,['.github/a.yml'],now=T)
            with self.assertRaises(ValueError):db.apply_scope_decision(1,'exclude','model test','a','main')
            db.close()
    def test_initial_observation_not_recent(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t);r=p/'rules';r.write_text('version: 2\nkeep: [".github/**"]\nexclude: []\n')
            db=WatchDB(p/'db',r);db.ingest_discovery([pr()],True,T);db.update_detail(1,['.github/a.yml'],now=T)
            a,_=db.render(T);self.assertIn('暂无近期更新。',a);db.close()
