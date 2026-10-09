# 技术领导 PPT 图形规范 — 经过原文复核的模块化制作入口

## Round15Q：封面与目录、原图/程序绘图标准（2026-10-09）

- [**当前封面/目录 V2 和全套技术语言禁用词规范**](leadership-technical-wording-v2-2026-10-09.md)：删除“投资”类展示措辞，封面写清楚具体研发动作，目录仅保留四章名称及页码；前三页可编辑样板已同步替换相关展示文本。
- [封面与目录、四章讲述结构](round15q-cover-agenda-and-chapter-map-2026-10-09.md)：实际制作两页可编辑样板；拟采用 2 张未编号前置页 + 15 张独立编号正文。
- [Python 图表与论文原始 Figure 的选型、裁剪和来源审计](figure-authoring-and-paper-figure-contract-v1-2026-10-09.md)：程序化实数绘图/原文 Figure/概念重绘的不同适用条件。


## Round15L 领导可读性重审（15 页）

- [Round15L 15 页领导可读性审计与逐页改稿方向](round15l-all-15-pages-leadership-readability-audit-2026-10-08.md)：把“标题讲结论、术语需解释、配套技术对准节点、论文基线可见”推广至 15 页。
- [第 5 页 ShadowNPU V2 生产合同：两篇论文分离、支撑步骤、实验基线](page-05-round15k-v2-leadership-readable-and-benchmark-contract-2026-10-08.md)：当前最新试制输入，V1 不再作正式内容源。



本目录用于存放**独立页面的制图规格**。原始 15 页蓝图、领导结论和完整内容合同不被本轮替换；仅对发现的问题做小范围纠正，避免一份巨型 Markdown 需要散点修改。

## 图形语言选型与制作规范

- [多语言制图规范](diagram-authoring-policy-v1-2026-10-08.md)：按技术内容选 Mermaid、PlantUML、Graphviz/DOT、Direct SVG、Excalidraw、SmartArt 或真实数据图；语义合同优先于工具样式。
- [15 页逐页选型表](page-visual-language-routing.md)：逐页推荐逻辑源、实际画法和不可越界条件。

## 面向非专业领导的叙事验收规范

- [领导可读性 Gate：10 秒理解结论、30 秒理解机制](leadership-readability-gate-v1-2026-10-08.md)
- [HeRo 第 8 页 V6 实物制作、PPTX/PNG 文件与基础 QA 记录](page-08-round15k-v6-pilot-qa-2026-10-08.md)：最新单页样板已生成，待用户对领导可读性审阅。
- [HeRo 第 8 页 V6：逐卡解释与公式分层内容合同](page-08-round15k-v6-leadership-readable-copy-2026-10-08.md)：V6 正式文案输入，保留 V5 视觉样式；V6 PPTX 尚未制作。

