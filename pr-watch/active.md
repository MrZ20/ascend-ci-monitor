# PR 关注列表

最近刷新：2026-11-14 02:50:19（上海时间）
当前关注的开放 PR：71

优先关注近期新增或代码变更；CI 分批轮转，以下保留最近已知结果与检查时间。

## 最近更新（72h）

- [11-14 02:37 · #21310 \[Refactor\]\[Core\] Remove dynamic chunk size CPP feature, configuration, and documentation](#pr-21310)
- [11-14 01:20 · #20914 \[Attention\]\[BugFix\] Use request incarnation IDs for sparse KV offload](#pr-20914)
- [11-14 00:39 · #21005 \[Misc\] main2main 1106](#pr-21005)
- [11-14 00:35 · #21549 \[Feature\] Add experimental Kimi KDA RecoverSSM support](#pr-21549)
- [11-13 23:31 · #21854 \[Doc\]\[Feature\] Add DeepSeek-R1-Distill-Qwen-32B support](#pr-21854)
- [11-13 23:31 · #21853 \[Feature\]\[HiSparse\] Add hi\_sparse\_resolve\_residency custom ACLNN op](#pr-21853)
- [11-13 22:35 · #18849 \[BugFix\]\[AscendStore\] Publish unique CPU KV events for sharded stores](#pr-18849)
- [11-13 22:14 · #20926 \[Feature\]\[HiSparse\] Add Ascend backend foundation](#pr-20926)
- [11-13 22:11 · #21607 \[Test\]\[Upstream\]rerun failed test case](#pr-21607)
- [11-13 21:07 · #20345 \[Performance\]\[Worker\] Reuse V2 attention metadata across cache groups and batch GDN state writes](#pr-20345)
- [11-13 20:51 · #21844 \[Test\] Add A2 KV-pool protection cases for Qwen3.8-27B W8A8](#pr-21844)
- [11-13 20:24 · #21839 \[CI\]test: Pr e2e ops](#pr-21839)
- [11-13 20:24 · #20756 \[BugFix\]\[Model\] Support dense sequence parallelism for the Qwen3.5 family (Qwen3.8-27B)](#pr-20756)
- [11-13 19:59 · #21834 \[CI\]\[Docker\] Bump mooncake-transfer-engine-npu to 0.3.14](#pr-21834)
- [11-13 19:39 · #21469 \[Misc\] main2main: upgrade verified vLLM main from 1106 to 1112](#pr-21469)
- [11-13 19:24 · #21848 \[CI\]\[Misc\] Bump AISBench tag to v3.1-20261113-master](#pr-21848)
- [11-13 19:10 · #21751 \[Feature\]\[Model\] Add Qwen PLE UVA host offload with DP memory sharing](#pr-21751)
- [11-13 18:39 · #21717 \[CI\] Restore A5 multi-node nightly test cases](#pr-21717)
- [11-13 18:39 · #21697 \[BugFix\]\[CI\] Add Qwen3.8-Flash-Next TP2 IPC coverage and preserve PLE sleep state](#pr-21697)
- [11-13 18:39 · #20633 \[CI\] add test cases for Qwen3.6-35B-w8a8](#pr-20633)
- [11-13 18:39 · #12751 \[CI\] Pin dorny/paths-filter to compatible v4.0.3](#pr-12751)
- [11-13 18:01 · #21190 \[Performance\]\[Worker\] Reuse attention metadata and keep DFlash2 lengths on device](#pr-21190)
- [11-13 18:00 · #21685 \[CI\] add presmoke for CI](#pr-21685)
- [11-13 17:55 · #21541 \[Doc\] add doc quality review workflow for docs/source changes](#pr-21541)
- [11-13 17:42 · #17833 \[Feature\]\[Worker\] Add MRV2 KV Trace](#pr-17833)
- [11-13 17:41 · #21284 \[Test\] Add five-round Kimi-K3 Experts256 A5 nightly coverage](#pr-21284)
- [11-13 17:40 · #21699 \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.32.0rc](#pr-21699)
- [11-13 17:39 · #21822 \[CI\]\[Feature\] Add Atlas 310P CI documentation and flaky reproduction test](#pr-21822)
- [11-13 17:39 · #20757 \[Test\] Add KV pool hit watch to A3 PR e2e cases](#pr-20757)
- [11-13 17:02 · #21833 \[Feature\] Add dynamic token deferral, state restoration and rebatching for MoE decoding](#pr-21833)
- [11-13 16:39 · #18604 \[Feature\]\[MoE\] Add exact expert offload for V2 eager and decode ACL graphs](#pr-18604)
- [11-13 16:39 · #21674 \[CI\] run.sh](#pr-21674)
- [11-13 15:39 · #21481 \[CI\] memcache cases](#pr-21481)
- [11-13 15:37 · #20575 \[CI\]\[Model\] Add combined GLM-5.3 P/PD/decode Weekly coverage](#pr-20575)
- [11-13 15:11 · #21385 \[releases/v0.30.0\]\[Test\]\[Feature\] Add Kimi-K3 W4A8 E256 accuracy test on A5](#pr-21385)
- [11-13 12:00 · #21713 \[BugFix\] Rename static operator build option to --soc\_series](#pr-21713)
- [11-13 12:00 · #21789 \[DevContainer\]\[Feature\] Add Dev Container environment settings for 310P/A2/A3/A5/CPU](#pr-21789)
- [11-13 10:34 · #21777 fix: pin torch==2.10.0+cpu to match torch-npu dependency](#pr-21777)
- [11-13 01:35 · #20427 \[Feature\] Restore A5 MRV2 ACL graphs in place across sleep](#pr-20427)
- [11-13 01:32 · #20528 \[Feature\] Integrate Ascend SleepModeBackend lifecycle](#pr-20528)
- [11-13 01:32 · #21260 \[Feature\]\[EPLB\] Export committed MRV2 expert placement](#pr-21260)
- [11-13 00:05 · #21746 test: cover Qwen3.6 Model Runner V2 with main-recorded goldens](#pr-21746)
- [11-12 19:54 · #21712 \[Doc\]\[Misc\] Document Ascend Docker Runtime container setup](#pr-21712)
- [11-12 18:41 · #21714 \[Refactor\]\[MRV2\] Adopt EPLB policy and model-state hooks](#pr-21714)
- [11-12 18:34 · #21705 \[Feature\] DSpark expert-pool routing for the expert-offload path](#pr-21705)
- [11-12 18:10 · #21716 \[临时/勿合入\] ci: route Nightly-A2 cases to offline-cluster runner labels](#pr-21716)
- [11-12 17:32 · #21045 \[CI\] Add DeepSeek-v4.1 test case](#pr-21045)
- [11-12 17:00 · #21701 \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](#pr-21701)
- [11-12 15:55 · #18559 \[CI\] kv\_pool cases](#pr-18559)
- [11-12 15:54 · #21689 \[CI\] Isolate lint images by branch and add a lightweight tools image](#pr-21689)
- [11-12 15:52 · #21594 \[Feature\]\[MoE\] Support anchor-union activation routing for DSpark and DFlash speculative decoding](#pr-21594)
- [11-12 15:52 · #21680 \[Feature\]\[MoE\] Add opt-in DSpark expert-pool routing for expert offload](#pr-21680)
- [11-12 14:50 · #20205 \[Feature\] Support draft model weight updates over HCCL](#pr-20205)
- [11-12 12:04 · #21661 \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](#pr-21661)
- [11-12 11:00 · #21623 \[Feature\]\[Engram\] Add local host VMM for shared A3 tables](#pr-21623)
- [11-12 10:47 · #21490 \[临时/勿合入\] 全量 A2/A3 业务选测跑 karc fed runner（对齐 #20716）](#pr-21490)
- [11-12 10:13 · #21643 \[Feature\]\[EC Connector\] Support encoder cache tiering offload on Ascend](#pr-21643)
- [11-12 09:10 · #21638 \[Feature\]\[Qwen\] Share PLE tables across Ascend services](#pr-21638)
- [11-11 15:23 · #21521 Upgrade/cann v0.32](#pr-21521)
- [11-11 14:46 · #21546 \[CI\] update cann=9.3.0\_20261110170400](#pr-21546)
- [11-11 14:43 · #21526 \[Performance\]\[Kernel\] Fuse DeepSeek-V4.1 indexer prologue on Ascend A2/A3](#pr-21526)
- [11-11 11:16 · #21513 \[Doc\] Add deepseek\_v41\_qli\_candidate to nav and fix FAQ anchor](#pr-21513)

## 当前关注

<a id="pr-21854"></a>

### [#21854 · \[Doc\]\[Feature\] Add DeepSeek-R1-Distill-Qwen-32B support](https://github.com/vllm-project/vllm-ascend/pull/21854)

在 MkDocs 导航中新增 DeepSeek-R1-Distill-Qwen-32B 教程入口。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** +169 / -0 · **最后提交：** 11-13 22:36

<a id="pr-21853"></a>

### [#21853 · \[Feature\]\[HiSparse\] Add hi\_sparse\_resolve\_residency custom ACLNN op](https://github.com/vllm-project/vllm-ascend/pull/21853)

将 hi\_sparse\_resolve\_residency 加入 Ascend 950 自定义算子构建清单。

**CI：** 失败（ci-gate） · **改动：** +1165 / -0 · **最后提交：** 11-13 23:02

<a id="pr-21848"></a>

### [#21848 · \[CI\]\[Misc\] Bump AISBench tag to v3.1-20261113-master](https://github.com/vllm-project/vllm-ascend/pull/21848)

将 310P、A2、A3、A5 nightly 镜像的 AISBench 默认版本更新为 v3.1-20261113-master，并同步多节点测试贡献指南。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +6 / -6 · **最后提交：** 11-13 18:14

<a id="pr-21844"></a>

### [#21844 · \[Test\] Add A2 KV-pool protection cases for Qwen3.8-27B W8A8](https://github.com/vllm-project/vllm-ascend/pull/21844)

为 Qwen3.8 KV-pool 保护测试登记 2700 秒耗时并路由到 A2 双卡池，同时透传 Mooncake master 额外参数。E2E runner 增加可序列化的引擎指标读取接口，DP runner 汇总各 rank 的计数器和 gauge。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +1303 / -1 · **最后提交：** 11-13 20:34

<a id="pr-21839"></a>

### [#21839 · \[CI\]test: Pr e2e ops](https://github.com/vllm-project/vllm-ascend/pull/21839)

将 two\_card/ops 算子测试集中到通用 A3 双卡 runner 的同一 pytest 进程，配套调整分组、耗时校验、覆盖率与日志命名，并为两条 FP8 类型判断增加精确 gitleaks 例外。当前工作流还临时将 CI 流水线变更限定为 ops 测试模式，而非全套测试。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** +34398 / -33 · **最后提交：** 11-13 18:28

<a id="pr-21834"></a>

### [#21834 · \[CI\]\[Docker\] Bump mooncake-transfer-engine-npu to 0.3.14](https://github.com/vllm-project/vllm-ascend/pull/21834)

将 PR/main2main CI 与各架构镜像中的 mooncake-transfer-engine-npu 从 0.3.14rc3 升级到 0.3.14，并同步依赖版本维护文档。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** +15 / -15 · **最后提交：** 11-13 16:58

<a id="pr-21833"></a>

### [#21833 · \[Feature\] Add dynamic token deferral, state restoration and rebatching for MoE decoding](https://github.com/vllm-project/vllm-ascend/pull/21833)

在 A3 算子构建清单中加入 attn\_metadata\_update、combine\_and\_dispatch\_rebatch、rebatch\_and\_update 与 moe\_token\_cut 四个编译目标。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** +11834 / -9 · **最后提交：** 11-11 09:57 · **Draft**

<a id="pr-21822"></a>

### [#21822 · \[CI\]\[Feature\] Add Atlas 310P CI documentation and flaky reproduction test](https://github.com/vllm-project/vllm-ascend/pull/21822)

取消 PR 流水线中 select-tests 和 run-selected-tests 对 pre-commit 的直接依赖，并新增 310P 主干回归记录与 CI 看护矩阵文档。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** +96 / -2 · **最后提交：** 11-13 16:42

<a id="pr-21789"></a>

### [#21789 · \[DevContainer\]\[Feature\] Add Dev Container environment settings for 310P/A2/A3/A5/CPU](https://github.com/vllm-project/vllm-ascend/pull/21789)

新增 CPU、310P、A2、A3、A5 的开发容器配置，统一源码挂载、编辑器格式化、依赖安装和 ccache 缓存；各硬件配置设置对应 CANN 镜像与编译环境。

**CI：** 失败（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +315 / -0 · **最后提交：** 11-13 11:36

<a id="pr-21777"></a>

### [#21777 · fix: pin torch==2.10.0+cpu to match torch-npu dependency](https://github.com/vllm-project/vllm-ascend/pull/21777)

将构建配置与运行依赖中的 PyTorch 固定版本从 2.10.0 改为 2.10.0+cpu。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +6 / -2 · **最后提交：** 11-13 10:24

<a id="pr-21751"></a>

### [#21751 · \[Feature\]\[Model\] Add Qwen PLE UVA host offload with DP memory sharing](https://github.com/vllm-project/vllm-ascend/pull/21751)

在 CI 预计耗时清单中登记 PLE host lookup 单卡 Triton 测试，预计运行 30 秒。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** +877 / -32 · **最后提交：** 11-13 15:29

<a id="pr-21746"></a>

### [#21746 · test: cover Qwen3.6 Model Runner V2 with main-recorded goldens](https://github.com/vllm-project/vllm-ascend/pull/21746)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21717"></a>

### [#21717 · \[CI\] Restore A5 multi-node nightly test cases](https://github.com/vllm-project/vllm-ascend/pull/21717)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21716"></a>

### [#21716 · \[临时/勿合入\] ci: route Nightly-A2 cases to offline-cluster runner labels](https://github.com/vllm-project/vllm-ascend/pull/21716)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

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

**CI：** 通过 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21697"></a>

### [#21697 · \[BugFix\]\[CI\] Add Qwen3.8-Flash-Next TP2 IPC coverage and preserve PLE sleep state](https://github.com/vllm-project/vllm-ascend/pull/21697)

在 CI 预计耗时清单中登记 Qwen3.8 双卡 RLHF IPC 权重传输测试，预计 180 秒。

**CI：** 失败（ci-gate） · **改动：** +294 / -4 · **最后提交：** 11-13 17:59

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

<a id="pr-21674"></a>

### [#21674 · \[CI\] run.sh](https://github.com/vllm-project/vllm-ascend/pull/21674)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21661"></a>

### [#21661 · \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](https://github.com/vllm-project/vllm-ascend/pull/21661)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21643"></a>

### [#21643 · \[Feature\]\[EC Connector\] Support encoder cache tiering offload on Ascend](https://github.com/vllm-project/vllm-ascend/pull/21643)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21638"></a>

### [#21638 · \[Feature\]\[Qwen\] Share PLE tables across Ascend services](https://github.com/vllm-project/vllm-ascend/pull/21638)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21623"></a>

### [#21623 · \[Feature\]\[Engram\] Add local host VMM for shared A3 tables](https://github.com/vllm-project/vllm-ascend/pull/21623)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21607"></a>

### [#21607 · \[Test\]\[Upstream\]rerun failed test case](https://github.com/vllm-project/vllm-ascend/pull/21607)

为上游 E2E 工作流增加 main、开发和 release 分支 PR 触发，启用在线 Hugging Face 访问，并将多卡和在线任务固定到指定 runner。测试套件改用 v0.33.0 配置，同时新增专项重跑清单。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +207 / -4 · **最后提交：** 11-13 17:15

<a id="pr-21594"></a>

### [#21594 · \[Feature\]\[MoE\] Support anchor-union activation routing for DSpark and DFlash speculative decoding](https://github.com/vllm-project/vllm-ascend/pull/21594)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21549"></a>

### [#21549 · \[Feature\] Add experimental Kimi KDA RecoverSSM support](https://github.com/vllm-project/vllm-ascend/pull/21549)

在 gitleaks 配置中为一条历史 bfloat16 类型断言增加精确误报例外，同时限定提交、文件路径与行模式。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +1439 / -156 · **最后提交：** 11-14 00:02 · **Draft**

<a id="pr-21546"></a>

### [#21546 · \[CI\] update cann=9.3.0\_20261110170400](https://github.com/vllm-project/vllm-ascend/pull/21546)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21541"></a>

### [#21541 · \[Doc\] add doc quality review workflow for docs/source changes](https://github.com/vllm-project/vllm-ascend/pull/21541)

新增文档质量检查工作流，结合规则脚本与 LLM 检查 Markdown 和 PO 翻译文件，归并问题并发布 PR 汇总与差异行评论。配套脚本生成修订建议并保存评估产物。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +2192 / -0 · **最后提交：** 11-13 17:37 · **Draft**

<a id="pr-21526"></a>

### [#21526 · \[Performance\]\[Kernel\] Fuse DeepSeek-V4.1 indexer prologue on Ascend A2/A3](https://github.com/vllm-project/vllm-ascend/pull/21526)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21521"></a>

### [#21521 · Upgrade/cann v0.32](https://github.com/vllm-project/vllm-ascend/pull/21521)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21513"></a>

### [#21513 · \[Doc\] Add deepseek\_v41\_qli\_candidate to nav and fix FAQ anchor](https://github.com/vllm-project/vllm-ascend/pull/21513)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21502"></a>

### [#21502 · \[Feature\]\[Performance\] Support InternLM2-20B-Chat and dispatch scaled RoPE variants to the NPU kernel](https://github.com/vllm-project/vllm-ascend/pull/21502)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21500"></a>

### [#21500 · \[BugFix\] Reap stale opc locks and cap build parallelism by cgroup memory limit](https://github.com/vllm-project/vllm-ascend/pull/21500)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21493"></a>

### [#21493 · \[临时/勿合入\] a3-800i fed-2 / fed-4 各跑 3 个用例（验证 runner 作业 pod）](https://github.com/vllm-project/vllm-ascend/pull/21493)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21490"></a>

### [#21490 · \[临时/勿合入\] 全量 A2/A3 业务选测跑 karc fed runner（对齐 #20716）](https://github.com/vllm-project/vllm-ascend/pull/21490)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21489"></a>

### [#21489 · \[Test\]\[Feature\] Add GLM-5.3 W4A4C8 MTP coverage on A5](https://github.com/vllm-project/vllm-ascend/pull/21489)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21481"></a>

### [#21481 · \[CI\] memcache cases](https://github.com/vllm-project/vllm-ascend/pull/21481)

扩充 A3 weekly 的 GLM-5.3 与 DeepSeek-V4-Flash Memcache/无 Memcache PD 测试配置，并将五个长上下文 GSM8K 数据集加入 CI 下载清单。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** +1236 / -1 · **最后提交：** 11-13 15:21

<a id="pr-21480"></a>

### [#21480 · \[Cherry-pick\]\[releases/v0.32.0rc\]\[CI\]\[BugFix\] Skip CANN 9.2.x custom-op .so validation in A5 wheel build (from #21479)](https://github.com/vllm-project/vllm-ascend/pull/21480)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-14 00:35；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21479"></a>

### [#21479 · \[CI\]\[BugFix\] Skip CANN 9.2.x custom-op .so validation in A5 wheel build](https://github.com/vllm-project/vllm-ascend/pull/21479)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21469"></a>

### [#21469 · \[Misc\] main2main: upgrade verified vLLM main from 1106 to 1112](https://github.com/vllm-project/vllm-ascend/pull/21469)

将 vLLM main 验证提交标记更新为 3b95523ed904cf02a26b872f4a900ef17e6be8ad，并登记 categorical sample bias 单卡测试预计耗时 120 秒。

**CI：** 失败（ci-gate） · **改动：** +3498 / -422 · **最后提交：** 11-13 18:18 · **Draft**

<a id="pr-21459"></a>

### [#21459 · \[临时/勿合入\] 验证 karc 线下成员：a3-800i-fed-16 + a2-fed-2 smoke](https://github.com/vllm-project/vllm-ascend/pull/21459)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败 · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21456"></a>

### [#21456 · \[Refactor\]\[CP\] Decouple PCP/DCP metadata, topology and backend selection](https://github.com/vllm-project/vllm-ascend/pull/21456)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21385"></a>

### [#21385 · \[releases/v0.30.0\]\[Test\]\[Feature\] Add Kimi-K3 W4A8 E256 accuracy test on A5](https://github.com/vllm-project/vllm-ascend/pull/21385)

为发布分支的 A5 nightly 工作流增加诊断文件收集和 AOP 二分日志上传，并接入 Kimi-K3 测试任务。通用单节点测试框架新增独立多轮执行及逐轮产物保留。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +592 / -4 · **最后提交：** 11-13 14:51

<a id="pr-21338"></a>

### [#21338 · \[CI\]\[Model\] Add Flash A3 ReplaySSM and Decode replay Weekly coverage](https://github.com/vllm-project/vllm-ascend/pull/21338)

在 A3 weekly 注册 GLM-5.3-Flash 的 ReplaySSM 与 Decode replay 两种双节点 PD 测试。配套 CPU 检查验证设备分配、命令渲染和缓存重放顺序，硬件效果仍待验证。

**CI：** 失败（ci-gate） · **改动：** +600 / -0 · **最后提交：** 11-09 16:22 · **Draft**

<a id="pr-21310"></a>

### [#21310 · \[Refactor\]\[Core\] Remove dynamic chunk size CPP feature, configuration, and documentation](https://github.com/vllm-project/vllm-ascend/pull/21310)

从 CI 精度测试清单、耗时配置及覆盖矩阵中移除 profiling chunk 性能测试，并删除动态分块流水线并行的文档导航与中英文标题映射。

**CI：** 失败 · **改动：** +204 / -5386 · **最后提交：** 11-14 01:21

<a id="pr-21284"></a>

### [#21284 · \[Test\] Add five-round Kimi-K3 Experts256 A5 nightly coverage](https://github.com/vllm-project/vllm-ascend/pull/21284)

为 A5 nightly 增加 Kimi-K3 测试配置及诊断产物下载，允许跳过不存在的可选日志路径。通用单节点测试框架支持按配置独立运行多轮，并逐轮保存结果和基准产物。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +354 / -5 · **最后提交：** 11-13 17:36

<a id="pr-21260"></a>

### [#21260 · \[Feature\]\[EPLB\] Export committed MRV2 expert placement](https://github.com/vllm-project/vllm-ascend/pull/21260)

将 MRv2 EPLB placement export 双卡用例加入 A5 精选 CI 测试集。

**CI：** 失败（ci-gate） · **改动：** +345 / -8 · **最后提交：** 11-13 01:15

<a id="pr-21190"></a>

### [#21190 · \[Performance\]\[Worker\] Reuse attention metadata and keep DFlash2 lengths on device](https://github.com/vllm-project/vllm-ascend/pull/21190)

为 cached GDN decode 和 GDN metadata reuse 两项端到端测试新增各 600 秒的 CI 调度预估时长。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +4553 / -218 · **最后提交：** 11-13 17:26

<a id="pr-21045"></a>

### [#21045 · \[CI\] Add DeepSeek-v4.1 test case](https://github.com/vllm-project/vllm-ascend/pull/21045)

为 A3 周测矩阵新增 MiniMax-M3、DeepSeek-V4.1-Flash 和 GLM-5.3-Flash 的 1M 上下文 PD 用例，并分别配置运行规模。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +867 / -118 · **最后提交：** 11-12 17:26

<a id="pr-21005"></a>

### [#21005 · \[Misc\] main2main 1106](https://github.com/vllm-project/vllm-ascend/pull/21005)

将 vLLM main 验证提交标记更新为 ba15685ab7f4f5fbed8630bbb7441f8837e76fbe。

**CI：** 失败（ci-gate） · **改动：** +1230 / -225 · **最后提交：** 11-13 22:40

<a id="pr-20926"></a>

### [#20926 · \[Feature\]\[HiSparse\] Add Ascend backend foundation](https://github.com/vllm-project/vllm-ascend/pull/20926)

将三个 HiSparse 单卡测试加入 CI 选择与 A5 runner 映射，预计各 30 秒，并加入文档导航及中英文标题。构建配置在 A5 工具链具备 SIMT 头文件时启用对应算子和 Torch 适配。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +6997 / -96 · **最后提交：** 11-13 16:26

<a id="pr-20914"></a>

### [#20914 · \[Attention\]\[BugFix\] Use request incarnation IDs for sparse KV offload](https://github.com/vllm-project/vllm-ascend/pull/20914)

为稀疏 KV offload 生命周期测试增加 A3 MemFabric AccOffload 安装与库格式、入口校验步骤，超时设为 15 分钟。将该测试路由至 A3 双卡池并登记预计耗时 600 秒。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +1016 / -33 · **最后提交：** 11-12 21:55

<a id="pr-20757"></a>

### [#20757 · \[Test\] Add KV pool hit watch to A3 PR e2e cases](https://github.com/vllm-project/vllm-ascend/pull/20757)

调整多项四卡端到端测试的 CI 耗时预估，并为通用 VllmRunner/DPVllmRunner 增加可跨进程传递的指标读取与跨 rank 汇总。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +1357 / -163 · **最后提交：** 11-13 16:51

<a id="pr-20756"></a>

### [#20756 · \[BugFix\]\[Model\] Support dense sequence parallelism for the Qwen3.5 family (Qwen3.8-27B)](https://github.com/vllm-project/vllm-ascend/pull/20756)

为 Qwen3.8-27B dense SP 双卡端到端用例新增 600 秒的 CI 调度预估时长。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +779 / -28 · **最后提交：** 11-13 12:03

<a id="pr-20633"></a>

### [#20633 · \[CI\] add test cases for Qwen3.6-35B-w8a8](https://github.com/vllm-project/vllm-ascend/pull/20633)

在 A3 nightly 和 weekly 配置中加入 Qwen3.6-35B-A3B w8a8 FullAndPiecewise 测试，分别指定 800i-16 与 800t-16 runner。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +454 / -346 · **最后提交：** 11-13 18:13

<a id="pr-20575"></a>

### [#20575 · \[CI\]\[Model\] Add combined GLM-5.3 P/PD/decode Weekly coverage](https://github.com/vllm-project/vllm-ascend/pull/20575)

为 Weekly-A3 增加 GLM-5.3 分拆及组合测试矩阵，并新增可由 PR 命令触发的 Weekly-A5 工作流与产物汇总。通用多节点配置解析同步支持替换基准参数中的集群地址占位符。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +3577 / -5 · **最后提交：** 11-13 15:16 · **Draft**

<a id="pr-20528"></a>

### [#20528 · \[Feature\] Integrate Ascend SleepModeBackend lifecycle](https://github.com/vllm-project/vllm-ascend/pull/20528)

在 Python 包的通用插件入口中注册 Ascend sleep-mode backend，并在开发指南首页加入后端说明入口。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +1561 / -72 · **最后提交：** 11-13 01:15

<a id="pr-20427"></a>

### [#20427 · \[Feature\] Restore A5 MRV2 ACL graphs in place across sleep](https://github.com/vllm-project/vllm-ascend/pull/20427)

将 sleep graph reuse 单卡用例加入 A5 精选 CI，指定 a5-4 runner，并增加 420 秒调度预估。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +2592 / -100 · **最后提交：** 11-13 01:17

<a id="pr-20345"></a>

### [#20345 · \[Performance\]\[Worker\] Reuse V2 attention metadata across cache groups and batch GDN state writes](https://github.com/vllm-project/vllm-ascend/pull/20345)

在 CI 耗时清单中新增 cached GDN decode 和 GDN metadata reuse v2 两项测试，各暂估 600 秒。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +2984 / -171 · **最后提交：** 11-13 19:37

<a id="pr-20205"></a>

### [#20205 · \[Feature\] Support draft model weight updates over HCCL](https://github.com/vllm-project/vllm-ascend/pull/20205)

在 CI 的预计耗时清单中登记双卡 RLHF draft HCCL 权重传输测试，预计运行 510 秒。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +739 / -52 · **最后提交：** 11-12 14:45

<a id="pr-18849"></a>

### [#18849 · \[BugFix\]\[AscendStore\] Publish unique CPU KV events for sharded stores](https://github.com/vllm-project/vllm-ascend/pull/18849)

在 mypy 配置中为缺少类型存根的 mooncake.engine 增加 ignore\_missing\_imports 例外，保留 memfabric\_hybrid 的现有设置。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-14 01:37；当前提交） · **改动：** +856 / -107 · **最后提交：** 11-13 21:49

<a id="pr-18604"></a>

### [#18604 · \[Feature\]\[MoE\] Add exact expert offload for V2 eager and decode ACL graphs](https://github.com/vllm-project/vllm-ascend/pull/18604)

将 expert offload 的单卡端到端用例加入 A5 精选 CI 测试集，指定 a5-4 runner，并设置 600 秒调度预估时长。

**CI：** 失败（ci-gate） · **改动：** +2017 / -0 · **最后提交：** 11-13 11:50

<a id="pr-18559"></a>

### [#18559 · \[CI\] kv\_pool cases](https://github.com/vllm-project/vllm-ascend/pull/18559)

在 A3 nightly 配置新增 DeepSeek-V4-flash w8a8 Mooncake 测试，并在 weekly 配置新增 DeepSeek-V4.1-Flash W8A8 Mooncake 测试，两项 size 均设为 2。

**CI：** 通过 · **改动：** +462 / -1 · **最后提交：** 11-12 15:39

<a id="pr-17833"></a>

### [#17833 · \[Feature\]\[Worker\] Add MRV2 KV Trace](https://github.com/vllm-project/vllm-ascend/pull/17833)

在 MkDocs 用户指南导航中加入 KV trace 页面入口，并新增 KV trace 单测包初始化文件。

**CI：** 失败（ci-gate） · **改动：** +1692 / -1 · **最后提交：** 11-13 17:30

<a id="pr-12751"></a>

### [#12751 · \[CI\] Pin dorny/paths-filter to compatible v4.0.3](https://github.com/vllm-project/vllm-ascend/pull/12751)

将 PR 测试工作流的 dorny/paths-filter 从 v4 固定到 v4.0.3。

**CI：** 失败（ci-gate） · **改动：** +1 / -1 · **最后提交：** 11-13 17:59
