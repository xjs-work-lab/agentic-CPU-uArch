# SlidePoise PPT 前置设计区（中文）

> **2026-10-23｜DRAFT v0.1｜尚未进入图像生成和可编辑 PPT 构建。**
> 本目录用于在聊天窗口形成可审计的技术内容、图形约束、图像候选与 GitHub 归档，再将被批准的输入交给本地 SlidePoise 执行 native PPT reconstruction。

## 当前已完成

| 文件 | 功能 | 状态 |
|---|---|---|
| [01-deck-outline.md](01-deck-outline.md) | 17 页叙事顺序、中心主张、上下页论证关系与冻结门槛 | DRAFT v0.1 |
| [02-slide-contracts.md](02-slide-contracts.md) | S01–S17 逐页内容、机制、图形、证据与拒收条件 | DRAFT v0.1 |
| [05-visual-spec.md](05-visual-spec.md) | 学术技术风格、SlidePoise 正文画布、原生对象与全过程 QA | DRAFT v0.1 |

## 后续计划（未完成，不要误认已有文件）

1. `03-evidence-map.md`：关键实验数字、论文、设备/模型/基线、结论、反证逐页对应。
2. `04-risk-boundaries.md`：高危错讲、错误数据混比、历史失效决策和图形禁区。
3. 在本地一次性导出 SlidePoise doctor、实际 Profile、frame/content canvas、中文字体与 Speaker Notes 支持情况；存为可审计的预检记录。**画布未确认之前，聊天图像只能标记 concept_only。**
4. 聊天窗口生成 S03/S05/S08/S15 四页视觉候选，逐张审查并将 PNG、manifest、精确尺寸/哈希及已知缺陷保存到 GitHub。
5. 编写 `07-work-mode-handoff.md`；本地严格按 SlidePoise 原生重建路径制作小样、渲染审计并完成 17 页可编辑 PPTX。

## 事实来源与重要边界

- [Agentic CPU 详细研究终稿（2026-10-20）](../../agentic-cpu-uarch-detailed-research-summary-cn-2026-10-20.md)提供内容基础；实际结论以 [current.md](../../current.md) 和正式决策事件为准。
- [2026-10-09 旧版 17 页备注](../archive/round16c-17-page-speaker-notes-2026-10-09.md)的页序与 2026-10-20 综合稿存在差异，只能按主题重新映射，**不可直接按页码粘贴**。
- 当前公开资料范围内有三项工程/平台优先、三项条件研究、零项得到充分公开证据支持的新增专用 CPU 硬件主押注。不能把任何储备方向说成已经批准的硅片设计。
- 本目录文本已归档到 GitHub；**不代表 PNG、Speaker Notes、PPTX/PDF 已生成或上传**。
