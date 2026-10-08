# Round15H — 技术所有权、强基线、路线与决策责任矩阵

## 一、各工程方向到底由谁控制？

| 具体控制点 | 倡议的技术所有权 | 关键技术抓手 | 已有最强公开基线 | 2027–2029 决策 |
|---|---|---|---|---|
| **CG-06 / C1** | CPU/LLVM/MLIR 团队 | 按 shape/precision/CPU ISA 选择 Linalg tiling/fusion/vector → ArmSME lowering | [MLIR ArmSME TOOL-015](../../01-evidence/tools/TOOL-015/deep.md)、[Linalg TOOL-017](../../01-evidence/tools/TOOL-017/deep.md) | 2027 适配/优化，2028 可移植性；非新 Agent IR |
| **CG-06 / C2** | AArch64 LLVM 后端 + Runtime | streaming PSTATE.SM、ZA live-state、SME call ABI、正确切换/减少不必要转换 | [LLVM AArch64 SME TOOL-014](../../01-evidence/tools/TOOL-014/deep.md) | 现有 ABI 正确性先于新 ISA，切换微秒开销未公开确证 |
| **CG-06 / C3** | CPU 微内核/Runtime 内存层 | KleidiAI Neon/SVE/SME2、GEMM/GEMV、packing 与布局重用 | [KleidiAI TOOL-016](../../01-evidence/tools/TOOL-016/deep.md)、[SMEPilot PAPER-052](../../01-evidence/papers/PAPER-052/deep.md) | 2027–28 主力工程能力，不是独立微架构 |
| **CG-06 / C4** | Compiler + Runtime 联合 | CPU/NPU 异构分区、dynamic shape、precision-role fallback、拷贝/同步边界 | [llm.npu PAPER-059](../../01-evidence/papers/PAPER-059/deep.md)、[ShadowNPU PAPER-057](../../01-evidence/papers/PAPER-057/deep.md) | 随 NPU 后端进化持续修正 CPU 使用场景 |
| **C / C5** | Runtime / OS + CPU 联合 | 部分 Agent DAG、criticality/affinity、DRAM/foreground QoE、NPU admission 和 cancellation | [HeRo PAPER-098](../../01-evidence/papers/PAPER-098/deep.md)、[Android NPU Manager VENDOR-027](../../01-evidence/vendors/VENDOR-027/deep.md) | 系统软件 BUILD，OS 接口可能依平台版本不同 |
| **PT-A** | Agent Framework / Runtime / OS/安全平台 | 权限和目标上下文绑定、可见效果 OutcomeReceipt、验证/有限恢复 | [Apple API VENDOR-032](../../01-evidence/vendors/VENDOR-032/deep.md)、[PATENT-033](../../01-evidence/patents/PATENT-033/claims-round15d.md) | 软件平台合同，不是 CPU ISA 任务 |

**公司里的真实团队、headcount、budget、sponsor 和内部芯片能力均未提供**，上述仅是技术层归属建议，不表示这些团队已接收任务。

## 二、每个方向最强的反方解释

- **CPU 不是永远胜 NPU。** [PAPER-009](../../01-evidence/papers/PAPER-009/deep.md) 仅对指定 Snapdragon 软件后端建立 CPU/NPU crossover；PAPER-059/057 展示图重构、量化和混合执行如何回收 CPU 工作。
- **手机 SME2 快，不是 Agent 手机能耗证据。** [TOOL-012](../../01-evidence/tools/TOOL-012/deep.md) 的 vivo X300 SqueezeSAM 单核对比是 CPU SME2 开/关，非 NPU 同条件 head-to-head，且由 Arm 参与发布。
- **软件已经能感知多数 Agent workflow 信息。** [LAS PAPER-119](../../01-evidence/papers/PAPER-119/deep.md)、[ProgRouter PAPER-121](../../01-evidence/papers/PAPER-121/deep.md) 支持从 ledger/verifier/progress 做有用控制，不能据此证明独立私有 RequiredProgress 物理必要。
- **同团队多篇论文并非独立复现。** llm.npu/ShadowNPU 同研究链条，Agent.xpu/HeRo 亦有相同研究血统。厂商营销与独立第三方结果必须区别。

## 三、2027–2029 方向×层级路线

| 主责层 | 2027：基于公开机制的能力建设建议 | 2028：接口和版本兼容建议 | 2029：条件性选项 |
|---|---|---|---|
| **CPU / LLVM** | C1–C3 现有 ISA SME2/Neon/SVE、compiler lowering、ABI、packing/kernel | Shape/precision/capability 合同与跨设备可移植执行 | 仅在公开资料确认特有 CPU continuation 物理残差后再考虑新结构 |
| **Compiler↔Runtime** | C4 stage/precision/shape 选择、复用 layout | 不同 CPU/NPU backend 和模型版本的运行时合同 | 有明确软件不足时才考虑新硬件接口 |
| **OS / Runtime / Agent** | C5 QoE、NPU admission、PT-A 目标绑定/效果验证 | 跨 App、跨引擎、安全权限/状态版本互操作 | 可信 Agent 的通用软件平台 |
| **Memory / Cache / LP SoC** | generic cache、QNN buffer、CHRE/低功耗 sensing | 版本化派生状态、LP useful-assistance energy 的外部证据 | B/R2 保留研究；CG-07 只在出现独立增量证据时重评 |

这不是研发任务排期，也不是新的实验计划；不需要实验来完成本阶段洞察。

## 四、三项储备的唯一允许升级条件：公开证据

| 储备 | 当下未确证的核心 | 强通用基线 | 新公开证据将如何改变判断 |
|---|---|---|---|
| **A** | 私有 RequiredProgress 超过完整可观察软件 B4-TX 的独立信息价值 | 个人历史、ledger、SLO/utility、验证和权限 | 独立公开论文明确隔离私有信息的额外贡献以及合理手机映射 |
| **B-residual** | S0/S1 修订造成 S2/S3 物理派生对象仍有通用 version/provenance 难覆盖的有效性成本 | [PATENT-032](../../01-evidence/patents/PATENT-032/claims-round15d.md) 与 Qualcomm QNN 公开缓冲接口 | 公开材料证明真实 CPU↔NPU/DRAM 状态可重用/失效差额超出 generic 控制 |
| **R2** | 长 Agent continuation 下 cache/TLB/branch predictor 特有保留价值 | Generic affinity/cache 设计和 [PATENT-024](../../01-evidence/patents/PATENT-024/claims-round15d.md) | 独立发表手机 continuation 微状态收益且软件/通用缓存无法吸收 |

**R1 = Watch；CG-07 = Explore/Follow；CG-01 = Benchmark/Follow；R3 = Blocked**。这些分类不构成预算审批，也不要求本项目运行技术验证。

## 五、正式投资决策保持不变

**CG-06 INVEST / PT-A PLATFORM_TRACK / C STRATEGIC_ENABLER；0 个独立差异化 Primary Bet；核心 Reserves A/B-residual/R2；R1 Watch；R3 Blocked。** 来源：[当前 portfolio](../current.md)、[DEC-PORTFOLIO-002](../../08-decisions/events/DEC-PORTFOLIO-002.md)。
