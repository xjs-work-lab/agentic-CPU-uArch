# 2027—2029 手机 Agentic AI：CPU 微架构、LLVM、异构 SoC 与 Runtime/OS 技术洞察详细研究终稿

- **文档用途：** 面向本地 Agent 的自包含研究输入源，用于生成技术领导汇报 PPT、逐页论证、图表设计与演讲者备注；也可供未参与本项目的研究人员独立理解结论。
- **研究对象：** 智能手机 Agentic AI 引起的工作负载变化，以及 CPU/uArch、LLVM/MLIR、AArch64、CPU↔GPU↔NPU、共享内存、OS/Runtime、可信工具执行和低功耗准入的技术应对。
- **时间范围：** 2027—2029 年技术路线规划。
- **综合稿日期：** 2026-10-20。
- **证据结题边界：** 本研究最终公开证据审计和正式结题状态截至 2026-10-09；本文件是对已归档成果的重新综合，不表示 2026-10-09 之后已完成新一轮全网检索或逐篇重新核验。
- **研究状态：** 公开证据范围内已结题；有明确证据边界；仅在出现可能改变技术决策的新公开原始证据时重开。
- **研究硬约束：** 仅使用公开论文、官方平台/工具文件、公开专利及厂商技术资料。项目没有执行、也不安排自有真机测试、benchmark、仿真、PoC、性能测量或未授权的外部合作。
- **阅读方式：** 关键结论、重要论文的设备/模型/基线/数值、适用范围、反证和决策门槛均写入正文。链接用于追溯原文和仓库证据卡，不应成为理解主结论的唯一途径。
- **权威性声明：** 本文是供汇报与本地 Agent 使用的综合研究底稿，不替代原始论文、正式 Claim/EvidenceCase 或 Decision Event。发生冲突时，以仓库的现行技术组合 [current.md](current.md)、正式决策 [DEC-PORTFOLIO-002](../08-decisions/events/DEC-PORTFOLIO-002.md)、[DEC-A-008](../08-decisions/events/DEC-A-008.md) 和结题验收 [final-research-archive-acceptance-2026-10-09.md](../00-project/final-research-archive-acceptance-2026-10-09.md) 为准。
- **汇报用语约束：** 使用“优先工程方向、平台能力、研究储备、跟进、暂不立项”等表述；避免把技术研究说成证券式“投资”。不得把条件储备写成已批准芯片项目，不得把未来年份写成厂商承诺的量产日期。

---

## 一、执行摘要：应做强现有软件与异构协同，不应在证据不足时发明 Agent 专用 CPU 硬件

### 1.1 总体结论

**2027—2029 年，Agentic AI 对手机 CPU 的主要影响不是让 CPU 取代 NPU，而是让系统从单次模型调用转向持续会话、动态多阶段异构执行、可信工具操作、状态修订和主动低功耗准入。CPU 的关键角色是可编程控制主机，以及在合适的算子、形状和精度条件下，利用现有 ISA 执行延迟敏感的控制或 AI 计算；真正的系统收益取决于 LLVM/微内核、NPU 软件栈、Runtime/OS、共享 DRAM 和前台体验之间的协同。**

公开证据支持三项优先工程/平台方向：

1. **CG-06：CPU + LLVM/AArch64 现有 ISA 的异构快速路径。** 重点是算子/阶段感知的编译与放置、微内核、数据布局复用、低开销调度，以及与优化 NPU 后端的公平比较。不能表述为“CPU 对 Agent 推理天然更快”，也没有证据支持新增 Agent 专用指令集。
2. **PT-A：可信 Agent 工具执行与结果验证。** 以软件/OS 为主，建立权限确认、操作目标的新鲜绑定、动作边界、真实效果回执、验证和有界恢复。普通权限、队列取消、缓存版本、事务回滚等能力已有大量软件/平台先例。
3. **C：异构 Runtime/OS 调度与前台 QoE。** 对动态工作流 DAG、阶段关键路径、xPU 亲和性、模型准入、共享 DRAM 争用和前台交互体验进行系统级控制。已有 Agent-aware 手机调度研究与 Android 平台机制构成强基线。

**同时，当前公开证据支持的新增、独立、差异化 CPU/uArch Primary Bet 数量是 0。** 这不是说 CPU 技术不重要，而是说现有证据足以支持做强软件和平台能力，却不足以证明某种新的 Agent 专用 CPU 指令、缓存结构、预测器、TLB 状态或硅片机制在强软件基线之上具有不可替代的手机收益。不能为了凑满 2—3 个名额，把普通编译优化或 Runtime 功能重新命名成硬件创新。

三项条件研究储备为：

- **A：** 完整可观察工作流状态之外，Agent 私有 RequiredProgress 信息是否仍有独立、不可重建且能改变最优决策的价值。
- **B-residual：** 跨 CPU/NPU/内存引擎的派生状态是否存在普通软件版本化、来源追踪、缓存失效和 OS Runtime 机制无法解决的物理生命周期成本。
- **R2：** CPU 任务继续执行时，是否存在软件亲和性、普通共享缓存、核心迁移与现有缓存机制无法吸收、且对手机用户体验足够重要的 continuation locality 物理残差。

其他状态：R1 为 WATCH；CG-07 为低功耗平台 FOLLOW/EXPLORE；CG-01 为跟踪竞争对手公开共享缓存与核心迁移能力；R3 新增 Agent 语义硬件 Hint/ISA 为 BLOCKED。

### 1.2 给技术领导的决策表

| 类型 | 当前正式方向 | 主要技术责任 | 当前证据能支持什么 | 不能据此声称什么 |
|---|---|---|---|---|
| 优先工程 1 | CG-06：CPU/LLVM/AArch64 异构快速路径 | 编译、微内核、现有 ISA、算子放置、数据布局和 CPU↔NPU 合同 | 真实手机上存在 CPU/NPU 阶段差异；现有 SME2 可加速特定 CPU 工作负载；优化 NPU 软件栈也能大幅改善执行 | CPU 永远胜过 NPU；SME 是独立于 CPU 的处理器；新 Agent ISA 必要 |
| 优先工程 2 | PT-A：可信 Agent 动作 | Agent Runtime、OS 权限、目标确认、结果验证与恢复 | 可信动作是产品系统的必要能力；现有软件与平台接口已覆盖大量控制逻辑 | 该能力需要专用 CPU 指令或独立硅片 |
| 优先工程 3 | C：异构系统调度与前台 QoE | Runtime/OS、CPU/GPU/NPU、DAG、DRAM、准入与优先级 | 商用手机 Agent 工作流调度有公开结果；背景 LLM 可影响前台体验；OS/NPU 管理机制已是重要基线 | 某种新硬件调度器已证明优于最强软件调度 |
| 条件储备 1 | A：私有 RequiredProgress | Agent 语义信息与可观察状态之间的剩余差异 | 可以提出可证伪的信息增量假设 | 该信息已证明不可由软件重建，或已证明能带来手机级收益 |
| 条件储备 2 | B-residual：跨引擎派生状态物理有效性 | 缓存/状态版本、跨 xPU 生命周期、内存/队列与恢复 | 版本与有效性是系统问题 | 普通软件状态、事务与共享缓冲不足，或必须新增硬件 |
| 条件储备 3 | R2：CPU continuation locality | 任务迁移、共享缓存、热状态/工作集保持 | 手机 CPU 的延续执行局部性可能值得进一步跟踪 | 已证明需要专用缓存/预测器/TLB 硬件 |
| 跟进 | CG-07、CG-01、R1 | 低功耗传感、共享缓存、通用 deadline/wakeup 与语义释放 | 这些领域已有平台与竞争者动向 | 跟进项等于新增立项或已验证差异化 |
| 暂不立项 | R3 及泛化 Agent-only ISA/uArch | 无 | 当前证据不支持新颖性和硬件必要性 | 不等于放弃软件功能或停止跟踪行业 |

### 1.3 三条最重要的管理含义

1. **把“工作负载变化”与“新硬件必要性”分开。** Agent 让手机软件工作流更动态，并不自动证明要新增 CPU 硬件。
2. **必须用最强的可公开软件基线比较。** 不能只比较默认 CPU 路径与未经优化的 NPU 后端；llm.npu、ShadowNPU、HeRo、LAS、ProgRouter、Android NPU Manager、LLVM/SME2 和现有 OS/Runtime 都会压缩宽泛硬件主张的空间。
3. **缺少公开硬件证据时，可以带边界结题。** 本研究不做自有实验，因此 FQ4 的硬件因果缺口需要诚实记录，但不意味着要无限期保留一个未被证据支持的硬件主押注。

---

## 二、研究目标、问题与边界

### 2.1 项目要回答的核心问题

本研究不是“搜集 Agent CPU 论文”，而是回答：

> 到 2027—2029 年，智能手机 Agentic AI 会引起哪些重要的用户体验与工作负载变化？在强现有 CPU/LLVM、NPU 软件栈、Runtime/OS 和共享内存基线之上，团队应优先建设哪些可控技术能力，保留哪些条件研究，哪些新增 CPU/uArch 方向目前不应立项？

### 2.2 最终七问（FQ1—FQ7）

| 编号 | 最终问题 | 结题状态 | 本文给出的答案 |
|---|---|---|---|
| FQ1 | 2027—2029 年哪些手机工作负载/用户体验变化最重要？ | CLOSED_WITH_BOUNDARY | 四项结构变化：持续会话与可信行动、反复异构阶段交接、可修订状态、主动低功耗准入；渗透率与每家 SoC 的具体成本仍不确定 |
| FQ2 | 学术与产业界已有哪些成熟方案和先前技术？ | CLOSED_WITH_BOUNDARY | 已审阅决策相关论文、官方工具/平台和三项专利权利要求；不宣称世界文献或专利族穷尽检索 |
| FQ3 | 哪些跨层技术主题最值得组织团队关注？ | CLOSED | F 执行与状态生命周期、P 主动低功耗准入、V 语义进度/QoE；它们是跨层主题，不是三项硅片项目 |
| FQ4 | 强软件基线下还有什么 CPU/SoC/uArch 机会？ | CLOSED_WITH_EVIDENCE_GAP | CPU/LLVM 现有 ISA 有具体工程价值；新增 Agent-only CPU 硬件的独立因果价值未被公开资料证明 |
| FQ5 | 哪些方向优先、储备、跟进或暂不立项？ | CLOSED | CG-06/PT-A/C 三项优先工程/平台；A/B-residual/R2 三项储备；R1 WATCH、CG-07 FOLLOW/EXPLORE、CG-01 BENCHMARK、R3 BLOCKED；独立硬件 Primary Bet 为 0 |
| FQ6 | 2027/2028/2029 应怎样分阶段安排技术路线？ | CLOSED_WITH_BOUNDARY | 已形成按 CPU/LLVM、Runtime/OS、内存状态、可信工具和低功耗分层的建议；不是批准的人力、预算或量产排期 |
| FQ7 | 哪些证据足以区分竞争假设并支撑结论？ | CLOSED_WITH_BOUNDARY | 对决策关键来源做过直接审阅、独立性与链接审计；不是每个外部 URL 当日可访问、不是完整 FTO，也不是自有实验验证 |

### 2.3 范围与排除项

- **主要平台：** 智能手机，重点 AArch64 移动 SoC；平板只在能够说明手机技术方向时作为辅助。
- **覆盖层次：** CPU 微架构与缓存、AArch64 ISA/SME2、LLVM/MLIR、CPU/NPU/GPU 执行分工、共享 DRAM、模型运行时、Android/iOS 平台接口、Agent 工具权限与结果核验、Always-on/低功耗准入。
- **证据类型：** 原始论文、会议/期刊论文、官方 SDK/OS/编译器文档、厂商技术披露、公开专利权利要求与已发表实验。
- **不做：** 自有设备测试、benchmark、仿真、PoC、外部合作、未授权数据获取、专利自由实施（FTO）法律意见。
- **不做的预测：** 不给出 Agent 手机普及率的确定数值，不断言某厂商某年必定量产某种 CPU 结构。
- **术语约束：** SME/SME2 是 Arm CPU 可执行的指令集扩展，不应在图中与 CPU 核作为同级处理器并列；若表达资源分工，应写“CPU 核内部的常规向量执行与 SME/SME2 矩阵能力协作”。

