# SlidePoise PPT 前置设计区（中文）

> **2026-10-23｜G1 内容归档已完成；G2 实际 16:9 尺寸的 SVG 视觉候选已入库；尚未生成 SlidePoise 正式 accepted-slide.png 或原生 PPTX。**
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
| [09-frame-and-content-region-contract.md](09-frame-and-content-region-contract.md) | 来自本机解析配置的 2048×1152 全页、41/1070/41 分层及母版职责 | 已核实本地尺寸；母版 PPTX 未验收 |
| [10-formal-content-region-samples.md](10-formal-content-region-samples.md) | 四张新版 2048×1070 正文矢量设计 + 四张完整 16:9 页壳组合预览；Git blob 与 SHA-256 | 真尺寸候选完成，视觉渲染待验 |
| [S05 语义连线合同](generated-images/formal-content-v02/S05-edge-contract-v02.json) | 10 个节点、13 条语义边和条件性分支，用于未来原生 PPT 箭头重建 | 已冻结为参考结构 |
| [蓝色母版建议 run overrides](profile-blue/academic-cpu-run-session-overrides.proposal.json) | 页眉、页脚短标签与原生页码开关；与本机实际设置区别记录 | 仅建议，尚未在本地应用 |
| [Round04 真尺寸静态审计](qa/round04-verified-canvas-static-design-audit-2026-10-23.md) | 实际画布、8 张 SVG 结构、关键数据/连线与未完成 G2/G3 | 静态通过，真实渲染待验 |
| [本机已解析的安全画布摘要](../slidepoise-config/slidepoise-preflight-export.json) | 正式 `academic-cpu-insight`、2048×1152 全页及 2048×1070 正文尺寸 | GitHub 已读取并确认 |
| [07-work-mode-handoff.md](07-work-mode-handoff.md) | 本地最小预检、四页 SlidePoise 重建、备注验证、17 页交付门槛 | Handoff v0.1 |
| [08-profile-adaptation-contract.md](08-profile-adaptation-contract.md) | 从 Consulting 迁移到蓝色学术 Profile 的历史执行合同 | 本地已成功应用；记录供审计 |
| [Academic CPU Profile JSON 补丁](profile-blue/academic-cpu-insight.profile-update.json) | 蓝色 Profile 修订内容；对应用户本地运行的配置 | 已应用，用户 preflight 验证 |
| [Windows CMD 一键配置脚本](scripts/configure-slidepoise.py) | 蓝色 Profile、正式 run、安全画布摘要生成 | 用户已执行成功 |
| [Round02 内容/证据审计](qa/round02-content-evidence-audit-2026-10-23.md) | 17 页逐页审稿、已修问题、4 张高风险样页的可执行关系图合同 | 仓内审稿完成，实物制图待验 |
| [Round03 样页概念图审计](qa/round03-visual-concept-audit-2026-10-23.md) | 首轮 ImageGen 候选 P0 拒收、四张 SVG 关系和数值审查及遗留验收项 | 源码审查完成，真实渲染待验 |
| [SlidePoise 最小本地预检](qa/slidepoise-local-preflight-minimal.md) | 最初的本地执行检查清单 | doctor/profile/解析画布已完成，Notes 待测 |
| [2026-10-23 最初配置审计](qa/slidepoise-preflight-snapshot-2026-10-23.md) | 历史审计：当时只有 doctor/profile，尚缺 run resolve | 已被新上传 preflight 结果补齐 |

## Round09 S03 总体决策页已生成并完成静态审计（2026-10-23）

- S03 是领导决策分层页：**3 项工程/平台优先、3 项条件研究储备、0 项有充分公开证据支持的新 Agent 专用 CPU 硬件主押注**。自然语言说明了每项做什么与重开硬件讨论的证据门槛。
- 本轮已真实生成正文 PNG（2048×1070）和完整 16:9 预览（2048×1152），检查了 57 个文字对象，未发现画布外越界；PNG/ZIP 已做实际渲染与完整性检查。
- **[S03 内容锁定与 native 重建合同](14-s03-approved-copy-and-reconstruction-contract.md)**、**[Round09 审计报告](qa/round09-s03-decision-portfolio-audit-2026-10-23.md)**、**[Speaker Notes](notes/S03-speaker-notes-2026-10-23.md)**、**[Work handoff](S03-work-handoff-v01.md)**、**[PNG/ZIP 哈希清单](generated-images/formal-content-v02/S03-controlled-png-v01.manifest.json)** 已归档。
- S03 完整素材 ZIP 包含正文 PNG、整页预览、SVG、QA、Notes、handoff、构建脚本及四个装饰图标；该 ZIP 通过当前聊天附件交付，**不是 GitHub 文件链接**。
- **GitHub 当前只保存文本合同、审计、Notes、handoff 和 manifest；PNG、SVG 与 ZIP 二进制尚未提交 GitHub**。不把哈希登记误写成二进制入库。
- S03 当前状态：`CONTENT_AND_RENDER_CANDIDATE / USER_VISUAL_SIGNOFF_PENDING`。还没开始 SlidePoise 原生 PPTX 试制。

