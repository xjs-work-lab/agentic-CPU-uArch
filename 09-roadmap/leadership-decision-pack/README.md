# Round15H — 技术领导决策包（五分钟版）

> **2026-10-09 最新交付版本说明（替代下方旧Round15H“最新设计阶段”等历史描述）**：完整17页可编辑PPT已做完，最终版本Round16C已经写入全17页“先解释页面、再逐来源核证”的演讲者备注。技术洞察正式结题见 [最终研究与归档验收](../../00-project/final-research-archive-acceptance-2026-10-09.md)；[成品长期存储、哈希与全备注原文入口](archive/README.md)。下方Round15H九页初纲、早期“尚未完成高保真PPT”等仅作历史过程保留，不再代表当前交付状态。

> **新的内容制作入口（Round15I V4 设计阶段）：[逐页内容—逻辑—证据—视觉设计蓝图（15 页+4 附录）](content-storyboard-v1-2026-10-08.md)**。该蓝图**先于**任何新版 PNG/PPT 制作，作为逐页审稿和设计关口；以下 Round15H 决策包仍提供研究事实和管理决策输入。

> **Round15J 最新制图入口：** [经论文方法抽查的模块化图形规格与静态结构审计](diagram-specs/README.md)。第 4–9 页以这里经过核对的独立页面规格为当前制图依据；第 1–3 页沿用 [Mermaid 逻辑规格](slide-01-03-mermaid-logic-spec-v1-2026-10-08.md)。Mermaid 原生渲染、原论文图像逐图校验与高保真 PPT 验收尚未完成。\n\n**2026-10-08 · v1 · 公开来源限定的战略建议，并非内部预算申请的既成事实。**

研究权威：[Round15G 完整洞察](../management-final-public-evidence-2027-2029.md)；投资状态权威：[Current Portfolio](../current.md) 与 [DEC-PORTFOLIO-002](../../08-decisions/events/DEC-PORTFOLIO-002.md)。

## 一句话决策

**未来手机 CPU 应保留两种角色：Agent/OS 可编程控制主机，与利用现有 AArch64 SIMD/SME2 的选择性 AI 快速执行端。此时更适合投入 CPU+LLVM/Runtime 的现有 ISA 能力，而非新 Agent 语义 ISA/专用硅片。**

当前建议：
- **三项优先工程/平台投入：** CG-06（CPU/LLVM + 异构快速路径）、PT-A（可信 Agent 工具动作/OutcomeReceipt）、C（OS/Runtime CPU↔GPU↔NPU/QoE）。
- **零个有足够公开证据支撑的独立差异化 CPU-uArch Primary Bet。** 不凑 2–3 个配额。
- **三个条件储备：** A（私有 RequiredProgress）、B-residual（派生物理状态有效性）、R2（CPU continuation locality）。
- **跟进而非新建硅片项目：** CG-07/CG-01；R1 Watch；R3 专用语义 Hint Blocked。
- A 旧 82.5 分只是历史评分，2026-10-08 已由 [DEC-A-008](../../08-decisions/events/DEC-A-008.md) 正式降为条件储备。

## 5 分钟陈述结构

| 时间 | 要回答的问题 | 结论 |
|---|---|---|
| 第 1 分钟 | Agent 手机负载为何不同？ | 长时会话、异构多阶段、可修订动作与主动观察，改变的是执行控制和状态生命周期 |
| 第 2 分钟 | CPU 还能做什么？ | 灵活控制 + 部分形状/精度 AI，但不能宣称 CPU 必胜 NPU |
| 第 3 分钟 | 具体投入哪些技术？ | LLVM lowering、SME/ZA ABI、CPU 微内核/packing、xPU 放置、QoE 五项接口 |
| 第 4 分钟 | 哪些是工程，哪些是创新 Bet？ | 三项工程平台优先，**零个已证实的独立 Agent 硬件 Bet** |
| 第 5 分钟 | 哪些存疑，管理层怎样决定？ | A/B/R2 条件储备，当前否决语义 ISA 等独立硬件预算，明确跨团队责任 |

## 需要领导讨论的三项选择

1. **方向优先级：** 是否以 CG-06、PT-A、C 为优先技术建设/协作方向，暂不设 Agent 专用 CPU-uArch Bet？
2. **组织所有权：** CPU/LLVM 团队宜主导 C1–C3；C4 需要 Runtime 协作；C5/可信动作和 NPU 管理主要为 Runtime、OS、Agent 平台所有权。**真实负责人、预算、人力未从公开资料获得，不在本报告中假定已经批准。**
3. **储备原则：** A/B/R2 以外部公开论文、专利与厂商技术披露为更新条件；本项目不开展自有实验、仿真、手机测试、PoC。

## 本包其他三份文件

- [技术所有权与三年决策矩阵](technical-matrix.md)：层级、强基线、技术边界与 2027–2029。
- [十四个技术质询及答辩](technical-qa.md)：支持、反证与不能夸大的证据。
- [九页学术型汇报提纲](slide-outline.md)：可供正式制作可编辑演示文稿；**本轮尚未创建 PPT**。

与完整报告、图谱、深读和原始链接保持一致。相关页面访问限制详见 [Round15G 来源审计](../../analysis/audits/round15g-final-source-and-ssot-audit-2026-10-08.md)。
