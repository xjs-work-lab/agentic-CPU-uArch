# 2027–2029 手机 Agentic AI：CPU/uArch、LLVM、OS、SoC 技术洞察与投资路线图

> **技术领导层决策稿 v1.0 · Round15G · 2026-10-08 · 公开证据研究成果**。
>
> 现行投资权威：[current.md](current.md)；[七问进度](../00-project/final-questions-status.md)；[原始证据独立性与审计](../analysis/audits/round15g-final-source-and-ssot-audit-2026-10-08.md)；[CPU/LLVM 技术细节](../analysis/engineering/round15f-cpu-llvm-compiler-pressure-2026-10-08.md)。

## 执行摘要：技术判断与决策请求

**Agentic AI 的手机影响，是从单次模型请求走向持续会话、动态 CPU↔NPU/GPU 多阶段执行、可撤销动作和主动帮助。CPU 的主要价值是“可编程控制主机 + 现有 ISA 支持的选择性小模型/算子执行端”，而非 CPU 将取代 NPU。**

**建议：批准 CG-06、PT-A、C 三项明确技术所有权的工程/平台投入；保留 A、B-residual、R2 三项研究储备；当前不设立 Agent 专属 CPU ISA/uArch/硅片 Primary Bet。** 当前独立差异化 Primary Bets 为 **0**，不是为完成配额而将成熟软件优化重新包装成硬件 Bet。

置信表达：**公开实证/官方能力**、**跨来源推断**、**有界架构假设**、**未被公开资料证实**。本项目未做、不安排实验、PoC、仿真或真机测试。

## 1. 2027–2029 四项重要结构变化（按战略意义排序）

| 趋势 | 工作负载/体验变化 | CPU/uArch、编译和 SoC 后果 | 证据/缺口 |
|---|---|---|---|
| **T1 持久会话与可信行动** | Agent 保持会话、跨 App 调工具、目标确认与结果验证 | CPU 控制和 OS Runtime、目标权限/效果合同、状态恢复 | Apple Foundation Models 官方 API 和 Android/Agent 学术资料；不是 Agent ISA 实证 |
| **T2 异构多阶段反复调用** | Prefill/Decode、tool、retrieval、rerank、分类、控制不断改变形状和精度、反复进入 CPU/NPU/GPU | **CG-06 CPU/LLVM+优化 NPU 分工、C 运行时 Stage DAG/DRAM/QoE** | PAPER-009/057/059/098 与已发表手机/SoC 结果，后端优化可能改变 CPU 角色 |
| **T3 修订/暂停/事务与多层状态** | 推理途中撤销、更换目标，派生 KV/缓存/外部效果不能混淆 | F 执行与状态生命周期；普通版本化、队列取消、共享缓冲已成熟 | 现有 Android/专利/软件基线强，特有物理 Agent 增量未证实 |
| **T4 主动感知与正确地不行动** | 背景事件→是否打扰用户→选择模型/唤醒，隐私及电池资源约束 | P 低功耗 admission；CG-07 跟进现有 CHRE/AOP/LP AI | 产品已出现，帮助率和电池负担跨设备量化稀缺 |

年份是**研究/投资规划时间轴**，不是宣称厂商将在哪一年量产特定功能。原产品趋势数据库 [T1–T8](product-evolution-map.md)仍保留更细的研究对象。

## 2. 三条跨层架构主题：机制与白区分开

