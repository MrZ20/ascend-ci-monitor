# PR 关注列表

最近刷新：2026-11-12 18:50:08（上海时间）
当前关注的开放 PR：117
范围：最近 30 天有创建、提交、CI、Draft 或目标分支变化证据的开放 PR；普通评论不算活动。
长期无元数据更新的旧 PR 未逐个追查仅 CI 重跑的活动，本页不代表这类活动已全覆盖。

活动待确认：387 个较早创建、近期 updated_at 变化的开放 PR 尚无最近 30 天有效活动证据，暂不纳入。

覆盖说明：984 个近 30 天范围内的 PR 文件范围或详情待补齐。

本轮覆盖缺口：84 项采集未完成；受影响状态显示未知或等待补齐。

## 最近更新（72h）

- [11-12 18:35 · #21717 \[CI\] Restore A5 multi-node nightly test cases](#pr-21717)
- [11-12 18:35 · #21716 \[临时/勿合入\] ci: route Nightly-A2 cases to offline-cluster runner labels](#pr-21716)
- [11-12 18:35 · #21715 \[Performance\] Fuse matmul-collective ops for dense sequence parallelism (MC2)](#pr-21715)
- [11-12 18:35 · #21714 \[Refactor\]\[MRV2\] Adopt EPLB policy and model-state hooks](#pr-21714)
- [11-12 18:35 · #21713 \[Doc\]soc\_version and soc\_series names refresh](#pr-21713)
- [11-12 18:35 · #21712 \[Doc\]\[Misc\] Document Ascend Docker Runtime container setup](#pr-21712)
- [11-12 18:35 · #21705 \[Feature\] DSpark expert-pool routing for the expert-offload path](#pr-21705)
- [11-12 18:35 · #21687 \[Feature\]\[Kimi\] Provision the shared draft embedding on the last PP stage](#pr-21687)
- [11-12 18:35 · #21686 \[BugFix\] Read quantized checkpoint indexes for RFork model state](#pr-21686)
- [11-12 18:35 · #21624 \[Feature\]\[Model\] Add Kimi fine-grained projection and shared-expert TP](#pr-21624)
- [11-12 18:35 · #21541 \[Doc\] add doc quality review workflow for docs/source changes](#pr-21541)
- [11-12 18:35 · #21536 \[Feature\]\[KV Cache\] Prototype FlashStates frontier integration on Ascend (WIP)](#pr-21536)
- [11-12 18:35 · #21481 \[CI\] memcache cases](#pr-21481)
- [11-12 18:35 · #21469 \[Misc\] main2main: upgrade verified vLLM main from 1106 to 1112](#pr-21469)
- [11-12 18:35 · #21464 \[v0.32.0rc\]\[Doc\]\[BugFix\] Fix truncated model support tables in Chinese docs](#pr-21464)
- [11-12 18:35 · #21459 \[临时/勿合入\] 验证 karc 线下成员：a3-800i-fed-16 + a2-fed-2 smoke](#pr-21459)
- [11-12 17:40 · #21709 \[Performance\] Replace padding-mask fills with a single writeback for GLM5.3-Flash decode](#pr-21709)
- [11-12 17:40 · #21707 \[Refactor\]\[RFork\] Drop Model Runner V1 EPLB bypass paths](#pr-21707)
- [11-12 17:40 · #21706 feat: add target LM head dynamic quantization for runner V2](#pr-21706)
- [11-12 17:40 · #21700 \[BugFix\] Surface actionable MemCache driver-version init errors](#pr-21700)
- [11-12 17:40 · #21636 \[Feature\]\[Stacked\]\[v0.32.0rc\]\[Qwen4Exp\] MRV2 preparation with union GBSA, CPU-sync and RecoverSSM](#pr-21636)
- [11-12 17:40 · #21587 \[Feature\] Fuse GatingTopK with EPLB expert mapping](#pr-21587)
- [11-12 17:40 · #21584 \[Performance\]\[Kernel\] Share exact radix sorting across BF16 and FP32 candidate packing](#pr-21584)
- [11-12 16:59 · #21701 \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](#pr-21701)
- [11-12 16:59 · #21699 \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.32.0rc](#pr-21699)
- [11-12 16:59 · #21697 \[BugFix\] Support Qwen3.8 text-only IPC weight-transfer CI](#pr-21697)
- [11-12 16:59 · #21695 \[Doc\]\[BugFix\] Fix truncated model support tables in Chinese docs](#pr-21695)
- [11-12 16:59 · #21694 \[bugfix\]pp oom](#pr-21694)
- [11-12 16:59 · #21693 \[Feature\]\[Model\] Support prefill context parallelism for Qwen3.8-Flash-Next](#pr-21693)
- [11-12 16:59 · #21690 \[BugFix\]\[Feature\] Enable Mooncake V2 layerwise push and preserve allocation blocks](#pr-21690)
- [11-12 16:59 · #21689 \[CI\] Isolate lint images by branch and add a lightweight tools image](#pr-21689)
- [11-12 16:59 · #21688 Pcp short prefill all backends](#pr-21688)
- [11-12 16:59 · #21685 \[CI\] add presmoke for CI](#pr-21685)
- [11-12 16:59 · #21683 \[BugFix\] Allow C8 KV transfer with AscendStore Memcache](#pr-21683)
- [11-12 16:59 · #21680 \[Feature\]\[MoE\] Add opt-in DSpark expert-pool routing for expert offload](#pr-21680)
- [11-12 16:59 · #21679 \[Performance\]\[MoE\] Move shared-expert padding before Down](#pr-21679)
- [11-12 16:59 · #21673 \[BugFix\]\[PD\] Preserve cache usage across proxy response chunks](#pr-21673)
- [11-12 16:59 · #21672 \[v0.32.0rc\]\[Doc\] Translated Doc files 2026-11-12](#pr-21672)
- [11-12 16:59 · #21671 \[Bugfix\] Build DSpark graph metadata with uniform query boundaries](#pr-21671)
- [11-12 16:59 · #21670 \[Feature\] Add independent shared-expert fine-grained TP](#pr-21670)
- [11-12 16:59 · #21669 \[Feature\]\[Model\] Add experimental MiniMax M3.1 indexer DCP](#pr-21669)
- [11-12 16:59 · #21668 \[Feature\] Support draft\_lm\_head\_quantization (fp8) on Ascend NPU](#pr-21668)
- [11-12 16:59 · #21664 \[BugFix\]\[Qwen4Exp\] Use Ascend UVA for pinned PLE weights](#pr-21664)
- [11-12 16:59 · #21663 \[Feature\] L2 Embedding Cache](#pr-21663)
- [11-12 16:59 · #21661 \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](#pr-21661)
- [11-12 16:59 · #21660 perf: fuse rotated Engram gate on A3](#pr-21660)
- [11-12 16:59 · #21659 \[Feature\]\[DeepSeek-V4.1\] Enable A3 metadata multistream execution](#pr-21659)
- [11-12 16:59 · #21657 \[Test\] kimi-k3 nightly](#pr-21657)
- [11-12 16:59 · #21655 \[Performance\] Fuse A5 recurrent GDN preprocessing and refresh gate bias after reload](#pr-21655)
- [11-12 16:59 · #21654 \[v0.32.0rc\]\[Qwen4Exp\] Consolidate A5 QSA and MRV2 performance patches](#pr-21654)
- [11-12 16:59 · #21653 \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.30.0](#pr-21653)
- [11-12 16:59 · #21652 \[BugFix\] Honor NZ mode for DeepSeek V4/V4.1 grouped output projections](#pr-21652)
- [11-12 16:59 · #21648 \[Doc\]\[BugFix\] Fix DeepSeek-V4.1-Flash launcher links in Chinese docs](#pr-21648)
- [11-12 16:59 · #21645 \[Attention\]\[BugFix\] Retain CANN FlashAttn for native MiniMax DSpark graphs](#pr-21645)
- [11-12 16:59 · #21643 \[Feature\]\[EC Connector\] Support encoder cache tiering offload on Ascend](#pr-21643)
- [11-12 16:59 · #21639 \[BugFix\] Select vLLM KV cache helpers by availability](#pr-21639)
- [11-12 16:59 · #21638 \[Feature\]\[Qwen\] Share PLE tables across Ascend services](#pr-21638)
- [11-12 16:59 · #21637 \[BugFix\]\[P/D\] Surface missing prompt-token details in the PD proxy](#pr-21637)
- [11-12 16:59 · #21635 \[Stacked\]\[Qwen4Exp\] MRV2 input preparation with union GBSA, CPU-sync and RecoverSSM](#pr-21635)
- [11-12 16:59 · #21631 \[Feature\] Add Ascend overlay for deepseek-ai/DeepSeek-V4-Flash](#pr-21631)
- [11-12 16:59 · #21630 \[BugFix\]\[SpecDecode\] Support replicated DFlash/DFlash2 execution with PCP on MRV2](#pr-21630)
- [11-12 16:59 · #21629 \[BugFix\]\[ExampleProxy\] Use round-robin ticket as heap tiebreaker to fix instance load skew](#pr-21629)
- [11-12 16:59 · #21627 \[Performance\] Integrate union GBSA prefill for Qwen4Exp](#pr-21627)
- [11-12 16:59 · #21623 \[Feature\]\[Engram\] Add local host VMM for shared A3 tables](#pr-21623)
- [11-12 16:59 · #21622 \[Feature\] Support bilateral DCP in MooncakePushConnector](#pr-21622)
- [11-12 16:59 · #21621 \[BugFix\]\[DSpark\]\[EPLB\] Fix V4.1 draft expert loading and registration](#pr-21621)
- [11-12 16:59 · #21607 \[Test\]\[Upstream\]rerun failed test case](#pr-21607)
- [11-12 16:59 · #21605 \[Performance\]\[A3\] Cache row weights for packed DCP LSE combine](#pr-21605)
- [11-12 16:59 · #21604 \[BugFix\]\[Quantization\] Reject native FP8 checkpoints on non-950 devices](#pr-21604)
- [11-12 16:59 · #21603 \[Performance\]\[Kernel\] Adapt owner-prefix peer counting on A3](#pr-21603)
- [11-12 16:59 · #21600 \[BugFix\]\[KVPool\] Report synchronous hybrid load failures by request](#pr-21600)
- [11-12 16:59 · #21594 \[Feature\]\[MoE\] Support anchor-union activation routing for DSpark and DFlash speculative decoding](#pr-21594)
- [11-12 16:59 · #21589 \[Performance\] Skip QSA CPU length sync for Ascend builder](#pr-21589)
- [11-12 16:59 · #21586 \[Performance\]\[Kernel\] Use rectangular tiles for D512 DCP output packing](#pr-21586)
- [11-12 16:59 · #21580 \[Feature\]\[Attention\] Support quant\_mode=5 pseudo-quant for MTP decode in C8 backend](#pr-21580)
- [11-12 16:59 · #21575 \[BugFix\] Preserve Mamba checkpoints in consumer chunked prefill](#pr-21575)
- [11-12 16:59 · #21565 \[Test\]\[Sleep Mode\] Harden RLHF sleep/wake harness timeouts](#pr-21565)
- [11-12 16:59 · #21557 \[BugFix\]\[v0.32.0rc\] Sync SWA block IDs before KV Pool prefill saves](#pr-21557)
- [11-12 16:59 · #21555 feat(ci): add /presmoke command for PR-level CANN image presmoke](#pr-21555)
- [11-12 16:59 · #21554 \[BugFix\]\[Model\] Re-pack Kimi K3.1 Pro KDA conv weight after layerwise reload](#pr-21554)
- [11-12 16:59 · #21553 \[Doc\]\[Recipe\] Add Ascend overlay for Qwen3-VL-235B-A22B-Instruct](#pr-21553)
- [11-12 16:59 · #21552 \[Doc\]\[Recipe\] Add Ascend overlay for Qwen3-Next-80B-A3B-Instruct](#pr-21552)
- [11-12 16:59 · #21549 \[Feature\] Add experimental Kimi KDA RecoverSSM support](#pr-21549)
- [11-12 16:59 · #21548 \[BugFix\] Allocate Mooncake PD handshake ports dynamically](#pr-21548)
- [11-12 16:59 · #21546 \[CI\] update cann=9.3.0\_20261110170400](#pr-21546)
- [11-12 16:59 · #21543 \[Performance\]\[Ops\] Add SwiGLU graph fusion pass](#pr-21543)
- [11-12 16:59 · #21530 \[BugFix\]\[v0.32.0rc\] Support multi-head QSA cache stores](#pr-21530)
- [11-12 16:59 · #21526 \[Performance\]\[Kernel\] Fuse DeepSeek-V4.1 indexer prologue on Ascend A2/A3](#pr-21526)
- [11-12 16:59 · #21524 \[Performance\] Add experimental V2 MTP greedy verification](#pr-21524)
- [11-12 16:59 · #21523 \[Feature\]\[MoE\] Integrate MegaMoeLowLatency operator](#pr-21523)
- [11-12 16:59 · #21521 Upgrade/cann v0.32](#pr-21521)
- [11-12 16:59 · #21520 \[BugFix\] Defer accepted-token sync for async Mamba decode](#pr-21520)
- [11-12 16:59 · #21519 \[Feature\]\[Model\] Support DeepSeek-V4.1 vision encoder ACL graphs](#pr-21519)
- [11-12 16:59 · #21518 \[Performance\]\[SpecDecode\] Fix DFlash context tile width to avoid per-bucket Triton recompilation](#pr-21518)
- [11-12 16:59 · #21517 \[Ops\]\[Feature\] Support pipeline parallelism on prefill side for Mooncake layerwise connector](#pr-21517)
- [11-12 16:59 · #21516 \[BugFix\]\[Quantization\] Reject native block FP8 on unsupported devices](#pr-21516)
- [11-12 16:59 · #21513 \[Doc\] Add deepseek\_v41\_qli\_candidate to nav and fix FAQ anchor](#pr-21513)
- [11-12 16:59 · #21512 \[Perf\]\[SpecDecode\] Use a fixed context tile width in the DFlash input launcher](#pr-21512)
- [11-12 16:59 · #21511 \[Feature\]\[DSV4.1\] Add PIECEWISE runtime support](#pr-21511)
- [11-12 16:59 · #21510 \[Attention\]\[Feature\] Support TP × PCP KDA sharding for GLM-5.3-Flash](#pr-21510)
- [11-12 16:59 · #21508 \[Feature\]\[A5\] Add INT8 and MXFP8 quantized all-reduce backends](#pr-21508)
- [11-12 16:59 · #21506 \[v0.32.0rc\]\[Ops\]\[BugFix\] Validate RecoverSSM speculative staging count](#pr-21506)
- [11-12 16:59 · #21502 \[Feature\]\[Performance\] Support InternLM2-20B-Chat and dispatch scaled RoPE variants to the NPU kernel](#pr-21502)
- [11-12 16:59 · #21500 \[BugFix\] Reap stale opc locks and cap build parallelism by cgroup memory limit](#pr-21500)
- [11-12 16:59 · #21496 fix: decouple GDN RecoverSSM from KDA builder to support DSpark on GD…](#pr-21496)
- [11-12 16:59 · #21495 \[Feature\]\[Model\] Add opt-in MiniMax M3 Union prefill with frozen policy routing](#pr-21495)
- [11-12 16:59 · #21493 \[临时/勿合入\] a3-800i fed-2 / fed-4 各跑 3 个用例（验证 runner 作业 pod）](#pr-21493)
- [11-12 16:59 · #21492 \[Feature\]\[Observability\] Add M4 token-repeat detection](#pr-21492)
- [11-12 16:59 · #21490 \[临时/勿合入\] 全量 A2/A3 业务选测跑 karc fed runner（对齐 #20716）](#pr-21490)
- [11-12 16:59 · #21489 \[Test\]\[Feature\] Add GLM-5.3 W4A4C8 MTP coverage on A5](#pr-21489)
- [11-12 16:59 · #21482 \[BugFix\] Validate EPLB intervals are positive and fix config error messages](#pr-21482)
- [11-12 16:59 · #21480 \[Cherry-pick\]\[releases/v0.32.0rc\]\[CI\]\[BugFix\] Skip CANN 9.2.x custom-op .so validation in A5 wheel build (from #21479)](#pr-21480)
- [11-12 16:59 · #21479 \[CI\]\[BugFix\] Skip CANN 9.2.x custom-op .so validation in A5 wheel build](#pr-21479)
- [11-12 16:59 · #21468 \[Performance\] Skip attention output write-back when the backend returns the same tensor](#pr-21468)
- [11-12 16:59 · #21467 \[Performance\] Avoid pre-zeroing fully overwritten GDN output rows](#pr-21467)
- [11-12 16:59 · #21466 \[Performance\] Consume strided BA inputs directly in GDN gating](#pr-21466)
- [11-12 16:59 · #21465 \[Performance\] Produce cumulative expert boundaries for local MXFP8 routing](#pr-21465)

## 当前关注

<a id="pr-21717"></a>

### [#21717 · \[CI\] Restore A5 multi-node nightly test cases](https://github.com/vllm-project/vllm-ascend/pull/21717)

恢复 A5 多节点 nightly 测试配置，重新启用 DeepSeek、GLM 和 Qwen 的五组双节点用例。

**CI：** 未知 · **改动：** +22 / -22 · **最后提交：** 11-12 18:06

<a id="pr-21716"></a>

### [#21716 · \[临时/勿合入\] ci: route Nightly-A2 cases to offline-cluster runner labels](https://github.com/vllm-project/vllm-ascend/pull/21716)

将 A2 单节点性能与精度测试的 nightly、PR-only runner 配置切换到 fed-karc 集群，覆盖 1、2、4、8 卡规格。

**CI：** 未知 · **改动：** +14 / -14 · **最后提交：** 11-12 18:07

<a id="pr-21715"></a>

### [#21715 · \[Performance\] Fuse matmul-collective ops for dense sequence parallelism (MC2)](https://github.com/vllm-project/vllm-ascend/pull/21715)

补充发布说明，记录稠密模型序列并行将 all-gather、reduce-scatter 融合进 GEMM 的适用条件，以及图捕获支持与回退限制。

**CI：** 未知 · **改动：** +1649 / -29 · **最后提交：** 11-12 17:57

<a id="pr-21714"></a>

### [#21714 · \[Refactor\]\[MRV2\] Adopt EPLB policy and model-state hooks](https://github.com/vllm-project/vllm-ascend/pull/21714)

更新经验证的 vLLM 主分支提交，并同步 EPLB 设计文档和发布说明中的接口依赖、默认 stair 策略说明；同时调整示例启动脚本的类型检查标记。

**CI：** 未知 · **改动：** +623 / -867 · **最后提交：** 11-12 18:23 · **Draft**

<a id="pr-21713"></a>

### [#21713 · \[Doc\]soc\_version and soc\_series names refresh](https://github.com/vllm-project/vllm-ascend/pull/21713)

统一五份注意力算子 README 中 Ascend SoC 型号的大小写和命名写法，所选变更为文档修正。

**CI：** 未知 · **改动：** +7 / -7 · **最后提交：** 11-12 17:57

<a id="pr-21712"></a>

### [#21712 · \[Doc\]\[Misc\] Document Ascend Docker Runtime container setup](https://github.com/vllm-project/vllm-ascend/pull/21712)

在安装及快速入门文档中补充可选的 Ascend Docker Runtime 配置、验证和容器启动示例，说明 NPU 可见性、设备映射及额外挂载要求。

**CI：** 未知 · **改动：** +80 / -1 · **最后提交：** 11-12 17:53

<a id="pr-21709"></a>

### [#21709 · \[Performance\] Replace padding-mask fills with a single writeback for GLM5.3-Flash decode](https://github.com/vllm-project/vllm-ascend/pull/21709)

新增发布说明，记录 GLM5.3-Flash decode 改为单次输出写回后的延迟优化。当前关注范围内仅包含这份 release note。

**CI：** 未知 · **改动：** +345 / -6 · **最后提交：** 11-12 17:31

<a id="pr-21707"></a>

### [#21707 · \[Refactor\]\[RFork\] Drop Model Runner V1 EPLB bypass paths](https://github.com/vllm-project/vllm-ascend/pull/21707)

更新 RFork 中文文档，说明旧 Model Runner V1 的静态、录制及动态 EPLB 配置已失效；同时删除 RFork 单测夹具中的旧 EPLB adaptor 和 routed-experts 模拟依赖。

**CI：** 未知 · **改动：** +88 / -279 · **最后提交：** 11-12 17:28

<a id="pr-21706"></a>

### [#21706 · feat: add target LM head dynamic quantization for runner V2](https://github.com/vllm-project/vllm-ascend/pull/21706)

补充 lm\_head\_quantization 配置文档，说明 Runner V2 下目标 LM head 动态量化的启用方式、A2/A3 与 A5 路径，以及权重格式、共享 draft head 和硬件限制。

**CI：** 未知 · **改动：** +607 / -3 · **最后提交：** 11-11 09:19

<a id="pr-21705"></a>

### [#21705 · \[Feature\] DSpark expert-pool routing for the expert-offload path](https://github.com/vllm-project/vllm-ascend/pull/21705)

将 A5 expert-offload 测试接入选测、预计耗时和 runner 配置，并补充 DSpark expert-pool 配置说明与 CPU 单测辅助夹具。

**CI：** 未知 · **改动：** +2871 / -6 · **最后提交：** 11-12 18:13

<a id="pr-21701"></a>

### [#21701 · \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](https://github.com/vllm-project/vllm-ascend/pull/21701)

临时精简 PR E2E 工作流，将两个四卡流水线并行用例固定到 karc 专用 A3 runner，验证工作区同步问题；PR 明确标注勿合入。

**CI：** 未知 · **改动：** +70 / -808 · **最后提交：** 11-12 16:27

<a id="pr-21700"></a>

### [#21700 · \[BugFix\] Surface actionable MemCache driver-version init errors](https://github.com/vllm-project/vllm-ascend/pull/21700)

新增发布说明，记录 MemCache 初始化失败将显示检测到的驱动 Innerversion 和挂载提示，而不只返回 AssertionError。

**CI：** 未知 · **改动：** +131 / -1 · **最后提交：** 11-12 17:16

<a id="pr-21699"></a>

### [#21699 · \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.32.0rc](https://github.com/vllm-project/vllm-ascend/pull/21699)

为 v0.32.0rc 新增 A5 UBX 的 Ubuntu 和 openEuler Dockerfile，明确暂用基础镜像及后续 CANN 包切换点。

**CI：** 未知 · **改动：** +419 / -0 · **最后提交：** 11-12 16:10

<a id="pr-21697"></a>

### [#21697 · \[BugFix\] Support Qwen3.8 text-only IPC weight-transfer CI](https://github.com/vllm-project/vllm-ascend/pull/21697)

新增 Qwen3.8 text-only IPC 权重传输的公共测试支持、运行准备工具与设备空闲检查，并补充工具单测和使用文档。

**CI：** 未知 · **改动：** +1202 / -39 · **最后提交：** 11-12 16:12

<a id="pr-21695"></a>

### [#21695 · \[Doc\]\[BugFix\] Fix truncated model support tables in Chinese docs](https://github.com/vllm-project/vllm-ascend/pull/21695)

修复 PO 提取与翻译对多行表头的处理，拒绝被截断的翻译响应，并为 MkDocs 增加合并单元格表格扩展和写作说明。

**CI：** 未知 · **改动：** +114 / -226 · **最后提交：** 11-12 16:00

<a id="pr-21694"></a>

### [#21694 · \[bugfix\]pp oom](https://github.com/vllm-project/vllm-ascend/pull/21694)

在仓库根目录提交两份补丁和 OOM 分析说明，涉及 MiniMax PP 缓存分配及 vLLM 校验；这些根目录文件尚不在排除范围内。

**CI：** 未知 · **改动：** +877 / -3 · **最后提交：** 10-28 17:23

<a id="pr-21693"></a>

### [#21693 · \[Feature\]\[Model\] Support prefill context parallelism for Qwen3.8-Flash-Next](https://github.com/vllm-project/vllm-ascend/pull/21693)

关注范围内新增发布说明，记录 Qwen3.8-Flash-Next 的 MRV2 prefill context parallel 支持；本次仅因 release notes 纳入。

**CI：** 未知 · **改动：** +697 / -65 · **最后提交：** 11-12 15:47

<a id="pr-21690"></a>

### [#21690 · \[BugFix\]\[Feature\] Enable Mooncake V2 layerwise push and preserve allocation blocks](https://github.com/vllm-project/vllm-ascend/pull/21690)

补充 MooncakeConnectorV2 逐层 push 的配置示例、默认行为及 MultiConnector 注意事项，并增加发布说明。

**CI：** 未知 · **改动：** +52 / -9 · **最后提交：** 11-12 15:24

<a id="pr-21689"></a>

### [#21689 · \[CI\] Isolate lint images by branch and add a lightweight tools image](https://github.com/vllm-project/vllm-ascend/pull/21689)

按目标分支隔离 lint 镜像，并新增轻量 lite-tools 镜像供测试选择、缓存准备和文档任务使用；配套调整镜像构建流程与维护说明。

**CI：** 未知 · **改动：** +278 / -97 · **最后提交：** 11-12 15:34

<a id="pr-21688"></a>

### [#21688 · Pcp short prefill all backends](https://github.com/vllm-project/vllm-ascend/pull/21688)

补充 context parallel 开发设计文档，说明缓存单 token 尾部在 PCP decode request sharding 下的处理边界。

**CI：** 未知 · **改动：** +546 / -63 · **最后提交：** 11-12 15:12 · **Draft**

<a id="pr-21687"></a>

### [#21687 · \[Feature\]\[Kimi\] Provision the shared draft embedding on the last PP stage](https://github.com/vllm-project/vllm-ascend/pull/21687)

补充发布说明，记录 DSpark 复用目标模型输入 embedding，以及 Kimi 在最后一个流水线阶段复用 embedding 分片以避免重复加载。

**CI：** 未知 · **改动：** +500 / -19 · **最后提交：** 11-12 18:23

<a id="pr-21686"></a>

### [#21686 · \[BugFix\] Read quantized checkpoint indexes for RFork model state](https://github.com/vllm-project/vllm-ascend/pull/21686)

更新 rfork 中文文档，说明优先使用默认 checkpoint 索引、再选择唯一匹配的量化索引，以及无法确定索引时扫描 safetensors 头部的回退顺序。

**CI：** 未知 · **改动：** +155 / -26 · **最后提交：** 11-12 17:33

<a id="pr-21685"></a>

### [#21685 · \[CI\] add presmoke for CI](https://github.com/vllm-project/vllm-ascend/pull/21685)

新增 /presmoke 镜像预构建及 /nightly --presmoke 消费路径，以独立仓库和标签隔离镜像，并补充 nightly CI 使用文档。

**CI：** 未知 · **改动：** +275 / -53 · **最后提交：** 11-12 14:57

<a id="pr-21683"></a>

### [#21683 · \[BugFix\] Allow C8 KV transfer with AscendStore Memcache](https://github.com/vllm-project/vllm-ascend/pull/21683)

关注范围内新增发布说明，记录 AscendStore Memcache 的 C8 KV transfer 启动检查修复；本次仅因 release notes 纳入。

**CI：** 未知 · **改动：** +77 / -10 · **最后提交：** 11-12 14:56

<a id="pr-21680"></a>

### [#21680 · \[Feature\]\[MoE\] Add opt-in DSpark expert-pool routing for expert offload](https://github.com/vllm-project/vllm-ascend/pull/21680)

将 expert-offload A5 用例加入 CI 路由和耗时配置，新增 CPU 单测辅助 fixture，并补充 DSpark expert-pool 的配置说明。

**CI：** 未知 · **改动：** +2630 / -6 · **最后提交：** 11-12 15:35 · **Draft**

<a id="pr-21679"></a>

### [#21679 · \[Performance\]\[MoE\] Move shared-expert padding before Down](https://github.com/vllm-project/vllm-ascend/pull/21679)

关注范围内新增发布说明，记录 shared-expert Down 投影前的 padding 优化；本次仅因 release notes 纳入。

**CI：** 未知 · **改动：** +774 / -17 · **最后提交：** 11-12 14:44 · **Draft**

<a id="pr-21673"></a>

### [#21673 · \[BugFix\]\[PD\] Preserve cache usage across proxy response chunks](https://github.com/vllm-project/vllm-ascend/pull/21673)

修改 PD 示例代理，先重组网络分块再解析 SSE/JSON，保留流式与非流式响应中的缓存使用统计；同步补充 Mooncake 多节点教程。

**CI：** 未知 · **改动：** +243 / -24 · **最后提交：** 11-12 13:07

<a id="pr-21672"></a>

### [#21672 · \[v0.32.0rc\]\[Doc\] Translated Doc files 2026-11-12](https://github.com/vllm-project/vllm-ascend/pull/21672)

更新 v0.32.0rc 的 MiniMax-M3.1-Flash 中文翻译，澄清不同设备和 PD 角色下的 draft 图执行及 KV cache 配置。

**CI：** 未知 · **改动：** +55 / -60 · **最后提交：** 11-12 12:21

<a id="pr-21671"></a>

### [#21671 · \[Bugfix\] Build DSpark graph metadata with uniform query boundaries](https://github.com/vllm-project/vllm-ascend/pull/21671)

关注范围内新增发布说明，记录 DSpark FULL 图元数据的 query boundary 一致性修复；本次仅因 release notes 纳入。

**CI：** 未知 · **改动：** +119 / -74 · **最后提交：** 11-12 12:09 · **Draft**

<a id="pr-21670"></a>

### [#21670 · \[Feature\] Add independent shared-expert fine-grained TP](https://github.com/vllm-project/vllm-ascend/pull/21670)

在 additional\_config 配置表中加入 shared\_expert\_tensor\_parallel\_size 的说明和入口链接，并增加发布说明。

**CI：** 未知 · **改动：** +702 / -61 · **最后提交：** 11-12 12:17 · **Draft**

<a id="pr-21669"></a>

### [#21669 · \[Feature\]\[Model\] Add experimental MiniMax M3.1 indexer DCP](https://github.com/vllm-project/vllm-ascend/pull/21669)

关注范围内新增发布说明，记录 MiniMax-M3.1 indexer DCP 实验性配置及 PD 使用限制；本次仅因 release notes 纳入。

**CI：** 未知 · **改动：** +447 / -9 · **最后提交：** 11-12 12:02 · **Draft**

<a id="pr-21668"></a>

### [#21668 · \[Feature\] Support draft\_lm\_head\_quantization (fp8) on Ascend NPU](https://github.com/vllm-project/vllm-ascend/pull/21668)

关注范围内新增发布说明，记录 Ascend 上 draft lm\_head FP8 量化支持和非 MXFP8 设备兼容修复；未涉及 CI 框架变更。

**CI：** 未知 · **改动：** +1325 / -25 · **最后提交：** 11-12 15:28

<a id="pr-21664"></a>

### [#21664 · \[BugFix\]\[Qwen4Exp\] Use Ascend UVA for pinned PLE weights](https://github.com/vllm-project/vllm-ascend/pull/21664)

关注范围内新增发布说明，记录 Qwen PLE 权重固定在主机内存时的 Ascend UVA 启动修复；本次仅因 release notes 纳入。

**CI：** 未知 · **改动：** +69 / -0 · **最后提交：** 11-12 11:45 · **Draft**

<a id="pr-21663"></a>

### [#21663 · \[Feature\] L2 Embedding Cache](https://github.com/vllm-project/vllm-ascend/pull/21663)

新增 L2 pHash 优化与接口迁移的开发文档，说明 band 配置、阈值约束及 CPU 像素处理路径。

**CI：** 未知 · **改动：** +4164 / -44 · **最后提交：** 11-12 11:32

<a id="pr-21661"></a>

### [#21661 · \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](https://github.com/vllm-project/vllm-ascend/pull/21661)

临时精简 PR E2E 工作流，将两个四卡流水线并行用例固定到 karc 专用 A3 runner，用于验证工作区同步问题；PR 明确标注勿合入。

**CI：** 未知 · **改动：** +70 / -808 · **最后提交：** 11-12 11:29

<a id="pr-21660"></a>

### [#21660 · perf: fuse rotated Engram gate on A3](https://github.com/vllm-project/vllm-ascend/pull/21660)

关注范围内新增发布说明草稿，记录 A3 上 rotated Engram gate 融合；片段的 PR 编号仍待填写。

**CI：** 未知 · **改动：** +186 / -28 · **最后提交：** 11-12 10:24

<a id="pr-21659"></a>

### [#21659 · \[Feature\]\[DeepSeek-V4.1\] Enable A3 metadata multistream execution](https://github.com/vllm-project/vllm-ascend/pull/21659)

关注范围内新增发布说明，记录 DeepSeek-V4.1 在 A3 上的 metadata 多流执行支持；本次仅因 release notes 纳入。

**CI：** 未知 · **改动：** +258 / -28 · **最后提交：** 11-12 11:48 · **Draft**

<a id="pr-21657"></a>

### [#21657 · \[Test\] kimi-k3 nightly](https://github.com/vllm-project/vllm-ascend/pull/21657)

在 nightly 配置中加入 Kimi-K3-W4A8-A3-1M-PD 八卡用例，指向已有模型测试配置目录。

**CI：** 未知 · **改动：** +18 / -14 · **最后提交：** 11-12 16:10

<a id="pr-21655"></a>

### [#21655 · \[Performance\] Fuse A5 recurrent GDN preprocessing and refresh gate bias after reload](https://github.com/vllm-project/vllm-ascend/pull/21655)

关注范围内新增发布说明，记录 A5 recurrent GDN 预处理融合及重载后 gate bias 刷新；未涉及 CI 框架变更。

**CI：** 未知 · **改动：** +405 / -11 · **最后提交：** 11-12 11:42 · **Draft**

<a id="pr-21654"></a>

### [#21654 · \[v0.32.0rc\]\[Qwen4Exp\] Consolidate A5 QSA and MRV2 performance patches](https://github.com/vllm-project/vllm-ascend/pull/21654)

新增 QSA union 的算子端到端验证，补充 v0.32.0rc 中 QSA/MRV2 性能改动的发布说明。

**CI：** 未知 · **改动：** +2223 / -173 · **最后提交：** 11-12 10:55 · **Draft**

<a id="pr-21653"></a>

### [#21653 · \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.30.0](https://github.com/vllm-project/vllm-ascend/pull/21653)

新增 A5 UBX 的 Ubuntu 与 openEuler Dockerfile，并接入定时和 nightly 镜像构建矩阵；同时调整基础镜像版本解析和相关依赖安装。

**CI：** 未知 · **改动：** +451 / -17 · **最后提交：** 11-12 14:04

<a id="pr-21652"></a>

### [#21652 · \[BugFix\] Honor NZ mode for DeepSeek V4/V4.1 grouped output projections](https://github.com/vllm-project/vllm-ascend/pull/21652)

在 additional\_config 指南中补充 weight\_nz\_mode=2 的适用范围和默认行为，并增加对应发布说明。

**CI：** 未知 · **改动：** +125 / -17 · **最后提交：** 11-12 10:50

<a id="pr-21648"></a>

### [#21648 · \[Doc\]\[BugFix\] Fix DeepSeek-V4.1-Flash launcher links in Chinese docs](https://github.com/vllm-project/vllm-ascend/pull/21648)

修正 DeepSeek-V4.1-Flash 中文翻译中的 DP 启动器标题锚点，保持教程内跳转链接一致。

**CI：** 未知 · **改动：** +6 / -6 · **最后提交：** 11-12 10:07

<a id="pr-21645"></a>

### [#21645 · \[Attention\]\[BugFix\] Retain CANN FlashAttn for native MiniMax DSpark graphs](https://github.com/vllm-project/vllm-ascend/pull/21645)

关注范围内新增发布说明，记录 MiniMax DSpark 图执行的 CANN FlashAttn 兼容修复；本次仅因 release notes 纳入。

**CI：** 未知 · **改动：** +240 / -1 · **最后提交：** 11-12 10:09 · **Draft**

<a id="pr-21643"></a>

### [#21643 · \[Feature\]\[EC Connector\] Support encoder cache tiering offload on Ascend](https://github.com/vllm-project/vllm-ascend/pull/21643)

更新 MkDocs 导航和中英文标题映射，将编码器缓存卸载文档接入站点导航。

**CI：** 未知 · **改动：** +549 / -65 · **最后提交：** 11-12 10:01

<a id="pr-21639"></a>

### [#21639 · \[BugFix\] Select vLLM KV cache helpers by availability](https://github.com/vllm-project/vllm-ascend/pull/21639)

关注范围内新增发布说明，记录兼容 vLLM 源码版本的 KV cache helper 导入修复；本次仅因 release notes 纳入。

**CI：** 未知 · **改动：** +88 / -11 · **最后提交：** 11-12 08:37 · **Draft**

<a id="pr-21638"></a>

### [#21638 · \[Feature\]\[Qwen\] Share PLE tables across Ascend services](https://github.com/vllm-project/vllm-ascend/pull/21638)

在 CMake 中按已安装 HIXL 条件构建并安装原生共享库，新增无需真实 NPU 的 ACL/HIXL 替身测试工具及运行说明。

**CI：** 未知 · **改动：** +4569 / -3 · **最后提交：** 11-12 08:53 · **Draft**

<a id="pr-21637"></a>

### [#21637 · \[BugFix\]\[P/D\] Surface missing prompt-token details in the PD proxy](https://github.com/vllm-project/vllm-ascend/pull/21637)

为 PD 示例代理增加缺失 prompt-token 明细的一次性告警，并在 EvalScope 指南中说明缓存命中率为零时的启动参数排查方法。

**CI：** 未知 · **改动：** +208 / -5 · **最后提交：** 11-12 02:12

<a id="pr-21636"></a>

### [#21636 · \[Feature\]\[Stacked\]\[v0.32.0rc\]\[Qwen4Exp\] MRV2 preparation with union GBSA, CPU-sync and RecoverSSM](https://github.com/vllm-project/vllm-ascend/pull/21636)

新增 Qwen GDN RecoverSSM 设计与部署验证文档，说明缓存布局、PD 分离和硬件限制；同时补充 Qwen4 union 算子的成员集合、CPU 对照及批量 prefill 分发测试。

**CI：** 未知 · **改动：** +7076 / -902 · **最后提交：** 11-12 16:59

<a id="pr-21635"></a>

### [#21635 · \[Stacked\]\[Qwen4Exp\] MRV2 input preparation with union GBSA, CPU-sync and RecoverSSM](https://github.com/vllm-project/vllm-ascend/pull/21635)

补充 Qwen GDN RecoverSSM 的开发设计文档及配置限制，并新增 QSA union 的算子端到端验证和发布说明。

**CI：** 未知 · **改动：** +6459 / -886 · **最后提交：** 11-12 08:59

<a id="pr-21631"></a>

### [#21631 · \[Feature\] Add Ascend overlay for deepseek-ai/DeepSeek-V4-Flash](https://github.com/vllm-project/vllm-ascend/pull/21631)

精简 DeepSeek-V4-Flash 的 Ascend recipe overlay，固定 A3 容器镜像并补充量化、PD 就绪和清理说明。

**CI：** 未知 · **改动：** +37 / -149 · **最后提交：** 11-11 23:21

<a id="pr-21630"></a>

### [#21630 · \[BugFix\]\[SpecDecode\] Support replicated DFlash/DFlash2 execution with PCP on MRV2](https://github.com/vllm-project/vllm-ascend/pull/21630)

新增发布说明，记录 Model Runner V2 中 PCP 对复制式 DFlash/DFlash2 草稿的支持，以及词表分片候选合并和草稿 EPLB 处理；当前关注范围命中的是 release notes。

**CI：** 未知 · **改动：** +383 / -48 · **最后提交：** 11-12 16:53

<a id="pr-21629"></a>

### [#21629 · \[BugFix\]\[ExampleProxy\] Use round-robin ticket as heap tiebreaker to fix instance load skew](https://github.com/vllm-project/vllm-ascend/pull/21629)

调整 PD 负载均衡示例代理的堆排序，在负载相同时使用轮转票号分配请求，避免固定实例持续占优。

**CI：** 未知 · **改动：** +12 / -4 · **最后提交：** 11-11 21:59

<a id="pr-21627"></a>

### [#21627 · \[Performance\] Integrate union GBSA prefill for Qwen4Exp](https://github.com/vllm-project/vllm-ascend/pull/21627)

新增 Qwen4 union 算子测试，覆盖稀疏选择集合、空行和 padding、大规模 CPU/NPU 对照，以及批量 prefill 与逐请求执行的一致性。

**CI：** 未知 · **改动：** +527 / -22 · **最后提交：** 11-11 20:16 · **Draft**

<a id="pr-21624"></a>

### [#21624 · \[Feature\]\[Model\] Add Kimi fine-grained projection and shared-expert TP](https://github.com/vllm-project/vllm-ascend/pull/21624)

补充共享专家张量并行参数的默认值和适用约束、相关发布说明，并为投机解码测试配置夹具加入 embedding 张量并行字段。

**CI：** 未知 · **改动：** +1777 / -95 · **最后提交：** 11-12 18:28 · **Draft**

<a id="pr-21623"></a>

### [#21623 · \[Feature\]\[Engram\] Add local host VMM for shared A3 tables](https://github.com/vllm-project/vllm-ascend/pull/21623)

为 A3 增加可选 Engram host VMM 原生库的 CMake 能力检测、构建和安装，并实现共享内存映射及清理接口；同步加入文档导航和发布说明。

**CI：** 未知 · **改动：** +2466 / -99 · **最后提交：** 11-11 21:00

<a id="pr-21622"></a>

### [#21622 · \[Feature\] Support bilateral DCP in MooncakePushConnector](https://github.com/vllm-project/vllm-ascend/pull/21622)

更新 PD 分离设计文档，说明 MooncakePushConnector 在 PCP=1 时支持两端独立 DCP 的 MLA KV 传输，以及页、条带、分块和模型类型限制。

**CI：** 未知 · **改动：** +590 / -21 · **最后提交：** 11-11 20:58

<a id="pr-21621"></a>

### [#21621 · \[BugFix\]\[DSpark\]\[EPLB\] Fix V4.1 draft expert loading and registration](https://github.com/vllm-project/vllm-ascend/pull/21621)

新增发布说明，记录启用 EPLB 时 DeepSeek V4.1 DSpark 的 MoE 注册和冗余专家权重映射修复。

**CI：** 未知 · **改动：** +135 / -4 · **最后提交：** 11-11 22:22

<a id="pr-21607"></a>

### [#21607 · \[Test\]\[Upstream\]rerun failed test case](https://github.com/vllm-project/vllm-ascend/pull/21607)

让 upstream E2E workflow 也由指定分支 PR 触发并关闭 Hugging Face 离线模式；测试运行器切换到新增的精选重跑用例配置。

**CI：** 未知 · **改动：** +32 / -2 · **最后提交：** 11-12 11:31

<a id="pr-21605"></a>

### [#21605 · \[Performance\]\[A3\] Cache row weights for packed DCP LSE combine](https://github.com/vllm-project/vllm-ascend/pull/21605)

新增 packed DCP LSE combine 的 NPU Graph 延迟回归基准，可记录软件及提交信息、对比基线、检查采样波动和性能退化；补充 A3 行权重缓存优化的发布说明。

**CI：** 未知 · **改动：** +406 / -5 · **最后提交：** 11-11 20:04 · **Draft**

<a id="pr-21604"></a>

### [#21604 · \[BugFix\]\[Quantization\] Reject native FP8 checkpoints on non-950 devices](https://github.com/vllm-project/vllm-ascend/pull/21604)

新增兼容性变更说明：非 Ascend 950 设备启动时拒绝原生分块 FP8 checkpoint，并给出 BF16 或重新量化的替代建议。

**CI：** 未知 · **改动：** +212 / -88 · **最后提交：** 11-11 20:10

<a id="pr-21603"></a>

### [#21603 · \[Performance\]\[Kernel\] Adapt owner-prefix peer counting on A3](https://github.com/vllm-project/vllm-ascend/pull/21603)

新增 owner-prefix 候选合并的 NPU Graph 回归基准，覆盖不同规模及分数分布，支持环境一致性、波动和退化检查；补充 A3 性能优化说明。

**CI：** 未知 · **改动：** +429 / -1 · **最后提交：** 11-11 20:32 · **Draft**

<a id="pr-21600"></a>

### [#21600 · \[BugFix\]\[KVPool\] Report synchronous hybrid load failures by request](https://github.com/vllm-project/vllm-ascend/pull/21600)

为 KVPool 单测依赖模拟补齐 model\_loader 与 mamba\_utils 模块，并新增同步 hybrid 加载失败处理的发布说明。

**CI：** 未知 · **改动：** +99 / -14 · **最后提交：** 11-11 22:03 · **Draft**

<a id="pr-21594"></a>

### [#21594 · \[Feature\]\[MoE\] Support anchor-union activation routing for DSpark and DFlash speculative decoding](https://github.com/vllm-project/vllm-ascend/pull/21594)

把 expert-offload A5 测试加入精选 CI，配置 a5-4 runner 和预计耗时，并增加 CPU 侧模型方法与 ACL/NPU 模拟夹具；补充 anchor-union 路由功能的发布说明。

**CI：** 未知 · **改动：** +3880 / -4 · **最后提交：** 11-12 15:47 · **Draft**

<a id="pr-21589"></a>

### [#21589 · \[Performance\] Skip QSA CPU length sync for Ascend builder](https://github.com/vllm-project/vllm-ascend/pull/21589)

补充发布说明，记录 QSA 推测解码消除逐步 CPU 序列长度同步开销的优化。

**CI：** 未知 · **改动：** +23 / -6 · **最后提交：** 11-11 17:47 · **Draft**

<a id="pr-21587"></a>

### [#21587 · \[Feature\] Fuse GatingTopK with EPLB expert mapping](https://github.com/vllm-project/vllm-ascend/pull/21587)

为 GatingTopK 原生算子增加可选 EPLB 路由表及形状校验，将专家映射融合到输出阶段；同时将对应 NPU 测试映射到 A3 runner。

**CI：** 未知 · **改动：** +552 / -18 · **最后提交：** 11-12 17:32

<a id="pr-21586"></a>

### [#21586 · \[Performance\]\[Kernel\] Use rectangular tiles for D512 DCP output packing](https://github.com/vllm-project/vllm-ascend/pull/21586)

新增 DCP output/LSE packing 的图回放性能对比脚本，并记录 A3 上 D512 BF16 打包优化。

**CI：** 未知 · **改动：** +271 / -1 · **最后提交：** 11-11 17:36 · **Draft**

<a id="pr-21584"></a>

### [#21584 · \[Performance\]\[Kernel\] Share exact radix sorting across BF16 and FP32 candidate packing](https://github.com/vllm-project/vllm-ascend/pull/21584)

新增 candidate packing 图回放回归基准，支持基线与候选结果比较；发布说明记录 A3 上共享精确 radix 排序的优化。

**CI：** 未知 · **改动：** +267 / -66 · **最后提交：** 11-12 17:29 · **Draft**

<a id="pr-21580"></a>

### [#21580 · \[Feature\]\[Attention\] Support quant\_mode=5 pseudo-quant for MTP decode in C8 backend](https://github.com/vllm-project/vllm-ascend/pull/21580)

补充发布说明，记录 C8 INT8 KV cache 在 MTP 解码下使用 quant\_mode=5 快速路径及不支持时的回退。

**CI：** 未知 · **改动：** +518 / -24 · **最后提交：** 11-11 22:18

<a id="pr-21575"></a>

### [#21575 · \[BugFix\] Preserve Mamba checkpoints in consumer chunked prefill](https://github.com/vllm-project/vllm-ascend/pull/21575)

补充发布说明，记录非 MTP KV consumer 分块预填充复用 Mamba/KDA 检查点的修复。

**CI：** 未知 · **改动：** +395 / -8 · **最后提交：** 11-12 11:55 · **Draft**

<a id="pr-21565"></a>

### [#21565 · \[Test\]\[Sleep Mode\] Harden RLHF sleep/wake harness timeouts](https://github.com/vllm-project/vllm-ascend/pull/21565)

加强 RLHF 通用测试服务生命周期管理：启动前等待显存和端口，独立进程组清理 EngineCore 子进程，避免超时后残留服务。

**CI：** 未知 · **改动：** +40 / -9 · **最后提交：** 11-11 16:00 · **Draft**

<a id="pr-21557"></a>

### [#21557 · \[BugFix\]\[v0.32.0rc\] Sync SWA block IDs before KV Pool prefill saves](https://github.com/vllm-project/vllm-ascend/pull/21557)

补充发布说明，记录 KV Pool 保存前刷新 SWA block ID、跳过已释放块及等待传输完成的修复。

**CI：** 未知 · **改动：** +158 / -25 · **最后提交：** 11-11 17:17

<a id="pr-21555"></a>

### [#21555 · feat(ci): add /presmoke command for PR-level CANN image presmoke](https://github.com/vllm-project/vllm-ascend/pull/21555)

增加 PR 级 /presmoke 命令，按 PR 提交重建 CANN 基础层和 nightly 镜像并运行测试；使用独立镜像后缀且禁止同步到 quay.io。

**CI：** 未知 · **改动：** +208 / -60 · **最后提交：** 11-11 15:09

<a id="pr-21554"></a>

### [#21554 · \[BugFix\]\[Model\] Re-pack Kimi K3.1 Pro KDA conv weight after layerwise reload](https://github.com/vllm-project/vllm-ascend/pull/21554)

补充发布说明，记录 Kimi K3.1 Pro KDA 在 level-2 唤醒并重载权重后重新打包卷积权重以避免 NaN 的修复。

**CI：** 未知 · **改动：** +46 / -0 · **最后提交：** 11-11 15:19 · **Draft**

<a id="pr-21553"></a>

### [#21553 · \[Doc\]\[Recipe\] Add Ascend overlay for Qwen3-VL-235B-A22B-Instruct](https://github.com/vllm-project/vllm-ascend/pull/21553)

新增 Qwen3-VL-235B-A22B-Instruct 的 Ascend recipe overlay，配置 A3 W8A8 QuaRot 部署参数和硬件信息。

**CI：** 未知 · **改动：** +109 / -0 · **最后提交：** 11-12 00:25

<a id="pr-21552"></a>

### [#21552 · \[Doc\]\[Recipe\] Add Ascend overlay for Qwen3-Next-80B-A3B-Instruct](https://github.com/vllm-project/vllm-ascend/pull/21552)

新增 Qwen3-Next-80B-A3B-Instruct 的 A3 BF16 recipe overlay，提供 TP4、全解码图和固定镜像版本等启动配置。

**CI：** 未知 · **改动：** +31 / -0 · **最后提交：** 11-12 00:25

<a id="pr-21549"></a>

### [#21549 · \[Feature\] Add experimental Kimi KDA RecoverSSM support](https://github.com/vllm-project/vllm-ascend/pull/21549)

补充实验性 Kimi KDA RecoverSSM 发布说明，注明 MRV2 推测解码、align 前缀缓存支持及 KV transfer 限制。

**CI：** 未知 · **改动：** +1251 / -153 · **最后提交：** 11-12 15:45 · **Draft**

<a id="pr-21548"></a>

### [#21548 · \[BugFix\] Allocate Mooncake PD handshake ports dynamically](https://github.com/vllm-project/vllm-ascend/pull/21548)

补充发布说明，记录 Mooncake PD 自动选择可用握手端口，避免固定端口占用导致启动失败。

**CI：** 未知 · **改动：** +333 / -69 · **最后提交：** 11-11 15:40

<a id="pr-21546"></a>

### [#21546 · \[CI\] update cann=9.3.0\_20261110170400](https://github.com/vllm-project/vllm-ascend/pull/21546)

将各型号 Ubuntu/openEuler Dockerfile 的 CANN 基础镜像从 9.2.1 更新为 SWR 上的 9.3.0\_20261110170400。

**CI：** 未知 · **改动：** +8 / -8 · **最后提交：** 11-11 14:26

<a id="pr-21543"></a>

### [#21543 · \[Performance\]\[Ops\] Add SwiGLU graph fusion pass](https://github.com/vllm-project/vllm-ascend/pull/21543)

补充发布说明，记录以 FX 融合将视觉 MLP 的 chunk/silu/mul 转为 npu\_swiglu 的优化。

**CI：** 未知 · **改动：** +261 / -1 · **最后提交：** 11-11 14:41

<a id="pr-21541"></a>

### [#21541 · \[Doc\] add doc quality review workflow for docs/source changes](https://github.com/vllm-project/vllm-ascend/pull/21541)

新增文档质量评估工作流及配套脚本，对 Markdown/PO 变更进行规则和模型评估，生成汇总及行内问题评论；支持标签、命令与手动触发，并区分同仓库和 fork 的执行路径。

**CI：** 未知 · **改动：** +2059 / -0 · **最后提交：** 11-12 18:33 · **Draft**

<a id="pr-21536"></a>

### [#21536 · \[Feature\]\[KV Cache\] Prototype FlashStates frontier integration on Ascend (WIP)](https://github.com/vllm-project/vllm-ascend/pull/21536)

加入 FlashStates Ascend 移植说明、vLLM 0.32 补丁集及 frontier 基准脚本和结果，记录混合状态检查点的使用条件、验证范围与硬件限制。

**CI：** 未知 · **改动：** +11029 / -0 · **最后提交：** 11-11 22:04

<a id="pr-21530"></a>

### [#21530 · \[BugFix\]\[v0.32.0rc\] Support multi-head QSA cache stores](https://github.com/vllm-project/vllm-ascend/pull/21530)

补充发布说明，记录 QSA KV-cache 写入对多个本地 KV head 的支持，覆盖张量并行为 1 的流水线部署场景。

**CI：** 未知 · **改动：** +57 / -22 · **最后提交：** 11-11 12:06 · **Draft**

<a id="pr-21526"></a>

### [#21526 · \[Performance\]\[Kernel\] Fuse DeepSeek-V4.1 indexer prologue on Ascend A2/A3](https://github.com/vllm-project/vllm-ascend/pull/21526)

新增 A2/A3 的 fused\_indexer\_prologue 算子，将 DeepSeek-V4.1 的 key 投影、归一化、RoPE、INT8 量化和分页缓存写入合并，并接入构建、Torch 绑定与元信息注册。

**CI：** 未知 · **改动：** +1136 / -17 · **最后提交：** 11-11 14:25

<a id="pr-21524"></a>

### [#21524 · \[Performance\] Add experimental V2 MTP greedy verification](https://github.com/vllm-project/vllm-ascend/pull/21524)

补充发布说明，记录默认关闭、需显式启用的 ModelRunnerV2 MTP 贪心验证路径，以及不支持的采样配置所使用的回退行为。

**CI：** 未知 · **改动：** +502 / -0 · **最后提交：** 11-11 11:40

<a id="pr-21523"></a>

### [#21523 · \[Feature\]\[MoE\] Integrate MegaMoeLowLatency operator](https://github.com/vllm-project/vllm-ascend/pull/21523)

补充 Mega MoE 低延迟及融合 gather 参数文档，说明 Ascend 950 算子路径、默认值、HCCL 配置与不兼容组合。

**CI：** 未知 · **改动：** +483 / -15 · **最后提交：** 11-11 11:33

<a id="pr-21521"></a>

### [#21521 · Upgrade/cann v0.32](https://github.com/vllm-project/vllm-ascend/pull/21521)

升级 CANN 分支的 vLLM 0.32 构建环境，调整容器基础镜像、算子包及 Python 依赖，并同步自定义算子构建列表。已核对的工程改动还包括镜像构建信息汇总、CI action 暂存脚本和主机内存注册能力检测。

**CI：** 未知 · **改动：** +235133 / -103646 · **最后提交：** 11-11 15:21

<a id="pr-21520"></a>

### [#21520 · \[BugFix\] Defer accepted-token sync for async Mamba decode](https://github.com/vllm-project/vllm-ascend/pull/21520)

补充发布说明，记录异步投机解码中延后读取 Mamba 已接受 token 的 CPU 快照，以同步正确的接受数量。

**CI：** 未知 · **改动：** +109 / -11 · **最后提交：** 11-11 11:25 · **Draft**

<a id="pr-21519"></a>

### [#21519 · \[Feature\]\[Model\] Support DeepSeek-V4.1 vision encoder ACL graphs](https://github.com/vllm-project/vllm-ascend/pull/21519)

新增 DeepSeek-V4.1 多模态 encoder 图捕获开发说明及发布说明，描述 packed ViT/aligner 图的启用方式、预算限制、eager 回退和 NPU 验证要求。

**CI：** 未知 · **改动：** +137 / -5 · **最后提交：** 11-11 11:17

<a id="pr-21518"></a>

### [#21518 · \[Performance\]\[SpecDecode\] Fix DFlash context tile width to avoid per-bucket Triton recompilation](https://github.com/vllm-project/vllm-ascend/pull/21518)

补充发布说明，记录 DFlash/DSpark 使用固定 tile 宽度，避免不同图桶重复触发 Triton 编译停顿。

**CI：** 未知 · **改动：** +236 / -5 · **最后提交：** 11-11 11:21

<a id="pr-21517"></a>

### [#21517 · \[Ops\]\[Feature\] Support pipeline parallelism on prefill side for Mooncake layerwise connector](https://github.com/vllm-project/vllm-ascend/pull/21517)

补充发布说明，记录 Mooncake prefill 流水线并行按阶段传输所属层、由末阶段通知完成的行为，并注明不支持 decode 流水线并行。

**CI：** 未知 · **改动：** +259 / -5 · **最后提交：** 11-11 15:26 · **Draft**

<a id="pr-21516"></a>

### [#21516 · \[BugFix\]\[Quantization\] Reject native block FP8 on unsupported devices](https://github.com/vllm-project/vllm-ascend/pull/21516)

补充发布说明，记录原生 block-FP8 在不支持的 A2/A3 设备上明确拒绝执行，而非将权重展开为 BF16。

**CI：** 未知 · **改动：** +60 / -57 · **最后提交：** 11-11 11:21 · **Draft**

<a id="pr-21513"></a>

### [#21513 · \[Doc\] Add deepseek\_v41\_qli\_candidate to nav and fix FAQ anchor](https://github.com/vllm-project/vllm-ascend/pull/21513)

在 MkDocs 导航中加入 DeepSeek-V4.1 QLI candidate 开发指南入口。

**CI：** 未知 · **改动：** +2 / -1 · **最后提交：** 11-11 10:54

<a id="pr-21512"></a>

### [#21512 · \[Perf\]\[SpecDecode\] Use a fixed context tile width in the DFlash input launcher](https://github.com/vllm-project/vllm-ascend/pull/21512)

补充发布说明，记录 DFlash 使用固定上下文 tile 宽度，减少随上下文长度变化产生的 Triton JIT 编译停顿。

**CI：** 未知 · **改动：** +160 / -5 · **最后提交：** 11-11 10:36

<a id="pr-21511"></a>

### [#21511 · \[Feature\]\[DSV4.1\] Add PIECEWISE runtime support](https://github.com/vllm-project/vllm-ascend/pull/21511)

新增 DeepSeek V4.1 PIECEWISE 执行设计文档与发布说明，说明图切分边界、decoder replay、Engram 输入准备及 NPU 验证要求；跨层 KV pool 的 PIECEWISE 集成仍未启用。

**CI：** 未知 · **改动：** +591 / -22 · **最后提交：** 11-11 10:34 · **Draft**

<a id="pr-21510"></a>

### [#21510 · \[Attention\]\[Feature\] Support TP × PCP KDA sharding for GLM-5.3-Flash](https://github.com/vllm-project/vllm-ascend/pull/21510)

补充 GLM-5.3-Flash KDA 的发布说明，记录注意力头和循环状态可按 TP 与 PCP 联合分片。

**CI：** 未知 · **改动：** +92 / -40 · **最后提交：** 11-11 10:32 · **Draft**

<a id="pr-21508"></a>

### [#21508 · \[Feature\]\[A5\] Add INT8 and MXFP8 quantized all-reduce backends](https://github.com/vllm-project/vllm-ascend/pull/21508)

扩展量化 all-reduce 配置文档及发布说明，明确 A2 默认 INT8、A5 默认 MXFP8，以及各后端的形状、规模、硬件限制和诊断方法。

**CI：** 未知 · **改动：** +813 / -94 · **最后提交：** 11-11 10:26

<a id="pr-21506"></a>

### [#21506 · \[v0.32.0rc\]\[Ops\]\[BugFix\] Validate RecoverSSM speculative staging count](https://github.com/vllm-project/vllm-ascend/pull/21506)

新增 RecoverSSM 修复说明，记录非法推测解码元数据在图暂存前报告 decode 数量与请求批大小。

**CI：** 未知 · **改动：** +33 / -1 · **最后提交：** 11-11 09:41

<a id="pr-21502"></a>

### [#21502 · \[Feature\]\[Performance\] Support InternLM2-20B-Chat and dispatch scaled RoPE variants to the NPU kernel](https://github.com/vllm-project/vllm-ascend/pull/21502)

把 InternLM2-20B-Chat 加入 nightly 精度任务、模型缓存清单、E2E 精度配置和文档导航，并登记双卡测试预估耗时及发布说明。

**CI：** 未知 · **改动：** +851 / -0 · **最后提交：** 11-11 00:02

<a id="pr-21500"></a>

### [#21500 · \[BugFix\] Reap stale opc locks and cap build parallelism by cgroup memory limit](https://github.com/vllm-project/vllm-ascend/pull/21500)

为自定义算子构建按 cgroup 内存限制设置默认并行度，并在构建前清理已失效的 opc 锁；新增对应工具单测，保留活进程锁。

**CI：** 未知 · **改动：** +136 / -1 · **最后提交：** 11-10 22:45

<a id="pr-21496"></a>

### [#21496 · fix: decouple GDN RecoverSSM from KDA builder to support DSpark on GD…](https://github.com/vllm-project/vllm-ascend/pull/21496)

新增发布说明，记录 GDN RecoverSSM 改为原生元数据构建器，以移除 KDA 调度假设并支持 GDN 混合模型的 MTP 与 DSpark。

**CI：** 未知 · **改动：** +307 / -3 · **最后提交：** 11-10 21:15

<a id="pr-21495"></a>

### [#21495 · \[Feature\]\[Model\] Add opt-in MiniMax M3 Union prefill with frozen policy routing](https://github.com/vllm-project/vllm-ascend/pull/21495)

补充 MiniMax M3 Union prefill 的实验性发布说明，标明默认关闭、冻结路由策略以及额外自定义算子依赖。

**CI：** 未知 · **改动：** +1056 / -26 · **最后提交：** 11-10 21:07 · **Draft**

<a id="pr-21493"></a>

### [#21493 · \[临时/勿合入\] a3-800i fed-2 / fed-4 各跑 3 个用例（验证 runner 作业 pod）](https://github.com/vllm-project/vllm-ascend/pull/21493)

将 PR 工作流临时改为 A3 FED 2 卡与 4 卡 runner 的各 3 个用例冒烟验证，省略常规 lint、CPU UT、推荐选测与标签门禁；文件明确标注勿合入。

**CI：** 未知 · **改动：** +71 / -806 · **最后提交：** 11-10 22:14

<a id="pr-21492"></a>

### [#21492 · \[Feature\]\[Observability\] Add M4 token-repeat detection](https://github.com/vllm-project/vllm-ascend/pull/21492)

新增独立 CPU M4 token-repeat 检测工具，包含 C++ 扩展、Python 适配、词表生成和构建打包配置；同时补充发布说明及 runtime guard 测试辅助锁。

**CI：** 未知 · **改动：** +1935 / -49 · **最后提交：** 11-12 15:30

<a id="pr-21490"></a>

### [#21490 · \[临时/勿合入\] 全量 A2/A3 业务选测跑 karc fed runner（对齐 #20716）](https://github.com/vllm-project/vllm-ascend/pull/21490)

将 PR 工作流临时切换为 FED runner 上的 A2/A3 全量选测，并为 upstream 可复用工作流增加 runner 输入；常规检查与标签门禁被省略，明确标注勿合入。

**CI：** 未知 · **改动：** +54 / -799 · **最后提交：** 11-12 09:39 · **Draft**

<a id="pr-21489"></a>

### [#21489 · \[Test\]\[Feature\] Add GLM-5.3 W4A4C8 MTP coverage on A5](https://github.com/vllm-project/vllm-ascend/pull/21489)

在 nightly 配置中新增 A5 8 卡 GLM-5.3 W4A4C8 MTP 测试任务，关联对应 SIT 模型配置。

**CI：** 未知 · **改动：** +78 / -0 · **最后提交：** 11-10 20:16

<a id="pr-21482"></a>

### [#21482 · \[BugFix\] Validate EPLB intervals are positive and fix config error messages](https://github.com/vllm-project/vllm-ascend/pull/21482)

新增 EPLB 配置修复说明：热度收集和算法执行间隔必须为正，冗余专家数量仍允许为零。

**CI：** 未知 · **改动：** +60 / -4 · **最后提交：** 11-11 10:40

<a id="pr-21481"></a>

### [#21481 · \[CI\] memcache cases](https://github.com/vllm-project/vllm-ascend/pull/21481)

在 weekly 配置中加入 GLM-5.3 与 DeepSeek-V4-Flash 的 Memcache/PD 任务，并补充相关长上下文数据集缓存清单。

**CI：** 未知 · **改动：** +535 / -1 · **最后提交：** 11-12 18:35

<a id="pr-21480"></a>

### [#21480 · \[Cherry-pick\]\[releases/v0.32.0rc\]\[CI\]\[BugFix\] Skip CANN 9.2.x custom-op .so validation in A5 wheel build (from #21479)](https://github.com/vllm-project/vllm-ascend/pull/21480)

在 A5 wheel 构建 Dockerfile 中为 CANN 9.2.x 自定义算子安装增加 --force，跳过缺少构建期 stub 所导致的共享库校验，并验证补丁和产物存在。

**CI：** 未知 · **改动：** +10 / -1 · **最后提交：** 11-10 19:48

<a id="pr-21479"></a>

### [#21479 · \[CI\]\[BugFix\] Skip CANN 9.2.x custom-op .so validation in A5 wheel build](https://github.com/vllm-project/vllm-ascend/pull/21479)

在 A5 wheel 构建 Dockerfile 中为 CANN 9.2.x 自定义算子安装增加 --force，跳过缺少构建期 stub 所导致的共享库校验，并验证补丁和产物存在。

**CI：** 未知 · **改动：** +10 / -1 · **最后提交：** 11-10 19:37

<a id="pr-21469"></a>

### [#21469 · \[Misc\] main2main: upgrade verified vLLM main from 1106 to 1112](https://github.com/vllm-project/vllm-ascend/pull/21469)

更新 CI 验证使用的 vLLM main 固定提交，并适配图调度、KV offload 与 release scheduler 的测试辅助接口；离线 DSD 配置生成器新增按版本约束的 drafter padding 选项。

**CI：** 未知 · **改动：** +3322 / -401 · **最后提交：** 11-12 17:53 · **Draft**

<a id="pr-21468"></a>

### [#21468 · \[Performance\] Skip attention output write-back when the backend returns the same tensor](https://github.com/vllm-project/vllm-ascend/pull/21468)

新增 attention 输出回写微基准，对比冗余复制与返回同一输出张量时跳过复制的路径，并补充对应性能发布说明。

**CI：** 未知 · **改动：** +200 / -2 · **最后提交：** 11-10 18:19 · **Draft**

<a id="pr-21467"></a>

### [#21467 · \[Performance\] Avoid pre-zeroing fully overwritten GDN output rows](https://github.com/vllm-project/vllm-ascend/pull/21467)

新增 GDN 输出初始化微基准，对比完整预清零与仅清零 padding 的路径，并记录避免重复清零的性能变化；脚本不把局部操作耗时当作模型吞吐。

**CI：** 未知 · **改动：** +155 / -10 · **最后提交：** 11-10 18:19 · **Draft**

<a id="pr-21466"></a>

### [#21466 · \[Performance\] Consume strided BA inputs directly in GDN gating](https://github.com/vllm-project/vllm-ascend/pull/21466)

新增 GDN gating 步幅微基准，对比 BA 连续化复制与直接读取原始步幅，并要求显式提供修改前内核作为基线；同时补充性能发布说明。

**CI：** 未知 · **改动：** +273 / -9 · **最后提交：** 11-12 00:40 · **Draft**

<a id="pr-21465"></a>

### [#21465 · \[Performance\] Produce cumulative expert boundaries for local MXFP8 routing](https://github.com/vllm-project/vllm-ascend/pull/21465)

新增 A5 MXFP8 MoE 路由微基准，对比单独 cumsum 与算子直接返回累计专家边界的路径，并补充性能发布说明。

**CI：** 未知 · **改动：** +250 / -6 · **最后提交：** 11-10 18:19 · **Draft**

<a id="pr-21464"></a>

### [#21464 · \[v0.32.0rc\]\[Doc\]\[BugFix\] Fix truncated model support tables in Chinese docs](https://github.com/vllm-project/vllm-ascend/pull/21464)

修正文档翻译提取与翻译器对多层表头、表格分隔符和截断响应的处理，启用多行表格扩展并补充写作指南，避免中文支持矩阵被截断。

**CI：** 通过 · **改动：** +112 / -224 · **最后提交：** 11-12 17:26

<a id="pr-21459"></a>

### [#21459 · \[临时/勿合入\] 验证 karc 线下成员：a3-800i-fed-16 + a2-fed-2 smoke](https://github.com/vllm-project/vllm-ascend/pull/21459)

将 PR 工作流临时改为线下 karc 的 A3 16 卡与 A2 2 卡冒烟测试，并调整可复用测试工作流的代理、依赖镜像、超时及下载并发设置；明确标注勿合入。

**CI：** 失败 · **改动：** +789 / -1466 · **最后提交：** 11-10 17:53 · **Draft**
