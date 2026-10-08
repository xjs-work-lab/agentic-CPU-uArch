# 技术领导 PPT 图形规范 — 经过原文复核的模块化制作入口

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

- [Round15J 审计报告](validation-round15j-2026-10-08.md)：11 图静态结构检查、论文证据和未通过 Gate
- [第 4 页 — Snapdragon 三种对照口径](page-04-stage-benchmark-data.md)
- [第 4 页 Round15M V3 · CPU Fallback 概念解释与两类开销](page-04-round15m-v3-cpu-fallback-explained-2026-10-08.md)：纯蓝色可编辑 PPTX/PNG 已在会话制作，待用户审阅。
- [第 4 页 Round15M 可编辑纯蓝色 PPT 样板与量化 QA](page-04-round15m-editable-pilot-2026-10-08.md)：三栏同模型实测，待用户审阅。
- [第 5 页 — ShadowNPU 方法及与 llm.npu 的分离](page-05-npu-software-path.md)
- [第 5 页 Round15K ShadowNPU 双论文分离式技术机制 PPT 样板及 QA](page-05-round15k-visual-pilot-status-2026-10-08.md)：16:9 PNG/PPTX 已在当前会话制作，待用户审阅。
- [第 6 页 — vivo X300 SME2 官方原始数据](page-06-sme2-x300-data.md)
- [第 6 页 Round15K 高保真样板与初步验收记录](page-06-round15k-visual-pilot-status.md)：单页 PNG/PPTX 已在会话交付，待用户视觉审阅
- [第 7 页 — SMEPilot 分配/流水/布局](page-07-smepilot-method.md)
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
