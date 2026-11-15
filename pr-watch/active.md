# PR 关注列表

最近刷新：2026-11-16 05:05:59（上海时间）
当前关注的开放 PR：101

优先关注近期新增或代码变更；CI 分批轮转，以下保留最近已知结果与检查时间。

## 最近更新（72h）

- [11-16 01:13 · #21906 \[BugFix\] Complete V2 thinking budget validation and acceptance coverage](#pr-21906)
- [11-16 00:47 · #21912 \[BugFix\] Validate layerwise prefetch before backend initialization](#pr-21912)
- [11-16 00:47 · #21456 \[Refactor\]\[CP\] Decouple PCP/DCP metadata, topology and backend selection](#pr-21456)
- [11-15 23:37 · #20528 \[Feature\] Integrate Ascend SleepModeBackend lifecycle](#pr-20528)
- [11-15 23:21 · #21917 \[Feature\] Add TopKPerRow aclnn operator (ragged per-row top-k)](#pr-21917)
- [11-15 23:14 · #20914 \[Attention\]\[BugFix\] Use request incarnation IDs for sparse KV offload](#pr-20914)
- [11-15 22:49 · #21886 \[CI\]\[Feature\] Publish failed Daily cases incrementally to one Issue](#pr-21886)
- [11-15 22:43 · #21261 \[BugFix\]\[EPLB\] Validate STAIR placements against per-step load](#pr-21261)
- [11-15 22:43 · #21260 \[Feature\]\[EPLB\] Export committed MRV2 expert placement](#pr-21260)
- [11-15 22:43 · #20427 \[Feature\] Restore A5 MRV2 ACL graphs in place across sleep](#pr-20427)
- [11-15 22:19 · #20494 \[Feature\]\[MoE\] Add CatCCOS MegaMoE backend for DeepSeek-V4-Flash on Ascend A5](#pr-20494)
- [11-15 22:18 · #20493 \[Feature\]\[MoE\] Add CatCCOS MegaMoE backend for Qwen3 on Ascend A5](#pr-20493)
- [11-15 20:42 · #21903 \[Refactor\]\[MRV2\] Reuse unified KV cache allocation for Kimi K3](#pr-21903)
- [11-15 19:41 · #21005 \[Misc\] main2main 1106](#pr-21005)
- [11-15 18:33 · #21889 \[BugFix\] Allow non-root users to load operator libraries](#pr-21889)
- [11-15 17:52 · #20757 \[Test\] Add KV pool hit watch to A3 PR e2e cases](#pr-20757)
- [11-15 16:57 · #17833 \[Feature\]\[Worker\] Add MRV2 KV Trace](#pr-17833)
- [11-15 16:39 · #21607 \[Test\]\[Upstream\]rerun failed test case](#pr-21607)
- [11-15 16:39 · #21190 \[Performance\]\[Worker\] Reuse attention metadata and keep DFlash2 lengths on device](#pr-21190)
- [11-15 16:39 · #20205 \[Feature\] Support draft model weight updates over HCCL](#pr-20205)
- [11-15 15:32 · #20345 \[Performance\]\[Worker\] Reuse V2 attention metadata across cache groups and batch GDN state writes](#pr-20345)
- [11-15 14:54 · #21469 \[Misc\] main2main: upgrade verified vLLM main from 1106 to 1112](#pr-21469)
- [11-15 14:47 · #21871 \[Doc\] Use --backend in the serving benchmark example](#pr-21871)
- [11-15 14:41 · #21844 \[Test\] Add A2 KV-pool protection cases for Qwen3.8-27B W8A8](#pr-21844)
- [11-15 14:41 · #21826 \[Performance\]\[Model\] Integrate the fused DeepSeek V4.1 attention epilogue on A5](#pr-21826)
- [11-15 14:41 · #19442 \[BugFix\]\[Test\] Declare GDN batch-invariance support and cover Qwen3.5-35B-A3B in the TP4 e2e](#pr-19442)
- [11-15 14:41 · #18849 \[BugFix\]\[AscendStore\] Publish unique CPU KV events for sharded stores](#pr-18849)
- [11-15 13:49 · #21887 \[BugFix\] Allow non-root users to load operator libraries](#pr-21887)
- [11-15 12:22 · #21905 \[CI\] Avoid host problem-matcher registration in containerized pre-commit](#pr-21905)
- [11-15 12:15 · #20299 \[Feature\] Integrate the packaged DeepGEMM V4.1 MegaMoE backend on Ascend 950](#pr-20299)
- [11-15 08:51 · #21900 \[Doc\] Fix broken in-page anchors in docs](#pr-21900)
- [11-15 02:26 · #21888 \[BugFix\] Allow non-root users to load operator libraries](#pr-21888)
- [11-14 23:59 · #21892 \[Feature\] Compose HiSparse with PCP on Ascend](#pr-21892)
- [11-14 23:34 · #20138 \[Feature\]\[RuntimeGuard\] Add rare\_chars detector with async pair collect](#pr-20138)
- [11-14 20:39 · #21890 \[Doc\] Fix stale file paths in docs](#pr-21890)
- [11-14 19:46 · #21885 \[Feature\] Integrate A3 W4A8 SiTU through the shared grouped matmul operator](#pr-21885)
- [11-14 18:11 · #21853 \[Feature\]\[HiSparse\] Add hi\_sparse\_resolve\_residency custom ACLNN op](#pr-21853)
- [11-14 17:29 · #21882 \[Test\] Use a local work\_dir in BuildManager UT fixture](#pr-21882)
- [11-14 17:12 · #21879 \[CI\]\[Build\] Bump CANN base images to 9.3.0\_20261113161300](#pr-21879)
- [11-14 15:44 · #21868 \[Feature\]\[MoE\] Add opt-in A3 MSD SiTU fusion through shared interfaces](#pr-21868)
- [11-14 15:31 · #21536 \[Feature\]\[KV Cache\] Add exact-position hybrid-state checkpoints on Ascend](#pr-21536)
- [11-14 14:32 · #21869 \[BugFix\]\[Upstream\] Fix routed experts capture on Ascend TP-sharded batches (#21619)](#pr-21869)
- [11-14 14:26 · #21870 \[BugFix\]\[Build\] Stop dropping AICPU sources and objects from RTY/UT builds](#pr-21870)
- [11-14 11:03 · #21862 \[TEST\] Add blank line in csrc/build.sh to exercise PR gate](#pr-21862)
- [11-13 22:46 · #21854 \[Doc\]\[Feature\] Add DeepSeek-R1-Distill-Qwen-32B support](#pr-21854)
- [11-13 20:24 · #21839 \[CI\]test: Pr e2e ops](#pr-21839)
- [11-13 20:24 · #20756 \[BugFix\]\[Model\] Support dense sequence parallelism for the Qwen3.5 family (Qwen3.8-27B)](#pr-20756)
- [11-13 19:59 · #21834 \[CI\]\[Docker\] Bump mooncake-transfer-engine-npu to 0.3.14](#pr-21834)
- [11-13 19:24 · #21848 \[CI\]\[Misc\] Bump AISBench tag to v3.1-20261113-master](#pr-21848)
- [11-13 19:10 · #21751 \[Feature\]\[Model\] Add Qwen PLE UVA host offload with DP memory sharing](#pr-21751)
- [11-13 18:39 · #21717 \[CI\] Restore A5 multi-node nightly test cases](#pr-21717)
- [11-13 18:39 · #21697 \[BugFix\]\[CI\] Add Qwen3.8-Flash-Next TP2 IPC coverage and preserve PLE sleep state](#pr-21697)
- [11-13 18:39 · #20633 \[CI\] add test cases for Qwen3.6-35B-w8a8](#pr-20633)
- [11-13 18:39 · #12751 \[CI\] Pin dorny/paths-filter to compatible v4.0.3](#pr-12751)
- [11-13 17:55 · #21541 \[Doc\] add doc quality review workflow for docs/source changes](#pr-21541)
- [11-13 17:41 · #21284 \[Test\] Add five-round Kimi-K3 Experts256 A5 nightly coverage](#pr-21284)
- [11-13 17:40 · #21699 \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.32.0rc](#pr-21699)
- [11-13 17:39 · #21822 \[CI\]\[Feature\] Add Atlas 310P CI documentation and flaky reproduction test](#pr-21822)
- [11-13 17:02 · #21833 \[Feature\] Add dynamic token deferral, state restoration and rebatching for MoE decoding](#pr-21833)
- [11-13 16:39 · #18604 \[Feature\]\[MoE\] Add exact expert offload for V2 eager and decode ACL graphs](#pr-18604)
- [11-13 16:39 · #21674 \[CI\] run.sh](#pr-21674)
- [11-13 15:39 · #21481 \[CI\] memcache cases](#pr-21481)
- [11-13 15:37 · #20575 \[CI\]\[Model\] Add combined GLM-5.3 P/PD/decode Weekly coverage](#pr-20575)
- [11-13 15:11 · #21385 \[releases/v0.30.0\]\[Test\]\[Feature\] Add Kimi-K3 W4A8 E256 accuracy test on A5](#pr-21385)
- [11-13 12:00 · #21713 \[BugFix\] Rename static operator build option to --soc\_series](#pr-21713)
- [11-13 12:00 · #21789 \[DevContainer\]\[Feature\] Add Dev Container environment settings for 310P/A2/A3/A5/CPU](#pr-21789)
- [11-13 11:58 · #21334 \[CI\] add single-node test for a3,a5- #20846](#pr-21334)
- [11-13 10:34 · #21777 fix: pin torch==2.10.0+cpu to match torch-npu dependency](#pr-21777)
- [11-13 09:53 · #19884 \[Feature\] Decoder Append-Prefill for Agentic Scenario Prefiller Offloading](#pr-19884)

## 当前关注

<a id="pr-21917"></a>

### [#21917 · \[Feature\] Add TopKPerRow aclnn operator (ragged per-row top-k)](https://github.com/vllm-project/vllm-ascend/pull/21917)

将按行窗口选择 TopK 的 ACLNN 算子加入 A2/A3 构建清单，新增 prefill/decode Torch 与 Meta 绑定，结果写入调用方提供的索引张量。实现支持 FP32/FP16/BF16 及 k≤2048，并按 UB 预算进行分块选择与合并。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +1119 / -0 · **最后提交：** 11-15 23:14 · **Draft**

<a id="pr-21912"></a>

### [#21912 · \[BugFix\] Validate layerwise prefetch before backend initialization](https://github.com/vllm-project/vllm-ascend/pull/21912)

在 MkDocs 功能导航中加入 layerwise KV pool 指南入口。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +1098 / -2280 · **最后提交：** 11-15 23:51 · **Draft**

<a id="pr-21906"></a>

### [#21906 · \[BugFix\] Complete V2 thinking budget validation and acceptance coverage](https://github.com/vllm-project/vllm-ascend/pull/21906)

为七项 thinking budget 测试配置 CI 耗时估计，覆盖基础/寻址、非约束生成、约束/自然抢占和服务场景，估计范围为 60 至 3600 秒；同时将功能教程加入 MkDocs 导航。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +1550 / -2 · **最后提交：** 11-15 19:12

<a id="pr-21905"></a>

### [#21905 · \[CI\] Avoid host problem-matcher registration in containerized pre-commit](https://github.com/vllm-project/vllm-ascend/pull/21905)

删除容器化 pre-commit 中复制及向宿主注册 problem matcher 的步骤，避免容器/宿主路径不一致导致注册失败；缓存键计算保持不变。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +0 / -15 · **最后提交：** 11-15 12:00 · **Draft**

<a id="pr-21903"></a>

### [#21903 · \[Refactor\]\[MRV2\] Reuse unified KV cache allocation for Kimi K3](https://github.com/vllm-project/vllm-ascend/pull/21903)

调整仓库 Python 编写规范，要求普通文档字符串与聚焦注释；将 DeepSeek V4.1 测试缓存视图改为复用 MRV2 统一缓存运行时接口，替代手工布局构造。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +1158 / -519 · **最后提交：** 11-15 19:22 · **Draft**

<a id="pr-21900"></a>

### [#21900 · \[Doc\] Fix broken in-page anchors in docs](https://github.com/vllm-project/vllm-ascend/pull/21900)

修正中英文模型部署教程模板内的标签页语法链接，将失效的 #3-tabs 锚点更新为 #4-tabs。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +14 / -14 · **最后提交：** 11-15 08:30

<a id="pr-21892"></a>

### [#21892 · \[Feature\] Compose HiSparse with PCP on Ascend](https://github.com/vllm-project/vllm-ascend/pull/21892)

在 Ascend MRV2 上组合 PCP 与原生 C8 HiSparse，分离本地 query 行和聚合 KV 写入/Host 镜像布局，复用 Core 加载调度并适配图执行及 MTP。相对 #20926 冻结基础修订的 PCP 增量为 13 文件；基础 PR 已合入，但作者注明当前 14a31903 尚未重跑 NPU，仍需对齐主线验证，DCP 和外部 P/D 不在支持范围。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +8011 / -96 · **最后提交：** 11-14 23:41

<a id="pr-21890"></a>

### [#21890 · \[Doc\] Fix stale file paths in docs](https://github.com/vllm-project/vllm-ascend/pull/21890)

更新社区斜杠命令和 E2E CI 贡献指南中的测试路径示例，改用现有 MRV2 Qwen、双卡数据并行及 310P dense model 测试入口。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +6 / -6 · **最后提交：** 11-14 20:18

<a id="pr-21889"></a>

### [#21889 · \[BugFix\] Allow non-root users to load operator libraries](https://github.com/vllm-project/vllm-ascend/pull/21889)

为各镜像中的 memfabric 内核安装及 ACLNN、batch-invariant 算子安装补充 --install-for-all，使生成的算子库可供非 root 用户加载。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +24 / -20 · **最后提交：** 11-14 20:07

<a id="pr-21888"></a>

### [#21888 · \[BugFix\] Allow non-root users to load operator libraries](https://github.com/vllm-project/vllm-ascend/pull/21888)

为各镜像（含 A5 UBX）的 memfabric 内核安装及 ACLNN、batch-invariant 算子安装补充 --install-for-all，避免仅 root 可访问的安装产物。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +26 / -26 · **最后提交：** 11-14 20:07

<a id="pr-21887"></a>

### [#21887 · \[BugFix\] Allow non-root users to load operator libraries](https://github.com/vllm-project/vllm-ascend/pull/21887)

在 Docker 镜像及 ACLNN、batch-invariant 构建安装脚本中启用 --install-for-all，使非 root 用户也能加载已安装算子库。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +12 / -8 · **最后提交：** 11-14 20:07

<a id="pr-21886"></a>

### [#21886 · \[CI\]\[Feature\] Publish failed Daily cases incrementally to one Issue](https://github.com/vllm-project/vllm-ascend/pull/21886)

将 Daily 失败用例增量归并到同一个主运行 Issue，跨 attempt 串行更新并保留事件去重，标题使用首次运行的东八区开始时间。正文按 UT/Nightly 分组并迁移旧平铺条目，兼容旧 attempt 标记，创建结果不明时不盲目重发。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +413 / -9 · **最后提交：** 11-15 22:30 · **Draft**

<a id="pr-21885"></a>

### [#21885 · \[Feature\] Integrate A3 W4A8 SiTU through the shared grouped matmul operator](https://github.com/vllm-project/vllm-ascend/pull/21885)

将 A3 INT8/INT4 MSD 的分组矩阵乘、SiTU 激活和逐 token 量化接入共享 GroupedMatmulSituQuant 算子，补齐 A3 构建、tiling、Torch/Meta 适配及微基准，保留 A5 MX 路径。算子接口扩展要求 OPP 与框架扩展同步重编译。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +4729 / -116 · **最后提交：** 11-14 18:16 · **Draft**

<a id="pr-21882"></a>

### [#21882 · \[Test\] Use a local work\_dir in BuildManager UT fixture](https://github.com/vllm-project/vllm-ascend/pull/21882)

为 BuildManager 单测 fixture 显式指定临时目录下的 work\_dir，避免非 root 本地测试访问默认 /root/.cache 而触发权限错误。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +3 / -0 · **最后提交：** 11-14 17:04

<a id="pr-21879"></a>

### [#21879 · \[CI\]\[Build\] Bump CANN base images to 9.3.0\_20261113161300](https://github.com/vllm-project/vllm-ascend/pull/21879)

将八份 Ubuntu/openEuler Dockerfile 的 CANN 基础镜像从 quay.io 9.2.1 切换到华为云仓库 9.3.0\_20261113161300，覆盖 310P、910B、A3 和 A5。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +8 / -8 · **最后提交：** 11-14 16:54

<a id="pr-21871"></a>

### [#21871 · \[Doc\] Use --backend in the serving benchmark example](https://github.com/vllm-project/vllm-ascend/pull/21871)

修正 serving benchmark 示例，将旧的 --endpoint-type 参数替换为 --backend openai-chat，保持数据集和聊天接口配置不变。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +1 / -1 · **最后提交：** 11-13 23:02

<a id="pr-21870"></a>

### [#21870 · \[BugFix\]\[Build\] Stop dropping AICPU sources and objects from RTY/UT builds](https://github.com/vllm-project/vllm-ascend/pull/21870)

修正 CMake 从实际 SOURCE\_DIR 搜索 AICPU 源文件，并统一使用 \_aicpu\_obj 目标名，避免 RTY/UT 相关静态库和符号库漏入 AICPU 对象。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +7 / -7 · **最后提交：** 11-14 14:09

<a id="pr-21869"></a>

### [#21869 · \[BugFix\]\[Upstream\] Fix routed experts capture on Ascend TP-sharded batches (#21619)](https://github.com/vllm-project/vllm-ascend/pull/21869)

从共享 upstream pytest 插件中移除 routed-experts forward-context 的手工桥接，保留统一补丁初始化和 spawn 设置，避免继续在测试入口重绑定该函数。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +424 / -383 · **最后提交：** 11-14 13:46

<a id="pr-21868"></a>

### [#21868 · \[Feature\]\[MoE\] Add opt-in A3 MSD SiTU fusion through shared interfaces](https://github.com/vllm-project/vllm-ascend/pull/21868)

将 A3 MSD SiTU 融合算子加入 ascend910\_93 构建，通过现有共享接口按 INT8 输入分派至新后端，保留 A5 FP8 路径及 ABI。模型融合路线为显式可选，文档注明初始算子测量尚未证明稳定性能收益，微基准也不代表服务性能。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +4645 / -3 · **最后提交：** 11-14 15:03 · **Draft**

<a id="pr-21862"></a>

### [#21862 · \[TEST\] Add blank line in csrc/build.sh to exercise PR gate](https://github.com/vllm-project/vllm-ascend/pull/21862)

调整 PR 工作流的 CPU 单测触发：纯文档、文本和图片变更可跳过，依赖清单及未知代码目录默认运行；触及源码或 CI 且尚无启用标签时暂不占用 CPU 单测，ci-gate 仍拒绝放行。同步修改下游跳过判定，并对构建脚本做空行及注释微调。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +100 / -11 · **最后提交：** 11-14 10:57

<a id="pr-21854"></a>

### [#21854 · \[Doc\]\[Feature\] Add DeepSeek-R1-Distill-Qwen-32B support](https://github.com/vllm-project/vllm-ascend/pull/21854)

在 MkDocs 模型导航中加入 DeepSeek-R1-Distill-Qwen-32B，并将其 A2、TP4、8192 上下文的 GSM8K 精度配置加入测试清单。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +169 / -0 · **最后提交：** 11-13 22:36

<a id="pr-21853"></a>

### [#21853 · \[Feature\]\[HiSparse\] Add hi\_sparse\_resolve\_residency custom ACLNN op](https://github.com/vllm-project/vllm-ascend/pull/21853)

将 HiSparse residency resolver 自定义算子加入 Ascend 950 构建清单，并注册原地更新调用方缓冲区的 Torch/Meta 接口。适配层补充热缓存大小及 SIMT UB 临时空间预算校验。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +1593 / -0 · **最后提交：** 11-14 18:09

<a id="pr-21848"></a>

### [#21848 · \[CI\]\[Misc\] Bump AISBench tag to v3.1-20261113-master](https://github.com/vllm-project/vllm-ascend/pull/21848)

将 310P、A2、A3、A5 nightly 镜像的 AISBench 默认版本更新为 v3.1-20261113-master，并同步多节点测试贡献指南。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +6 / -6 · **最后提交：** 11-13 18:14

<a id="pr-21844"></a>

### [#21844 · \[Test\] Add A2 KV-pool protection cases for Qwen3.8-27B W8A8](https://github.com/vllm-project/vllm-ascend/pull/21844)

将 Qwen3.8 KV-pool 保护测试明确路由至新增 A2 双卡分区，设置 2700 秒调度估计。共享测试设施增加 DP 指标汇总，并允许向 Mooncake master 透传额外参数。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +1322 / -1 · **最后提交：** 11-14 10:26

<a id="pr-21839"></a>

### [#21839 · \[CI\]test: Pr e2e ops](https://github.com/vllm-project/vllm-ascend/pull/21839)

将 two\_card/ops 算子测试集中到通用 A3 双卡 runner 的同一 pytest 进程，配套调整分组、耗时校验、覆盖率与日志命名，并为两条 FP8 类型判断增加精确 gitleaks 例外。当前工作流还临时将 CI 流水线变更限定为 ops 测试模式，而非全套测试。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +34398 / -33 · **最后提交：** 11-13 18:28

<a id="pr-21834"></a>

### [#21834 · \[CI\]\[Docker\] Bump mooncake-transfer-engine-npu to 0.3.14](https://github.com/vllm-project/vllm-ascend/pull/21834)

将 PR/main2main CI 与各架构镜像中的 mooncake-transfer-engine-npu 从 0.3.14rc3 升级到 0.3.14，并同步依赖版本维护文档。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +15 / -15 · **最后提交：** 11-13 16:58

<a id="pr-21833"></a>

### [#21833 · \[Feature\] Add dynamic token deferral, state restoration and rebatching for MoE decoding](https://github.com/vllm-project/vllm-ascend/pull/21833)

在 A3 算子构建清单中加入 attn\_metadata\_update、combine\_and\_dispatch\_rebatch、rebatch\_and\_update 与 moe\_token\_cut 四个编译目标。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +11834 / -9 · **最后提交：** 11-11 09:57 · **Draft**

<a id="pr-21826"></a>

### [#21826 · \[Performance\]\[Model\] Integrate the fused DeepSeek V4.1 attention epilogue on A5](https://github.com/vllm-project/vllm-ascend/pull/21826)

在 pre-commit 拼写检查的允许词中加入小写 nd，避免相关代码术语被误报；该配置改动本身不代表融合注意力算子的性能或精度已验证。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +287 / -2 · **最后提交：** 11-14 17:19 · **Draft**

<a id="pr-21822"></a>

### [#21822 · \[CI\]\[Feature\] Add Atlas 310P CI documentation and flaky reproduction test](https://github.com/vllm-project/vllm-ascend/pull/21822)

取消 PR 流水线中 select-tests 和 run-selected-tests 对 pre-commit 的直接依赖，并新增 310P 主干回归记录与 CI 看护矩阵文档。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +96 / -2 · **最后提交：** 11-13 16:42

<a id="pr-21789"></a>

### [#21789 · \[DevContainer\]\[Feature\] Add Dev Container environment settings for 310P/A2/A3/A5/CPU](https://github.com/vllm-project/vllm-ascend/pull/21789)

新增 CPU、310P、A2、A3、A5 的开发容器配置，统一源码挂载、编辑器格式化、依赖安装和 ccache 缓存；各硬件配置设置对应 CANN 镜像与编译环境。

**CI：** 失败（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +315 / -0 · **最后提交：** 11-13 11:36

<a id="pr-21777"></a>

### [#21777 · fix: pin torch==2.10.0+cpu to match torch-npu dependency](https://github.com/vllm-project/vllm-ascend/pull/21777)

将构建配置与运行依赖中的 PyTorch 固定版本从 2.10.0 改为 2.10.0+cpu。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +6 / -2 · **最后提交：** 11-13 10:24

<a id="pr-21751"></a>

### [#21751 · \[Feature\]\[Model\] Add Qwen PLE UVA host offload with DP memory sharing](https://github.com/vllm-project/vllm-ascend/pull/21751)

在 CI 预计耗时清单中登记 PLE host lookup 单卡 Triton 测试，预计运行 30 秒。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +877 / -32 · **最后提交：** 11-13 15:29

<a id="pr-21746"></a>

### [#21746 · test: cover Qwen3.6 Model Runner V2 with main-recorded goldens](https://github.com/vllm-project/vllm-ascend/pull/21746)

将 Qwen3.6 MRV2 golden 测试加入 A3 nightly，新增单卡及 TP2 测试的 900/480 秒耗时估计，并把 TP2 用例加入精度测试清单。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +4112 / -0 · **最后提交：** 11-12 23:14

<a id="pr-21717"></a>

### [#21717 · \[CI\] Restore A5 multi-node nightly test cases](https://github.com/vllm-project/vllm-ascend/pull/21717)

恢复 A5 nightly 的五项双节点测试配置，涵盖 DeepSeek V4.1/V4、GLM 5.3/5.2 和 Qwen3.5 的 PD 或 MTP 场景。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +22 / -22 · **最后提交：** 11-13 16:14

<a id="pr-21716"></a>

### [#21716 · \[临时/勿合入\] ci: route Nightly-A2 cases to offline-cluster runner labels](https://github.com/vllm-project/vllm-ascend/pull/21716)

将 Nightly-A2 的九项单节点模型用例和五组精度任务改为 linux-aarch64-a2b3-fed-karc 的对应 1/2/4/8 卡 runner 标签，测试配置与模型清单保持不变。该 PR 标为临时验证，摘要不将其视为已合入生产配置。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +14 / -14 · **最后提交：** 11-12 18:07

<a id="pr-21714"></a>

### [#21714 · \[Refactor\]\[MRV2\] Adopt EPLB policy and model-state hooks](https://github.com/vllm-project/vllm-ascend/pull/21714)

将 CI 使用的已验证 vLLM main 固定提交从 24420b7 更新为 2be40ef。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +623 / -867 · **最后提交：** 11-12 18:23 · **Draft**

<a id="pr-21713"></a>

### [#21713 · \[BugFix\] Rename static operator build option to --soc\_series](https://github.com/vllm-project/vllm-ascend/pull/21713)

将静态算子库编译和资源文件生成的长选项由 --soc\_version 统一改为 --soc\_series，保留 -s，并同步更新参数传递、临时目录及 SoC 系列帮助说明。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +10 / -10 · **最后提交：** 11-12 20:07

<a id="pr-21712"></a>

### [#21712 · \[Doc\]\[Misc\] Document Ascend Docker Runtime container setup](https://github.com/vllm-project/vllm-ascend/pull/21712)

补充 Ascend Docker Runtime 安装、验证、显式设备选择和附加宿主路径挂载说明，并从 Quick Start 链接到该可选方式。文档提示安装会重启 Docker、设备变量与 --device 会叠加，以及旧 runtime 对文件挂载项的兼容性限制。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +90 / -1 · **最后提交：** 11-12 19:48

<a id="pr-21705"></a>

### [#21705 · \[Feature\] DSpark expert-pool routing for the expert-offload path](https://github.com/vllm-project/vllm-ascend/pull/21705)

将 expert offload 单卡测试加入 A5 精选 CI 清单，路由至 a5-4 并设置 600 秒耗时估计；新增使用布局和 ACL 替身的 CPU fixture，辅助检查真实专家权重处理及传输方法。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +2871 / -6 · **最后提交：** 11-12 18:13

<a id="pr-21701"></a>

### [#21701 · \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](https://github.com/vllm-project/vllm-ascend/pull/21701)

临时将 PR E2E 工作流缩为 A3 四卡流水并行验证，固定 linux-aarch64-a3-800i-fed-karc-4，仅选取 test\_pipeline\_parallel.py，并复用已验证 vLLM main 与 csrc 缓存流程。补丁移除 lint、CPU 单测、推荐测试、其他 NPU 套件及 ci-gate，明确为 fork 专用 runner 排查而非完整合入验收。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +70 / -808 · **最后提交：** 11-12 16:27

<a id="pr-21699"></a>

### [#21699 · \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.32.0rc](https://github.com/vllm-project/vllm-ascend/pull/21699)

新增 A5 UBX 的 Ubuntu/openEuler Dockerfile，接入基础镜像及 nightly 构建矩阵，支持解析 ARG 间接引用的 CANN 基镜像和独立 UBX 标签；nightly 默认芯片列表仍不启用该变体。镜像采用 UBX CANN/PTA 组合，并统一修正 A2/A3/A5 的 FLA 下载目录，ops-transformer 与最终 UBX 版本对齐仍留 TODO。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +474 / -16 · **最后提交：** 11-13 17:21

<a id="pr-21697"></a>

### [#21697 · \[BugFix\]\[CI\] Add Qwen3.8-Flash-Next TP2 IPC coverage and preserve PLE sleep state](https://github.com/vllm-project/vllm-ascend/pull/21697)

在 CI 预计耗时清单中登记 Qwen3.8 双卡 RLHF IPC 权重传输测试，预计 180 秒。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +294 / -4 · **最后提交：** 11-13 17:59

<a id="pr-21689"></a>

### [#21689 · \[CI\] Isolate lint images by branch and add a lightweight tools image](https://github.com/vllm-project/vllm-ascend/pull/21689)

将 lint 镜像按 main/development 与 release 分支隔离，新增预装常用脚本及归档依赖的双架构 lite-tools 镜像，供测试选择、缓存准备和文档规划使用。lint 的 PR 构建不发布，tools 镜像仅手动发布，并同步更新工作流依赖条件及使用说明。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +278 / -97 · **最后提交：** 11-12 15:34

<a id="pr-21680"></a>

### [#21680 · \[Feature\]\[MoE\] Add opt-in DSpark expert-pool routing for expert offload](https://github.com/vllm-project/vllm-ascend/pull/21680)

将 expert offload 单卡测试加入 A5 精选 CI 清单，路由至 a5-4 并设置 600 秒耗时估计；新增使用布局与 ACL 替身的 CPU fixture，检查实际专家权重处理及传输方法。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +2630 / -6 · **最后提交：** 11-12 15:35 · **Draft**

<a id="pr-21674"></a>

### [#21674 · \[CI\] run.sh](https://github.com/vllm-project/vllm-ascend/pull/21674)

恢复五项 A5 双节点 nightly 测试，并将共享多节点脚本的 Git 来源从探测 CDN、ghfast、直连回退改为固定 ghfast 代理。移除低速传输中止设置及退出时额外失败提示，原日志备份和返回码处理保留。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +23 / -105 · **最后提交：** 11-13 16:20

<a id="pr-21661"></a>

### [#21661 · \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](https://github.com/vllm-project/vllm-ascend/pull/21661)

临时将 PR E2E 工作流缩为 A3 四卡流水并行验证，固定 linux-aarch64-a3-800i-fed-karc-4，仅选择 test\_pipeline\_parallel.py，并复用已验证 vLLM main 与 csrc 缓存流程。补丁移除 lint、CPU 单测、其他 NPU 套件及标签门禁，用于 fork 内排查 Post Checkout 同步停滞，不代表完整合入验收。

**CI：** 失败（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +70 / -808 · **最后提交：** 11-12 11:29

<a id="pr-21643"></a>

### [#21643 · \[Feature\]\[EC Connector\] Support encoder cache tiering offload on Ascend](https://github.com/vllm-project/vllm-ascend/pull/21643)

将 MkDocs 中的编码器缓存 CPU 卸载入口改为通用编码器缓存卸载，并同步更新中英文导航标题与文档路径。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** +549 / -65 · **最后提交：** 11-12 10:01

<a id="pr-21638"></a>

### [#21638 · \[Feature\]\[Qwen\] Share PLE tables across Ascend services](https://github.com/vllm-project/vllm-ascend/pull/21638)

在检测到 HIXL 头文件与 cann\_hixl 库时，新增编译安装独立 C ABI 的 engram\_hixl 共享库。原生封装支持内存注册、连接和同步读取、按行打包及资源清理，并校验监听端口与本地通信资源配置。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +4569 / -3 · **最后提交：** 11-12 08:53 · **Draft**

<a id="pr-21623"></a>

### [#21623 · \[Feature\]\[Engram\] Add local host VMM for shared A3 tables](https://github.com/vllm-project/vllm-ascend/pull/21623)

在 A3 构建中探测可选 CANN Fabric-handle API，满足条件时编译安装 Engram 主机 VMM 共享库，并新增中英文文档导航。原生实现提供跨进程句柄导入、映射生命周期和失败清理重试，不将这些实现视为硬件验证结果。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +2466 / -99 · **最后提交：** 11-11 21:00

<a id="pr-21607"></a>

### [#21607 · \[Test\]\[Upstream\]rerun failed test case](https://github.com/vllm-project/vllm-ascend/pull/21607)

为 upstream E2E 增加 PR 触发，启用单卡任务在线下载，并把多卡及在线任务固定路由到 linux-aarch64-a2b3-0。新增重跑/0.33.0 测试清单，默认切换到增补清单；补丁中仍有重复测试条目和重复 YAML 分组键，尚不能视为覆盖校验已完成。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +239 / -6 · **最后提交：** 11-14 16:58

<a id="pr-21594"></a>

### [#21594 · \[Feature\]\[MoE\] Support anchor-union activation routing for DSpark and DFlash speculative decoding](https://github.com/vllm-project/vllm-ascend/pull/21594)

将 expert offload 单卡测试加入 A5 精选 CI 清单，路由至 a5-4 并设置 600 秒耗时估计；新增使用布局与 ACL 替身的 CPU fixture，检查实际专家权重处理及传输方法。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +3880 / -4 · **最后提交：** 11-12 15:47 · **Draft**

<a id="pr-21546"></a>

### [#21546 · \[CI\] update cann=9.3.0\_20261110170400](https://github.com/vllm-project/vllm-ascend/pull/21546)

将 A2、A3、A5 和 310P 的 Ubuntu/openEuler 共八个 Dockerfile 基础镜像从 CANN 9.2.1 更新为 9.3.0\_20261110170400，并由 Quay 切换到华为云 atlas\_inference 仓库。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +8 / -8 · **最后提交：** 11-11 14:26

<a id="pr-21541"></a>

### [#21541 · \[Doc\] add doc quality review workflow for docs/source changes](https://github.com/vllm-project/vllm-ascend/pull/21541)

新增文档质量检查工作流，结合规则脚本与 LLM 检查 Markdown 和 PO 翻译文件，归并问题并发布 PR 汇总与差异行评论。配套脚本生成修订建议并保存评估产物。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +2192 / -0 · **最后提交：** 11-13 17:37 · **Draft**

<a id="pr-21536"></a>

### [#21536 · \[Feature\]\[KV Cache\] Add exact-position hybrid-state checkpoints on Ascend](https://github.com/vllm-project/vllm-ascend/pull/21536)

在 MkDocs 功能导航中加入 FlashState 混合状态检查点文档入口，并建立对应单测包。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +3543 / -0 · **最后提交：** 11-14 15:14

<a id="pr-21526"></a>

### [#21526 · \[Performance\]\[Kernel\] Fuse DeepSeek-V4.1 indexer prologue on Ascend A2/A3](https://github.com/vllm-project/vllm-ascend/pull/21526)

将 fused\_indexer\_prologue 接入 A2/A3 算子构建清单，注册 Torch NPU 与 Meta 接口，支持原地更新 K cache 和 scale cache；摘要聚焦构建与绑定接入。（保留上次摘要；当前提交待核验。）

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21521"></a>

### [#21521 · Upgrade/cann v0.32](https://github.com/vllm-project/vllm-ascend/pull/21521)

相关文件已纳入关注，当前提交的变更摘要待补齐。（保留上次摘要；当前提交待核验。）

**CI：** 失败（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21513"></a>

### [#21513 · \[Doc\] Add deepseek\_v41\_qli\_candidate to nav and fix FAQ anchor](https://github.com/vllm-project/vllm-ascend/pull/21513)

在 MkDocs 开发者导航中补入 DeepSeek V4.1 QLI candidate 页面，使该文档可从站点目录访问。（保留上次摘要；当前提交待核验。）

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21502"></a>

### [#21502 · \[Feature\]\[Performance\] Support InternLM2-20B-Chat and dispatch scaled RoPE variants to the NPU kernel](https://github.com/vllm-project/vllm-ascend/pull/21502)

将 InternLM2-20B-Chat 加入 nightly 精度测试、模型下载清单与文档导航，并为双卡测试设置 900 秒调度估计及 Atlas A2 BF16/TP2 精度配置。（保留上次摘要；当前提交待核验。）

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21500"></a>

### [#21500 · \[BugFix\] Reap stale opc locks and cap build parallelism by cgroup memory limit](https://github.com/vllm-project/vllm-ascend/pull/21500)

相关文件已纳入关注，当前提交的变更摘要待补齐。（保留上次摘要；当前提交待核验。）

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 01:52；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21493"></a>

### [#21493 · \[临时/勿合入\] a3-800i fed-2 / fed-4 各跑 3 个用例（验证 runner 作业 pod）](https://github.com/vllm-project/vllm-ascend/pull/21493)

将 E2E 工作流临时缩减为 A3 FED 2 卡和 4 卡 runner 各三个用例，以验证作业 Pod，并使用已验证的 vLLM main 提交。该验证显式省略 lint、CPU UT、其他 NPU 测试和标签门禁，补丁注明不用于合入。（保留上次摘要；当前提交待核验。）

**CI：** 失败（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21490"></a>

### [#21490 · \[临时/勿合入\] 全量 A2/A3 业务选测跑 karc fed runner（对齐 #20716）](https://github.com/vllm-project/vllm-ascend/pull/21490)

临时将 main 的 A2/A3 全量业务选测分组改派至对应卡数的 FED runner，上游单卡测试也改用 A2 FED 标签，同时保留已验证 vLLM main 和 csrc 缓存流程。补丁省略 lint、CPU 单测、精确推荐及标签门禁，用于 runner 验证，不代表完整合入验收。

**CI：** 失败（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +54 / -799 · **最后提交：** 11-12 09:39 · **Draft**

<a id="pr-21489"></a>

### [#21489 · \[Test\]\[Feature\] Add GLM-5.3 W4A4C8 MTP coverage on A5](https://github.com/vllm-project/vllm-ascend/pull/21489)

相关文件已纳入关注，当前提交的变更摘要待补齐。（保留上次摘要；当前提交待核验。）

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21481"></a>

### [#21481 · \[CI\] memcache cases](https://github.com/vllm-project/vllm-ascend/pull/21481)

在 A3 weekly 中新增一项四节点 GLM 长上下文 Memcache 测试及四项双节点 DeepSeek Memcache/无缓存对照测试，并补齐五个前缀缓存相关数据集下载项。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +1236 / -1 · **最后提交：** 11-13 15:21

<a id="pr-21480"></a>

### [#21480 · \[Cherry-pick\]\[releases/v0.32.0rc\]\[CI\]\[BugFix\] Skip CANN 9.2.x custom-op .so validation in A5 wheel build (from #21479)](https://github.com/vllm-project/vllm-ascend/pull/21480)

相关文件已纳入关注，当前提交的变更摘要待补齐。（保留上次摘要；当前提交待核验。）

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21479"></a>

### [#21479 · \[CI\]\[BugFix\] Skip CANN 9.2.x custom-op .so validation in A5 wheel build](https://github.com/vllm-project/vllm-ascend/pull/21479)

相关文件已纳入关注，当前提交的变更摘要待补齐。（保留上次摘要；当前提交待核验。）

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21469"></a>

### [#21469 · \[Misc\] main2main: upgrade verified vLLM main from 1106 to 1112](https://github.com/vllm-project/vllm-ascend/pull/21469)

将 CI 使用的已验证 vLLM main 提交更新为 3b95523，并为 categorical sample bias 测试增加 120 秒估计。补充主线/0.33.0 图调度及缓存请求 ABI 测试适配，保持旧版本补丁测试与当前主线接口分离。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +3614 / -445 · **最后提交：** 11-15 11:42 · **Draft**

<a id="pr-21459"></a>

### [#21459 · \[临时/勿合入\] 验证 karc 线下成员：a3-800i-fed-16 + a2-fed-2 smoke](https://github.com/vllm-project/vllm-ascend/pull/21459)

相关文件已纳入关注，当前提交的变更摘要待补齐。（保留上次摘要；当前提交待核验。）

**CI：** 失败（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21456"></a>

### [#21456 · \[Refactor\]\[CP\] Decouple PCP/DCP metadata, topology and backend selection](https://github.com/vllm-project/vllm-ascend/pull/21456)

为 A3-560T nightly 增加 Qwen3 GQA PCP2/DCP2 32k 和 DeepSeek MLA PCP2/DCP4 128k 两项配置，并将四卡 CP 矩阵测试加入精度清单，设置 3600 秒初始调度估计。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +3572 / -345 · **最后提交：** 11-15 22:54

<a id="pr-21385"></a>

### [#21385 · \[releases/v0.30.0\]\[Test\]\[Feature\] Add Kimi-K3 W4A8 E256 accuracy test on A5](https://github.com/vllm-project/vllm-ascend/pull/21385)

为发布分支的 A5 nightly 工作流增加诊断文件收集和 AOP 二分日志上传，并接入 Kimi-K3 测试任务。通用单节点测试框架新增独立多轮执行及逐轮产物保留。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +592 / -4 · **最后提交：** 11-13 14:51

<a id="pr-21338"></a>

### [#21338 · \[CI\]\[Model\] Add Flash A3 ReplaySSM and Decode replay Weekly coverage](https://github.com/vllm-project/vllm-ascend/pull/21338)

在 A3 weekly 注册 GLM-5.3-Flash 的 ReplaySSM 与 Decode replay 两种双节点 PD 测试。配套 CPU 检查验证设备分配、命令渲染和缓存重放顺序，硬件效果仍待验证。（保留上次摘要；当前提交待核验。）

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21334"></a>

### [#21334 · \[CI\] add single-node test for a3,a5- #20846](https://github.com/vllm-project/vllm-ascend/pull/21334)

为 PR CI 增加 A3/A5 单节点算子精选套件，分别固定到 a3-800i-8 与 a5-4 runner，由 ready-precise/ready-all 触发并纳入 ci-gate。runner 映射校验扩展到完整 E2E 树，选中测试脚本改为继续执行其他目标后再汇总失败。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +162 / -3 · **最后提交：** 11-12 17:08

<a id="pr-21284"></a>

### [#21284 · \[Test\] Add five-round Kimi-K3 Experts256 A5 nightly coverage](https://github.com/vllm-project/vllm-ascend/pull/21284)

为 A5 nightly 增加 Kimi-K3 测试配置及诊断产物下载，允许跳过不存在的可选日志路径。通用单节点测试框架支持按配置独立运行多轮，并逐轮保存结果和基准产物。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +354 / -5 · **最后提交：** 11-13 17:36

<a id="pr-21276"></a>

### [#21276 · \[Refactor\] remove simple cpu offload](https://github.com/vllm-project/vllm-ascend/pull/21276)

从 CI 耗时配置和 upstream 测试清单中删除 simple CPU/KV offload 相关项目，并移除生成测试矩阵中的两项用例及对应测试包说明。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +15 / -1041 · **最后提交：** 11-11 16:04

<a id="pr-21261"></a>

### [#21261 · \[BugFix\]\[EPLB\] Validate STAIR placements against per-step load](https://github.com/vllm-project/vllm-ascend/pull/21261)

将 MRV2 STAIR 逐步负载校验的四卡测试加入 A5 精选 CI 清单。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +209 / -39 · **最后提交：** 11-15 21:43

<a id="pr-21260"></a>

### [#21260 · \[Feature\]\[EPLB\] Export committed MRV2 expert placement](https://github.com/vllm-project/vllm-ascend/pull/21260)

将 MRV2 已提交专家布局导出的双卡测试加入 A5 精选 CI 清单。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +345 / -8 · **最后提交：** 11-15 21:43

<a id="pr-21190"></a>

### [#21190 · \[Performance\]\[Worker\] Reuse attention metadata and keep DFlash2 lengths on device](https://github.com/vllm-project/vllm-ascend/pull/21190)

为 cached GDN decode 和 metadata reuse 两项 NPU 测试增加各 600 秒初始 CI 调度估计，并新增对齐状态索引及图状态批量写入微基准；这些微基准不代表模型 TPOT 或 DFlash 接受率验证。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +4822 / -220 · **最后提交：** 11-15 16:28

<a id="pr-21045"></a>

### [#21045 · \[CI\] Add DeepSeek-v4.1 test case](https://github.com/vllm-project/vllm-ascend/pull/21045)

在 A3 weekly 调度中新增三节点 MiniMax-M3 W8A8 1M PD，以及两节点 DeepSeek-V4.1-Flash W8A8 1M PD 和 GLM-5.3-Flash W8A8 1M 1P1D 配置。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +867 / -118 · **最后提交：** 11-12 17:26

<a id="pr-21005"></a>

### [#21005 · \[Misc\] main2main 1106](https://github.com/vllm-project/vllm-ascend/pull/21005)

将 CI 使用的已验证 vLLM main 提交更新为 ba15685，并为 KV offload 单测的模拟模型信息补齐 speculator\_config\_class 字段。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +1232 / -220 · **最后提交：** 11-15 17:43

<a id="pr-20914"></a>

### [#20914 · \[Attention\]\[BugFix\] Use request incarnation IDs for sparse KV offload](https://github.com/vllm-project/vllm-ascend/pull/20914)

为 sparse KV offload 生命周期测试增加 A3 专用 MemFabric AccOffload 安装及 ELF/加载入口校验步骤，限定 15 分钟。该测试被路由至 A3 双卡 runner，并配置 600 秒调度估计。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 00:47；当前提交） · **改动：** +1016 / -33 · **最后提交：** 11-14 10:17

<a id="pr-20757"></a>

### [#20757 · \[Test\] Add KV pool hit watch to A3 PR e2e cases](https://github.com/vllm-project/vllm-ascend/pull/20757)

在共享 E2E runner 中增加引擎计数器/仪表指标读取和跨 DP rank 汇总，支持 KV pool 命中观测，同时上调六项 A3 测试的 CI 调度耗时估计。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +1409 / -162 · **最后提交：** 11-15 17:33

<a id="pr-20756"></a>

### [#20756 · \[BugFix\]\[Model\] Support dense sequence parallelism for the Qwen3.5 family (Qwen3.8-27B)](https://github.com/vllm-project/vllm-ascend/pull/20756)

为 Qwen3.8-27B dense SP 双卡端到端用例新增 600 秒的 CI 调度预估时长。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +779 / -28 · **最后提交：** 11-13 12:03

<a id="pr-20633"></a>

### [#20633 · \[CI\] add test cases for Qwen3.6-35B-w8a8](https://github.com/vllm-project/vllm-ascend/pull/20633)

在 A3 nightly 和 weekly 配置中加入 Qwen3.6-35B-A3B w8a8 FullAndPiecewise 测试，分别指定 800i-16 与 800t-16 runner。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +454 / -346 · **最后提交：** 11-13 18:13

<a id="pr-20575"></a>

### [#20575 · \[CI\]\[Model\] Add combined GLM-5.3 P/PD/decode Weekly coverage](https://github.com/vllm-project/vllm-ascend/pull/20575)

为 Weekly-A3 增加 GLM-5.3 分拆及组合测试矩阵，并新增可由 PR 命令触发的 Weekly-A5 工作流与产物汇总。通用多节点配置解析同步支持替换基准参数中的集群地址占位符。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +3577 / -5 · **最后提交：** 11-13 15:16 · **Draft**

<a id="pr-20528"></a>

### [#20528 · \[Feature\] Integrate Ascend SleepModeBackend lifecycle](https://github.com/vllm-project/vllm-ascend/pull/20528)

注册 Ascend sleep backend 通用插件入口，补充开发者导航、资源所有权和分阶段唤醒说明，并增加睡眠/恢复、请求边界及备份失败回滚的测试探针。CaMem 在释放物理内存后清空句柄，避免睡眠张量删除时重复释放；文档明确新后端为显式可选，配置支持不等于硬件验收。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +1587 / -72 · **最后提交：** 11-15 21:43

<a id="pr-20494"></a>

### [#20494 · \[Feature\]\[MoE\] Add CatCCOS MegaMoE backend for DeepSeek-V4-Flash on Ascend A5](https://github.com/vllm-project/vllm-ascend/pull/20494)

修正共享 Bisheng 包装脚本的文件清空语法，并在 Ascend950 构建中规避 CANN 9.1 SwigluGroupQuant schema 冲突、生成和校验旋转算子二进制元数据。新增 DeepSeek CatCCOS 接入说明及配套服务 A/B、profiling 工具和导航，区分实际通信路径与全局/本 rank token 数，避免将诊断耗时当成正式性能结论。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +3650 / -173 · **最后提交：** 11-15 22:03 · **Draft**

<a id="pr-20493"></a>

### [#20493 · \[Feature\]\[MoE\] Add CatCCOS MegaMoE backend for Qwen3 on Ascend A5](https://github.com/vllm-project/vllm-ascend/pull/20493)

修正共享 Bisheng 包装脚本的文件清空语法，并新增 CatCCOS/native MC2 服务 A/B 与 profiling 文档、导航和工具。工具按实际后端及全局/本 rank token 数汇总耗时，文档要求正式性能测试关闭 profiler，并保留超出 MC2 容量时的原生回退对照。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +3002 / -125 · **最后提交：** 11-15 22:03 · **Draft**

<a id="pr-20427"></a>

### [#20427 · \[Feature\] Restore A5 MRV2 ACL graphs in place across sleep](https://github.com/vllm-project/vllm-ascend/pull/20427)

将 sleep graph reuse 测试加入 A5 精选清单，指定 a5-4 runner 并设置 420 秒耗时估计。CaMem 分离物理所有权与映射状态，增加互斥、释放完成回调和失败后拒绝继续使用的保护，减少睡眠或部分驱动失败后的重复释放风险。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +2605 / -100 · **最后提交：** 11-15 21:43

<a id="pr-20345"></a>

### [#20345 · \[Performance\]\[Worker\] Reuse V2 attention metadata across cache groups and batch GDN state writes](https://github.com/vllm-project/vllm-ascend/pull/20345)

为 cached GDN decode 和 metadata reuse 两项 NPU 测试增加各 600 秒初始 CI 调度估计，并新增对齐状态索引及图状态批量写入微基准；这些微基准不代表模型 TPOT 或 DFlash 接受率验证。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +2984 / -171 · **最后提交：** 11-14 18:27

<a id="pr-20299"></a>

### [#20299 · \[Feature\] Integrate the packaged DeepGEMM V4.1 MegaMoE backend on Ascend 950](https://github.com/vllm-project/vllm-ascend/pull/20299)

将固定修订的 DeepGEMM 原生扩展及 JIT 头文件纳入 A5 wheel/可编辑安装，记录依赖版本和构建校验信息；A5 镜像与 CI 同步安装 GCC 13+、elfutils 和固定版本解析器依赖，编译器选择仅作用于该扩展。另增加面向调用方输出缓冲区的 MXFP8 量化绑定，实际数值与多卡性能仍需独立验证。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +1378 / -14 · **最后提交：** 11-14 18:27 · **Draft**

<a id="pr-20205"></a>

### [#20205 · \[Feature\] Support draft model weight updates over HCCL](https://github.com/vllm-project/vllm-ascend/pull/20205)

为通过 HCCL 更新 draft 模型权重的双卡测试新增 510 秒 CI 调度耗时估计。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +787 / -53 · **最后提交：** 11-14 11:14

<a id="pr-20138"></a>

### [#20138 · \[Feature\]\[RuntimeGuard\] Add rare\_chars detector with async pair collect](https://github.com/vllm-project/vllm-ascend/pull/20138)

调整 setuptools 构建，将 rare\_feed\_native 纯 CPython 扩展与 CMake 扩展分开处理，保证关闭自定义 Ascend 算子时仍可打包，并纳入 rare 配置和表数据。同步为引入的 rare\_chars 算法目录设置格式与拼写检查豁免。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +5245 / -43 · **最后提交：** 11-14 23:18

<a id="pr-19884"></a>

### [#19884 · \[Feature\] Decoder Append-Prefill for Agentic Scenario Prefiller Offloading](https://github.com/vllm-project/vllm-ascend/pull/19884)

在 MkDocs 功能导航中加入 Decoder Append-Prefill 文档入口，使该功能说明可从站点目录访问。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +5941 / -2 · **最后提交：** 11-13 09:34

<a id="pr-19442"></a>

### [#19442 · \[BugFix\]\[Test\] Declare GDN batch-invariance support and cover Qwen3.5-35B-A3B in the TP4 e2e](https://github.com/vllm-project/vllm-ascend/pull/19442)

将 TP4 batch-invariance 测试的 CI 调度耗时估计从 160 秒提高至 360 秒，以配合扩展后的测试覆盖。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +82 / -32 · **最后提交：** 11-14 15:14

<a id="pr-18922"></a>

### [#18922 · \[Test\]\[Misc\] update A5 muiltinodes cases](https://github.com/vllm-project/vllm-ascend/pull/18922)

新增 Weekly-A5 工作流与 /weekly A5 分发及结果链接，接入 A5 单机、多机测试矩阵和镜像构建。（保留上次摘要；当前提交待核验。）

**CI：** 失败（ci-gate）（最近已知；上次完整检查：11-15 13:00；提交对应关系待核验）（恢复保留；待刷新） · **改动：** +524 / -1 · **最后提交：** 11-10 09:27

<a id="pr-18849"></a>

### [#18849 · \[BugFix\]\[AscendStore\] Publish unique CPU KV events for sharded stores](https://github.com/vllm-project/vllm-ascend/pull/18849)

为未提供类型桩的 mooncake.engine 增加 mypy 缺失导入豁免，保留现有 memfabric\_hybrid 配置。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +783 / -112 · **最后提交：** 11-15 11:21

<a id="pr-18604"></a>

### [#18604 · \[Feature\]\[MoE\] Add exact expert offload for V2 eager and decode ACL graphs](https://github.com/vllm-project/vllm-ascend/pull/18604)

将 expert offload 的单卡端到端用例加入 A5 精选 CI 测试集，指定 a5-4 runner，并设置 600 秒调度预估时长。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +2017 / -0 · **最后提交：** 11-13 11:50

<a id="pr-18559"></a>

### [#18559 · \[CI\] kv\_pool cases](https://github.com/vllm-project/vllm-ascend/pull/18559)

在 A3 nightly 配置新增 DeepSeek-V4-flash w8a8 Mooncake 测试，并在 weekly 配置新增 DeepSeek-V4.1-Flash W8A8 Mooncake 测试，两项 size 均设为 2。（保留上次摘要；当前提交待核验。）

**CI：** 通过（最近已知；上次完整检查：11-15 13:33；提交对应关系待核验）（恢复保留；待刷新） · **改动：** +462 / -1 · **最后提交：** 11-12 15:39

<a id="pr-18057"></a>

### [#18057 · \[Performance\] \[310P\] integrate GDN custom ops via cann\_ops\_transformer](https://github.com/vllm-project/vllm-ascend/pull/18057)

为 310P 精选 CI 新增 GDN 包预构建、缓存恢复及校验流程，缓存键包含架构、镜像标签、固定源码版本和构建脚本摘要，并复用独立 Torch 扩展目录。Ubuntu/openEuler 310P 镜像同步构建安装匹配的算子包与 Python 桥接，设置自定义算子搜索路径。（保留上次摘要；当前提交待核验。）

**CI：** 失败（ci-gate）（最近已知；上次完整检查：11-15 13:00；提交对应关系待核验）（恢复保留；待刷新） · **改动：** +641 / -4 · **最后提交：** 10-30 14:10

<a id="pr-18042"></a>

### [#18042 · \[Test\]\[Kimi\] Add Kimi K3 MRV2 PR and nightly coverage](https://github.com/vllm-project/vllm-ascend/pull/18042)

将 Kimi K3 MRV2 加入 A3 nightly、模型下载清单，并为四卡 PR 测试设置 720 秒调度估计；新增四节点、每节点 16 NPU 的 DP4/TP16/EP64 配置。该配置中的 GPQA 门槛暂宽松，性能基线暂禁用，不能当作精度或性能已经验收。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 03:01；当前提交） · **改动：** +293 / -7 · **最后提交：** 10-16 12:01

<a id="pr-17833"></a>

### [#17833 · \[Feature\]\[Worker\] Add MRV2 KV Trace](https://github.com/vllm-project/vllm-ascend/pull/17833)

为 KV Trace 单卡测试配置 600 秒初始 CI 耗时估计，覆盖 eager/FULL 与 trace 开关组合，并将 KV Trace 功能文档加入 MkDocs 导航。

**CI：** 通过（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +2284 / -1 · **最后提交：** 11-15 10:50

<a id="pr-12751"></a>

### [#12751 · \[CI\] Pin dorny/paths-filter to compatible v4.0.3](https://github.com/vllm-project/vllm-ascend/pull/12751)

将 PR 测试工作流的 dorny/paths-filter 从 v4 固定到 v4.0.3。

**CI：** 失败（ci-gate）（最近已知；待刷新；上次完整检查：11-16 04:18；当前提交） · **改动：** +1 / -1 · **最后提交：** 11-13 17:59
