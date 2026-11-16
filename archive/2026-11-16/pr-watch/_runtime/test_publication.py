import unittest
from publication import merge_archive,archive_sections
class Tests(unittest.TestCase):
 def test_preserve(self):
  old='# PR 归档\n\n<a id="pr-1"></a>\n\n### PR 1\n\n**已关闭：** 2026-01-01 09:00:00\n'
  new='# PR 归档\n\n暂无归档。\n'
  self.assertIn('pr-1',merge_archive(new,old));self.assertNotIn('暂无归档',merge_archive(new,old))
 def test_new_wins(self):
  a='<a id="pr-1"></a>\n**已关闭：** 2026-01-01 09:00:00\n'
  b='<a id="pr-1"></a>\n**已合入：** 2026-01-02 09:00:00\n'
  self.assertEqual(merge_archive(b,a).count('pr-1'),1);self.assertIn('已合入',merge_archive(b,a))
 def test_bad(self):
  with self.assertRaises(ValueError):archive_sections('<a id="pr-1"></a>\nmissing time')
if __name__=='__main__':unittest.main()

class PrunedArchiveTest(unittest.TestCase):
    def test_explicit_prune_survives_remote_merge(self):
        from publication import merge_archive
        remote='# PR 归档\n\n<a id="pr-21681"></a>\n### PR\n**已合入：** 2026-11-11 01:00:00\n'
        result=merge_archive('# PR 归档\n\n<!-- pr-watch-pruned: [21681] -->\n\n暂无归档。',remote)
        self.assertNotIn('<a id="pr-21681">',result);self.assertIn('pr-watch-pruned: [21681]',result)