### 2.4 证据等级

| 标签 | 含义 | 写作规则 |
|---|---|---|
| **[FACT / 公开事实]** | 原始论文、官方文件或专利原文明确披露的内容 | 写明来源、测试对象、基线、测量指标与限制 |
| **[OBSERVATION / 观察]** | 多个事实之间的模式或值得关注的现象 | 不升级成因果结论 |
| **[INFERENCE / 跨来源推断]** | 结合多个独立来源得出的技术判断 | 明确说明推断链和可能替代解释 |
| **[HYPOTHESIS / 假设]** | 仍需新公开证据才能区分的机制 | 不写成既成事实或已批准项目 |
| **[NOT ESTABLISHED / 未证实]** | 当前公开资料不能支持的结论 | 必须在对应章节或图表中保留边界 |
| **[DECISION / 正式决策]** | 已记录的技术组合选择 | 以正式决策事件为准，不用历史评分替代 |

---

## 三、Agentic AI 为什么会改变手机执行模式

### 3.1 四项结构变化

#### T1：持续会话与可信行动

Agent 不只是一次提示词后生成文本。它可能维护上下文，跨应用调用工具，读取返回状态，再决定下一步；同时需要确认用户权限、操作对象、目标 App/窗口是否仍然有效，并核验动作是否真的产生了预期效果。

- **用户侧变化：** 任务跨多个步骤、应用和时间段；错误可能来自目标选错、权限失效、操作未完成或重复执行。
- **系统侧变化：** 需要会话/状态管理、CPU 控制路径、工具权限、目标绑定、结果回执与有界恢复。
- **证据边界：** Apple Foundation Models 的 LanguageModelSession 和工具接口是公开产品能力；这说明软件会话/工具控制正在出现，不证明需要 Agent 专用 CPU ISA，也不保证所有设备具有相同实现。

#### T2：CPU↔NPU/GPU 多阶段反复执行

典型工作流可能在模型 Prefill、Decode、检索、重排、分类、工具执行、结果校验之间反复切换。不同阶段的张量形状、精度、算子覆盖、内存访问和延迟约束都不同。

- **用户侧变化：** 端到端等待时间不只由一次大模型计算决定；短阶段的启动、同步、数据布局和前后台争用也可能影响响应。
- **系统侧变化：** 从固定“把模型扔给某个加速器”转向阶段级/子图级动态调度。
- **证据边界：** 手机论文已经观察到阶段/算子依赖的 CPU/NPU 交叉点和 Agentic RAG 动态工作流；具体赢家随设备、后端、模型与软件版本变化。

#### T3：可修订、可中断的动作与派生状态

Agent 可能改写计划、取消任务、重试、切换模型或回滚外部操作。中间产物包括 KV、缓存、检索结果、模型输出和外部工具状态；这些对象必须有版本、来源、权限和有效期。

- **用户侧变化：** 不应把旧结果当成当前结果，也不应把“模型输出成功”当成“外部动作已完成”。
- **系统侧变化：** 软件层先建立状态版本化、取消/恢复、来源追踪、事务合法性与内存生命周期合同。
- **硬件边界：** 只有证明这些状态在跨 CPU/NPU/内存引擎时存在软件不能吸收的物理成本，才可继续讨论专用硬件；普通缓存、事务、版本化不是新硬件的充分理由。

#### T4：主动感知与“正确地不行动”

后台感知可能触发“是否值得打扰用户”的判断。高质量系统不应仅追求更多触发，而应控制误报、漏报、隐私、唤醒次数和整日能耗。

- **系统侧变化：** 事件门控、上下文许可、低功耗域、共享 NPU 与主 SoC 的唤醒策略。
- **现有基线：** Android CHRE、Apple AOP、Qualcomm Sensing Hub、MediaTek 低功耗 AI 等是必须跟踪的产品/平台路线。
- **证据边界：** “Agent”产品宣传不证明专用低功耗硬件相对于现有感知域具有额外收益。帮助率调整后的整日能耗、隐私与误触发成本仍缺少统一的跨厂商比较。

### 3.2 Agent 工作流的示意结构

可将典型工作流抽象为：

用户意图与上下文 → Agent 计划/工具路由 → 检索/重排/分类/小模型阶段 → 大模型 Prefill/Decode → 工具调用 → 结果验证 → 状态更新/继续/取消/恢复。

实际执行图是动态 DAG：有些步骤可以并行，有些步骤依赖前一步结果；部分阶段由 CPU 执行，部分阶段由 GPU/NPU 执行；不支持的算子或不满足精度要求的残差也可能回到 CPU/GPU。这个图是概念结构，不代表所有产品都按相同流程执行。

### 3.3 为什么不能只比较单次算子峰值

一个阶段的端到端时间可概念化为：

\[
T_{\mathrm{stage}} =
T_{\mathrm{compute}}+
T_{\mathrm{launch}}+
T_{\mathrm{sync}}+
T_{\mathrm{layout/copy}}+
T_{\mathrm{fallback}}+
T_{\mathrm{queue/contention}}
\]

该式是帮助拆分成本的会计框架。真实测量时各项可能重叠，不能在未定义边界的情况下简单相加；它也不是任何一篇论文的统一实测模型。

如果只把其中的计算项加速，而启动、同步、格式转换、CPU 回退或 DRAM 争用仍然存在，端到端收益可能很小。

Amdahl 定律可用于说明局部加速的限制：

\[
S_{\mathrm{total}}=\frac{1}{(1-p)+p/s}
\]

其中 \(p\) 是原始总时间中被优化部分的占比，\(s\) 是该部分的加速比。它只用于解释“局部更快不等于整体大幅更快”，不能替代具体手机工作流的测量。

---

## 四、关键技术概念与必要公式

### 4.1 Prefill 与 Decode 不是同一种工作负载

- **Prefill：** 模型处理输入上下文，输入 token 较多，通常涉及大块矩阵计算、注意力和较大张量；长上下文 Agent 任务可能使它成为主要延迟来源。
- **Decode：** 逐步生成输出 token，常涉及反复执行较小的矩阵向量计算、KV 访问和内存流量；单步计算快不等于整体输出阶段一定快。
- **Attention：** Transformer 中的注意力计算。不同系统可能把部分 Attention 留在 CPU/GPU、把低精度的“重要性估计”放到 NPU，再把少量高精度残差交给 CPU/GPU。不能笼统说“Attention 都给 CPU/GPU”或“Attention 都给 NPU”。
- **CPU fallback（CPU 回退）：** 当某个算子/子图不受 NPU 后端支持、形状不匹配或精度要求不允许当前 NPU 路径时，该部分转到 CPU 执行。代价可能包括 CPU 计算、内存复制、同步、数据重排、精度转换和再次交接。它不表示 NPU 故障，也不表示整模型都回退。
- **xPU：** 在本项目语境中泛指 CPU/GPU/NPU 等执行处理单元；是一个系统级统称，不是新的处理器类型。
- **SME/SME2：** Arm Scalable Matrix Extension / 第二代扩展，属于 CPU 架构可执行的指令集能力。SME 资源不能与 CPU 核作为对等芯片在图中并列；合理表达是“CPU 核利用 SME2 完成矩阵阶段，并与同一 CPU 核上的常规向量/标量阶段协同”。
- **LLVM/MLIR：** 编译器基础设施。MLIR 的 Linalg/ArmSME 等已有变换路径，LLVM 的 AArch64 SME 文档定义 ABI、函数属性和状态约束；这是可用的软件基线，不是 Agent 专属功能。
- **静态 NPU 图：** 预先编译的计算图通常要求相对固定的形状、算子和量化形式。通过图分桶、分块和残差分解可以提高覆盖，但仍需考虑准备开销、内存占用和工作流变化。
- **DRAM 争用：** 多个 CPU/GPU/NPU 或前后台工作共享内存带宽时，后台模型可能让前台应用卡顿，即使后台模型本身吞吐损失很小。

### 4.2 Roofline 与 CPU/SME 算子分工

Roofline 模型给出一个常用的性能上界：

\[
P \leq \min(P_{\mathrm{peak}}, B_{\mathrm{mem}}\times I)
\]

其中 \(P\) 是实际计算性能，\(P_{\mathrm{peak}}\) 是计算峰值，\(B_{\mathrm{mem}}\) 是可用内存带宽，\(I\) 是算术强度（每搬运一个字节对应的运算数）。这说明算子并不总是由峰值矩阵吞吐决定；低算术强度、布局转换和内存流量可能成为瓶颈。

SMEPilot 的意义在于：对每个算子根据形状、算术强度和布局选择 CPU-only、SME-only 或 CPU+SME 协作，并通过 tile 分区、阶段流水和打包数据复用改善 CPU 内部资源使用。这里的“协作”发生在 CPU 内部执行资源之间，不是 SME 与 CPU 核作为两颗处理器协作。

### 4.3 动态 DAG 与前台体验

对于依赖图 \(G=(V,E)\)，端到端最短可能时间通常受关键路径限制，而不是所有节点耗时的简单平均：

\[
T_{\mathrm{workflow}}\geq
\max_{\pi\in\mathrm{Paths}(G)}
\sum_{v\in\pi} T_v
\]

当节点共享 DRAM、缓存、NPU SRAM、CPU 核或模型驻留资源时，\(T_v\) 还受并发与资源争用影响。该表达是调度概念，不是 HeRo 或 SERENO 论文的统一原始公式。

### 4.4 A 方向：私有 RequiredProgress 信息的可证伪假设

A 的关键不是“语义信息很重要”——语义摘要、验证结果、任务进度、历史记录和模型收益预测已经可以在软件中获得。需要检验的是：当两种状态在完整软件可观察状态下几乎相同时，Agent 内部的 RequiredProgress 是否仍提供不可由软件重建、且能改变正确决策的信息。

概念上可表达为：

\[
\Delta V =
\mathbb{E}[U\mid O,R]-
\mathbb{E}[U\mid O]
\]

其中 \(O\) 是完整可观察状态（工作流账本、历史、权限、验证、任务阶段、模型收益等），\(R\) 是声称额外的私有 RequiredProgress，\(U\) 是在相同质量/权限/延迟/能耗约束下的决策效用。这个式子只是研究假设的表达，不能将 \(\Delta V\) 写成已测得的正数。现有公开研究尚未完成严格的同观测条件对照。

---

## 五、最强现有基线地图：新增硬件主张必须跨过哪些门槛

