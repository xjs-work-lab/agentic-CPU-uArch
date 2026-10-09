# Agentic CPU-uArch：2027—2029 年手机 Agentic AI 技术洞察

本项目研究 **Agentic AI（智能体 AI）在未来三年将如何改变手机的工作负载，以及 CPU 微架构、LLVM 编译器、操作系统和异构计算系统应该怎样演进**。目标不是单纯汇总论文，而是基于可追溯的公开证据，回答团队**应优先投入什么、保留哪些长期研究方向、哪些新增硬件方案目前不值得立项**，形成面向 2027—2029 年的技术路线和领导汇报材料。

> **当前状态｜2026-10-09：公开证据研究已结题，转入按需更新。** 七个最终决策问题均已获得有明确证据边界的答案；研究结论、来源、决策记录和 17 页汇报的备注全文已归档。**最终 PPTX、PDF 和交付包已保存到 ChatGPT Library，尚未上传为 GitHub Release 资产**。研究结题不等于所有技术假设已被实验完全证明。
>
> **从这里继续：** [新窗口/新成员恢复入口](CONTINUE-HERE.md) · [正式结题验收](00-project/final-research-archive-acceptance-2026-10-09.md) · [正式研究报告](09-roadmap/management-final-public-evidence-2027-2029.md) · [最终汇报归档](09-roadmap/leadership-decision-pack/archive/README.md)

## 一、项目目标与研究边界

**核心问题：** 2027—2029 年，智能手机从“单次 AI 请求”走向“持续、多阶段、可执行操作的 Agent 工作流”后，哪些 CPU/系统能力会真正影响性能、能耗、响应体验和可靠性？现有软硬件技术已经解决了什么，什么问题还有值得投入的增量价值？

研究范围包括：

- **目标平台：** 智能手机为主；平板仅在能够解释手机技术方向时作为辅助。重点关注 AArch64 移动 CPU。
- **技术层次：** CPU 核心与微架构、存储/缓存、LLVM/MLIR 与现有 ISA、CPU↔GPU↔NPU 协同、运行时与操作系统、低功耗及可信 Agent 工具操作。
- **决策输出：** 重要负载变化、业界与学术界现有方案、最强替代基线、工程优先方向、条件研究储备、暂不投资事项，以及 2027/2028/2029 分阶段技术路线。
- **证据要求：** 优先原始论文、权威会议与学者、专利权利要求、官方技术文档和已公开发表的实验；区分**来源已证明的事实、跨来源推断、待证实假设和无法支持的主张**。

**研究硬约束：仅使用公开资料。** 本项目没有进行，也不安排自行真机测试、仿真、性能测量或 PoC。公开资料无法回答的硬件问题会记录为证据边界，不会用虚构实验结果或强行凑满投资名额来填补。

## 二、当前进展：研究已结题，交付归档基本完成

| 工作阶段 | 当前进展 | 权威入口 |
|---|---|---|
| 研究目标与最终问题定义 | **完成**：已建立七个决策问题与跨层技术范围 | [七问与累计研究状态](00-project/final-questions-status.md) |
| 文献、专利、官方资料与已有能力对照 | **完成当前决策所需范围**：关键原始来源、成熟软件基线、反证及独立性已审计 | [原始证据目录](01-evidence/README.md) · [关键来源审计](analysis/audits/round15g-final-source-and-ssot-audit-2026-10-08.md) |
| 技术机会辨析及方向收敛 | **完成**：区分可实施工程、条件储备和缺乏证据的新硬件主张 | [现行技术组合](09-roadmap/current.md) |
| 2027—2029 技术路线与研究报告 | **完成**：分年度、分技术层形成有边界建议 | [最终管理技术洞察报告](09-roadmap/management-final-public-evidence-2027-2029.md) |
| 领导汇报材料 | **完成制作**：17 页可编辑 PPT，17 页详细讲者备注；仍待 Windows PowerPoint/实际投影使用体验确认 | [汇报成品归档索引](09-roadmap/leadership-decision-pack/archive/README.md) |
| 研究仓库归档与质量检查 | **通过结构性验收**：已修复历史失效链接、澄清新旧文档及关键入口；不代表全网资料今日均已重新验证 | [全仓归档审计](analysis/audits/repository-wide-archive-and-currentness-audit-2026-10-09.md) |