## 当前有效的四页 PNG 二进制交接（2026-10-23）

- **四页素材已经永久保存到 ChatGPT Library**，路径：`/Agentic-CPU-uArch/slidepoise/four-slide-pilot/`，含 S03/S05/S08/S15 各一张 2048×1070 正文 PNG、各一张 2048×1152 全页预览 PNG、各一份完整源 ZIP：12/12 上传成功，上传后独立 list 验证。
- 抽取 S03 正文 PNG 和 S08 ZIP 从 Library 回写为原始字节并执行 SHA-256，和原图值一致。
- 当前唯一可执行的取图说明：[四页 Library 二进制交接](15-library-binary-handoff-and-github-archive.md)；具体 [文件名、字节数、SHA-256 manifest](binary-assets/four-slide-pilot/library-assets-manifest.json)。Work 应优先检索 Library，若访问不到，由用户在 Work 中从 Library 附加四个 ZIP。
- 注意区分状态：**ChatGPT Library 中的真实二进制已存好**，但 **GitHub 仓库中还没有这十二个二进制文件**。只有 Work 真正提交并 GitHub read-back 后才可写 GitHub PNG 归档完成。
- 当前阶段：视觉已获用户认可的四页可做 native PPTX 试制，16:9 全页、上下 frame 各 41px、正文 2048×1070；尚未在 Work 制成 PPTX。
## Round08 S15 技术路线目标 PNG 已生成（2026-10-23）

- 已在本次对话中真正生成 **S15 正文 PNG 2048×1070** 和 **标准 16:9 全页预览 2048×1152**，并附有 SVG、5 个 Image2.5 装饰图标、构图脚本、QA 与完整讲者备注的 ZIP。
- Image2.5 首张全页草图含未经证实的 2029 硬件/规模化研发里程碑，**P0 拒收**；仅使用它生成的 5 个无文字图标，最终 5 技术层×3 年路线以研究终稿和 current.md 的真实合同重绘。
- **[S15 技术内容与 Work 原生重建合同](13-s15-roadmap-content-and-reconstruction-contract.md)**、**[Round08 视觉/事实 QA](qa/round08-s15-image2p5-and-roadmap-audit-2026-10-23.md)**、**[PNG/SVG/ZIP 哈希清单](generated-images/formal-content-v02/S15-controlled-png-v01.manifest.json)** 和 **[演讲者备注](notes/S15-speaker-notes-2026-10-23.md)** 均已写入 GitHub。
- 已实物渲染/目视检查，65 个受控文本对象无画布外溢，且未产生非法加速数字或“2029 硬件必定交付”结论。**等待最终用户视觉确认与 SlidePoise native PPTX 验收**。
- PNG/ZIP 二进制可在当前聊天下载；**本轮 GitHub 归档的是文本合同、QA 和哈希清单，还未真正把 PNG/ZIP 二进制推送到 GitHub**，请勿写成已存仓。

## Round07 S08 SME2 目标图与手机数据审查

- 本次对话已真实生成 **S08 正文 2048×1070 PNG** 与 **16:9 整页 2048×1152 预览 PNG**。Image2.5 的蓝色芯片插画只承担审美素材，CPU/SME2 层级与 vivo X300 的实验数字由受控矢量内容生成。
- **[S08 技术/文本/原生重建合同](12-s08-approved-copy-and-reconstruction-contract.md)**：明确 INT8 555.8→304.1ms、FP16 1163.0→298.2ms、数据移动 41.4%/39.9%、单核 Normal mode、SqueezeSAM 视觉任务与不能外推的范围。
- **[Round07 实际 PNG/实验审计](qa/round07-s08-image2p5-and-measurement-audit-2026-10-23.md)** + **[S08 哈希与素材清单](generated-images/formal-content-v02/S08-controlled-png-v01.manifest.json)** 已入库，55 个图中文字对象未检测到越界，CPU/SME2 结构正确；仍待用户最终视觉签收。
- 与 S05 同样：**本次连接尚未把 PNG 二进制真正提交至 GitHub**；现有的真实文件从当前对话附件下载，后续可把 ZIP 一并交给本地 Work。没有 `accepted-slide.png` 或 native PPTX，不虚报。
- 下一张候选为 **S15：2027–2029 分层技术路线**。优先采用本轮的 Image2.5 视觉素材 + 受控文字/图表混合路径，不允许模型自由添加路线日期、研发承诺或数据。

