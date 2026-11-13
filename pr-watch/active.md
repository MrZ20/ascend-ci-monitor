# PR 关注列表

最近刷新：2026-11-13 15:27:46（上海时间）
当前关注的开放 PR：43

优先关注近期新增或代码变更；CI 分批轮转，以下保留最近已知结果与检查时间。

## 最近更新（72h）

- [11-13 15:22 · #21751 \[Feature\]\[Model\] Add Qwen PLE UVA host offload with DP memory sharing](#pr-21751)
- [11-13 15:11 · #21587 \[Feature\] Fuse GatingTopK with EPLB expert mapping](#pr-21587)
- [11-13 15:11 · #21385 \[releases/v0.30.0\]\[Test\]\[Feature\] Add Kimi-K3 W4A8 E256 accuracy test on A5](#pr-21385)
- [11-13 15:11 · #21284 \[Test\] Add five-round Kimi-K3 Experts256 A5 nightly coverage](#pr-21284)
- [11-13 15:09 · #21699 \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.32.0rc](#pr-21699)
- [11-13 12:57 · #21469 \[Misc\] main2main: upgrade verified vLLM main from 1106 to 1112](#pr-21469)
- [11-13 12:48 · #21481 \[CI\] memcache cases](#pr-21481)
- [11-13 12:00 · #21713 \[BugFix\] Rename static operator build option to --soc\_series](#pr-21713)
- [11-13 11:36 · #21789 \[DevContainer\]\[Feature\] Add Dev Container environment settings for 310P/A2/A3/A5/CPU](#pr-21789)
- [11-13 11:28 · #21778 \[CI\] Align weekly scheduling with nightly and extend multi-node timeouts](#pr-21778)
- [11-13 10:24 · #21777 fix: pin torch==2.10.0+cpu to match torch-npu dependency](#pr-21777)
- [11-13 09:49 · #21653 \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.30.0](#pr-21653)
- [11-13 00:05 · #21746 test: cover Qwen3.6 Model Runner V2 with main-recorded goldens](#pr-21746)
- [11-12 20:34 · #21685 \[CI\] add presmoke for CI](#pr-21685)
- [11-12 19:54 · #21712 \[Doc\]\[Misc\] Document Ascend Docker Runtime container setup](#pr-21712)
- [11-12 19:08 · #21541 \[Doc\] add doc quality review workflow for docs/source changes](#pr-21541)
- [11-12 18:41 · #21714 \[Refactor\]\[MRV2\] Adopt EPLB policy and model-state hooks](#pr-21714)
- [11-12 18:34 · #21705 \[Feature\] DSpark expert-pool routing for the expert-offload path](#pr-21705)
- [11-12 18:31 · #21717 \[CI\] Restore A5 multi-node nightly test cases](#pr-21717)
- [11-12 18:10 · #21716 \[临时/勿合入\] ci: route Nightly-A2 cases to offline-cluster runner labels](#pr-21716)
- [11-12 17:00 · #21701 \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](#pr-21701)
- [11-12 15:54 · #21689 \[CI\] Isolate lint images by branch and add a lightweight tools image](#pr-21689)
- [11-12 15:52 · #21594 \[Feature\]\[MoE\] Support anchor-union activation routing for DSpark and DFlash speculative decoding](#pr-21594)
- [11-12 15:52 · #21680 \[Feature\]\[MoE\] Add opt-in DSpark expert-pool routing for expert offload](#pr-21680)
- [11-12 14:45 · #20205 \[Feature\] Support draft model weight updates over HCCL](#pr-20205)
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

**CI：** 未知（待刷新；尚无完整检查记录） · **改动：** +315 / -0 · **最后提交：** 11-13 11:36

<a id="pr-21778"></a>

### [#21778 · \[CI\] Align weekly scheduling with nightly and extend multi-node timeouts](https://github.com/vllm-project/vllm-ascend/pull/21778)

为 nightly/weekly 工作流增加显式 drain\_pr\_runs 开关，避免普通手动调度误取消 PR 运行，并按测试分支隔离部分并发组。区分测试执行与整体 Job 超时，给排队和日志上传预留时间，同时更新贡献文档。

**CI：** 未知（待刷新；尚无完整检查记录） · **改动：** +381 / -45 · **最后提交：** 11-13 11:28

<a id="pr-21777"></a>

### [#21777 · fix: pin torch==2.10.0+cpu to match torch-npu dependency](https://github.com/vllm-project/vllm-ascend/pull/21777)

将构建配置与运行依赖中的 PyTorch 固定版本从 2.10.0 改为 2.10.0+cpu。

**CI：** 未知（待刷新；尚无完整检查记录） · **改动：** +6 / -2 · **最后提交：** 11-13 10:24

<a id="pr-21751"></a>

### [#21751 · \[Feature\]\[Model\] Add Qwen PLE UVA host offload with DP memory sharing](https://github.com/vllm-project/vllm-ascend/pull/21751)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21746"></a>

### [#21746 · test: cover Qwen3.6 Model Runner V2 with main-recorded goldens](https://github.com/vllm-project/vllm-ascend/pull/21746)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21717"></a>

### [#21717 · \[CI\] Restore A5 multi-node nightly test cases](https://github.com/vllm-project/vllm-ascend/pull/21717)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21716"></a>

### [#21716 · \[临时/勿合入\] ci: route Nightly-A2 cases to offline-cluster runner labels](https://github.com/vllm-project/vllm-ascend/pull/21716)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21714"></a>

### [#21714 · \[Refactor\]\[MRV2\] Adopt EPLB policy and model-state hooks](https://github.com/vllm-project/vllm-ascend/pull/21714)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21713"></a>

### [#21713 · \[BugFix\] Rename static operator build option to --soc\_series](https://github.com/vllm-project/vllm-ascend/pull/21713)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21712"></a>

### [#21712 · \[Doc\]\[Misc\] Document Ascend Docker Runtime container setup](https://github.com/vllm-project/vllm-ascend/pull/21712)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21705"></a>

### [#21705 · \[Feature\] DSpark expert-pool routing for the expert-offload path](https://github.com/vllm-project/vllm-ascend/pull/21705)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21701"></a>

### [#21701 · \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](https://github.com/vllm-project/vllm-ascend/pull/21701)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21699"></a>

### [#21699 · \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.32.0rc](https://github.com/vllm-project/vllm-ascend/pull/21699)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 运行中 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21689"></a>

### [#21689 · \[CI\] Isolate lint images by branch and add a lightweight tools image](https://github.com/vllm-project/vllm-ascend/pull/21689)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21685"></a>

### [#21685 · \[CI\] add presmoke for CI](https://github.com/vllm-project/vllm-ascend/pull/21685)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21680"></a>

### [#21680 · \[Feature\]\[MoE\] Add opt-in DSpark expert-pool routing for expert offload](https://github.com/vllm-project/vllm-ascend/pull/21680)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21661"></a>

### [#21661 · \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](https://github.com/vllm-project/vllm-ascend/pull/21661)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21653"></a>

### [#21653 · \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.30.0](https://github.com/vllm-project/vllm-ascend/pull/21653)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21643"></a>

### [#21643 · \[Feature\]\[EC Connector\] Support encoder cache tiering offload on Ascend](https://github.com/vllm-project/vllm-ascend/pull/21643)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21638"></a>

### [#21638 · \[Feature\]\[Qwen\] Share PLE tables across Ascend services](https://github.com/vllm-project/vllm-ascend/pull/21638)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21623"></a>

### [#21623 · \[Feature\]\[Engram\] Add local host VMM for shared A3 tables](https://github.com/vllm-project/vllm-ascend/pull/21623)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21607"></a>

### [#21607 · \[Test\]\[Upstream\]rerun failed test case](https://github.com/vllm-project/vllm-ascend/pull/21607)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21594"></a>

### [#21594 · \[Feature\]\[MoE\] Support anchor-union activation routing for DSpark and DFlash speculative decoding](https://github.com/vllm-project/vllm-ascend/pull/21594)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21587"></a>

### [#21587 · \[Feature\] Fuse GatingTopK with EPLB expert mapping](https://github.com/vllm-project/vllm-ascend/pull/21587)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 14:33；旧提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21546"></a>

### [#21546 · \[CI\] update cann=9.3.0\_20261110170400](https://github.com/vllm-project/vllm-ascend/pull/21546)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21541"></a>

### [#21541 · \[Doc\] add doc quality review workflow for docs/source changes](https://github.com/vllm-project/vllm-ascend/pull/21541)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21526"></a>

### [#21526 · \[Performance\]\[Kernel\] Fuse DeepSeek-V4.1 indexer prologue on Ascend A2/A3](https://github.com/vllm-project/vllm-ascend/pull/21526)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21521"></a>

### [#21521 · Upgrade/cann v0.32](https://github.com/vllm-project/vllm-ascend/pull/21521)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21513"></a>

### [#21513 · \[Doc\] Add deepseek\_v41\_qli\_candidate to nav and fix FAQ anchor](https://github.com/vllm-project/vllm-ascend/pull/21513)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21502"></a>

### [#21502 · \[Feature\]\[Performance\] Support InternLM2-20B-Chat and dispatch scaled RoPE variants to the NPU kernel](https://github.com/vllm-project/vllm-ascend/pull/21502)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21500"></a>

### [#21500 · \[BugFix\] Reap stale opc locks and cap build parallelism by cgroup memory limit](https://github.com/vllm-project/vllm-ascend/pull/21500)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21493"></a>

### [#21493 · \[临时/勿合入\] a3-800i fed-2 / fed-4 各跑 3 个用例（验证 runner 作业 pod）](https://github.com/vllm-project/vllm-ascend/pull/21493)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21490"></a>

### [#21490 · \[临时/勿合入\] 全量 A2/A3 业务选测跑 karc fed runner（对齐 #20716）](https://github.com/vllm-project/vllm-ascend/pull/21490)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21489"></a>

### [#21489 · \[Test\]\[Feature\] Add GLM-5.3 W4A4C8 MTP coverage on A5](https://github.com/vllm-project/vllm-ascend/pull/21489)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21481"></a>

### [#21481 · \[CI\] memcache cases](https://github.com/vllm-project/vllm-ascend/pull/21481)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21480"></a>

### [#21480 · \[Cherry-pick\]\[releases/v0.32.0rc\]\[CI\]\[BugFix\] Skip CANN 9.2.x custom-op .so validation in A5 wheel build (from #21479)](https://github.com/vllm-project/vllm-ascend/pull/21480)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21479"></a>

### [#21479 · \[CI\]\[BugFix\] Skip CANN 9.2.x custom-op .so validation in A5 wheel build](https://github.com/vllm-project/vllm-ascend/pull/21479)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21469"></a>

### [#21469 · \[Misc\] main2main: upgrade verified vLLM main from 1106 to 1112](https://github.com/vllm-project/vllm-ascend/pull/21469)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21459"></a>

### [#21459 · \[临时/勿合入\] 验证 karc 线下成员：a3-800i-fed-16 + a2-fed-2 smoke](https://github.com/vllm-project/vllm-ascend/pull/21459)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21456"></a>

### [#21456 · \[Refactor\]\[CP\] Decouple PCP/DCP metadata, topology and backend selection](https://github.com/vllm-project/vllm-ascend/pull/21456)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-13 14:33；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21385"></a>

### [#21385 · \[releases/v0.30.0\]\[Test\]\[Feature\] Add Kimi-K3 W4A8 E256 accuracy test on A5](https://github.com/vllm-project/vllm-ascend/pull/21385)

为发布分支的 A5 nightly 工作流增加诊断文件收集和 AOP 二分日志上传，并接入 Kimi-K3 测试任务。通用单节点测试框架新增独立多轮执行及逐轮产物保留。

**CI：** 未知（待刷新；尚无完整检查记录） · **改动：** +592 / -4 · **最后提交：** 11-13 14:51

<a id="pr-21284"></a>

### [#21284 · \[Test\] Add five-round Kimi-K3 Experts256 A5 nightly coverage](https://github.com/vllm-project/vllm-ascend/pull/21284)

在 A5 nightly 配置中接入 Kimi-K3 任务，默认启用 AOP 并收集该任务的诊断产物，允许跳过缺失的可选日志。通用单节点测试入口新增多轮参数化执行及逐轮结果归档。

**CI：** 未知（待刷新；尚无完整检查记录） · **改动：** +354 / -5 · **最后提交：** 11-13 14:51

<a id="pr-20205"></a>

### [#20205 · \[Feature\] Support draft model weight updates over HCCL](https://github.com/vllm-project/vllm-ascend/pull/20205)

在 CI 的预计耗时清单中登记双卡 RLHF draft HCCL 权重传输测试，预计运行 510 秒。

**CI：** 未知（待刷新；尚无完整检查记录） · **改动：** +739 / -52 · **最后提交：** 11-12 14:45
