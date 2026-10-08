# 技术领导 PPT 图形规范 — 经过原文复核的模块化制作入口

本目录用于存放**独立页面的制图规格**。原始 15 页蓝图、领导结论和完整内容合同不被本轮替换；仅对发现的问题做小范围纠正，避免一份巨型 Markdown 需要散点修改。

## 图形语言选型与制作规范

- [多语言制图规范](diagram-authoring-policy-v1-2026-10-08.md)：按技术内容选 Mermaid、PlantUML、Graphviz/DOT、Direct SVG、Excalidraw、SmartArt 或真实数据图；语义合同优先于工具样式。
- [15 页逐页选型表](page-visual-language-routing.md)：逐页推荐逻辑源、实际画法和不可越界条件。

- [Round15J 审计报告](validation-round15j-2026-10-08.md)：11 图静态结构检查、论文证据和未通过 Gate
- [第 4 页 — Snapdragon 三种对照口径](page-04-stage-benchmark-data.md)
- [第 5 页 — ShadowNPU 方法及与 llm.npu 的分离](page-05-npu-software-path.md)
- [第 6 页 — vivo X300 SME2 官方原始数据](page-06-sme2-x300-data.md)
- [第 6 页 Round15K 高保真样板与初步验收记录](page-06-round15k-visual-pilot-status.md)：单页 PNG/PPTX 已在会话交付，待用户视觉审阅
- [第 7 页 — SMEPilot 分配/流水/布局](page-07-smepilot-method.md)
- [第 8 页 — HeRo 动态 DAG 调度](page-08-hero-runtime.md)
- [第 8 页 Round15K 高保真样板、数据与 QA 记录](page-08-round15k-visual-pilot-status.md) · [Graphviz DOT 逻辑源](hero-semantic-graph.dot)
- [第 9 页 — LLVM/CPU、GPU/NPU、Runtime 所有权](page-09-compiler-runtime-ownership.md)

仍沿用：
- [第 1–3 页 Mermaid 设计](../slide-01-03-mermaid-logic-spec-v1-2026-10-08.md)
- [第 10–12 页 Mermaid 初版](../slide-04-15-visual-logic-audit-v1-2026-10-08.md)
- [全套 15 页内容蓝图](../content-storyboard-v1-2026-10-08.md)
- [正式组合](../../current.md)

优先级：现行研究 SSOT > 已经核对的独立 page 制图规格 > 结构审计 v1 > 最早故事板 > 生成的 PNG。Image Generator 的视觉样稿不得反向成为技术事实权威。
