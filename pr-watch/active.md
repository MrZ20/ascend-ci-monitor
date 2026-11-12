# PR 关注列表

最近刷新：2026-11-12 21:51:59（上海时间）
当前关注的开放 PR：35
范围：最近 30 天有创建、提交、CI、Draft 或目标分支变化证据的开放 PR；普通评论不算活动。
长期无元数据更新的旧 PR 未逐个追查仅 CI 重跑的活动，本页不代表这类活动已全覆盖。

活动待确认：370 个较早创建、近期 updated_at 变化的开放 PR 尚无最近 30 天有效活动证据，暂不纳入。

CI 待刷新：7 个 PR 尚未取得本轮所需的完整检查结果；上次状态不代表当前结果。

覆盖说明：1008 个近 30 天范围内的 PR 文件范围或详情待补齐。

本轮覆盖缺口：4 项采集未完成；受影响状态显示未知或等待补齐。

## 最近更新（72h）

- [11-12 21:39 · #21469 \[Misc\] main2main: upgrade verified vLLM main from 1106 to 1112](#pr-21469)
- [11-12 21:24 · #21713 \[BugFix\] Rename static operator build option to --soc\_series](#pr-21713)
- [11-12 20:34 · #21685 \[CI\] add presmoke for CI](#pr-21685)
- [11-12 20:32 · #21712 \[Doc\]\[Misc\] Document Ascend Docker Runtime container setup](#pr-21712)
- [11-12 20:32 · #21587 \[Feature\] Fuse GatingTopK with EPLB expert mapping](#pr-21587)
- [11-12 20:32 · #21481 \[CI\] memcache cases](#pr-21481)
- [11-12 19:36 · #21541 \[Doc\] add doc quality review workflow for docs/source changes](#pr-21541)
- [11-12 18:41 · #21714 \[Refactor\]\[MRV2\] Adopt EPLB policy and model-state hooks](#pr-21714)
- [11-12 18:35 · #21705 \[Feature\] DSpark expert-pool routing for the expert-offload path](#pr-21705)
- [11-12 18:31 · #21717 \[CI\] Restore A5 multi-node nightly test cases](#pr-21717)
- [11-12 18:10 · #21716 \[临时/勿合入\] ci: route Nightly-A2 cases to offline-cluster runner labels](#pr-21716)
- [11-12 17:00 · #21701 \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](#pr-21701)
- [11-12 16:33 · #21699 \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.32.0rc](#pr-21699)
- [11-12 15:54 · #21689 \[CI\] Isolate lint images by branch and add a lightweight tools image](#pr-21689)
- [11-12 15:52 · #21594 \[Feature\]\[MoE\] Support anchor-union activation routing for DSpark and DFlash speculative decoding](#pr-21594)
- [11-12 15:52 · #21680 \[Feature\]\[MoE\] Add opt-in DSpark expert-pool routing for expert offload](#pr-21680)
- [11-12 15:39 · #21653 \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.30.0](#pr-21653)
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

<a id="pr-21717"></a>

### [#21717 · \[CI\] Restore A5 multi-node nightly test cases](https://github.com/vllm-project/vllm-ascend/pull/21717)

恢复 A5 多节点 nightly 测试配置，重新启用 DeepSeek、GLM 和 Qwen 的五组双节点用例。

**CI：** 未知（待刷新；上次完整检查：11-12 20:32 · 通过） · **改动：** +22 / -22 · **最后提交：** 11-12 18:06

<a id="pr-21716"></a>

### [#21716 · \[临时/勿合入\] ci: route Nightly-A2 cases to offline-cluster runner labels](https://github.com/vllm-project/vllm-ascend/pull/21716)

将 A2 单节点性能与精度测试的 nightly、PR-only runner 配置切换到 fed-karc 集群，覆盖 1、2、4、8 卡规格。

**CI：** 未知（待刷新；上次完整检查：11-12 20:32 · 失败（ci-gate）） · **改动：** +14 / -14 · **最后提交：** 11-12 18:07

<a id="pr-21714"></a>

### [#21714 · \[Refactor\]\[MRV2\] Adopt EPLB policy and model-state hooks](https://github.com/vllm-project/vllm-ascend/pull/21714)

更新经验证的 vLLM 主分支提交，并同步 EPLB 设计文档和发布说明中的接口依赖、默认 stair 策略说明；同时调整示例启动脚本的类型检查标记。

**CI：** 未知（待刷新；上次完整检查：11-12 20:32 · 失败（ci-gate）） · **改动：** +623 / -867 · **最后提交：** 11-12 18:23 · **Draft**

<a id="pr-21713"></a>

### [#21713 · \[BugFix\] Rename static operator build option to --soc\_series](https://github.com/vllm-project/vllm-ascend/pull/21713)

将静态算子构建工具的参数统一为 --soc\_series，并同步资源生成及编译目录引用，属于通用构建链修正。

**CI：** 失败（ci-gate） · **改动：** +10 / -10 · **最后提交：** 11-12 20:07

<a id="pr-21712"></a>

### [#21712 · \[Doc\]\[Misc\] Document Ascend Docker Runtime container setup](https://github.com/vllm-project/vllm-ascend/pull/21712)

Getting Started 补充 Ascend Docker Runtime 安装验证、设备选择及额外挂载说明，并从 Quick Start 链接新指南。

**CI：** 未知（待刷新；上次完整检查：11-12 20:32 · 失败（ci-gate）） · **改动：** +90 / -1 · **最后提交：** 11-12 19:48

<a id="pr-21705"></a>

### [#21705 · \[Feature\] DSpark expert-pool routing for the expert-offload path](https://github.com/vllm-project/vllm-ascend/pull/21705)

将 A5 expert-offload 测试接入选测、预计耗时和 runner 配置，并补充 DSpark expert-pool 配置说明与 CPU 单测辅助夹具。

**CI：** 未知（待刷新；上次完整检查：11-12 20:32 · 失败（ci-gate）） · **改动：** +2871 / -6 · **最后提交：** 11-12 18:13

<a id="pr-21701"></a>

### [#21701 · \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](https://github.com/vllm-project/vllm-ascend/pull/21701)

临时精简 PR E2E 工作流，将两个四卡流水线并行用例固定到 karc 专用 A3 runner，验证工作区同步问题；PR 明确标注勿合入。

**CI：** 未知（待刷新；上次完整检查：11-12 20:32 · 通过） · **改动：** +70 / -808 · **最后提交：** 11-12 16:27

<a id="pr-21699"></a>

### [#21699 · \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.32.0rc](https://github.com/vllm-project/vllm-ascend/pull/21699)

为 v0.32.0rc 新增 A5 UBX 的 Ubuntu 和 openEuler Dockerfile，明确暂用基础镜像及后续 CANN 包切换点。

**CI：** 通过 · **改动：** +419 / -0 · **最后提交：** 11-12 16:10

<a id="pr-21689"></a>

### [#21689 · \[CI\] Isolate lint images by branch and add a lightweight tools image](https://github.com/vllm-project/vllm-ascend/pull/21689)

按目标分支隔离 lint 镜像，并新增轻量 lite-tools 镜像供测试选择、缓存准备和文档任务使用；配套调整镜像构建流程与维护说明。

**CI：** 失败（ci-gate） · **改动：** +278 / -97 · **最后提交：** 11-12 15:34

<a id="pr-21685"></a>

### [#21685 · \[CI\] add presmoke for CI](https://github.com/vllm-project/vllm-ascend/pull/21685)

为 CI 增加 presmoke 镜像构建及 nightly 使用隔离镜像的入口，将仓库和标签后缀传递到各硬件工作流，并补充贡献指南。

**CI：** 通过 · **改动：** +392 / -54 · **最后提交：** 11-12 20:16

<a id="pr-21680"></a>

### [#21680 · \[Feature\]\[MoE\] Add opt-in DSpark expert-pool routing for expert offload](https://github.com/vllm-project/vllm-ascend/pull/21680)

将 expert-offload A5 用例加入 CI 路由和耗时配置，新增 CPU 单测辅助 fixture，并补充 DSpark expert-pool 的配置说明。

**CI：** 失败（ci-gate） · **改动：** +2630 / -6 · **最后提交：** 11-12 15:35 · **Draft**

<a id="pr-21661"></a>

### [#21661 · \[临时/勿合入\] 验证 karc 专用 4 卡档：a3-800i-fed-karc-4 两用例](https://github.com/vllm-project/vllm-ascend/pull/21661)

临时精简 PR E2E 工作流，将两个四卡流水线并行用例固定到 karc 专用 A3 runner，用于验证工作区同步问题；PR 明确标注勿合入。

**CI：** 失败 · **改动：** +70 / -808 · **最后提交：** 11-12 11:29

<a id="pr-21653"></a>

### [#21653 · \[Feat\]\[Misc\] Add A5 UBX Dockerfiles for v0.30.0](https://github.com/vllm-project/vllm-ascend/pull/21653)

新增 A5 UBX 的 Ubuntu 与 openEuler Dockerfile，并接入定时和 nightly 镜像构建矩阵；同时调整基础镜像版本解析和相关依赖安装。

**CI：** 通过 · **改动：** +451 / -17 · **最后提交：** 11-12 14:04

<a id="pr-21643"></a>

### [#21643 · \[Feature\]\[EC Connector\] Support encoder cache tiering offload on Ascend](https://github.com/vllm-project/vllm-ascend/pull/21643)

更新 MkDocs 导航和中英文标题映射，将编码器缓存卸载文档接入站点导航。

**CI：** 失败（ci-gate） · **改动：** +549 / -65 · **最后提交：** 11-12 10:01

<a id="pr-21638"></a>

### [#21638 · \[Feature\]\[Qwen\] Share PLE tables across Ascend services](https://github.com/vllm-project/vllm-ascend/pull/21638)

在 CMake 中按已安装 HIXL 条件构建并安装原生共享库，新增无需真实 NPU 的 ACL/HIXL 替身测试工具及运行说明。

**CI：** 失败（ci-gate） · **改动：** +4569 / -3 · **最后提交：** 11-12 08:53 · **Draft**

<a id="pr-21623"></a>

### [#21623 · \[Feature\]\[Engram\] Add local host VMM for shared A3 tables](https://github.com/vllm-project/vllm-ascend/pull/21623)

为 A3 增加可选 Engram host VMM 原生库的 CMake 能力检测、构建和安装，并实现共享内存映射及清理接口；同步加入文档导航和发布说明。

**CI：** 失败（ci-gate） · **改动：** +2466 / -99 · **最后提交：** 11-11 21:00

<a id="pr-21607"></a>

### [#21607 · \[Test\]\[Upstream\]rerun failed test case](https://github.com/vllm-project/vllm-ascend/pull/21607)

让 upstream E2E workflow 也由指定分支 PR 触发并关闭 Hugging Face 离线模式；测试运行器切换到新增的精选重跑用例配置。

**CI：** 失败（ci-gate） · **改动：** +32 / -2 · **最后提交：** 11-12 11:31

<a id="pr-21594"></a>

### [#21594 · \[Feature\]\[MoE\] Support anchor-union activation routing for DSpark and DFlash speculative decoding](https://github.com/vllm-project/vllm-ascend/pull/21594)

把 expert-offload A5 测试加入精选 CI，配置 a5-4 runner 和预计耗时，并增加 CPU 侧模型方法与 ACL/NPU 模拟夹具；补充 anchor-union 路由功能的发布说明。

**CI：** 失败（ci-gate） · **改动：** +3880 / -4 · **最后提交：** 11-12 15:47 · **Draft**

<a id="pr-21587"></a>

### [#21587 · \[Feature\] Fuse GatingTopK with EPLB expert mapping](https://github.com/vllm-project/vllm-ascend/pull/21587)

CI runner 映射新增 test\_gating\_map\_npu.py，默认分配 a3-2，明确该测试的运行硬件。

**CI：** 失败（ci-gate） · **改动：** +572 / -18 · **最后提交：** 11-12 19:53

<a id="pr-21546"></a>

### [#21546 · \[CI\] update cann=9.3.0\_20261110170400](https://github.com/vllm-project/vllm-ascend/pull/21546)

将各型号 Ubuntu/openEuler Dockerfile 的 CANN 基础镜像从 9.2.1 更新为 SWR 上的 9.3.0\_20261110170400。

**CI：** 通过 · **改动：** +8 / -8 · **最后提交：** 11-11 14:26

<a id="pr-21541"></a>

### [#21541 · \[Doc\] add doc quality review workflow for docs/source changes](https://github.com/vllm-project/vllm-ascend/pull/21541)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 失败（ci-gate） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21526"></a>

### [#21526 · \[Performance\]\[Kernel\] Fuse DeepSeek-V4.1 indexer prologue on Ascend A2/A3](https://github.com/vllm-project/vllm-ascend/pull/21526)

新增 A2/A3 的 fused\_indexer\_prologue 算子，将 DeepSeek-V4.1 的 key 投影、归一化、RoPE、INT8 量化和分页缓存写入合并，并接入构建、Torch 绑定与元信息注册。

**CI：** 失败（ci-gate） · **改动：** +1136 / -17 · **最后提交：** 11-11 14:25

<a id="pr-21521"></a>

### [#21521 · Upgrade/cann v0.32](https://github.com/vllm-project/vllm-ascend/pull/21521)

升级 CANN 分支的 vLLM 0.32 构建环境，调整容器基础镜像、算子包及 Python 依赖，并同步自定义算子构建列表。已核对的工程改动还包括镜像构建信息汇总、CI action 暂存脚本和主机内存注册能力检测。

**CI：** 失败 · **改动：** +235133 / -103646 · **最后提交：** 11-11 15:21

<a id="pr-21513"></a>

### [#21513 · \[Doc\] Add deepseek\_v41\_qli\_candidate to nav and fix FAQ anchor](https://github.com/vllm-project/vllm-ascend/pull/21513)

在 MkDocs 导航中加入 DeepSeek-V4.1 QLI candidate 开发指南入口。

**CI：** 失败（ci-gate） · **改动：** +2 / -1 · **最后提交：** 11-11 10:54

<a id="pr-21502"></a>

### [#21502 · \[Feature\]\[Performance\] Support InternLM2-20B-Chat and dispatch scaled RoPE variants to the NPU kernel](https://github.com/vllm-project/vllm-ascend/pull/21502)

把 InternLM2-20B-Chat 加入 nightly 精度任务、模型缓存清单、E2E 精度配置和文档导航，并登记双卡测试预估耗时及发布说明。

**CI：** 失败（ci-gate） · **改动：** +851 / -0 · **最后提交：** 11-11 00:02

<a id="pr-21500"></a>

### [#21500 · \[BugFix\] Reap stale opc locks and cap build parallelism by cgroup memory limit](https://github.com/vllm-project/vllm-ascend/pull/21500)

为自定义算子构建按 cgroup 内存限制设置默认并行度，并在构建前清理已失效的 opc 锁；新增对应工具单测，保留活进程锁。

**CI：** 失败（ci-gate） · **改动：** +136 / -1 · **最后提交：** 11-10 22:45

<a id="pr-21493"></a>

### [#21493 · \[临时/勿合入\] a3-800i fed-2 / fed-4 各跑 3 个用例（验证 runner 作业 pod）](https://github.com/vllm-project/vllm-ascend/pull/21493)

将 PR 工作流临时改为 A3 FED 2 卡与 4 卡 runner 的各 3 个用例冒烟验证，省略常规 lint、CPU UT、推荐选测与标签门禁；文件明确标注勿合入。

**CI：** 失败 · **改动：** +71 / -806 · **最后提交：** 11-10 22:14

<a id="pr-21490"></a>

### [#21490 · \[临时/勿合入\] 全量 A2/A3 业务选测跑 karc fed runner（对齐 #20716）](https://github.com/vllm-project/vllm-ascend/pull/21490)

将 PR 工作流临时切换为 FED runner 上的 A2/A3 全量选测，并为 upstream 可复用工作流增加 runner 输入；常规检查与标签门禁被省略，明确标注勿合入。

**CI：** 失败 · **改动：** +54 / -799 · **最后提交：** 11-12 09:39 · **Draft**

<a id="pr-21489"></a>

### [#21489 · \[Test\]\[Feature\] Add GLM-5.3 W4A4C8 MTP coverage on A5](https://github.com/vllm-project/vllm-ascend/pull/21489)

在 nightly 配置中新增 A5 8 卡 GLM-5.3 W4A4C8 MTP 测试任务，关联对应 SIT 模型配置。

**CI：** 通过 · **改动：** +78 / -0 · **最后提交：** 11-10 20:16

<a id="pr-21481"></a>

### [#21481 · \[CI\] memcache cases](https://github.com/vllm-project/vllm-ascend/pull/21481)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 通过 · **改动：** 待更新 · **最后提交：** 待更新

<a id="pr-21480"></a>

### [#21480 · \[Cherry-pick\]\[releases/v0.32.0rc\]\[CI\]\[BugFix\] Skip CANN 9.2.x custom-op .so validation in A5 wheel build (from #21479)](https://github.com/vllm-project/vllm-ascend/pull/21480)

在 A5 wheel 构建 Dockerfile 中为 CANN 9.2.x 自定义算子安装增加 --force，跳过缺少构建期 stub 所导致的共享库校验，并验证补丁和产物存在。

**CI：** 通过 · **改动：** +10 / -1 · **最后提交：** 11-10 19:48

<a id="pr-21479"></a>

### [#21479 · \[CI\]\[BugFix\] Skip CANN 9.2.x custom-op .so validation in A5 wheel build](https://github.com/vllm-project/vllm-ascend/pull/21479)

在 A5 wheel 构建 Dockerfile 中为 CANN 9.2.x 自定义算子安装增加 --force，跳过缺少构建期 stub 所导致的共享库校验，并验证补丁和产物存在。

**CI：** 失败（ci-gate） · **改动：** +10 / -1 · **最后提交：** 11-10 19:37

<a id="pr-21469"></a>

### [#21469 · \[Misc\] main2main: upgrade verified vLLM main from 1106 to 1112](https://github.com/vllm-project/vllm-ascend/pull/21469)

相关文件已纳入关注，当前提交的变更摘要待补齐。

**CI：** 未知（待刷新；上次完整检查：11-12 20:32 · 失败（ci-gate）） · **改动：** 待更新 · **最后提交：** 待更新 · **Draft**

<a id="pr-21459"></a>

### [#21459 · \[临时/勿合入\] 验证 karc 线下成员：a3-800i-fed-16 + a2-fed-2 smoke](https://github.com/vllm-project/vllm-ascend/pull/21459)

将 PR 工作流临时改为线下 karc 的 A3 16 卡与 A2 2 卡冒烟测试，并调整可复用测试工作流的代理、依赖镜像、超时及下载并发设置；明确标注勿合入。

**CI：** 失败 · **改动：** +789 / -1466 · **最后提交：** 11-10 17:53 · **Draft**

<a id="pr-21456"></a>

### [#21456 · \[Refactor\]\[CP\] Decouple PCP/DCP metadata, topology and backend selection](https://github.com/vllm-project/vllm-ascend/pull/21456)

在夜间CI配置中加入Qwen3与DeepSeek上下文并行组合，并将context-parallel矩阵测试接入accuracy列表和耗时估计。

**CI：** 失败（ci-gate） · **改动：** +3721 / -591 · **最后提交：** 11-10 18:22
