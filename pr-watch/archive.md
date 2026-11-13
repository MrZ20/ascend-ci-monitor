# PR 归档

最近刷新：2026-11-14 06:49:42（上海时间）

仅记录开始跟踪后确认合入或关闭的 PR，不追溯全部历史。

<!-- pr-watch-pruned: [21681] -->

<a id="pr-21653"></a>

### [#21653 · \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.30.0](https://github.com/vllm-project/vllm-ascend/pull/21653)

新增 Ubuntu/openEuler 的 A5 UBX 镜像及构建矩阵，使用独立 CANN/PTA 版本，并支持解析 ARG 引用的基础镜像和 nightly 变体标签。同步修正 FLA 下载路径，A5 wheel 构建增加自定义算子强制安装及产物存在检查。

**CI：** 失败 · **改动：** +450 / -17 · **最后提交：** 11-13 17:14 · **已合入：** 2026-11-13 20:51:01

<a id="pr-20612"></a>

### [#20612 · \[Feature\]\[Engram\] Share A2/A5 host tables across P/D instances via RDMA](https://github.com/vllm-project/vllm-ascend/pull/20612)

构建配置新增可选 engram\_hixl 共享库：仅在检测到 HIXL 头文件和 cann\_hixl 库后构建、链接并安装，同时设为主扩展依赖。

**CI：** 运行中 · **改动：** +2407 / -22 · **最后提交：** 11-12 20:00 · **已合入：** 2026-11-13 20:15:01

<a id="pr-21223"></a>

### [#21223 · \[CI\] Add Weekly test cases](https://github.com/vllm-project/vllm-ascend/pull/21223)

为 A3 weekly 配置增加 MiniMax M3、GLM-5.3、DeepSeek-V4.1-Flash 与 GLM-5.3-Flash 的 1M 上下文 PD 测试项，分别配置对应模型 YAML 和规模。

**CI：** 未知 · **改动：** +1049 / -9 · **最后提交：** 11-13 18:33 · **已合入：** 2026-11-13 19:01:26

<a id="pr-21778"></a>

### [#21778 · \[CI\] Align weekly scheduling with nightly and extend multi-node timeouts](https://github.com/vllm-project/vllm-ascend/pull/21778)

为 nightly/weekly 工作流增加显式 drain\_pr\_runs 开关，避免普通手动调度误取消 PR 运行，并按测试分支隔离部分并发组。区分测试执行与整体 Job 超时，给排队和日志上传预留时间，同时更新贡献文档。

**CI：** 通过 · **改动：** +381 / -45 · **最后提交：** 11-13 11:28 · **已合入：** 2026-11-13 18:01:56

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
