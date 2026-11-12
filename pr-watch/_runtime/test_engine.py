import json
from pathlib import Path
import tempfile
import unittest

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
        self.db = WatchDB(Path(self.tmp.name) / "watch.db", RULES)

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
        self.assertEqual(self.db.row(1)["meaningful_updated_at"], T)

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
        self.db.update_ci(1, "passed", now="2026-11-12T02:00:00Z")
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
        self.db.update_ci(1, "passed", now="2026-11-12T02:00:00Z")
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