- [15 页统一页码与页眉规范](slide-page-number-and-header-contract-v1-2026-10-08.md)：正文页码统一 `01 / 15` 至 `15 / 15`，固定页眉位置、字体和蓝色系统；最终合并前逐页验收。
- [Round15P：正文第 1–3 页纯蓝色可编辑 PPT 样板与 QA](round15p-slides-01-03-blue-editable-pilot-2026-10-08.md)：已完成 3 页同源 PPTX/PNG，待用户审阅。
- [Round15J 审计报告](validation-round15j-2026-10-08.md)：11 图静态结构检查、论文证据和未通过 Gate
- [第 4 页 — Snapdragon 三种对照口径](page-04-stage-benchmark-data.md)
- [第 4 页 Round15M V3 · CPU Fallback 概念解释与两类开销](page-04-round15m-v3-cpu-fallback-explained-2026-10-08.md)：纯蓝色可编辑 PPTX/PNG 已在会话制作，待用户审阅。
- [第 4 页 Round15M 可编辑纯蓝色 PPT 样板与量化 QA](page-04-round15m-editable-pilot-2026-10-08.md)：三栏同模型实测，待用户审阅。
- [第 5 页 — ShadowNPU 方法及与 llm.npu 的分离](page-05-npu-software-path.md)
- [第 5 页 Round15K ShadowNPU 双论文分离式技术机制 PPT 样板及 QA](page-05-round15k-visual-pilot-status-2026-10-08.md)：16:9 PNG/PPTX 已在当前会话制作，待用户审阅。
- [第 6 页 — vivo X300 SME2 官方原始数据](page-06-sme2-x300-data.md)
- [第 6 页 Round15K 高保真样板与初步验收记录](page-06-round15k-visual-pilot-status.md)：单页 PNG/PPTX 已在会话交付，待用户视觉审阅
- [第 7 页 — SMEPilot 分配/流水/布局](page-07-smepilot-method.md)
- [第 7 页 Round15N V2 — SME 属于 CPU ISA 扩展的架构层级修正版](page-07-round15n-v2-cpu-isa-hierarchy-pilot-2026-10-08.md)：已重制 PPTX/PNG；经基础 QA，待用户审阅。
- [第 7 页 Round15N SMEPilot 纯蓝色可编辑样板及实验口径 QA](page-07-round15n-smepilot-editable-pilot-2026-10-08.md)：PPTX/PNG 已交付会话，待用户视觉审核。
- [第 8 页 Round15K V5 · 五卡片边界修正与 batch/token 术语澄清](page-08-round15k-v5-layout-and-workload-terms-2026-10-08.md)：当前最新待审版本，V4 有右侧溢出问题。
- [第 8 页 Round15K V4 · 结论式标题与 xPU 术语定义](page-08-round15k-v4-titles-and-xpu-terminology-2026-10-08.md)：当前最新样板，保留 V3 公式和五阶段。待用户视觉审阅。
- [第 8 页 Round15K V3 · 增加公式、输入/判断/输出与技术解释](page-08-round15k-v3-technical-explanation-formulas-2026-10-08.md)：新一轮正式设计与 PPT 样板，待用户审阅；V2 只作为上一轮视觉参考。
- [第 8 页 Round15K V2 重绘试制与箭头 QA](page-08-round15k-v2-redesign-pilot-status.md)：旧版已退回；新版 5 步单向主路径，4 条箭头，待用户评审。
- [第 8 页设计纠错 v2 — 从 HeRo Algorithm 1 重建可读主流程](page-08-hero-design-correction-v2-2026-10-08.md)：当前正式制图输入；前一版 PPT 已判定不通过。
- [第 8 页 — HeRo 动态 DAG 调度（旧机制摘要）](page-08-hero-runtime.md)
- [第 8 页 Round15K 高保真样板、数据与 QA 记录](page-08-round15k-visual-pilot-status.md) · [Graphviz DOT 逻辑源](hero-semantic-graph.dot)
- [第 9 页 — LLVM/CPU、GPU/NPU、Runtime 所有权](page-09-compiler-runtime-ownership.md)

仍沿用：
- [第 1–3 页 Mermaid 设计](../slide-01-03-mermaid-logic-spec-v1-2026-10-08.md)
- [第 10–12 页 Mermaid 初版](../slide-04-15-visual-logic-audit-v1-2026-10-08.md)
- [全套 15 页内容蓝图](../content-storyboard-v1-2026-10-08.md)
- [正式组合](../../current.md)

优先级：现行研究 SSOT > 已经核对的独立 page 制图规格 > 结构审计 v1 > 最早故事板 > 生成的 PNG。Image Generator 的视觉样稿不得反向成为技术事实权威。

- [第 9 页 Round15R：CPU/LLVM 编译路径与 Runtime/OS 责任分工样板](page-09-round15r-cpu-llvm-runtime-ownership-pilot-2026-10-09.md)：可编辑 PPTX/PNG 已制作并完成基础 QA，待用户审阅。

- [第 10 页 Round15S：工具真实效果与跨引擎派生状态有效性样板](page-10-round15s-tool-effect-derived-state-pilot-2026-10-09.md)：可编辑 PPTX/PNG 已完成基础 QA，待用户审阅。
- [第 11 页 Round15T：主动 Agent 低功耗事件初筛与分级唤醒](page-11-round15t-proactive-agent-lowpower-pilot-2026-10-09.md)：可编辑 PPTX/PNG 已制作、证据边界已审核，待用户审阅。
- [第 12 页 Round15U：Agent 专用 CPU 硬件的四道证据检查](page-12-round15u-agent-hardware-four-evidence-gates-pilot-2026-10-09.md)：纯蓝可编辑 PPTX/PNG 已制作，含四关核查、三项待研究问题和来源边界；待用户审阅。