## Round06 S05 受控原始 PNG 已生成（2026-10-23）

- **本轮有真实 PNG 文件，不再只是 SVG 视觉规范**：`S05-controlled-content-v04.png`（2048×1070 正文）、`S05-16x9-frame-preview-v04.png`（2048×1152 完整 16:9 示意）。
- 依据 [S05 内容锁定合同](11-s05-approved-copy-and-reconstruction-contract.md) 与 [S05 DAG 边合同](generated-images/formal-content-v02/S05-edge-contract-v02.json)，重新绘制了 10 个节点、13 条有向边；实际渲染后进行了技术事实与视觉布局检查；没有无依据的加速/节能/带宽图。
- PNG 保留用户认可的 Image2.5 蓝白视觉体系，但**主要文字、节点与箭头由程序受控准确排版**，并非图片模型自由生成的新技术数据。
- [Round06 实物 PNG 质量审计](qa/round06-s05-png-content-control-render-2026-10-23.md)和 [含 SHA-256 的 PNG Manifest](generated-images/formal-content-v02/S05-controlled-png-v04.manifest.json) 已写入 GitHub。**二进制 PNG 当前以聊天可下载附件交付，尚未真正上传 GitHub**；本仓本轮仅已归档 QA 文本及 Manifest，绝不将 PNG 状态冒称为 GitHub 已有文件。
- 当前候选状态：`content_safe + rendered_preview_reviewed + user_visual_signoff_pending`；还不是本地 SlidePoise `accepted-slide.png`，也不是可编辑 PPTX。

## Round05 S05 图像内容审计（本轮最新关口）

- 用户认可两张 Image2.5 视觉版式，但**认可视觉不等于认可技术内容**。两张 S05 均含无来源算子加速/端到端效益；第三次尝试修图仍生成 40–60% 等无证据统计，全部 `REJECT_TECHNICAL_P0`。
- [Round05 审计报告](qa/round05-s05-imagegen-content-audit-2026-10-23.md)逐项说明哪些可保留、哪些必须删除。
- [S05 文案、DAG、备注与 native 重建锁定合同](11-s05-approved-copy-and-reconstruction-contract.md) 为 **S05 页面科学内容的唯一权威**，并有 [机器可读文案与禁用数字](generated-images/formal-content-v02/S05-locked-content-v03.json) 及 [机器可读 DAG 边合同](generated-images/formal-content-v02/S05-edge-contract-v02.json)。
- **工作阶段规则**：Image2.5 只可产生视觉候选，未经本轮合规审稿不能标 `accepted-slide.png`；Work 负责原生可编辑重建，不能从有问题 PNG 重新编造技术内容，见 [07 Work Handoff](07-work-mode-handoff.md)。
- 目前还没有通过技术+视觉双审核的 S05 Image2.5 PNG。**不能虚报已生成/上传正式 PNG。**

## 最新状态（2026-10-23，优先阅读）

- **画布真值已获证实**：用户上传的 [slidepoise-preflight-export.json](../slidepoise-config/slidepoise-preflight-export.json) 显示 `academic-cpu-insight` 已实际应用，全页 **2048×1152 16:9**，header/footer 各 41px，正文 **2048×1070**，全页 y 偏移 41px。
- **新一轮成果**：四张重新排版的 [正文 SVG + 16:9 整页示意](10-formal-content-region-samples.md) 已保存；[09 母版合同](09-frame-and-content-region-contract.md) 区分动态结论标题、引用区、共享 frame 与 PowerPoint 原生页码，未拉伸旧 1600×900。
- **内容真实性**：S03 正式三工程/三储备/0 硬件主押注，S05 有向 DAG，S08 CPU 内 SME2 与来源绑定的手机测量，S15 技术层×三年路线。源级静态审核记录在 [Round04 QA](qa/round04-verified-canvas-static-design-audit-2026-10-23.md)。
- **尚未完成**：真实全分辨率图形渲染与人工目视、SlidePoise packaged image-generation request、`accepted-slide.png`、真实 PowerPoint 原生重建、母版/页码/Notes 验证。因此目前**不能把这四张 SVG 标为正式交付 PPT 页面**。
- **下一步**：四页目标图真实渲染/冷读复核 → SlidePoise 官方管线生成并验收四页原生 PPTX → 扩展其余 13 页；不要重新要求用户做已经完成的本地 profile/canvas 预检。

## 历史过程记录（以下 Round03/02 只反映当时阶段，不覆盖最新状态）

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
- 本目录文本及 8 张真实 SVG 矢量设计/预览已归档到 GitHub；**不代表正式 PNG、Speaker Notes、PPTX/PDF 已生成或上传**。