| 主题 | 强公开基线 | 剩余有界机会 | 现行动作 |
|---|---|---|---|
| **F Execution–State Lifecycle (AO1/2/3)** | Android NPU Manager 模型/工作状态、Qualcomm QNN 共享缓冲、版本化软件缓存/事务恢复、已有异构调度 | 跨 CPU/NPU 引擎派生状态的授权版本、安全保留与物理回收之间是否有软件不能吸收的真实成本 | **C/PT-A BUILD；B-residual/R2 RESERVE**；无新硬件 |
| **P Proactive Low-Power Admission (AO4)** | Android CHRE、Apple AOP、Qualcomm Sensing Hub、MediaTek LP AI 与软件用户需求预测 | 比既有 event gating + 共用 NPU 更低且有效的帮助率调整后日能耗，尚待**外部公开证据** | **CG-07 FOLLOW / EXPLORE** |
| **V Semantic Progress / QoE (AO5)** | [LAS — ACL 2026](https://aclanthology.org/2026.acl-long.581/) 与 [ProgRouter — arXiv 2026](https://arxiv.org/abs/2608.25992) 在软件 ledger/validator、进度和预算内调度 | 不可由历史、效用、workflow、权限、验证记录重建的私有 RequiredProgress 是否真有额外结果价值 | **A CONDITIONAL_RESERVE**；不立新语义 ISA |

## 3. P0 投入：具体技术控制点

### CG-06 — CPU/LLVM/AArch64 异构快速路径（INVEST）

**方向结论：投资现有 CPU ISA 的编译、微内核、低开销状态与跨处理器放置能力。不要投资“CPU 对所有 Agent 推理天然更优”或新 Agent 指令集。**

- **原始手机证据**：[When NPUs Are Not Always Faster (PAPER-009)](https://arxiv.org/abs/2605.27435) 在 Snapdragon 8 Gen 3/Hexagon v75 的 CPU/NPU 版本报告阶段/后端依赖的 crossover；不可移植为永恒规律。
- **SME CPU 实现**：[SMEPilot (PAPER-052)](https://arxiv.org/abs/2606.16332) 证明现有 SME/CPU 混合算子、packing 与流水化的价值；Apple M4 Pro 能耗与手机不能混作一项实测。
- **真手机 CPU 技术数据**：[ExecuTorch/Arm SME2 官方博客 (TOOL-012)](https://pytorch.org/blog/accelerating-on-device-ml-inference-with-executorch-and-arm-sme2/) 报告 vivo X300 SqueezeSAM 单 CPU 核 INT8 **555.8→304.1ms**、FP16 **1163.0→298.2ms**，SME2 后 data movement 占约 40%。**视觉分割而非 Agent/NPU 对比；作者包含 Arm 人员。**

五项可归属工程能力：

| ID | 技术抓手 | 执行层所有权 | 已有强基线/避坑 |
|---|---|---|---|
| **C1** | 按形状、精度、向量/矩阵能力选择编译降低、tile/fusion/layout | **MLIR/LLVM/AArch64 编译** | 官方 [ArmSME](https://mlir.llvm.org/docs/Dialects/ArmSME/)、[Linalg](https://mlir.llvm.org/docs/Dialects/Linalg/) 和向量化已存在 |
| **C2** | Streaming PSTATE.SM、ZA 调用约定和跨 scalar↔SME 函数正确边界 | **LLVM 后端+Runtime ABI** | [LLVM AArch64 SME](https://llvm.org/docs/AArch64SME.html) 已支持规范；**不能虚构手机切换的微秒开销** |
| **C3** | KleidiAI 级 GEMM/GEMV/packing 微内核及持续布局重用 | **CPU 内核库+Runtime 数据生命周期** | [Arm KleidiAI](https://github.com/ARM-software/kleidiai) 已公开，与具体调度/内存由调用端分工 |
| **C4** | CPU/NPU 分阶段、精度敏感残差和动态 offload/fallback | **编译+Runtime 的跨引擎合同** | NPU 图重构/量化分工是必须比较的成熟软件竞争面 |
| **C5** | Agent 部分 DAG/criticality、前台 QoE/共享 DRAM 和 NPU admission | **Runtime/OS（主属 C）** | HeRo 和 Android 管理接口是强基线，不算 CG-06 自创物理调度器 |

**NPU 反证**：[llm.npu — ASPLOS 2025 (PAPER-059)](https://doi.org/10.1145/3669940.3707239)、[ShadowNPU — MobiSys 2026 (PAPER-057)](https://doi.org/10.1145/3745756.3809205)、[HeRo — Agentic RAG 手机调度 (PAPER-098)](https://arxiv.org/abs/2603.01661) 分别改善图形静态化、低/高精度角色分拆和动态异构工作流。前两项研究共用作者/研究集团，**是持续技术路线，不是两次独立复现**。CPU 角色需要跟随优化 NPU 能力变化。

### PT-A — 可信 Agent 工具、权限与 OutcomeReceipt（PLATFORM_TRACK / BUILD）

核心平台合同：**能力/权限确认 → 新鲜的目标 App/上下文绑定 → 安全动作边界 → 已发生效果可观测 OutcomeReceipt → 验证 → 有界恢复**。优先考虑软件/OS，而非专用 CPU 指令。多 Agent 事务回退一般机制已见 [CN120704926A 权利要求](https://patents.google.com/patent/CN120704926A/en)，只能在超出这些已公开软件机制之处再谈差异化。

### C — 跨 CPU/NPU/GPU 资源控制和前台 QoE（STRATEGIC_ENABLER / BUILD）

动态 Stage/PU affinity、部分 DAG、shape、shared DRAM、前台资源冲突是可投资的软件/OS 合同。[HeRo](https://arxiv.org/abs/2603.01661) 在实际 Snapdragon 手机 Agentic RAG 展示软件调度的改进；[SERENO — OSDI 2026](https://www.usenix.org/system/files/osdi26-xin.pdf) 涵盖移动共享带宽和 QoE 争用。已有 Android NPU 工作状态/优先级接口，**证明普通 Agent 优先级管理不是全新 uArch 功能**。特殊硬件物理接口还需强于这些已知机制的直接外部证据。

## 4. 2027 / 2028 / 2029 分技术层路线

| 层 | **2027：建立/适配** | **2028：强化跨层契约** | **2029：条件储备** |
|---|---|---|---|
| **CPU / LLVM / uArch** | 现有 AArch64 SME2/SVE/Neon C1–C3、微内核和 packed-layout 复用；CPU 可编程响应链 | shape/precision/capability 适配与可移植 CPU/NPU codegen/ABI；跟踪公开 CPU 续执行局部性 | 仅在新的外部证据确认硬件物理残差时研究 uArch 选项；不预定专用 ISA |
| **CPU↔GPU↔NPU / OS / Runtime** | C4/C5，优化 NPU 的真实强基线、阶段级分工、前台 QoE/工作调度 | 部分工作流 DAG + 状态版本/模型生命周期/权限对齐，提升跨运行时可复用性 | 条件性跨引擎状态安全保留/撤销协议研究；非新硅片承诺 |
| **Agent 动作/信任** | PT-A 授权、目标锁定、工具结果合同、验证与恢复 | 跨 App/本地服务状态与效果数据合同 | 可复用可信 Agent 平台机制 |
| **Memory/KV/Cache** | Generic cache/Coherence/版本、packed layout、共享缓冲既有能力 | 多模型 KV/派生对象有效性与功耗权衡的公开进展 | B-residual/R2 仅保留为严格限定研究问题 |
| **低功耗/Always-on** | CHRE、Sensing Hub、LP NPU 现有解决方案与关闭无用触发 | “不行动”质量、隐私与帮助率/电量的外部证据融合 | 只有证明超越通用低功耗平台的增量才讨论 Agent 专用域 |

这是**研究提出的技术规划**，不是厂商产品 roadmap、内部开发排期或任何实验计划。

## 5. 正式投资组合与 Kill

| 领域 | 本轮正式结论 | 判断依据 |
|---|---|---|
| **优先工程 INVEST/BUILD：3** | **CG-06、PT-A、C** | 软件+SoC 产品/论文实证，团队可控，已有强原始基线 |
| **差异化 Primary Bet：0** | **不填名额** | 无独立充分公开证据证明新 Agent 特有 CPU-uArch 原语的手机效益 |
| **战略储备：3** | **A、B-residual、R2** | A 私有信息、B 派生物理状态版本、R2 CPU continuation 微状态仍是有界未证实可能性 |
| **技术跟进** | **CG-07 Explore；CG-01 Benchmark/Follow；R1 Watch** | 泛化既有能力成熟、独立硬件新增价值低置信 |
| **Kill/Blocked** | **R3 Agent 语义硬件 Hint、泛化 NPU 优先级/取消、通用零拷贝、普通 Agent 语义缓存/事务机制“新硬件独特性”主张** | 已有 SDK、软件和专利，不等于不做常规软件功能 |

**A 历史 82.5/Primary Bet 在 [DEC-A-008](../08-decisions/events/DEC-A-008.md) 已正式降级**；当前只保留条件研究储备，不能仍按旧分数对领导声称已获科学证实。**Kill 范围是独立新颖性或硬件预算，不是杀死真正的用户功能。**

## 6. 哪些证据强、哪些只是推断、哪些未知？

- **有原始论文/官方资料支持：** 现有 ISA 手机上 CPU SME2 能加速特定模型；mobile NPU 优化能扩大其主导区域；软件 Agent DAG 调度具有真实手机结果；可信行为验证/权限和官方 AI SDK 已出现。
- **跨来源推断：** “双重角色 CPU”会持续有用；2027–29 的投入排序和 F/P/V 对应的跨层研发责任。它们不是未来市场占比预测。
- **未由公开资料证明：** 私有 RequiredProgress 对强软件 B4-TX 的额外信息；新 CPU uArch Hint/缓存/TLB/指令；跨厂商端到端 Agent 24h 电池+前台 QoE + 任务成功率严格可比收益；未公开厂商 SoC 内部硬件缺失。

部分官方文档在本轮直接浏览受限；详细状态见 [Round15G 证据审计](../analysis/audits/round15g-final-source-and-ssot-audit-2026-10-08.md)。未取得直接页面访问的资料不能写成“最新全文核验通过”。未公开的直接实证是置信边界，**不阻止基于现有公开证据完成技术战略报告。**

## 7. 建议技术管理层当下作出的决策

**批准**三条团队可控 P0 工程能力：① CPU+LLVM 现有 ISA 和异构 placement，② 可信 Agent 行为平台合同，③ QoE-aware Runtime/OS 资源控制。**保留研究选项** A/B-residual/R2，但不给予当前 silicon Bet 权限。**暂不投资**专用 Agent ISA、只为 Agent 命名的新 CPU cache/hint/always-on 域。

后续只有来自新发表的可比手机 Agent 原始论文、独立作者性能反证或厂商/标准技术接口实质变化，才可能触发重排。研究阶段交付到此有明确决策结论；公开证据不足的硬件假设应作为风险披露而非强制开展实验的任务。