| 基线领域 | 代表公开来源 | 已经能做什么 | 对新硬件主张的约束 |
|---|---|---|---|
| 手机 CPU/NPU 阶段交叉 | PAPER-009, When NPUs Are Not Always Faster | 证明在特定 Snapdragon 栈上 Prefill/Decode 的 CPU/NPU 收益不同 | 说明“默认 NPU 全包”不总是最佳；但不能推出 CPU 永远更快 |
| NPU 图重构与量化/精度分工 | PAPER-059, llm.npu | 通过 chunk-sharing graph、outlier residual、子图调度提升 NPU 利用率 | 必须用优化 NPU 后端作为比较对象，不能只打败默认后端 |
| NPU 低精度注意力估计 + 高精度稀疏残差 | PAPER-057, ShadowNPU | 让 NPU 执行容忍低精度的 token 重要性估计，CPU/GPU 处理少量高精度残差 | “Attention 必须由 CPU 执行”或“Attention 全部无法上 NPU”都不成立 |
| CPU 内部现有 ISA 协同 | PAPER-052, SMEPilot；TOOL-012, vivo X300 SME2 | 现有 SME2、布局、微内核和调度可以显著改善特定 CPU 工作负载 | 先做强现有 ISA 和编译路径，再讨论新增指令 |
| 动态 Agentic RAG 手机调度 | PAPER-098, HeRo | 在商用手机上按阶段亲和性、形状、部分依赖和 DRAM 争用调度 | 静态单引擎/单模型基线不足；必须与动态异构软件调度比较 |
| 前后台共享内存争用 | PAPER-003, SERENO | 商用手机上，背景 LLM 的内存带宽压力可能伤害前台 QoE | QoE 问题真实，但不自动意味着需要 Agent 专属硬件 |
| Agent 工作流质量/成本控制 | PAPER-119, LLM-as-Scheduler；PAPER-121, ProgRouter | 从产物验证、工作流账本、语义摘要、模型收益和预算状态做软件路由 | 泛化“语义进度提示”已被软件基线挤压；必须证明不可重建的残余 |
| 长期用户历史的主动帮助 | PAPER-044, ProAgentBench | 真实连续历史比合成样本能改善何时/如何帮助的预测 | 私有 NeedState 需要超越历史与上下文基线，而不是重复它们 |
| OS/Runtime 资源控制 | VENDOR-027 Android NPU Manager；VENDOR-029 Qualcomm QNN shared buffer | 已有模型准入、优先级、状态/缓冲接口和平台管理路线 | 通用优先级、取消、共享缓冲、模型生命周期不是新颖硬件本身 |
| 会话与工具平台接口 | VENDOR-032 Apple Foundation Models | 会话 transcript、工具调用和上下文管理已有产品 API | Agent 软件价值不等于 CPU 硬件差异化 |
| 语义缓存与事务专利先例 | PATENT-032、PATENT-033 | 公开申请覆盖部分对话/推理缓存有效性、任务结果/事务回滚思路 | 宽泛“语义缓存/事务/回滚是全新”的说法需收窄；不构成 FTO 结论 |

### 5.1 证据独立性原则

- llm.npu 与 ShadowNPU 有持续的作者/研究团队谱系，是优化 NPU 软件路线的连续发展，不应计作两次完全独立的复制验证。
- HeRo 与 Agent.xpu 有作者/研究组谱系，能够支持 Agent 工作流异构调度的技术路线，但不是完全独立的生态普查。
- PyTorch/Arm SME2 官方博客包含工具/厂商作者，是真实手机技术数据，但不是独立第三方的 Agent 端到端 benchmark。
- 官方平台文档证明 API/能力被公开描述，不等于所有量产手机都启用相同功能，更不等于独立测得系统收益。
- 专利公开申请不是产品部署证据，不是有效性判决，不是自由实施（FTO）意见。

---

## 六、核心论文深入分析 I：手机 CPU/NPU 交叉点与现有 CPU ISA

### 6.1 PAPER-009 — When NPUs Are Not Always Faster

- **原始来源：** arXiv:2605.27435，https://arxiv.org/abs/2605.27435
- **设备：** Snapdragon 8 Gen 3 手机，Hexagon v75 NPU。
- **问题：** 为什么把更多 LLM 工作交给 NPU，不一定缩短端到端延迟或降低能耗？
- **方法：** 将 Prefill、Decode、算子计算、通信/调度和 fallback 分开测量，而不是把“LLM 推理”当成单一阶段。
- **代表结果（限论文测试栈）：**
  - NPU Prefill 路径在被测条件下比 6 核 CPU 慢约 **1.27—1.62×**。
  - Decode 的核心 MUL_MAT 算子由 NPU 执行时，延迟约低 **1.55—1.67×**。
  - NPU 路径通信开销约占 **9.9%—13.0%**。
  - 被测 fallback 路径的相对惩罚约 **1—1.5×**，具体依论文路径定义。
  - Llama-3.2-3B 的电池消耗实验报告，在更长输入/更高程度 NPU offload 条件下耗电增加约 **22%、32%、51%**（对应论文列出的不同 prompt 长度/配置；不能当作所有手机通用倍率）。
