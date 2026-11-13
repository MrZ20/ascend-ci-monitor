# PR 归档

最近刷新：2026-11-13 17:54:42（上海时间）

仅记录开始跟踪后确认合入或关闭的 PR，不追溯全部历史。

<!-- pr-watch-pruned: [21681] -->

<a id="pr-21657"></a>

### [#21657 · \[Test\] kimi-k3 nightly](https://github.com/vllm-project/vllm-ascend/pull/21657)

在 nightly 配置中加入 Kimi-K3-W4A8-A3-1M-PD 八卡用例，指向已有模型测试配置目录。

**CI：** 未知 · **改动：** +18 / -14 · **最后提交：** 11-12 16:10 · **已合入：** 2026-11-12 20:07:26

<a id="pr-21555"></a>

### [#21555 · feat(ci): add /presmoke command for PR-level CANN image presmoke](https://github.com/vllm-project/vllm-ascend/pull/21555)

增加 PR 级 /presmoke 命令，按 PR 提交重建 CANN 基础层和 nightly 镜像并运行测试；使用独立镜像后缀且禁止同步到 quay.io。

**CI：** 未知 · **改动：** +208 / -60 · **最后提交：** 11-11 15:09 · **已关闭：** 2026-11-12 19:55:02

<a id="pr-21464"></a>

### [#21464 · \[v0.32.0rc\]\[Doc\]\[BugFix\] Fix truncated model support tables in Chinese docs](https://github.com/vllm-project/vllm-ascend/pull/21464)

修正文档翻译提取与翻译器对多层表头、表格分隔符和截断响应的处理，启用多行表格扩展并补充写作指南，避免中文支持矩阵被截断。

**CI：** 通过 · **改动：** +112 / -224 · **最后提交：** 11-12 17:26 · **已合入：** 2026-11-12 19:08:12

<a id="pr-21695"></a>

### [#21695 · \[Doc\]\[BugFix\] Fix truncated model support tables in Chinese docs](https://github.com/vllm-project/vllm-ascend/pull/21695)

修复 PO 提取与翻译对多行表头的处理，拒绝被截断的翻译响应，并为 MkDocs 增加合并单元格表格扩展和写作说明。

**CI：** 未知 · **改动：** +114 / -226 · **最后提交：** 11-12 16:00 · **已合入：** 2026-11-12 19:07:33