**结题判定：** 七问已达到公开资料能够支持的技术管理决策深度；其中“新增 Agent 专用 CPU 硬件是否具有不可被现有软硬件吸收的独特收益”仍缺乏直接充分证据。**这是明确的结论边界，不是本轮必须执行实验的遗留任务。** 详见[正式结题验收](00-project/final-research-archive-acceptance-2026-10-09.md)。

## 三、目前最重要的技术洞察

### 1. 手机 Agent 工作负载出现四类值得关注的变化

1. **持续会话与可信行动：** Agent 跨应用调用工具，不仅要完成推理，还要检查权限、操作对象、真实效果和异常恢复。
2. **CPU/NPU/GPU 多阶段反复执行：** 模型计算、工具调用与数据处理交替出现，真实收益取决于算子覆盖、数据搬运、回退、调度及前台体验，而非单个加速器峰值性能。
3. **可修改、可撤销的状态生命周期：** 工具结果、缓存和派生数据可能失效；先比较软件版本化、事务与资源管理能力，再讨论是否存在不可替代的物理机制。
4. **主动感知与低功耗决策：** 系统不只需要“能运行模型”，还要判断何时值得唤醒、执行或不行动，并考虑隐私、电池与打扰成本。

这些负载变化被归纳为**执行与状态生命周期、主动低功耗准入、语义进度与体验质量**三类跨层研究主题；它们**不等于三个新的 CPU 硅片项目**。

### 2. 当前技术组合：三项工程优先、三项条件储备、零项新增硬件主押注

| 类型 | 技术方向 | 当前判断 |
|---|---|---|
| **优先工程 ①** | CPU/LLVM 现有 AArch64/SME2 能力、微内核、数据布局与 CPU/NPU 分阶段快速路径（CG-06） | 利用现有 ISA 与强异构后端开展工程优化；不能宣称 CPU 对所有 Agent 推理天然更快 |
| **优先工程 ②** | 可信 Agent 工具执行、权限/目标确认、真实效果核验与有界恢复（PT-A） | 主要属于 Agent 平台、运行时及 OS 的工程合同，不是专用 CPU 指令 |
| **优先工程 ③** | CPU/GPU/NPU 异构资源管理、关键路径与前台体验优化（C） | 优先对照已有运行时、系统调度与平台接口 |
| **条件研究储备 3 项** | Agent 私有进度信息（A）；跨引擎派生状态的物理有效性（B-residual）；CPU 续执行局部性（R2） | 保留为待新公开证据支持的问题，**不代表已批准设计或量产** |
| **新增差异化 CPU 硬件主押注：0 项** | Agent 专用新 ISA/缓存/预测器/状态原语等 | 当前公开资料不足以证明相对于强软件与现有硬件基线的新增必要性 |
| **跟进或不启动** | 低功耗 Agent、通用缓存等持续跟进；无依据的 Agent 语义硬件新颖性主张暂不立项 | “不投入独有硬件”不等于放弃有价值的软件功能 |

**重要历史纠正：** A 曾在旧方案中被列为硬件主押注，现已正式降级为**条件研究储备**。以 [当前技术组合](09-roadmap/current.md)和[正式决策事件](08-decisions/events/DEC-A-008.md)为准，不能引用旧版本的评分作为今天的立项依据。

## 四、关键资料入口（按阅读需求）