- **机制：** 算子/阶段形状、后端支持、精度转换、CPU↔NPU 调用、数据搬运、同步和 fallback 会改变赢家。Decode 中单个矩阵向量算子更快，并不保证完整 Decode 或整次任务同幅度加速。
- **能支持的结论：** 在该代设备/软件栈上，CPU/NPU 的优劣依阶段与实现而变；不能只按理论吞吐量决定放置。
- **不能支持的结论：** Prefill 本质上永远属于 CPU；所有 Attention 都应放 CPU/GPU；下一代 NPU 仍有相同交叉点；CPU 因为“Agent 语义”而必然更快。
- **对路线的作用：** 为 CG-06 提供阶段级交叉点的直接手机证据，也提醒必须把优化 NPU 软件栈作为更强基线。
- **原文与仓内深读：** [arXiv 原文](https://arxiv.org/abs/2605.27435) · [PAPER-009 完整证据卡](../01-evidence/papers/PAPER-009/deep.md)。

### 6.2 PAPER-052 — SMEPilot

- **原始来源：** arXiv:2606.16332，https://arxiv.org/abs/2606.16332
- **平台：** Apple M4 Pro CPU、MediaTek Dimensity 9500 手机 SoC、KunPeng 920 服务器 CPU。
- **模型/工作负载：** Llama-3.2-3B、Qwen3-4B、Qwen3-30B-A3B（大 MoE 配置使用 4-bit 权重），包括长上下文、问答与长生成。
- **基线：** llama.cpp 默认 CPU 后端。
- **核心机制：** 根据算子形状与算术强度，在 CPU-only、SME-only、CPU+SME 三种模式之间选择；使用 tile 级分区提升空间利用率，用 CPU 向量/softmax 阶段与 SME 矩阵阶段重叠，离线路径打包静态权重并复用运行时布局。
- **量化结果：**
  - 报告的配置中端到端速度提升最高 **3.94×**；这是“最高值”，不是所有设备/模型平均提升。
  - 去掉 tile partition 后，GEMM 延迟增加 **1.46×**。
  - 去掉 Attention pipeline 后，Prefill Attention 延迟增加 **2.07×**。
  - 将 packing 放在运行时关键路径中的一个 Decode GEMV 案例，延迟由 **0.52 ms 增至 1.71 ms**。
  - Apple M4 Pro 上 Qwen3-4B/Ruler-4K 的能耗由 **482.813 J 降至 233.931 J**，约为原基线的 **0.485×**。
  - Apple M4 Pro 上的 GPU 对照结果约为 SMEPilot 性能的 **0.72—0.96×**（限论文给出的对应配置）。
- **关键解释：** 该论文证明现有 CPU 内部矩阵扩展、运行时调度和布局复用有很大优化空间；SME 是 CPU 指令集扩展，CPU 核通过执行 SME 指令完成矩阵计算。
- **重要边界：** 能耗结果来自 Apple M4 Pro，不应称为手机能耗；论文没有直接比较同一手机上的优化 NPU，也不是 Agent 端到端实验。它支持 CG-06 的软件/编译工程价值，不支持新 Agent ISA 的必要性。
- **原文与仓内深读：** [arXiv 原文](https://arxiv.org/abs/2606.16332) · [PAPER-052 证据卡](../01-evidence/papers/PAPER-052/deep.md)。

### 6.3 TOOL-012 — ExecuTorch + Arm SME2 on vivo X300

- **原始来源：** PyTorch 官方博客，https://pytorch.org/blog/accelerating-on-device-ml-inference-with-executorch-and-arm-sme2/
- **设备/模型：** vivo X300 手机，SqueezeSAM 视觉分割模型；ExecuTorch + XNNPACK + KleidiAI。
- **单 CPU 核：**
  - INT8：**555.8 ms → 304.1 ms**。
  - FP16：**1163.0 ms → 298.2 ms**。
- **四 CPU 核：**
  - INT8：**195 ms → 180 ms**。
  - FP16：**374 ms → 193 ms**。
- **数据搬运占比：** SME2 路径 INT8 约 **125.8 ms / 41.4%**，FP16 约 **119.1 ms / 39.9%**。
- **能支持的结论：** 现有手机 CPU SME2 结合编译/内核库，能显著加速该视觉分割模型的特定 CPU 执行路径；数据移动仍是重要成本。
- **不能支持的结论：** 这是 Agent 模型、是 CPU 与 NPU 的对照、SME2 一定对所有工作负载有效。作者包含 Arm/框架生态参与者，因此不是独立的 Agent 系统评测。
- **对路线的作用：** 这是 CG-06 最直接的“手机上现有 ISA + 软件栈值得做强”证据之一。
- **仓内来源卡：** [TOOL-012](../01-evidence/tools/TOOL-012/README.md)。

### 6.4 LLVM/MLIR 现有能力与工程切入点

公开官方工具链资料已覆盖：
- LLVM AArch64 SME 的 ABI、函数属性、PSTATE.SM 和 ZA 状态约束；
- MLIR ArmSME 的矩阵运算路径，例如从 Linalg 表达转换为 SME FMOPA；
- MLIR Linalg 的 tiling/fusion/vectorization 等通用变换；
- LLVM vectorizer 的成本模型；
- Arm KleidiAI 的现有微内核实现。

因此 CG-06 的优先工程任务应落在：形状/精度感知的 lowering、packing 与布局复用、算子融合、关键路径内的同步/数据搬运、CPU↔NPU 放置与可移植接口，而不是宣称“需要新 Agent ISA”。公开文档没有给出所有手机的 SME 状态切换微秒开销；本研究不能编造这个数值。

官方参考：[LLVM AArch64 SME](https://llvm.org/docs/AArch64SME.html)、[MLIR ArmSME](https://mlir.llvm.org/docs/Dialects/ArmSME/)、[MLIR Linalg](https://mlir.llvm.org/docs/Dialects/Linalg/)、[LLVM Vectorizers](https://llvm.org/docs/Vectorizers.html)、[Arm KleidiAI](https://github.com/ARM-software/kleidiai)。

---

## 七、核心论文深入分析 II：优化 NPU 软件栈会持续改变 CPU 的可用空间

### 7.1 PAPER-059 — Fast On-device LLM Inference with NPUs（llm.npu）

- **发表：** ASPLOS 2025。
- **DOI：** 10.1145/3669940.3707239；[arXiv](https://arxiv.org/abs/2407.05858)；[artifact DOI](https://doi.org/10.5281/zenodo.14392760)。
- **设备：** Xiaomi 14、Redmi K60 Pro/K70 级 Snapdragon 手机平台。
- **模型：** Qwen1.5-1.8B、Gemma-2B、Phi-2-2.7B、Llama-2-7B、Mistral-7B。
- **Agent 相关工作负载：** DroidTask UI 自动化、LongBench 上下文邮件回复、Persona-Chat 摘要等。
- **问题：** 手机 LLM 的 Prefill 常占总延迟大头；静态 NPU 图、动态 prompt 形状、按组量化和 FP Attention/Norm 等限制了简单 offload。
- **方法：**
  1. Prompt 层：把可变 prompt 分成固定 chunks，复用预建静态图并共享与 prompt 长度无关的算子；
  2. Tensor 层：NPU 处理快速 INT8 MatMul，将稀疏激活 outlier 交给 CPU/GPU 并行执行；
  3. Block 层：按亲和性与精度敏感性安排 CPU/GPU/NPU 子图，在线调度以减少 NPU stall。
- **报告的代表性结果：** 平均 Prefill 加速 **22.4×**、能耗节省 **30.7×**，以及最高端到端应用加速 **32.8×**（均为论文特定模型、设备和基线下的结果，不可跨设备外推）。
- **为什么重要：** 它表明优化 NPU 后端的软件重构可以把大量原先留在 CPU/GPU 的工作转移到 NPU，CPU 机会不是静态不变的。
- **不能声称：** 所有阶段都由 NPU 执行、所有模型都获得同样倍率、NPU 普遍优于 CPU、CPU 硬件没有价值。
- **独立性：** 与 ShadowNPU 属于持续的研究团队/技术路线，不能将两篇当作两次完全独立复现。
- **决策意义：** CG-06 必须对照优化 NPU 的真实 frontier，而不是只对照默认 NPU 运行时。
- **仓内深读：** [PAPER-059](../01-evidence/papers/PAPER-059/deep.md)。

### 7.2 PAPER-057 — ShadowNPU: System and Algorithm Co-design for NPU-Centric On-Device LLM Inference

- **发表：** ACM MobiSys 2026。
- **作者：** Wangsong Yin、Daliang Xu、Mengwei Xu、Gang Huang、Xuanzhe Liu；北京大学与北京邮电大学研究线。
- **来源：** [arXiv:2508.16703](https://arxiv.org/abs/2508.16703)、[ACM DOI](https://doi.org/10.1145/3745756.3809205)、[Zenodo artifact](https://zenodo.org/records/19555734)；论文的 artifact 状态标为可用且通过功能评估。
- **设备：** Xiaomi 14 / Snapdragon 8 Gen 3、Redmi K60 Champion Edition / Snapdragon 8 Gen 2。
- **模型/数据集：** Qwen2-0.5B/1.5B、PhoneLM-0.5B/1.5B；ArxivSum、DroidCall、Octopus。
- **问题：** 完整 Attention 直接转到 NPU INT8，在论文评估的模型/任务上平均损失约 **18 个百分点**的准确率；留在 CPU/GPU 又会消耗通用处理资源。
- **机制：** 利用一个重要的不对称性——“找出重要 token 的相对排序”比“精确计算全部 Attention 输出”更能容忍低精度。NPU 执行 INT8 重要性估计；CPU/GPU 对选中的小部分 token 做 top-k 和高精度稀疏残差计算。系统还使用 fused NPU head launch、head-wise 流水、按图形/形状分桶，以及资源隔离。
- **关键边界：**
  - 该系统的默认对照仅允许一个中等 CPU 核执行残差/控制工作，目标是 NPU-centric 执行；
  - 主要替换的是 Prefill Attention；论文所述 Decode 设计仍把完整 Attention 留在 CPU/GPU；
  - 论文不是“所有 Attention 都搬到 NPU”，而是对 Attention 内部不同计算阶段做精度与执行位置分工。
- **报告结果：** 论文报告的跨模型/数据集平均准确率指标中，ShadowNPU 为 **36.4**，NPU-Full 为 **18.8**；相对于使用 4 个 CPU 核/GPU 的 llm.npu 原生 Attention 路径，报告最高约 **3.0×** 更低延迟；某些模型条件下报告最高约 **7.66×** 更低能耗。所有“最高值”均依论文配置，不能写成普遍收益。
- **能支持的结论：** 优化 NPU 的算法与系统软件正在重新争取原本落在 CPU/GPU 的计算；精度容忍、稀疏残差与调度能改变执行位置。
- **不能支持的结论：** CPU 对所有 Attention 都更好；NPU 无法做 Attention；Agent 需要新 CPU ISA；这篇与 llm.npu 是独立的两次复现。
- **仓内深读：** [PAPER-057](../01-evidence/papers/PAPER-057/deep.md)。

### 7.3 NPU 软件 frontier 对 CG-06 的具体约束

CG-06 应当按真实阶段与工作负载进行工程化，而不是把“CPU 路径”视为固定业务。对每种任务至少要明确：
- 模型、prompt 长度、输出长度、精度和算子形状；
- CPU/NPU/GPU 端的实际算子覆盖；
- 静态图构建与分桶成本；
- CPU fallback 的执行时间、内存复制、同步与格式转换；
- 端到端延迟、总能耗与前台 QoE 的测量口径；
- 数据布局与 KV/激活复用；
- 持续运行时热限制与后台争用。

本项目没有执行这些测试；上面是未来若获得授权后的证据要求，不是已经安排或执行的实验计划。

---

## 八、核心论文深入分析 III：Agent 工作流调度与前台 QoE

### 8.1 PAPER-098 — HeRo: Adaptive Orchestration of Agentic RAG on Heterogeneous Mobile SoC

- **来源：** [arXiv:2603.01661](https://arxiv.org/abs/2603.01661)；作者团队的 IF-Lab 发表页面列为 DAC 2026。公开审计未把这条记录扩展为所有出版元数据都已独立复核。
- **平台：** 商用 Snapdragon 手机；Redmi K80（12 GB LPDDR5X）和 OnePlus 13（24 GB LPDDR5X）。
- **问题：** Agentic RAG 不是固定的“检索→生成”两步。Agent 可能重写查询、拆分子问题、进行多次搜索、重排文档、追加/跳过阶段，导致执行图动态生成。
- **机制：** 从单模型算子放置升级为工作流 Stage/Sub-stage 调度，显式考虑阶段与 PU 的亲和性、工作负载形状、共享 DRAM 争用与部分未来依赖。
- **基线：** Powerserve-NPU、GPU-only 或 NPU-only、静态多 xPU 映射及相关异构系统方法；仍未完整覆盖所有最强通用动态调度器。
- **报告结果：** 论文中的两个消融案例，基线约 **5.79 s → 3.82 s（1.52×）**，以及 **17.23 s → 5.38 s（3.20×）**。这两组数字对应各自案例和基线，不是全任务平均速度提升。
- **限制：** 报告主要看单查询平均延迟，不等同于真实前台应用并发时的完整 QoE/电池数据；部分异常延迟样本按论文方法过滤；HeRo 与 Agent.xpu 存在作者/研究组谱系。
- **结论：** 动态 Agent 工作流在商用手机上的系统级调度有公开证据；C 的 Runtime/OS 工程方向有现实依据。但“调度有效”不等于已经证明新硬件调度器必要。
- **仓内深读：** [PAPER-098](../01-evidence/papers/PAPER-098/deep.md)。

### 8.2 PAPER-003 — SERENO: Taming Memory Bandwidth Contention in Mobile LLM Inference

- **发表：** OSDI 2026。
- **作者：** Tong Xin、Xinrui Shi、Mingkai Dong、Zeyu Mi；IPADS / 上海交通大学研究线。
- **原始来源：** [USENIX PDF](https://www.usenix.org/system/files/osdi26-xin.pdf)。
- **设备：** OnePlus 13 / Snapdragon 8 Elite、OnePlus 12。
- **问题：** 背景 LLM 推理可能大量消耗共享内存带宽，使前台交互出现卡顿；背景任务本身吞吐可能下降不多，但前台体验明显变差。
- **机制：** 以共享带宽/资源分配为控制点，在前台敏感度与后台 AI 需求之间做资源控制；不是新颖于“前台优先”这一口号，而是针对现代商用手机背景 LLM 的测量与调控。
- **论文报告的背景吞吐变化：** 在相关保护前台的配置中，Prefill 吞吐损失约 **1.01%**，Decode 约 **1.64%**（需按原文具体配置理解；不应把它误写成所有后台负载或所有手机的固定代价）。
- **结论：** 前台 QoE 和共享 DRAM 是实际系统问题，值得归入 C 的 Runtime/OS 责任；不能由此推出 Agent 专用 CPU 硬件的必要性。
- **边界：** 不是 Agent 专用机制，也不证明新 ISA/uArch；其具体效果受设备、内存系统和调度实现约束。
- **仓内深读：** [PAPER-003](../01-evidence/papers/PAPER-003/deep.md)。

### 8.3 HeRo 与 SERENO 如何共同解释 C

HeRo 主要回答“动态 Agent 工作流中哪些阶段该在什么执行单元运行、何时运行”；SERENO 主要回答“后台 AI 与前台交互共享 DRAM 时，怎样保护用户体验”。两者互补但不是同一件事：

- HeRo 的主对象是动态 DAG、阶段亲和性和端到端工作流调度；
- SERENO 的主对象是共享内存带宽争用和前台 QoE；
- 二者共同支持 C 的软件/OS 系统能力；
- 二者都没有证明需要独立的 Agent 专用 CPU 指令或硬件调度单元。

---

## 九、Agent 语义、工作流状态与强软件基线

### 9.1 PAPER-119 — LLM-as-Scheduler（LAS）

- **发表：** ACL 2026 long paper；DOI 10.18653/v1/2026.acl-long.581。
- **原始来源：** https://aclanthology.org/2026.acl-long.581/
- **研究对象：** 多 Agent 软件工作流；使用产物验证和条件化的额外检查/修订路由，减少固定重型流程的浪费。
- **机制：** 每个 Agent 产生结构化产物包；门控特征包括程序化规格符合性、小模型判断、候选一致性和历史 Agent 可靠性；只有必要时才由较重控制器查看摘要、中间产物与 DAG，决定提前结束、验证、测试或修订。
- **基线与工作负载：** HumanEval/MBPP 代码生成、GSM8K 数学推理；比较 IO、CoT、Self-Refine、Reflexion、ADAS、AFlow 等工作流。
- **MBPP 例子：** AFlow 基线为 **94.2% 准确率 / 6643.2 输出 token / 134.28 s**；LAS 完整方案为 **93.7% / 2430.2 token / 77.99 s**。论文汇总的输出 token 减少约 37.4%—63.4%，延迟降低约 36.8%—41.9%，准确率最多下降约 1.4 个百分点；应明确这是云端/软件 benchmark，不是手机端测量。
- **消融边界：** 在 MBPP，Gate-only 为 86.7% / 2516.4 token / 65.24 s，LAS-only 为 93.9% / 3678.1 / 90.25 s，联合方案为 93.7% / 2430.2 / 77.99 s。Gate 每步报告开销约 0 token、0.15 s；LAS 控制器约 725 token、19.44 s。门控精确率约 66.29%、召回约 98.60%，说明未经校准的廉价门控可能过早终止。
- **决策意义：** 软件可以用已有产物、验证结果和 DAG 状态做有价值的语义相关调度；泛化“语义进度提示是新颖硬件”的主张因此受到明显挤压。
- **限制：** 云端 LLM API、基准调优门控、无手机 CPU/uArch 测量；不否定真正不可观察的 RequiredProgress 可能有残余价值。
- **仓内深读：** [PAPER-119](../01-evidence/papers/PAPER-119/deep.md)。

### 9.2 PAPER-121 — ProgRouter

- **原始来源：** [arXiv:2608.25992 v2](https://arxiv.org/abs/2608.25992)。
- **作者：** Songyuan Li（Aston University）、Ahmed M. Abdelmoniem（Queen Mary University of London）、Shiqiang Wang（University of Exeter）。
- **发表状态边界：** v2 日期为 2026-08-30；作者报告已被 Findings of EMNLP 2026 接收，但当前审计未独立确认最终出版论文集。
- **问题：** 多 Agent 工作流在每个子任务上选择何种模型，需要结合进度、剩余预算与模型的边际收益，而不是静态地按整个请求选模型。
- **机制：** 协调器维护目标、角色、历史动作/输出、子任务完成状态等结构化 ledger；进度评分组合完成比例、最近趋势、状态质量/语义变化等；第二条预测路径把协调器从同一 ledger 生成的摘要做语义嵌入；融合后预测不同模型的进度收益，并用延迟/能耗惩罚和虚拟队列控制预算违约。
- **关键解释：** 论文的“semantic”是软件从可观察的工作流账本生成的语义摘要，不是证明 CPU/OS 必须读取不可见的 Agent 私有 oracle。
- **工作负载/环境：** HumanEval+、MBPP、MATH-500、ASQA；单台 NVIDIA RTX PRO 6000 Blackwell GPU 工作站，Ollama 0.24.0、AG2 0.11.3、Qwen3-Coder-Next 80B-A3B 协调器。
- **代表结果：**
  - HumanEval+：ProgRouter **93.0% pass / 4796 J / 13.7 s**；
  - MATH-500：**84.3% / 6112 J / 19.0 s**；CASCADIA 为 **87.8% / 6875 J / 24.6 s**。ProgRouter 不一定每个指标都最高，应理解为质量—成本 Pareto 取舍。
  - HumanEval+ 消融：full 93.0% / 4796 J；no predictor 89.0% / 4785 J；structured-only 90.9% / 4400 J；semantic-only 87.2% / 4784 J。不同消融的能耗并不匹配，因此不能把语义路径的单独信息价值解释为已完成的等能耗控制实验。
- **能耗边界：** 使用 NVIDIA NVML 以 100 ms 采样 GPU 板卡功率，估算模型冷加载、Prefill、Decode 与协调器/worker 的 GPU 执行；按论文假设排除 CPU 协调、主机 RAM、存储和网络能耗。这不是手机电池、NPU 电源轨或整机系统能耗。
- **决策意义：** 把结构化 ledger、进度趋势、语义摘要和模型收益预测都纳入最强软件基线 B4-TX。A 只能在这些状态匹配后仍有额外、不可重建的信息增益时重开。
- **仓内深读：** [PAPER-121](../01-evidence/papers/PAPER-121/deep.md)。

### 9.3 PAPER-044 — ProAgentBench

- **研究对象：** 以真实连续行为历史判断“何时帮助”和“如何帮助”的主动 Agent 预测基线。
- **数据：** 公开数据集包括 17 名参与者、28,528 个事件、超过 500 小时以及 167,423 张截图；样本以学生群体为主，因此对一般手机人群的代表性有限。
- **方法：** 使用时间切分和用户自身历史，负样本不是简单的无活动时刻；比较合成样本与真实历史样本的微调。
- **报告结果：** LLaMA-3.1-8B-Instruct 的 When-to-Assist：zero-shot **57.3% accuracy / 66.7% F1**，合成微调约 **62.1% / 70.2%**，真实历史微调约 **74.0% / 78.5%**；How-to-Assist 意图准确率约从合成数据的 **34.8%** 提升至真实数据的 **42.1%**。Qwen3-VL-8B-Instruct 也显示真实历史微调优于合成微调。
- **决策意义：** 用户历史和上下文是 A 的强基线。A 不能只是把可观察历史或意图预测重新包装为专用硬件状态。
- **边界：** 这不是 CPU/SoC benchmark，也不是对手机日能耗的测量；参与者规模和人群构成限制泛化。
- **仓内深读：** [PAPER-044](../01-evidence/papers/PAPER-044/deep.md)。

### 9.4 A 的正确表述

- **保留的假设：** Agent 私有 RequiredProgress 可能包含某种软件账本无法重建的信息。
- **已被压缩的宽泛主张：** “语义进度”“任务完成度”“模型收益”本身足以构成硬件差异化。LAS、ProgRouter、ProAgentBench 和官方 Agent API 都表明软件可利用可观察产物、历史和上下文。
- **尚未被证明的关键问题：** 在所有 B4-TX 可观察状态匹配后，加入私有 RequiredProgress 是否仍能改变正确路由/停止/恢复决策，并在同样的质量、权限、延迟和能耗约束下获得独立收益。
- **决策：** A 已由历史 Primary Bet 降级为 Conditional Reserve，保持 HYPOTHESIS_OPEN；这不是实证否定，也不是当前主押注。

---

## 十、官方平台、厂商技术与专利边界

### 10.1 Android NPU Manager（VENDOR-027）

- **原始官方文档：** https://source.android.com/docs/core/perf/npu-manager
- **公开能力类型：** Android 17+ 平台文档描述的 NPU 管理接口，包括模型加载准入、优先级/重新排序、系统卸载与执行事件等生命周期管理。
- **为什么重要：** 通用 NPU 工作优先级、模型驻留/回收和取消/状态控制已有 OS 级基线，不应一概宣称需要新 Agent CPU 硬件。
- **证据边界：** 这是平台规格/API 能力，不是手机 Agent 延迟、抢占恢复时间、内存回收时间或电池的独立测量；不能声称所有 Android 手机都部署了同一功能。
- **仓内来源卡：** [VENDOR-027](../01-evidence/vendors/VENDOR-027/deep.md)。

### 10.2 Qualcomm QNN HTP Shared Buffer（VENDOR-029）

- **官方技术文档：** Qualcomm QNN HTP shared-buffer tutorial，https://docs.qualcomm.com/nav/home/htp_shared_buffer_tutorial.html?product=924033590759186372
- **证据：** 官方文档描述缓冲类型和某些顺序/并发约束；完整交互式手册的直接访问在本次审计中受限，使用已索引的技术段落与表格。
- **可以说：** 已有共享缓冲接口与运行时合同，必须作为 CPU/NPU 数据交接的基线。
- **不可以说：** 所有 CPU↔NPU 数据都零拷贝；所有引擎间共享状态自动一致；存在通用 Agent 物理状态协议。
- **仓内来源卡：** [VENDOR-029](../01-evidence/vendors/VENDOR-029/deep.md)。

### 10.3 Apple Foundation Models / LanguageModelSession（VENDOR-032）

- **官方 API：** https://developer.apple.com/documentation/FoundationModels/LanguageModelSession
- **公开能力：** 合资格 Apple Intelligence 设备上的应用可使用 LanguageModelSession；会话可累积 transcript，可从 transcript 初始化，可通过 prewarm(promptPrefix:) 预热，并通过 Tool 对象调用应用提供的函数。相关 DynamicProfile/历史支持 API 有 beta 与版本边界。
- **约束：** 单个 session 最多一个并发 respond；transcript 可能超过上下文容量并报错。
- **决策意义：** 会话状态与工具控制已经有软件平台接口；没有公开资料保证跨 CPU/GPU/NPU 的持久 KV 一致性、私有 RequiredProgress ABI 或全天 Agent 能耗收益。
- **证据等级：** 官方产品/API 能力，不是独立性能验证。
- **仓内来源卡：** [VENDOR-032](../01-evidence/vendors/VENDOR-032/deep.md)。

### 10.4 Pixel 与 Samsung 的产品信号

- **Google Pixel 10 / Tensor G5（VENDOR-033）：** 官方产品信息可以支持厂商把 Gemini Nano/设备侧 AI 作为产品能力推进的事实；厂商内部比较不是独立第三方性能验证。
- **Samsung Galaxy S26（VENDOR-034）：** 官方发布材料体现 Agentic AI 产品定位；S26 Ultra 使用 Snapdragon 平台，不能据此当作 Samsung 自研 CPU/uArch 的独立证据。
- **共通边界：** 产品营销可以说明趋势和产品功能，不足以证明某种新 CPU 硬件必要、跨厂商普遍收益或严格的全天能耗改善。

### 10.5 三项重点专利边界

**PATENT-024 — US9626295B2**

- 原文：https://patents.google.com/patent/US9626295B2/en
- 公开权利要求涉及缓存需求驱动的 CPU 异构簇迁移等机制。
- 对 R2 的意义：普通缓存/核心迁移已有先前技术；不能把通用 continuation locality 直接命名为新 Agent 硬件。
- 边界：不是 Agent xPU 物理一致性协议的证明，也不是法律 FTO 结论。

**PATENT-032 — CN121960775A**

- 原文：https://patents.google.com/patent/CN121960775A/en
- 公开申请于 2026-05-01 发布；来源审阅时 Google Patents 显示 Pending。发布申请不是已授权可执行权利。
- 被审阅的独立权利要求涉及检索语义相似的对话结果/推理缓存记录、身份/时间/服务版本有效性、完整/部分/未满足的问题覆盖分级、复用/纠正与缓存更新；其他权利要求覆盖系统/设备/程序实现。
- 对 A 的意义：泛化的 Agent 语义需求、推理缓存复用与版本有效性已处在公开权利要求范围中，不能简单声称完全新颖。
- 边界：权利要求的具体组合不等于涵盖所有类似概念；不是专利有效性、侵权或 FTO 意见。

**PATENT-033 — CN120704926A**

- 原文：https://patents.google.com/patent/CN120704926A/en
- 被审阅权利要求涉及多 Agent 软件事务回滚/结果管理的相关方案。
- 对 PT-A/B-residual 的意义：通用事务/回滚有软件先例；要主张新硬件，需要证明超出软件事务合同的物理瓶颈。
- 边界：不能把软件事务回滚等同于 NPU 物理队列取消或跨引擎状态一致性。

**PATENT-026 的防误用说明：** 该项目早期曾讨论过一项华为 2022 年专利，但未找到足够依据证明其明确披露 Agentic AI 机制。因此不得把它作为“Agent 专用 CPU 硬件已被该专利证实”的直接证据。专利相关结论应引用经过实际权利要求审阅的具体文档，而不是根据标题或术语相似性推断。

---

## 十一、三条跨层架构主题：F、P、V

这三条是研究和组织责任的主题，不是三项独立芯片项目，也不能与三项优先工程/平台方向一一机械等同。

### 11.1 F — Execution–State Lifecycle（执行与状态生命周期）

**核心问题：** Agent 工作流的优先级、取消、重试、模型准入、缓存/派生状态的有效性和物理回收，如何在 Runtime、OS、CPU/NPU 和内存之间保持一致？

- **已有基线：** Android NPU Manager 的模型/任务生命周期控制；Qualcomm QNN 的共享缓冲接口；软件版本化、来源追踪、缓存有效性、事务恢复与队列控制。
- **工程归属：** C 与 PT-A 负责主要系统/动作合同；B-residual 与 R2 仅保留跨引擎物理状态和 continuation locality 的剩余问题。
- **研究储备门槛：** 必须有公开证据证明在匹配软件状态版本、共享缓冲、OS 调度和缓存基线后，仍存在显著的物理状态失效、重建、恢复或局部性成本。
- **不能这样说：** “Agent 需要一个新的状态缓存指令”或“事务回滚本身就是硬件创新”。

### 11.2 P — Proactive Low-Power Admission（主动低功耗准入）

**核心问题：** 从事件、上下文和用户意图到“是否应该唤醒/是否应该帮助”，如何控制隐私、误触发、前台 QoE 和全天能耗？

- **已有基线：** Android CHRE、Apple AOP、Qualcomm Sensing Hub、MediaTek 低功耗 AI 领域与软件历史/上下文预测。
- **工程方向：** 跟踪现有低功耗域和共享 NPU 的产品化；软件提供透明的同意、唤醒理由、预算、模型门控和失败处理。
- **储备门槛：** 只有公开证据显示现有 CHRE/AOP/共享 NPU 不能达到目标，且新的低功耗硬件域在帮助率调整后的总能耗上有增量，才考虑新硬件方向。
- **不能这样说：** “Agent 是 Always-on，所以必须增加专用 LP AI 硬件”。

### 11.3 V — Semantic Progress / QoE Policy（语义进度与体验策略）

**核心问题：** 系统何时继续、停止、验证、升级模型或放弃动作？这需要综合可观察任务账本、用户历史、模型收益、权限和验证结果。

- **已有基线：** LAS 的产物门控与条件化工作流路由；ProgRouter 的账本进度/语义摘要/模型收益预测/预算控制；ProAgentBench 的连续用户历史。
- **工程方向：** 把软件可观察信息纳入统一的 Runtime 决策接口，并优先保障正确性和用户体验。
- **A 储备边界：** 仅保留“私有 RequiredProgress 在完整可观察状态之外是否还有独立信息增益”的窄问题。
- **不能这样说：** “有语义进度就需要 CPU 指令”或“模型收益预测已经证明需要硬件 hint”。

---

## 十二、当前正式技术组合与每个方向的具体任务

### 12.1 CG-06 — CPU/LLVM/AArch64 异构快速路径（优先工程方向）

**方向目标：** 在现有 CPU ISA 和优化 NPU 软件栈共存的条件下，改善 CPU 局部推理/控制路径及 CPU↔NPU 分工。

五个技术控制点：

| 控制点 | 应做的事 | 归属层 | 现有基线/边界 |
|---|---|---|---|
| C1：形状/精度感知 lowering | 根据算子形状、算术强度、精度约束和后端能力选择 lowering、fusion、tile 与布局 | LLVM/MLIR/编译 | LLVM vectorizer、MLIR Linalg/ArmSME 已有通用路径 |
| C2：SME 状态与 ABI 边界 | 正确管理 PSTATE.SM、ZA、函数属性与标量/向量/矩阵代码边界 | LLVM 后端 + Runtime ABI | 官方文档有约束定义；未测得的手机切换开销不能编造 |
| C3：微内核与布局复用 | 优化 GEMM/GEMV、权重打包、激活/KV 布局、避免关键路径中的重复 packing | CPU 内核库 + Runtime 数据生命周期 | SMEPilot 显示布局与 packing 会显著影响延迟 |
| C4：CPU/NPU 分阶段放置 | 依据实际后端覆盖、精度、启动/同步/搬运成本安排算子与残差 | 编译 + Runtime | llm.npu/ShadowNPU 说明 NPU 软件前沿会变化 |
| C5：阶段级 QoE/DRAM 调度 | 关键路径、共享 DRAM、前后台优先级、NPU admission | Runtime/OS（主要归 C） | HeRo/SERENO 是强基线，不要把系统调度冒充 CG-06 单独发明 |

**不包含：** 新 Agent 专用 ISA、CPU 永远优于 NPU、仅凭单个 benchmark 就把 CPU-local 作为所有模型的默认路径。

### 12.2 PT-A — 可信 Agent 工具执行与结果验证（平台方向）

建议将工具执行合同表达为：

权限/用户意图确认 → 对当前 App/对象做新鲜绑定 → 受限动作执行 → 获取可观察的 OutcomeReceipt（实际发生的结果）→ 校验是否满足目标 → 成功提交或进行有界恢复/撤销。

- “调用工具返回成功”不等于外部状态已改变。
- “模型说操作成功”不等于动作被验证。
- 需要区分权限、目标新鲜度、动作幂等性、外部效果与恢复策略。
- 主要由 Agent Runtime、应用接口、安全层和 OS 完成；当前没有证据证明需要专用 CPU 指令。
- Apple Foundation Models/Tools、Android AppFunctions 与软件事务/缓存先例构成现有平台基线。

### 12.3 C — Runtime/OS 异构调度与前台 QoE（系统方向）

- 对动态工作流 DAG 做阶段级调度，而不是只按整个模型选择 CPU 或 NPU。
- 显式考虑阶段/PU 亲和性、算子形状、部分未来依赖、共享 DRAM 和前台交互敏感度。
- 处理 NPU 模型加载、优先级、取消、状态和资源回收。
- 把总任务成功率、前台延迟、用户可感知卡顿和系统能耗分开定义；不能只用某个加速器的局部吞吐代表用户收益。
- 对照 HeRo、SERENO、Android NPU Manager、QNN shared-buffer 和现有 Runtime 调度方案。
- 不因“调度重要”就立项新硬件；只有公开原始证据表明软件接口无法满足且存在稳定、可重复的物理瓶颈时，才重新评估。

### 12.4 三项条件研究储备

| 储备 | 仍然开放的窄问题 | 当前强基线 | 何种新公开证据才允许升级 |
|---|---|---|---|
| A：私有 RequiredProgress | 完整可观察账本/历史/权限/验证/模型收益都匹配后，私有需求信息是否仍改变正确路由或停止决策？ | LAS、ProgRouter、ProAgentBench、Apple/Android Runtime API、PATENT-032 | 原始公开研究做同观测状态对照，并证明质量、权限、延迟/能耗条件下的独立增益 |
| B-residual：跨引擎派生状态物理有效性 | CPU/NPU/内存之间的派生数据是否有软件版本/来源/失效管理无法解决的实际成本？ | 版本化缓存、QNN/HAL、Android NPU 管理、软件事务与缓存专利 | 同时公开测量状态失效、重建/恢复成本与软件最强基线；明确器件/平台和总系统影响 |
| R2：CPU continuation locality | 继续执行的任务在跨核心/阶段迁移时，是否有普通亲和性/共享缓存机制无法吸收的成本？ | CPU 异构簇迁移/共享缓存先例、Qualcomm Oryon Flex Cache 公开机制、软件亲和性 | 公开手机数据隔离核心迁移、缓存工作集和端到端收益，排除仅靠软件亲和性可解释的部分 |

### 12.5 其他方向的状态

- **R1 — WATCH：** 通用 deadline、wakeup、slack 和软件释放策略已有先前技术；当前没有足够手机/CPU 证据支持把 post-ready semantic release timing 作为核心储备。
- **CG-07 — FOLLOW/EXPLORE：** 跟踪 CHRE/AOP/Qualcomm Sensing Hub/MediaTek 低功耗 AI；不预先承诺 Agent 专用 LP 硬件。
- **CG-01 — BENCHMARK/FOLLOW：** 跟踪公开共享 CPU cache 与核心迁移能力，例如 Qualcomm Oryon/Flex Cache；这不是已证实的对等产品能力比较。
- **R3 — BLOCKED：** 不启动泛化的 Agent 语义 ISA、CPU hint、专用缓存/TLB/预测器等硬件主张。
- **宽泛新颖性 Kill：** 通用任务调度、NPU 优先级/取消、普通零拷贝、版本化缓存、语义结果复用、事务回滚等已有软件/平台/专利基线的功能，不应仅因与 Agent 有关就声称是新硬件机制。

---

## 十三、2027—2029 技术路线（规划建议，不是厂商承诺）

| 技术层 | 2027：建立可移植基础 | 2028：强化跨层合同 | 2029：条件性架构选项 |
|---|---|---|---|
| CPU/uArch/cache | 跟进现有 Arm C2/SME2、SVE/Neon 与公开 CPU/cache 机制；优先标量控制、现有 ISA 的向量/矩阵执行和低开销路径 | 跟踪 CPU continuation warm-state、缓存共享/亲和性、软件局部性；用公开真实手机证据更新判断 | 仅在出现明确的跨引擎物理残差证据后研究共享缓存/状态生命周期/低开销命令路径；不预定 Agent 专用 ISA |
| LLVM/AArch64/编译 | CG-06：shape/precision-aware lowering、fusion、tile、packing、布局复用、现有 SME2 路径 | 建立 capability-aware CPU↔NPU operator placement 与模型/驱动版本兼容接口 | 保持可移植编译/runtime contract；新 Agent 指令必须有跨厂商原始证据和不可被软件吸收的必要性 |
| Agent Runtime/可信工具 | PT-A：权限、目标新鲜度、OutcomeReceipt、验证与有界恢复 | 跨 App 的安全状态/权限清单、动作谱系、取消与恢复合同 | 跨平台可移植的本地 Agent 生命周期和可信动作接口；以正确结果而非工具调用次数衡量 |
| OS/Runtime/异构 SoC | C：阶段 DAG、前台 QoE、DRAM 争用、模型准入/优先级、优化 NPU 对照 | 状态版本、模型驻留/回收、并发与队列公平性、权限敏感的取消/恢复 | 若公开资料超过软件基线，才研究跨引擎物理状态保留/撤销或低开销交接 |
| 内存/KV/派生状态 | 采用版本、来源、有效期、缓存重用与共享缓冲的强软件合同 | 研究跨模型/跨引擎状态兼容和失效成本 | B-residual/R2 仅为研究储备；不宣称硬件一致性需求已被证明 |
| Always-on/低功耗 | 跟进 CHRE/AOP/Sensing Hub/LP NPU；明确“不行动”与误报/漏报成本 | 把隐私同意、唤醒理由、能耗预算、帮助率和平台兼容性纳入接口 | 只有公开证据证明增量收益后，才考虑专用低功耗域 |

**时间边界：** 2027/2028/2029 是技术规划分段，不是已确认的产品量产年份、预算安排或内部交付承诺。

---

## 十四、公开证据能证明什么、不能证明什么

### 14.1 可直接支持的事实

- 在一代特定 Snapdragon 手机/软件栈上，CPU 与 NPU 的收益会随 Prefill、Decode、算子和交接成本变化（PAPER-009）。
- 在公开评估平台上，SME/SME2 与运行时分工、布局复用可以改善特定 CPU 工作负载；vivo X300 的 SqueezeSAM 有直接手机数据（PAPER-052、TOOL-012）。
- 优化 NPU 软件栈可以通过图重构、量化分工和残差执行显著改变 CPU/GPU/NPU 的工作划分（PAPER-059、PAPER-057）。
- Agentic RAG 的动态工作流调度已在商用 Snapdragon 手机上有公开结果（PAPER-098）。
- 背景 LLM 的共享内存带宽压力会影响前台 QoE，已有商用手机系统研究（PAPER-003）。
- 软件工作流可利用产物、验证、任务账本、语义摘要和用户历史进行动态路由/进度估计（PAPER-119、PAPER-121、PAPER-044）。
- 官方 OS/SDK/工具链已经公开了多种会话、工具、NPU 管理、共享缓冲与 SME/LLVM 能力（VENDOR-027/029/032、TOOL-012/014/015/016/017/018）。

### 14.2 跨来源推断

- CPU 将持续作为可编程控制主机，并在特定阶段/算子/精度条件下作为选择性 AI 执行端；但具体边界随 NPU 软件成熟度而变化。
- 动态 Agent 工作流增加了 Runtime/OS 对 DAG、状态、资源和前台 QoE 的要求。
- 现有软件和平台基线越强，新增 CPU/uArch 主张需要越具体的物理机制与独立证据。
- 三项优先工程方向比新增 Agent 专用 CPU 硬件更符合当前公开证据的强度。

### 14.3 当前没有被公开资料证明的主张

- 新 Agent 专用 CPU ISA/uArch/缓存/预测器/TLB/Hint 的手机级因果收益。
- A 的 RequiredProgress 在完整软件可观察状态之外具有不可重建的信息价值。
- B-residual 需要新硬件才能保证跨引擎派生状态正确。
- R2 需要专用缓存或微架构状态才能改善用户体验。
- 新增 Always-on Agent 硬件域一定优于现有 CHRE/AOP/共享 NPU。
- 跨厂商、跨模型、跨设备的统一 Agent 任务成功率—总能耗—前台 QoE 数值。
- 任一单篇论文的最高加速比可直接迁移到其他手机、模型或未来芯片。

### 14.4 证据覆盖的边界

最终来源审计直接检查了决策关键论文、官方工具链/平台文件与重点专利条目；当时审计检查了 22 个优先 Markdown 文档中的 84 个仓内相对链接，没有发现缺失目标。这个结果不是对所有外部 URL 实时在线的保证，不是所有论文全文逐字重读，也不是专利族穷尽检索或 FTO 法律意见。

官方页面若存在 JavaScript、访问限制或本轮无法直接打开，本文会保留其访问边界，不得把“之前的来源卡有记录”写成“今天已重新打开全文”。

---

## 十五、七问最终结题矩阵与管理决策

| 问题 | 结题结论 | 给领导可使用的答案 | 保留边界 |
|---|---|---|---|
| FQ1 工作负载变化 | 已结题（有边界） | 关注持续可信任务、异构多阶段执行、可修订状态、主动低功耗准入 | 2027—2029 的普及程度和每家 SoC 经济性未被精确预测 |
| FQ2 现有先前技术 | 已结题（有边界） | 关键论文、官方工具/OS、Agent 软件基线与专利权利要求已覆盖到足以支撑当前方向判断 | 不是全世界所有文献/专利穷尽检索；不构成 FTO |
| FQ3 跨层主题 | 已结题 | F 执行/状态、P 主动低功耗准入、V 语义进度/QoE | 主题不是三个硅片项目 |
| FQ4 硬件必要性 | 带证据缺口结题 | 现有 CPU/LLVM/异构软件有工程价值；新增 Agent-only CPU 硬件的因果价值未证实 | 项目不做自有实验；公开证据缺口作为结论边界保留 |
| FQ5 技术组合 | 已结题 | CG-06/PT-A/C 优先工程；A/B-residual/R2 储备；R1 WATCH；CG-07 FOLLOW/EXPLORE；CG-01 BENCHMARK；R3 BLOCKED | 0 个有充分公开证据支持的独立差异化 CPU/uArch Primary Bet |
| FQ6 2027—2029 路线 | 已结题（有边界） | 按层分年做可移植工程、跨层接口与条件研究 | 不是预算、人力或产品量产承诺 |
| FQ7 证据充分性 | 已结题（有边界） | 决策关键原始资料、基线、反证、来源独立性与访问限制已审计 | 不代表全部外部链接今日在线、全部研究事实实时更新或专利法律审查完成 |

### 15.1 重新打开研究的条件

默认不再宽泛搜索。只有出现下列新公开原始证据时，才针对相关问题局部重开：

- 真实手机上、同一设备/模型/任务的 CPU 与优化 NPU 对照，明确拆分算子、启动、复制、同步、fallback、能耗和前台 QoE；
- 对 Agent 工作流调度的独立公开结果，能够对照最强软件调度基线；
- 在完整可观察状态匹配后，严格隔离 A 的额外信息价值；
- 对跨引擎状态失效/重建或 CPU continuation locality 的物理残差，提供匹配软件基线和可复核测量；
- 新的官方编译器/OS/硬件接口改变现有可行性；
- 发现关键来源归属、数值、原文含义或证据链有实质错误。

没有这些变化时，不因为历史文档中有旧的“Next”就自动重启项目。

---

## 十六、关键原始文献与资料清单（可独立阅读）

以下清单只列对最终技术判断有实质影响的决策关键来源，不等同于整个仓库全部来源。每条包含标题、出版/来源信息、主要贡献、本文使用方式与关键限制。所有数值都必须与该条原始来源中的设备、模型、基线和指标一起理解。

### A. 手机 CPU/NPU 与 CPU 现有 ISA

**A1. When NPUs Are Not Always Faster — PAPER-009**

- 来源：arXiv:2605.27435，https://arxiv.org/abs/2605.27435。
- 对象：Snapdragon 8 Gen 3 / Hexagon v75。
- 主要结果：Prefill NPU 路径比 6 核 CPU 慢 1.27—1.62×；Decode 核心 MUL_MAT 的 NPU 路径快 1.55—1.67×；NPU 路径通信约 9.9%—13.0%；不同 prompt 配置下更高 offload 报告耗电增加 22%/32%/51%。
- 论据作用：支持阶段/算子/实现决定 CPU/NPU 交叉点。
- 限制：单一代际/软件栈；不是普遍规律，不是 Agent 专用硬件因果证据。
- 深读：[PAPER-009](../01-evidence/papers/PAPER-009/deep.md)。

**A2. SMEPilot — PAPER-052**

- 来源：arXiv:2606.16332，https://arxiv.org/abs/2606.16332。
- 对象：Apple M4 Pro、Dimensity 9500、KunPeng 920；Llama-3.2-3B、Qwen3-4B、Qwen3-30B-A3B。
- 主要结果：相对 llama.cpp 默认 CPU 后端最高 3.94×；去掉 tile partition 后 GEMM 增加 1.46×；去掉 Attention pipeline 后 Prefill Attention 增加 2.07×；M4 Pro 一组能耗 482.813 J → 233.931 J。
- 论据作用：证明现有 CPU 矩阵扩展与编译/布局/流水工程值得做强。
- 限制：最高值不代表平均；能耗来自 M4 Pro；没有同手机优化 NPU 对照；不是 Agent 工作流实测。
- 深读：[PAPER-052](../01-evidence/papers/PAPER-052/deep.md)。

**A3. Accelerating on-device ML inference with ExecuTorch and Arm SME2 — TOOL-012**

- 来源：PyTorch 官方博客，https://pytorch.org/blog/accelerating-on-device-ml-inference-with-executorch-and-arm-sme2/。
- 对象：vivo X300，SqueezeSAM，ExecuTorch + XNNPACK + KleidiAI。
- 主要结果：单 CPU 核 INT8 555.8→304.1 ms、FP16 1163.0→298.2 ms；四核 INT8 195→180 ms、FP16 374→193 ms；SME2 后数据移动占比约 40%。
- 论据作用：真实手机上的 CPU ISA/软件栈技术证据。
- 限制：不是 Agent 模型，不是 CPU/NPU 比较，博客作者包含生态参与者。
- 来源卡：[TOOL-012](../01-evidence/tools/TOOL-012/README.md)。

### B. 优化 NPU 的软件/算法路线

**B1. Fast On-device LLM Inference with NPUs (llm.npu) — PAPER-059**

- 发表：ASPLOS 2025；DOI 10.1145/3669940.3707239；arXiv https://arxiv.org/abs/2407.05858；artifact https://doi.org/10.5281/zenodo.14392760。
- 对象：Xiaomi 14、Redmi K60 Pro/K70 级 Snapdragon 手机；Qwen1.5、Gemma、Phi-2、Llama-2、Mistral；DroidTask/LongBench/Persona-Chat 等。
- 主要机制：固定 chunk 图复用、INT8 NPU + CPU/GPU outlier residual、子图级在线调度。
- 主要结果：平均 Prefill 加速 22.4×、能耗节省 30.7×、端到端最高 32.8×（限定于论文配置）。
- 论据作用：最强 NPU 软件比较路线之一。
- 限制：不是所有阶段都 NPU 执行；不能外推到所有模型；与 ShadowNPU 有研究谱系。
- 深读：[PAPER-059](../01-evidence/papers/PAPER-059/deep.md)。

**B2. ShadowNPU: System and Algorithm Co-design for NPU-Centric On-Device LLM Inference — PAPER-057**

- 发表：ACM MobiSys 2026；DOI 10.1145/3745756.3809205；arXiv https://arxiv.org/abs/2508.16703；artifact https://zenodo.org/records/19555734。
- 作者：Wangsong Yin、Daliang Xu、Mengwei Xu、Gang Huang、Xuanzhe Liu。
- 对象：Xiaomi 14/Snapdragon 8 Gen3、Redmi K60/Snapdragon 8 Gen2；Qwen2、PhoneLM；ArxivSum、DroidCall、Octopus。
- 主要机制：NPU 低精度 Attention 重要性估计 + CPU/GPU 高精度稀疏残差、head-wise 流水、图分桶与融合 launch。
- 主要结果：完整 Attention 转 NPU INT8 平均准确率下降约 18 个百分点；ShadowNPU 的跨模型/任务平均准确率指标 36.4 vs NPU-Full 18.8；对比 llm.npu 的特定配置最高约 3.0× 延迟改善、最高约 7.66× 能耗改善。
- 论据作用：显示 NPU 软件前沿继续扩张，并且 CPU/GPU 残差仍可与 NPU 协作。
- 限制：最高值和具体任务限定；主要改 Prefill Attention，Decode 设计仍保留 CPU/GPU Attention；与 llm.npu 不是独立复现。
- 深读：[PAPER-057](../01-evidence/papers/PAPER-057/deep.md)。

### C. Agentic 工作流与 QoE

**C1. HeRo: Adaptive Orchestration of Agentic RAG on Heterogeneous Mobile SoC — PAPER-098**

- 来源：arXiv:2603.01661，https://arxiv.org/abs/2603.01661；作者团队页面列为 DAC 2026。
- 对象：Redmi K80、OnePlus 13 等 Snapdragon 手机。
- 机制：对动态 Agentic RAG DAG 按阶段/子阶段调度，考虑 xPU 亲和性、shape、部分未来依赖和 DRAM 争用。
- 结果：两个案例 5.79→3.82 s（1.52×）、17.23→5.38 s（3.20×）。
- 论据作用：C 有直接手机 Agent 工作流证据。
- 限制：不是所有通用动态调度器的完整对照；主要单查询平均延迟；与 Agent.xpu 有团队谱系。
- 深读：[PAPER-098](../01-evidence/papers/PAPER-098/deep.md)。

**C2. Inference in the Shadows: Taming Memory Bandwidth Contention in Mobile LLM Inference with SERENO — PAPER-003**

- 发表：OSDI 2026；作者 Tong Xin、Xinrui Shi、Mingkai Dong、Zeyu Mi；来源 https://www.usenix.org/system/files/osdi26-xin.pdf。
- 对象：OnePlus 13/Snapdragon 8 Elite、OnePlus 12。
- 机制：在前台交互与后台 LLM 之间进行共享内存/带宽资源控制。
- 结果：相关配置下背景 Prefill 吞吐损失约 1.01%、Decode 约 1.64%，而研究目标是保护前台 QoE。
- 论据作用：支持共享 DRAM/前台体验是现实问题。
- 限制：不是 Agent 专用硬件证据；结果限定于论文设备/配置。
- 深读：[PAPER-003](../01-evidence/papers/PAPER-003/deep.md)。

### D. Agent 软件状态与语义进度基线

**D1. LLM-as-Scheduler — PAPER-119**

- 发表：ACL 2026 long paper；DOI 10.18653/v1/2026.acl-long.581；https://aclanthology.org/2026.acl-long.581/。
- 机制：对中间产物、规格符合性、模型判断、一致性和历史可靠性做低成本门控，条件化调用验证/测试/修订工作流。
- 代表结果：MBPP AFlow 94.2% / 6643.2 token / 134.28 s；LAS 93.7% / 2430.2 token / 77.99 s；汇总 token 减少约 37.4%—63.4%，延迟减少约 36.8%—41.9%。
- 论据作用：可观察的软件状态已经能驱动有效的 Agent 工作流优化。
- 限制：云端基准，不是手机能耗/CPU 测量。
- 深读：[PAPER-119](../01-evidence/papers/PAPER-119/deep.md)。

**D2. ProgRouter — PAPER-121**

- 来源：arXiv:2608.25992 v2，https://arxiv.org/abs/2608.25992。
- 作者：Songyuan Li、Ahmed M. Abdelmoniem、Shiqiang Wang。
- 机制：协调器 ledger、完成比例、进度趋势、状态质量、语义摘要嵌入、模型边际收益预测和预算虚拟队列。
- 代表结果：HumanEval+ 93.0% / 4796 J / 13.7 s；MATH-500 84.3% / 6112 J / 19.0 s；CASCADIA 在 MATH-500 为 87.8% / 6875 J / 24.6 s。
- 论据作用：泛化语义进度可以通过软件从可观察状态估计。
- 限制：GPU 板卡能耗，不是手机整机；没有匹配可观察状态与私有 RequiredProgress 的严格因果测试。
- 深读：[PAPER-121](../01-evidence/papers/PAPER-121/deep.md)。

**D3. ProAgentBench — PAPER-044**

- 数据：17 名参与者、28,528 事件、500+ 小时、167,423 张截图，学生样本偏多。
- 代表结果：LLaMA-3.1-8B When-to-Assist 从 zero-shot 57.3% accuracy/66.7% F1，真实历史微调提升到 74.0%/78.5%；How-to-Assist 意图准确率约从合成 34.8% 提升到真实历史 42.1%。
- 论据作用：连续用户历史与上下文是主动帮助策略的强软件基线。
- 限制：不证明硬件收益，且参与者规模/人群有限。
- 深读：[PAPER-044](../01-evidence/papers/PAPER-044/deep.md)。

### E. 官方平台/工具与专利

**E1. Android NPU Manager — VENDOR-027**  
https://source.android.com/docs/core/perf/npu-manager。公开平台文档描述模型准入、优先级、卸载和执行事件；是 OS 级资源管理基线，不是跨设备统一部署证明或独立性能测量。

**E2. Qualcomm QNN HTP Shared Buffer — VENDOR-029**  
https://docs.qualcomm.com/nav/home/htp_shared_buffer_tutorial.html?product=924033590759186372。提供共享缓冲与顺序/并发约束的官方技术信息；不应宣称所有路径都零拷贝或跨 xPU 状态天然一致。

**E3. Apple Foundation Models LanguageModelSession — VENDOR-032**  
https://developer.apple.com/documentation/FoundationModels/LanguageModelSession。官方 API 有 transcript、session、prewarm 和 Tool 接口；部分能力有 beta/版本边界。它证明软件会话与工具接口存在，不证明 Agent 专用硬件。

**E4. LLVM/MLIR/Arm 工具链 — TOOL-014/015/016/017/018**  
LLVM AArch64 SME、MLIR ArmSME、MLIR Linalg、Arm KleidiAI 和 LLVM vectorizer 是现有编译/微内核基线。它们不提供所有手机的状态切换开销或 Agent 端到端收益测量。

**E5. 专利权利要求边界 — PATENT-024/032/033**  
US9626295B2 涉及 CPU 异构簇迁移/缓存相关先前技术；CN121960775A 涉及对话/推理缓存版本与需求覆盖有效性；CN120704926A 涉及多 Agent 软件事务回滚相关方案。它们用于收窄新颖性主张，不构成法律意见或 FTO。

---

## 十七、建议本地 Agent 使用本报告生成 PPT 的叙事结构

本节是内容交付合同，不是对所有页面版式的硬性限制。最终标题必须是陈述句，直接表达观点；不能用“我们要回答什么问题？”式标题，也不能只写主题名。每页应能独立回答：这页结论是什么、证据在哪里、对技术路线意味着什么。

### 17.1 推荐的 17 页叙事骨架

| 页码 | 陈述句式的核心结论标题（建议） | 本页必须解释的内容 | 推荐图形/证据 | 来源与限制 |
|---|---|---|---|---|
| 1 | 手机 Agentic AI 的系统演进要求重新审视 CPU、编译器与异构协同 | 研究范围、2027—2029、公开证据边界 | 简洁封面；手机 SoC/工作流抽象图 | 不暗示已有新芯片项目 |
| 2 | 本报告先解释工作负载变化，再用现有基线收敛技术方向 | 章节顺序：趋势→证据→技术机制→路线 | 目录/章节地图 | 不加页码说明小字 |
| 3 | 现有 CPU 与异构软件值得做强，但新 Agent 专用 CPU 硬件尚无充分证据 | 三项优先工程、三项储备、0 项独立差异化 Primary Bet | 结论分层图；工程方向与储备不能同色同级 | current.md、DEC-PORTFOLIO-002 |
| 4 | 手机 Agent 将持续触发工具、推理与状态验证，而非只运行一次模型 | T1—T4 四项结构变化及证据边界 | Agent 生命周期/状态图 | Apple API、PAPER-044、PAPER-098 |
| 5 | 动态 Agent 工作流使调度对象从单个算子扩展到阶段依赖图 | 动态 DAG、阶段亲和性、shape、部分未来依赖和 DRAM | HeRo 工作流示意；每条箭头标注依赖含义 | PAPER-098；不是所有工作流相同 |
| 6 | CPU 与 NPU 的效率交叉点取决于阶段和交接成本 | Prefill/Decode 区别、fallback、通信/同步/电池边界 | PAPER-009 的原文数据图或忠实重绘；标出手机/芯片/基线 | 不外推为普遍 CPU 优势 |
| 7 | 优化 NPU 软件栈正在回收原先留在 CPU/GPU 的工作 | llm.npu 图分桶/量化残差；ShadowNPU 低精度估计+高精度稀疏残差 | 两篇论文机制图的解释性对照 | 同一研究谱系，不当作独立复制 |
| 8 | 现有 SME2 与编译/布局协同已经提供明确的 CPU 优化空间 | SME 是 CPU 指令扩展；SMEPilot 的 tile/pipe/layout；vivo X300 实测 | CPU 核内部 SME2 结构 + 结果对比 | M4 Pro 能耗与手机结果分开 |
| 9 | 动态工作流调度与前台内存争用属于 Runtime/OS 的系统责任 | HeRo 的 DAG 调度与 SERENO 的 DRAM/QoE | 两个机制并列但不混同 | 不把系统调度当新 CPU 硬件 |
| 10 | 可信工具动作需要权限、目标新鲜度与真实结果验证 | PT-A 的动作链与恢复边界 | 权限→目标→动作→OutcomeReceipt→验证/恢复 | Apple/Android API、专利软件先例 |
| 11 | 软件账本、验证与用户历史已构成强语义进度基线 | LAS、ProgRouter、ProAgentBench；A 的残余假设 | 观察状态与私有信息的对照图 | 云端能耗不能写成手机电池 |
| 12 | 三条跨层主题分别管理执行状态、低功耗准入与语义进度 | F/P/V 的范围、owner 与相互依赖 | 分层架构图；箭头表示输入/约束/输出 | F/P/V 不是三个硅片项目 |
| 13 | 三项优先工程方向有公开证据支撑，但性质各不相同 | CG-06、PT-A、C 的责任边界 | 三条并列但不同技术 owner 的方向图 | 不能用同一硬件“投资”标签 |
| 14 | 三项研究储备只有在新增证据跨过软件基线后才能升级 | A、B-residual、R2 的问题/基线/触发条件；R1 WATCH、R3 BLOCKED | 决策门槛表或证据阶梯 | 不将储备画成已批准项目 |
| 15 | 2027—2029 应先建立可移植软件基础，再条件性研究硬件残差 | 按 CPU/LLVM、Runtime/OS、状态、低功耗的逐年路线 | 年份×技术层路线图 | 年份是规划窗口，不是量产承诺 |
| 16 | 当前结论的强度由公开证据边界决定，而非由论文数量决定 | FACT/INFERENCE/HYPOTHESIS/NOT ESTABLISHED；来源独立性与访问限制 | 证据等级图/反证表 | 不声称全世界穷尽检索 |
| 17 | 下一步只应跟随可能改变决策的新公开证据定向更新 | 当前决策、重开门槛和结题状态 | 最终决策摘要与门槛列表 | 无新证据时不自动重开泛化研究 |

### 17.2 每页必须交付的内容合同

每一页在制作前先形成独立的 Slide Contract，至少包含：

1. **一句话主张：** 用陈述句直接说结论，不使用问句标题或只写主题名。
2. **受众需要理解的因果链：** 这页解决什么问题、为什么证据能支撑结论、结论改变什么技术判断。
3. **正文信息：** 每个关键术语第一次出现时给出通俗解释；保留必要英文术语，但不做生硬直译。
4. **图表结构：** 说明节点、边、箭头方向、连接语义、颜色意义、单位、基线和数据来源；不允许靠观众猜箭头。
5. **证据归属：** 每个关键数字或机制对应到原始论文/官方文件；区分事实、推断与假设。
6. **边界：** 标明设备、模型、基线、指标、样本或官方声明的限制。
7. **讲者备注：** 先对本页实际投影内容作详细解释；再逐条解释每个来源来自哪里、主要论据是什么、支撑哪条结论、不能支撑什么。
8. **改版控制：** 修正箭头时不随意改文案；改备注时不改投影画面；如需改文字必须单独进入内容审核。
9. **可编辑性：** 主标题、正文、数据标签和关键流程优先使用原生 PowerPoint 对象；复杂论文图可在确认含义后裁剪/嵌入，但不得把整页扁平化成一张图片。
10. **渲染验收：** 必须查看整页 PNG，不只看文字提取或代码；检查越界、箭头端点、标题栏、页脚、引用留白、文字层级、色彩聚焦与内容密度。

### 17.3 公式和论文图的使用规则

- 公式只有在帮助解释技术机制时才使用，并在正文附近解释变量。推荐的通用概念式包括端到端成本分解、Amdahl 定律、Roofline 和动态 DAG 关键路径；不得把概念公式伪装成论文原式或本项目实测模型。
- 如果使用论文原图，必须确认原图所表达的对象、坐标、单位、实验装置、对照和结论；备注要解释图的含义。不能只因为图“看起来科技感强”就贴入 PPT。
- 如果把论文结果重新绘制为 Python 图，必须保留原始单位、基线和具体设备；“最高提升”“平均提升”“消融结果”不可混为一谈。
- 不得使用未核实的图号；若需要裁剪某张原文图，先由研究员确认原文图与本页主张对应。
- 所有配色可以随报告主题调整，但页面几何、信息层级、边距、对齐、箭头语义、来源留白与可编辑性不得随主题变化。

---

## 十八、最终结论与维护规则

**最终结论：** 当前公开证据足以支持团队优先做强 CPU/LLVM 现有 ISA 的异构快速路径、可信 Agent 工具执行和 Runtime/OS 前台 QoE；足以保留 A、B-residual、R2 三项有边界研究储备；不足以支持新增 Agent 专用 CPU/uArch/ISA Primary Bet。该结果是证据驱动的技术选择，不是对 CPU 价值的否定。

**本文件的用途：** 作为本地 Agent 生成 PPT 的完整研究底稿。Agent 可以从中抽取叙事、事实、机制、图表和来源，但不得为了让故事更漂亮而提高证据等级、补造数据、抹掉负面结果或把不同设备/基线的数字放在一张无条件可比的图里。

**维护规则：**
- 默认研究已结题，不继续宽泛扩张检索。
- 只有出现能够改变技术组合的新公开原始证据，或发现关键论文/数字/归属/链接存在实质错误时，才定向更新对应章节。
- 研究结论更新后，必须同步更新正式技术组合、证据卡、决策事件、管理报告与 PPT 底稿；不得只改汇报稿而不更新证据链。
- 历史轮次中的 A 旧 Primary Bet/82.5 评分、旧路线和旧 “Next” 是历史，不可覆盖当前正式决策。
- 不将 GitHub 的 Markdown 备注/设计合同误称为已把最终 PPTX 二进制存入 GitHub；PPTX 归档状态与研究结题状态分开管理。

### 最终权威入口

- [项目恢复入口 CONTINUE-HERE](../CONTINUE-HERE.md)
- [项目首页 README](../README.md)
- [正式结题验收](../00-project/final-research-archive-acceptance-2026-10-09.md)
- [七问累计状态](../00-project/final-questions-status.md)
- [当前正式技术组合](current.md)
- [2027—2029 管理报告](management-final-public-evidence-2027-2029.md)
- [来源独立性与 SSOT 审计](../analysis/audits/round15g-final-source-and-ssot-audit-2026-10-08.md)
- [CPU/LLVM 技术机制与基线](../analysis/engineering/round15f-cpu-llvm-compiler-pressure-2026-10-08.md)
- [最终 PPT 备注与归档索引](leadership-decision-pack/archive/README.md)
