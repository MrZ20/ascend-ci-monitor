# PR 关注列表

最近刷新：2026-11-13 16:52:30（上海时间）
当前关注的开放 PR：53

优先关注近期新增或代码变更；CI 分批轮转，以下保留最近已知结果与检查时间。

## 最近更新（72h）

- [11-13 16:42 · #20345 \[Performance\]\[Worker\] Reuse V2 attention metadata across cache groups and batch GDN state writes](#pr-20345)
- [11-13 16:39 · #21674 \[CI\] run.sh](#pr-21674)
- [11-13 16:37 · #21685 \[CI\] add presmoke for CI](#pr-21685)
- [11-13 16:37 · #21541 \[Doc\] add doc quality review workflow for docs/source changes](#pr-21541)
- [11-13 16:37 · #21469 \[Misc\] main2main: upgrade verified vLLM main from 1106 to 1112](#pr-21469)
- [11-13 16:37 · #20926 \[Feature\]\[HiSparse\] Add Ascend backend foundation](#pr-20926)
- [11-13 16:37 · #20633 \[CI\] add test cases for Qwen3.6-35B-w8a8](#pr-20633)
- [11-13 16:30 · #17833 \[Feature\]\[Worker\] Add MRV2 KV Trace without Scheduler patches](#pr-17833)
- [11-13 15:39 · #21481 \[CI\] memcache cases](#pr-21481)
- [11-13 15:37 · #21751 \[Feature\]\[Model\] Add Qwen PLE UVA host offload with DP memory sharing](#pr-21751)
- [11-13 15:37 · #21697 \[BugFix\]\[CI\] Add Qwen3.8 TP2 IPC coverage and preserve PLE sleep state](#pr-21697)
- [11-13 15:37 · #20575 \[CI\]\[Model\] Add combined GLM-5.3 P/PD/decode Weekly coverage](#pr-20575)
- [11-13 15:11 · #21385 \[releases/v0.30.0\]\[Test\]\[Feature\] Add Kimi-K3 W4A8 E256 accuracy test on A5](#pr-21385)
- [11-13 15:11 · #21284 \[Test\] Add five-round Kimi-K3 Experts256 A5 nightly coverage](#pr-21284)
- [11-13 15:09 · #21699 \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.32.0rc](#pr-21699)
- [11-13 12:03 · #20756 \[BugFix\]\[Model\] Support dense sequence parallelism for the Qwen3.5 family (Qwen3.8-27B)](#pr-20756)
- [11-13 12:00 · #21713 \[BugFix\] Rename static operator build option to --soc\_series](#pr-21713)
- [11-13 12:00 · #21789 \[DevContainer\]\[Feature\] Add Dev Container environment settings for 310P/A2/A3/A5/CPU](#pr-21789)
- [11-13 11:53 · #21310 \[Refactor\]\[Core\] Remove dynamic chunk size CPP feature, configuration, and documentation](#pr-21310)
- [11-13 11:50 · #21778 \[CI\] Align weekly scheduling with nightly and extend multi-node timeouts](#pr-21778)
- [11-13 11:50 · #18604 \[Feature\]\[MoE\] Add exact expert offload for V2 eager and decode ACL graphs](#pr-18604)
- [11-13 10:34 · #21777 fix: pin torch==2.10.0+cpu to match torch-npu dependency](#pr-21777)
- [11-13 09:49 · #21653 \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.30.0](#pr-21653)
- [11-13 00:05 · #21746 test: cover Qwen3.6 Model Runner V2 with main-recorded goldens](#pr-21746)
- [11-12 20:00 · #20612 \[Feature\]\[Engram\] Share A2/A5 host tables across P/D instances via RDMA](#pr-20612)
- [11-12 19:54 · #21712 \[Doc\]\[Misc\] Document Ascend Docker Runtime container setup](#pr-21712)
- [11-12 18:41 · #21714 \[Refactor\]\[MRV2\] Adopt EPLB policy and model-state hooks](#pr-21714)
- [11-12 18:34 · #21705 \[Feature\] DSpark expert-pool routing for the expert-offload path](#pr-21705)
- [11-12 18:31 · #21717 \[CI\] Restore A5 multi-node nightly test cases](#pr-21717)
- [11-12 18:10 · #21716 \[临时/勿合入\] ci: route Nightly-A2 cases to offline-cluster runner labels](#pr-21716)
- [11-12 17:00 · #21701 \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](#pr-21701)
- [11-12 15:54 · #21689 \[CI\] Isolate lint images by branch and add a lightweight tools image](#pr-21689)
- [11-12 15:52 · #21594 \[Feature\]\[MoE\] Support anchor-union activation routing for DSpark and DFlash speculative decoding](#pr-21594)
- [11-12 15:52 · #21680 \[Feature\]\[MoE\] Add opt-in DSpark expert-pool routing for expert offload](#pr-21680)
- [11-12 14:50 · #20205 \[Feature\] Support draft model weight updates over HCCL](#pr-20205)
- [11-12 12:42 · #21607 \[Test\]\[Upstream\]rerun failed test case](#pr-21607)
- [11-12 12:04 · #21661 \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](#pr-21661)
- [11-12 11:00 · #21623 \[Feature\]\[Engram\] Add local host VMM for shared A3 tables](#pr-21623)
- [11-12 10:47 · #21490 \[临时/勿合入\] 全量 A2/A3 业务选测跑 karc fed runner（对齐 #20716）](#pr-21490)
- [11-12 10:13 · #21643 \[Feature\]\[EC Connector\] Support encoder cache tiering offload on Ascend](#pr-21643)
- [11-12 09:10 · #21638 \[Feature\]\[Qwen\] Share PLE tables across Ascend services](#pr-21638)
- [11-11 15:23 · #21521 Upgrade/cann v0.32](#pr-21521)
- [11-11 14:46 · #21546 \[CI\] update cann=9.3.0\_20261110170400](#pr-21546)
- [11-11 14:43 · #21526 \[Performance\]\[Kernel\] Fuse DeepSeek-V4.1 indexer prologue on Ascend A2/A3](#pr-21526)
- [11-11 11:16 · #21513 \[Doc\] Add deepseek\_v41\_qli\_candidate to nav and fix FAQ anchor](#pr-21513)
- [11-11 00:22 · #21502 \[Feature\]\[Performance\] Support InternLM2-20B-Chat and dispatch scaled RoPE variants to the NPU kernel](#pr-21502)
- [11-10 23:09 · #21493 \[临时/勿合入\] a3-800i fed-2 / fed-4 各跑 3 个用例（验证 runner 作业 pod）](#pr-21493)
- [11-10 23:04 · #21500 \[BugFix\] Reap stale opc locks and cap build parallelism by cgroup memory limit](#pr-21500)
- [11-10 22:16 · #21479 \[CI\]\[BugFix\] Skip CANN 9.2.x custom-op .so validation in A5 wheel build](#pr-21479)
- [11-10 20:43 · #21489 \[Test\]\[Feature\] Add GLM-5.3 W4A4C8 MTP coverage on A5](#pr-21489)
- [11-10 20:15 · #21480 \[Cherry-pick\]\[releases/v0.32.0rc\]\[CI\]\[BugFix\] Skip CANN 9.2.x custom-op .so validation in A5 wheel build (from #21479)](#pr-21480)
- [11-10 19:26 · #21456 \[Refactor\]\[CP\] Decouple PCP/DCP metadata, topology and backend selection](#pr-21456)
- [11-10 18:58 · #21459 \[临时/勿合入\] 验证 karc 线下成员：a3-800i-fed-16 + a2-fed-2 smoke](#pr-21459)

## 当前关注

<a id="pr-21789"></a>

### [#21789 · \[DevContainer\]\[Feature\] Add Dev Container environment settings for 310P/A2/A3/A5/CPU](https://github.com/vllm-project/vllm-ascend/pull/21789)

新增 CPU、310P、A2、A3、A5 的开发容器配置，统一源码挂载、编辑器格式化、依赖安装和 ccache 缓存；各硬件配置设置对应 CANN 镜像与编译环境。

**CI：** 失败（最近已知；待刷新；上次完整检查：11-13 15:37；当前提交） · **改动：** +315 / -0 · **最后提交：** 11-13 11:36

<a id="pr-21778"></a>

### [#21778 · \[CI\] Align weekly scheduling with nightly and extend multi-node timeouts](https://github.com/vllm-project/vllm-ascend/pull/21778)

为 nightly/weekly 工作流增加显式 drain\_pr\_runs 开关，避免普通手动调度误取消 PR 运行，并按测试分支隔离部分并发组。区分测试执行与整体 Job 超时，给排队和日志上传预留时间，同时更新贡献文档。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-13 15:37；当前提交） · **改动：** +381 / -45 · **最后提交：** 11-13 11:28

<a id="pr-21777"></a>

### [#21777 · fix: pin torch==2.10.0+cpu to match torch-npu dependency](https://github.com/vllm-project/vllm-ascend/pull/21777)

将构建配置与运行依赖中的 PyTorch 固定版本从 2.10.0 改为 2.10.0+cpu。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 15:37；当前提交） · **改动：** +6 / -2 · **最后提交：** 11-13 10:24

<a id="pr-21751"></a>

### [#21751 · \[Feature\]\[Model\] Add Qwen PLE UVA host offload with DP memory sharing](https://github.com/vllm-project/vllm-ascend/pull/21751)

在 CI 预计耗时清单中登记 PLE host lookup 单卡 Triton 测试，预计运行 30 秒。

**CI：** 失败（最近已知；待刷新；上次完整检查：11-13 15:11；旧提交） · **改动：** +877 / -32 · **最后提交：** 11-13 15:29

<a id="pr-21746"></a>

### [#21746 · test: cover Qwen3.6 Model Runner V2 with main-recorded goldens](https://github.com/vllm-project/vllm-ascend/pull/21746)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-13 15:11；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21717"></a>

### [#21717 · \[CI\] Restore A5 multi-node nightly test cases](https://github.com/vllm-project/vllm-ascend/pull/21717)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-13 15:11；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21716"></a>

### [#21716 · \[临时/勿合入\] ci: route Nightly-A2 cases to offline-cluster runner labels](https://github.com/vllm-project/vllm-ascend/pull/21716)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 15:11；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21714"></a>

### [#21714 · \[Refactor\]\[MRV2\] Adopt EPLB policy and model-state hooks](https://github.com/vllm-project/vllm-ascend/pull/21714)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 15:11；当前提交） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21713"></a>

### [#21713 · \[BugFix\] Rename static operator build option to --soc\_series](https://github.com/vllm-project/vllm-ascend/pull/21713)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-13 15:11；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21712"></a>

### [#21712 · \[Doc\]\[Misc\] Document Ascend Docker Runtime container setup](https://github.com/vllm-project/vllm-ascend/pull/21712)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 15:11；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21705"></a>

### [#21705 · \[Feature\] DSpark expert-pool routing for the expert-offload path](https://github.com/vllm-project/vllm-ascend/pull/21705)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 15:11；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21701"></a>

### [#21701 · \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](https://github.com/vllm-project/vllm-ascend/pull/21701)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-13 15:11；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21699"></a>

### [#21699 · \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.32.0rc](https://github.com/vllm-project/vllm-ascend/pull/21699)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 运行中（最近已知；待刷新；上次完整检查：11-13 15:11；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21697"></a>

### [#21697 · \[BugFix\]\[CI\] Add Qwen3.8 TP2 IPC coverage and preserve PLE sleep state](https://github.com/vllm-project/vllm-ascend/pull/21697)

在 CI 预计耗时清单中登记 Qwen3.8 双卡 RLHF IPC 权重传输测试，预计运行 180 秒。

**CI：** 失败（ci-gate） · **改动：** +293 / -4 · **最后提交：** 11-13 15:29

<a id="pr-21689"></a>

### [#21689 · \[CI\] Isolate lint images by branch and add a lightweight tools image](https://github.com/vllm-project/vllm-ascend/pull/21689)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 15:11；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21685"></a>

### [#21685 · \[CI\] add presmoke for CI](https://github.com/vllm-project/vllm-ascend/pull/21685)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-13 15:11；旧提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21680"></a>

### [#21680 · \[Feature\]\[MoE\] Add opt-in DSpark expert-pool routing for expert offload](https://github.com/vllm-project/vllm-ascend/pull/21680)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 15:11；当前提交） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21674"></a>

### [#21674 · \[CI\] run.sh](https://github.com/vllm-project/vllm-ascend/pull/21674)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21661"></a>

### [#21661 · \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](https://github.com/vllm-project/vllm-ascend/pull/21661)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（最近已知；待刷新；上次完整检查：11-13 15:11；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21653"></a>

### [#21653 · \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.30.0](https://github.com/vllm-project/vllm-ascend/pull/21653)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-13 15:11；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21643"></a>

### [#21643 · \[Feature\]\[EC Connector\] Support encoder cache tiering offload on Ascend](https://github.com/vllm-project/vllm-ascend/pull/21643)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21638"></a>

### [#21638 · \[Feature\]\[Qwen\] Share PLE tables across Ascend services](https://github.com/vllm-project/vllm-ascend/pull/21638)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21623"></a>

### [#21623 · \[Feature\]\[Engram\] Add local host VMM for shared A3 tables](https://github.com/vllm-project/vllm-ascend/pull/21623)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21607"></a>

### [#21607 · \[Test\]\[Upstream\]rerun failed test case](https://github.com/vllm-project/vllm-ascend/pull/21607)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21594"></a>

### [#21594 · \[Feature\]\[MoE\] Support anchor-union activation routing for DSpark and DFlash speculative decoding](https://github.com/vllm-project/vllm-ascend/pull/21594)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21546"></a>

### [#21546 · \[CI\] update cann=9.3.0\_20261110170400](https://github.com/vllm-project/vllm-ascend/pull/21546)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21541"></a>

### [#21541 · \[Doc\] add doc quality review workflow for docs/source changes](https://github.com/vllm-project/vllm-ascend/pull/21541)

新增文档质量检查工作流及配套脚本，对 Markdown 与 PO 翻译文件执行规则和 LLM 评估，生成可更新的 PR 汇总评论与定位到差异行的评论。支持标签、授权成员命令和手动触发，并保留评估产物。

**CI：** 失败（ci-gate） · **改动：** +2122 / -0 · **最后提交：** 11-13 16:29 · **Draft**

<a id="pr-21526"></a>

### [#21526 · \[Performance\]\[Kernel\] Fuse DeepSeek-V4.1 indexer prologue on Ascend A2/A3](https://github.com/vllm-project/vllm-ascend/pull/21526)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21521"></a>

### [#21521 · Upgrade/cann v0.32](https://github.com/vllm-project/vllm-ascend/pull/21521)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21513"></a>

### [#21513 · \[Doc\] Add deepseek\_v41\_qli\_candidate to nav and fix FAQ anchor](https://github.com/vllm-project/vllm-ascend/pull/21513)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21502"></a>

### [#21502 · \[Feature\]\[Performance\] Support InternLM2-20B-Chat and dispatch scaled RoPE variants to the NPU kernel](https://github.com/vllm-project/vllm-ascend/pull/21502)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 15:37；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21500"></a>

### [#21500 · \[BugFix\] Reap stale opc locks and cap build parallelism by cgroup memory limit](https://github.com/vllm-project/vllm-ascend/pull/21500)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 15:37；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21493"></a>

### [#21493 · \[临时/勿合入\] a3-800i fed-2 / fed-4 各跑 3 个用例（验证 runner 作业 pod）](https://github.com/vllm-project/vllm-ascend/pull/21493)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（最近已知；待刷新；上次完整检查：11-13 15:37；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21490"></a>

### [#21490 · \[临时/勿合入\] 全量 A2/A3 业务选测跑 karc fed runner（对齐 #20716）](https://github.com/vllm-project/vllm-ascend/pull/21490)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（最近已知；待刷新；上次完整检查：11-13 15:37；当前提交） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21489"></a>

### [#21489 · \[Test\]\[Feature\] Add GLM-5.3 W4A4C8 MTP coverage on A5](https://github.com/vllm-project/vllm-ascend/pull/21489)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-13 15:37；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21481"></a>

### [#21481 · \[CI\] memcache cases](https://github.com/vllm-project/vllm-ascend/pull/21481)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-13 15:37；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21480"></a>

### [#21480 · \[Cherry-pick\]\[releases/v0.32.0rc\]\[CI\]\[BugFix\] Skip CANN 9.2.x custom-op .so validation in A5 wheel build (from #21479)](https://github.com/vllm-project/vllm-ascend/pull/21480)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-13 15:37；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21479"></a>

### [#21479 · \[CI\]\[BugFix\] Skip CANN 9.2.x custom-op .so validation in A5 wheel build](https://github.com/vllm-project/vllm-ascend/pull/21479)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 15:37；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21469"></a>

### [#21469 · \[Misc\] main2main: upgrade verified vLLM main from 1106 to 1112](https://github.com/vllm-project/vllm-ascend/pull/21469)

将 vLLM main 验证提交标记更新为 3b95523ed904cf02a26b872f4a900ef17e6be8ad，并在 CI 耗时清单中登记 categorical sample bias 单卡测试，预计 120 秒。

**CI：** 运行中（最近已知；待刷新；上次完整检查：11-13 15:37；旧提交） · **改动：** +3485 / -421 · **最后提交：** 11-13 16:01 · **Draft**

<a id="pr-21459"></a>

### [#21459 · \[临时/勿合入\] 验证 karc 线下成员：a3-800i-fed-16 + a2-fed-2 smoke](https://github.com/vllm-project/vllm-ascend/pull/21459)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（最近已知；待刷新；上次完整检查：11-13 15:37；当前提交） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21456"></a>

### [#21456 · \[Refactor\]\[CP\] Decouple PCP/DCP metadata, topology and backend selection](https://github.com/vllm-project/vllm-ascend/pull/21456)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21385"></a>

### [#21385 · \[releases/v0.30.0\]\[Test\]\[Feature\] Add Kimi-K3 W4A8 E256 accuracy test on A5](https://github.com/vllm-project/vllm-ascend/pull/21385)

为发布分支的 A5 nightly 工作流增加诊断文件收集和 AOP 二分日志上传，并接入 Kimi-K3 测试任务。通用单节点测试框架新增独立多轮执行及逐轮产物保留。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 15:37；当前提交） · **改动：** +592 / -4 · **最后提交：** 11-13 14:51

<a id="pr-21310"></a>

### [#21310 · \[Refactor\]\[Core\] Remove dynamic chunk size CPP feature, configuration, and documentation](https://github.com/vllm-project/vllm-ascend/pull/21310)

从 CI 测试清单和耗时预估中移除 profiling chunk performance 用例，并移除文档导航中的动态分块流水线并行入口。

**CI：** 通过 · **改动：** +188 / -5388 · **最后提交：** 11-12 19:53

<a id="pr-21284"></a>

### [#21284 · \[Test\] Add five-round Kimi-K3 Experts256 A5 nightly coverage](https://github.com/vllm-project/vllm-ascend/pull/21284)

在 A5 nightly 配置中接入 Kimi-K3 任务，默认启用 AOP 并收集该任务的诊断产物，允许跳过缺失的可选日志。通用单节点测试入口新增多轮参数化执行及逐轮结果归档。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 15:37；当前提交） · **改动：** +354 / -5 · **最后提交：** 11-13 14:51

<a id="pr-20926"></a>

### [#20926 · \[Feature\]\[HiSparse\] Add Ascend backend foundation](https://github.com/vllm-project/vllm-ascend/pull/20926)

将三个 HiSparse 单卡测试加入 CI 选择与 A5 runner 映射，预计各 30 秒，并加入文档导航及中英文标题。构建配置在 A5 工具链具备 SIMT 头文件时启用对应算子和 Torch 适配。

**CI：** 未知（待刷新；尚无完整检查记录） · **改动：** +6997 / -96 · **最后提交：** 11-13 16:26

<a id="pr-20756"></a>

### [#20756 · \[BugFix\]\[Model\] Support dense sequence parallelism for the Qwen3.5 family (Qwen3.8-27B)](https://github.com/vllm-project/vllm-ascend/pull/20756)

为 Qwen3.8-27B dense SP 双卡端到端用例新增 600 秒的 CI 调度预估时长。

**CI：** 未知（待刷新；尚无完整检查记录） · **改动：** +779 / -28 · **最后提交：** 11-13 12:03

<a id="pr-20633"></a>

### [#20633 · \[CI\] add test cases for Qwen3.6-35B-w8a8](https://github.com/vllm-project/vllm-ascend/pull/20633)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-20612"></a>

### [#20612 · \[Feature\]\[Engram\] Share A2/A5 host tables across P/D instances via RDMA](https://github.com/vllm-project/vllm-ascend/pull/20612)

构建配置新增可选 engram\_hixl 共享库：仅在检测到 HIXL 头文件和 cann\_hixl 库后构建、链接并安装，同时设为主扩展依赖。

**CI：** 未知（待刷新；尚无完整检查记录） · **改动：** +2407 / -22 · **最后提交：** 11-12 20:00

<a id="pr-20575"></a>

### [#20575 · \[CI\]\[Model\] Add combined GLM-5.3 P/PD/decode Weekly coverage](https://github.com/vllm-project/vllm-ascend/pull/20575)

为 Weekly-A3 增加 GLM-5.3 分拆及组合测试矩阵，并新增可由 PR 命令触发的 Weekly-A5 工作流与产物汇总。通用多节点配置解析同步支持替换基准参数中的集群地址占位符。

**CI：** 失败（ci-gate） · **改动：** +3577 / -5 · **最后提交：** 11-13 15:16 · **Draft**

<a id="pr-20345"></a>

### [#20345 · \[Performance\]\[Worker\] Reuse V2 attention metadata across cache groups and batch GDN state writes](https://github.com/vllm-project/vllm-ascend/pull/20345)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 运行中 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-20205"></a>

### [#20205 · \[Feature\] Support draft model weight updates over HCCL](https://github.com/vllm-project/vllm-ascend/pull/20205)

在 CI 的预计耗时清单中登记双卡 RLHF draft HCCL 权重传输测试，预计运行 510 秒。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 15:37；当前提交） · **改动：** +739 / -52 · **最后提交：** 11-12 14:45

<a id="pr-18604"></a>

### [#18604 · \[Feature\]\[MoE\] Add exact expert offload for V2 eager and decode ACL graphs](https://github.com/vllm-project/vllm-ascend/pull/18604)

将 expert offload 的单卡端到端用例加入 A5 精选 CI 测试集，指定 a5-4 runner，并设置 600 秒调度预估时长。

**CI：** 未知（待刷新；尚无完整检查记录） · **改动：** +2017 / -0 · **最后提交：** 11-13 11:50

<a id="pr-17833"></a>

### [#17833 · \[Feature\]\[Worker\] Add MRV2 KV Trace without Scheduler patches](https://github.com/vllm-project/vllm-ascend/pull/17833)

在 MkDocs 用户指南导航中加入 KV trace 页面入口，并新增 debug 单测包的初始化文件。

**CI：** 未知（待刷新；尚无完整检查记录） · **改动：** +1692 / -1 · **最后提交：** 11-13 16:30