| 你想了解什么 | 建议从哪里读 |
|---|---|
| **新聊天或新成员如何接手** | [CONTINUE-HERE：当前状态、权威文档与恢复规则](CONTINUE-HERE.md) |
| **研究最后得出了什么，为什么** | [2027—2029 年正式技术洞察报告](09-roadmap/management-final-public-evidence-2027-2029.md) |
| **现在建议投入、储备和停止什么** | [唯一生效的技术组合](09-roadmap/current.md) · [正式决策事件目录](08-decisions/README.md) |
| **七个问题是否都回答了** | [七问研究进展](00-project/final-questions-status.md) · [结题验收](00-project/final-research-archive-acceptance-2026-10-09.md) |
| **具体来源、论文机制及证据局限** | [论文/专利/厂商/工具资料库](01-evidence/README.md) · [来源与独立性审计](analysis/audits/round15g-final-source-and-ssot-audit-2026-10-08.md) |
| **CPU/LLVM 与 SME 等技术细节** | [CPU/LLVM 技术机制与最强 NPU 反证](analysis/engineering/round15f-cpu-llvm-compiler-pressure-2026-10-08.md) |
| **PPT、全部备注及制作历史** | [最终 PPT 归档索引](09-roadmap/leadership-decision-pack/archive/README.md) · [17 页备注原文](09-roadmap/leadership-decision-pack/archive/round16c-17-page-speaker-notes-2026-10-09.md) · [历史设计与 QA](09-roadmap/leadership-decision-pack/diagram-specs/README.md) |
| **仓库结构、质量及历史记录** | [项目治理](00-project/README.md) · [全仓文件与链接审计](analysis/audits/repository-wide-archive-and-currentness-audit-2026-10-09.md) · [研究历史](history/README.md) |

### 数据与目录怎样组织

本仓不是单篇研究报告，而是可追溯的技术研究资料库：

`01-evidence` **原始证据** → `02-claims` **技术主张** → `03-evidence-cases` **支持、反证与边界** → `06-trends / 06-opportunities / 06-directions` **趋势、机会与方向** → `08-decisions` **决策事件** → `09-roadmap` **现行路线与汇报**。

人员机构与已有能力分别保存在 `04-actors`、`05-capabilities`；`views/graph` 是衍生关系图，不替代上述权威对象。旧迁移过程和历史研究轮次保留在 `00-project`、`history` 等位置，但不能覆盖当前已生效的方向决策。

## 五、最终 PPT 保存在哪里？

**最新版本为 17 页可编辑演讲版，逐页备注遵循“先解释 PPT 内容，再逐条解读来源及论据”。**

- **GitHub 已归档：** [全部 17 页备注文字](09-roadmap/leadership-decision-pack/archive/round16c-17-page-speaker-notes-2026-10-09.md)、[交付清单与文件哈希](09-roadmap/leadership-decision-pack/archive/README.md)、逐页设计与质量检查记录。
- **ChatGPT Library 已保存：** `/Research-Archives/Agentic-CPU-uArch/2026-10-09/`，包含最终可编辑 PPTX、完整交付 ZIP、备注稿与校验清单。
- **GitHub 尚待补充：** 将 PPTX、PDF 与完整交付包作为版本化 GitHub Release 资产上传。**在真实 Release 链接出现前，不应声称 PPT 二进制已归档到 GitHub。**
- **使用前仍需确认：** Windows PowerPoint 字体、讲者备注显示与实际投影效果；它们不影响本轮研究结题状态。

## 六、后续如何维护

**默认不再进行宽泛新增研究。** 只有出现足以改变技术判断的**新公开原始证据**，或者发现关键来源、归属、数字或引用错误时，才针对受影响的问题重新审查，更新对应的证据、主张、方向与决策事件，再同步管理报告及 PPT。

研究结论属于截至 **2026 年 10 月 9 日**的公开证据判断，并非已获批准的组织预算、产品量产承诺或对 2029 年行业格局的确定预测。

> **研究资料仓库：** 当前唯一权威为 `xjs-work-lab/agentic-CPU-uArch` 的 `main` 分支；旧仓 `xiejinsen/agentic-CPU-uArch` 及旧版实验/路线图只保留历史追溯意义。通用研究与洞察汇报 Skill 已单独归档在 [skills-lab](https://github.com/xjs-work-lab/skills-lab)，不属于本研究事实的权威来源。
