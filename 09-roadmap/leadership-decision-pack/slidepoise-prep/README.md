# SlidePoise PPT 前置设计区（中文）

> **2026-10-23｜DRAFT v0.1｜尚未进入图像生成和可编辑 PPT 构建。**
> 本目录用于在聊天窗口形成可审计的技术内容、图形约束、图像候选与 GitHub 归档，再将被批准的输入交给本地 SlidePoise 执行 native PPT reconstruction。

## 当前已完成

| 文件 | 功能 | 状态 |
|---|---|---|
| [01-deck-outline.md](01-deck-outline.md) | 17 页叙事顺序、中心主张、上下页论证关系与冻结门槛 | DRAFT v0.1 |
| [02-slide-contracts.md](02-slide-contracts.md) | S01–S17 逐页内容、机制、图形、证据与拒收条件 | DRAFT v0.1 |
| [03-evidence-map.md](03-evidence-map.md) | S01–S17 的论文、设备/模型/基线/数值、证据等级和待核原图 | 仓内证据交叉核对 v0.1 |
| [04-risk-boundaries.md](04-risk-boundaries.md) | P0/P1/P2 拒收条件、16 条高风险表达与图形防误用规则 | 已归档 v0.1 |
| [05-visual-spec.md](05-visual-spec.md) | 学术技术风格、SlidePoise 正文画布、原生对象与全过程 QA | DRAFT v0.1 |
| [06-sample-slides-manifest.md](06-sample-slides-manifest.md) | 四张真实 SVG 矢量概念图、Git blob SHA、技术审查与未完成的真实渲染检查 | 四图 CONCEPT_ONLY，已归档 |
| [07-work-mode-handoff.md](07-work-mode-handoff.md) | 本地最小预检、四页 SlidePoise 重建、备注验证、17 页交付门槛 | Handoff v0.1 |
| [08-profile-adaptation-contract.md](08-profile-adaptation-contract.md) | 用户已上传 Consulting Profile 的冲突分析、独立蓝色科研风 Profile 设计及终端配置流程 | 草案已归档 / 本地未应用 |
| [Academic CPU Profile JSON 补丁](profile-blue/academic-cpu-insight.profile-update.json) | 机器可读的蓝色 Profile 字段 payload，使用 CLI update 并需本机验证 | 候选配置 / 未激活 |
| [Round02 内容/证据审计](qa/round02-content-evidence-audit-2026-10-23.md) | 17 页逐页审稿、已修问题、4 张高风险样页的可执行关系图合同 | 仓内审稿完成，实物制图待验 |
| [Round03 样页概念图审计](qa/round03-visual-concept-audit-2026-10-23.md) | 首轮 ImageGen 候选 P0 拒收、四张 SVG 关系和数值审查及遗留验收项 | 源码审查完成，真实渲染待验 |
| [SlidePoise 最小本地预检](qa/slidepoise-local-preflight-minimal.md) | 仅采集真实 Profile/画布/字体/备注能力，避免在 Work 模式重新探索 | 待用户本地执行 |
| [2026-10-23 实际上传配置审计](qa/slidepoise-preflight-snapshot-2026-10-23.md) | 已核 doctor/profile；发现内置 Consulting 橙色/Georgia 与蓝色中文研究风冲突，resolved canvas 尚缺 | 部分预检通过 / 正式出图未放行 |

## Round04 配置对齐现状（2026-10-23）

- 已从 [slidepoise-config/doctor.json](../slidepoise-config/doctor.json) 与 [profile-show.json](../slidepoise-config/profile-show.json) 核实本地上传配置：Codex、Python、PptxGenJS、LibreOffice、Poppler 均在 doctor 列表中，激活 Profile 为 `consulting`。
- 已确认 `consulting` 原生风格约束为橙色/Georgia/Arial，与项目蓝色科研风相冲突；为避免生成/重建漂移，不通过图片 prompt 粗暴覆盖，也不直接改内置 Consulting。
- 已准备可机器读取的 [蓝色学术 Profile 更新 payload](profile-blue/academic-cpu-insight.profile-update.json) 和 [终端执行合同](08-profile-adaptation-contract.md)，**但尚未在用户本地创建或运行**。
- 原上传数据尚无 `resolved-config.json`；实际 `design.full_slide_px`、frame 高度和 `derived.generation_region_px` 仍未获知，因此四张 SVG 维持 `concept_only`，正式图片仍不能放行。
- 下一步普通终端创建并核验独立 Profile、解析正式 run、上传脱敏后的 resolved config；然后聊天窗口使用实际画布做正式样页图与视觉审计。

## Round03 已完成与下一步

- 已在 [generated-images/](generated-images/) 真实提交 S03、S05、S08、S15 四张 **1600×900 SVG 矢量概念样页**；图中内容、关系和来源分别绑定到研究合同，不是泛化 ImageGen 四宫格图。
- 第一轮自动图片存在 P0 内容错误，已拒收；后续 SVG 设计改为严格受控，并记录在 [Round03 QA](qa/round03-visual-concept-audit-2026-10-23.md)。
- 完成 SVG 的 XML 标签/属性、必需技术内容、文件路径和 Git blob SHA 检查，**没有进行本地完整渲染**，因此还不能声称图像视觉验收通过。
- 接下来：按 [最小本地预检](qa/slidepoise-local-preflight-minimal.md) 在**普通本地终端**取得 SlidePoise frame/substantive canvas/Profile 参数；然后聊天窗口继续正式比例 target image 设计及视觉核验；通过后按 [Work Handoff](07-work-mode-handoff.md) 做真正的 editable PPTX reconstruction。

## Round02 审计摘要

- **内容合同**：S01–S17 共 17 页；10 页可进入概念图设计，7 页有原始图表/接口/复杂关系的额外检查点。它们均非最终 PPT 验收状态。
- **实际修订**：S03 工程与平台的区分、S06 不同测试配置的措辞、S10 Android AppFunctions 来源审查状态、S16「证据不足≠科学否定」。
- **未完成**：本地 SlidePoise Profile/frame/content canvas 快照、精准论文原图/表复核、图片与哈希、Speaker Notes/PPTX 渲染。当前不得标记任何 `accepted-slide.png`。

## 事实来源与重要边界

- [Agentic CPU 详细研究终稿（2026-10-20）](../../agentic-cpu-uarch-detailed-research-summary-cn-2026-10-20.md)提供内容基础；实际结论以 [current.md](../../current.md) 和正式决策事件为准。
- [2026-10-09 旧版 17 页备注](../archive/round16c-17-page-speaker-notes-2026-10-09.md)的页序与 2026-10-20 综合稿存在差异，只能按主题重新映射，**不可直接按页码粘贴**。
- 当前公开资料范围内有三项工程/平台优先、三项条件研究、零项得到充分公开证据支持的新增专用 CPU 硬件主押注。不能把任何储备方向说成已经批准的硅片设计。
- 本目录文本已归档到 GitHub；**不代表 PNG、Speaker Notes、PPTX/PDF 已生成或上传**。
