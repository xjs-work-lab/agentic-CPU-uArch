# Round15H — 九页学术型技术领导汇报提纲（不是 PPT 文件）

保持淡色、少修饰、学术感。每页一个判断、一个技术图或矩阵、原始出处和边界；尤其保留细小图标/术语布局的可编辑性。尚未生成演示文稿。

| 页 | 标题与推荐图形 | 该页必须说清的内容 | 关键出处 |
|---|---|---|---|
| 1 | **决策结论：3+3+0**；三栏对比 | 三优先工程/平台、三储备、零独立 Agent-uArch Bet；不是缺乏发展方向 | [正式组合](../current.md) |
| 2 | **Agent 工作负载四变化**；四段状态时间线 | 长会话、异构阶段、可修订动作、主动“必要时才帮助” | [15G 报告](../management-final-public-evidence-2027-2029.md) |
| 3 | **CPU-NPU 不是二选一**；原始论文对照矩阵 | PAPER-009 CPU/NPU crossover，llm.npu/ShadowNPU 优化反证，HeRo 动态 Agent DAG | [PAPER-009](../../01-evidence/papers/PAPER-009/deep.md)、[PAPER-057](../../01-evidence/papers/PAPER-057/deep.md)、[PAPER-098](../../01-evidence/papers/PAPER-098/deep.md) |
| 4 | **现有 SME2 的手机证据**；设备/模型/功耗口径表 | vivo X300 SqueezeSAM CPU 开关 SME2；SMEPilot 对不同设备的 CPU/SME 模型支持；无 NPU 同任务对照 | [TOOL-012](../../01-evidence/tools/TOOL-012/deep.md)、[PAPER-052](../../01-evidence/papers/PAPER-052/deep.md) |
| 5 | **五个可控技术抓手 C1–C5**；LLVM→Kernel→Runtime→OS 分层图 | 基本 ArmSME/LLVM/KleidiAI 已存在，核心是工程集成和目标场景适配 | [技术矩阵](technical-matrix.md) |
| 6 | **F/P/V 三主线**；基线/研究假设二维矩阵 | F 状态生命周期、P LP Admission、V 语义进度/QoE；三主线≠三硅片 Bet | [15G 报告](../management-final-public-evidence-2027-2029.md) |
| 7 | **正式投资/储备/Kill**；三列清单 | CG-06/PT-A/C vs A/B/R2；R1 Watch、R3 Blocked；旧 82.5 为历史 | [DEC-PORTFOLIO-002](../../08-decisions/events/DEC-PORTFOLIO-002.md) |
| 8 | **2027→2029 技术分层路线**；年×层矩阵 | 2027 现有 ISA 适配；2028 ABI/runtime/OS 契约；2029 条件性 CPU/SoC 研究保留 | [技术矩阵](technical-matrix.md) |
| 9 | **领导需决策什么＋证据边界**；三项决策问题 | 投入什么、谁负责、哪些不做；公开资料限制不写成已证明的硬件效益 | [来源审计](../../analysis/audits/round15g-final-source-and-ssot-audit-2026-10-08.md)、[答辩](technical-qa.md) |

**讲述红线：** 不把同学术研究组论文算成独立多次验证；不把 vendor claimed uplift 算为第三方 Agent 手机测量；不拼不同设备的 speedup；不宣称已批准内部预算；不承诺实验或 PoC。
