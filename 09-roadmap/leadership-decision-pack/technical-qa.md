# Round15H — 技术领导可能提出的十四个尖锐问题

使用方式：每条先回答核心结论，再明确最强反证和不能宣称的内容。主证据依 [15G 审计](../../analysis/audits/round15g-final-source-and-ssot-audit-2026-10-08.md)。

## Q1. NPU 性能越来越强，为什么还要在 CPU AI 上投入？

CPU 稳定承担可编程控制与灵活执行，但 CPU AI 的胜出区域由算子形状、精度、backend、转换/调度决定。[PAPER-009](../../01-evidence/papers/PAPER-009/deep.md) 曾观察到特定栈的 CPU/NPU crossover，[PAPER-059](../../01-evidence/papers/PAPER-059/deep.md) 和 [PAPER-057](../../01-evidence/papers/PAPER-057/deep.md) 则证明强 NPU 软件会蚕食它。**投可移植执行/选择能力，不宣称 CPU 永远胜出。**

## Q2. 现有 SME2 手机数据是否证明 Agent 更适合 CPU？

**否。** [TOOL-012](../../01-evidence/tools/TOOL-012/deep.md) vivo X300 测的是 SqueezeSAM 单核 CPU 开关 SME2；无同条件优化 NPU/Agent 全流程对照。[PAPER-052](../../01-evidence/papers/PAPER-052/deep.md) 在不同平台评估 CPU/SME，苹果能耗不等于手机。

## Q3. LLVM/MLIR 的新意在哪里？基本 lowering 不都有了吗？

已存在的 [ArmSME](../../01-evidence/tools/TOOL-015/deep.md)、[SME ABI](../../01-evidence/tools/TOOL-014/deep.md)、[KleidiAI](../../01-evidence/tools/TOOL-016/deep.md) **不允许重报发明**。投资价值是动态 shape/precision、packing、kernel dispatch、调用/状态边界与 NPU 分工的工程组合。无公开数据时不能声称 SME 模式切换消耗已经量化。

## Q4. Arm C2 强调 CPU 执行 Agent AI，为什么不是原创新硬件 Bet？

Arm [VENDOR-018](../../01-evidence/vendors/VENDOR-018/deep.md) 为产品/官方宣称；SME2 是已公开通用 ISA/硬件能力。我们建议跟进并利用，不声称新 Agent ISA 的独立新颖性，也不把厂商对比当独立实证。

## Q5. HeRo 表明 Agent-aware 调度有效，为什么不给硬件加优先级 hint？

[HeRo](../../01-evidence/papers/PAPER-098/deep.md) 使用软件可见 partial DAG、shape/affinity、DRAM bandwidth 等信息。证明软件/Runtime 有价值，不证明新 CPU hint 的额外收益。必须先区分通用可重建信号与真正不可重建的物理需求。

## Q6. A 原来 82.5 分 Primary Bet，为什么降级？

软件可以借助 ledger/history/validator 取得语义进度价值，[LAS](../../01-evidence/papers/PAPER-119/deep.md) 与 [ProgRouter](../../01-evidence/papers/PAPER-121/deep.md) 是强反证。但不能说私有 RequiredProgress 被证明无效。**A 仍是条件储备，不是现行 Bet**；[DEC-A-008](../../08-decisions/events/DEC-A-008.md)。

## Q7. 预期 2–3 个 Primary Bets，却只有 0 个，是不是研究失败？

不。三项高置信的工程/平台 BUILD 与独立有投资资格的 CPU/uArch 创新赌注不是一回事。凑数会误导投入。当前研究的明确 Kill 与储备机制也是可执行的技术决策。

## Q8. PT-A、C 都偏软件，为何出现在 CPU-uArch 研究？

理解最强软件基线是判断硬件还剩什么技术白区的必要条件。PT-A 主要由 Agent/OS/安全负责，C5 主要由 Runtime/OS 负责。CPU/LLVM 团队直接着力 C1–C3，联合参与 C4/C5，**不能自认对其他团队有组织授权**。

## Q9. B-residual/R2 是不是已经实质没有新颖性？

普通缓存/version、CPU 上下文、affinity 等确实有大量已公开技术。两方向只保留细粒度物理残差的有界问题，未有公开实测明确获益，更不能开立新的 cache/TLB/predictor 硅片项目。[PATENT-024](../../01-evidence/patents/PATENT-024/claims-round15d.md) 与 [PATENT-032](../../01-evidence/patents/PATENT-032/claims-round15d.md) 都对宽泛主张施加强基线压力。

## Q10. 为什么不专设 Agent 语义 ISA 或 Dedicated Always-On 硬件域？

现有 compiler→scheduler hint、CHRE、Sensing Hub 和优先级/缓冲管理已经存在。没有可靠的 Agent 专属软件不足＋物理必要性公开链条，就不应仅按 Agent 名称新建硬件。[CHRE](../../01-evidence/vendors/VENDOR-024/deep.md) 是现有低功耗机制。

## Q11. 没有自有实验还能给领导汇报技术路线吗？

可以提供有边界的公开资料战略研究。别人发表的测量可在原始平台/任务适用范围内引用；本项目不跑实验或 PoC。未知的硬件收益被明确列为证据缺口，不强行以测试作为交付前提。

## Q12. 不同论文、厂商宣传和专利可以直接相加吗？

不可以。llm.npu/ShadowNPU 是同一研究血统，Agent.xpu/HeRo 也有关联；Arm/PyTorch 原始数据有厂商参与。专利申请不等于产品已部署或法律 FTO 结论。不同模型、手机、精度和电量计量也不可直接拼 speedup。[来源审计](../../analysis/audits/round15g-final-source-and-ssot-audit-2026-10-08.md)。

## Q13. 那明年团队优先的三件工程事情是什么？

**技术优先建议**：① CPU/LLVM 现有 SME2/Neon/SVE 与 kernel/布局可移植能力；② 联合 Runtime 的 CPU/NPU 阶段和精度角色合同；③ 与 OS/Agent 平台就安全动作 OutcomeReceipt、前台 QoE 和 NPU 控制明确技术接口。实际人力和项目排期需组织内部判断。

## Q14. 哪种新公开事实会使结论改成“应该新做 CPU-uArch”？

独立原始研究同时揭示：某类 Agent state/执行行为对优化软件仍不可替代的物理成本、通用硬件/OS 控制无法吸收该成本、具体新控制原语可带来手机用户价值，以及已公开的实现/成本边界。少一个环节就只可作为研究假设，**不要求本项目实验**。
