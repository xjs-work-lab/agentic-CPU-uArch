# 05｜SlidePoise 技术研究 PPT 视觉与可编辑重建规范（v0.1）

> DRAFT｜2026-10-23｜为 Agentic CPU 微架构技术领导汇报服务。此文件定义视觉判断原则、页面角色、图形关系和重建 QA；**不是可代替本机 Profile JSON 的运行配置；当前本地 Profile/画布已被证实，正式 SlidePoise ImageGen target 和 PowerPoint 渲染仍未完成**。  
> SlidePoise 官方依据：[Skill](https://github.com/henryhyw/slidepoise/blob/main/slidepoise/SKILL.md)、[Deck orchestration](https://github.com/henryhyw/slidepoise/blob/main/slidepoise/references/deck-orchestration.md)、[Reconstruction](https://github.com/henryhyw/slidepoise/blob/main/slidepoise/references/reconstruction.md)、[Workflow](https://github.com/henryhyw/slidepoise/blob/main/slidepoise/references/workflow.md)。

## A. 视觉意图：研究型、精确、有解释力

- **读者**：公司技术领导，其中有 CPU/编译背景和对 Agentic AI 不熟悉者。每页必须可独立看懂「结论—为什么—技术后果」。
- **气质**：学术论文图的精确性 + 技术管理汇报的叙事清晰度。严禁为了科技感添加无解释价值的发光、假三维芯片、背景数据流和廉价图标。
- **输出**：16:9 中文可编辑 PPTX；讲者备注含逐条来源说明；PDF 仅作预览副本。高信息量但不使用密集的小字填满每个空位。
- **主调色**：深海军蓝/中蓝/浅蓝的同色系分层，加白、冷灰作中性背景。用线型、图例、文本和空白辅助区分语义，不仅靠深浅蓝。避免紫、橙、红、绿等多种高饱和混用；错误/证据警示不必硬使用红色。
- **风格基线**：优先自建 `Academic Technical Insight` Profile（可继承 SlidePoise Consulting 的功能，但不照搬咨询页的泛用装饰）。Profile 仅是视觉资源与配置选择，不得覆盖本研究事实。
- **元素形态**：短而完整的结论标题；源于实际关系的节点/矩阵/箭头；细线型 icon；克制圆角；少量必要阴影；不要大块渐变抢走主图视觉权重。

## B. 共享框架与正文画布——重要的 SlidePoise 硬约束

### 2026-10-23 本机实测配置更新（当前设计以此为准）

- 用户已上传实际运行的 [SlidePoise preflight](../slidepoise-config/slidepoise-preflight-export.json)：Profile academic-cpu-insight、全页 **2048×1152（16:9）**、header/footer 各 **41px**、substantive content **2048×1070**、全页起点偏移 y=41。
- 四张新正文 SVG 和整页 16:9 母版组合预览已归档在 [10-formal-content-region-samples.md](10-formal-content-region-samples.md)，旧 1600×900 版本只作历史参考，不得拉伸。
- 本规范下方某些较早表述中的“待导出本地配置”是历史背景；实际尺寸已获证实。仍未完成的是 **真实图像渲染目视、accepted-slide.png、native PPTX、Notes 回读**。
- Header/footer 的实际 left/right 文案当前为空；预览中的母版标签来自 [建议 run override](profile-blue/academic-cpu-run-session-overrides.proposal.json)，不是本机已应用设置。


**SlidePoise 官方要求：图像生成对象是实质内容区，不是整张 PowerPoint 页面。** 完整 16:9 幻灯片的共享页眉、页脚、页码等在 PowerPoint 的 inherited frame 中生成；图片生成画布高宽必须在读取实际已选 Profile/运行时配置后，扣除已启用页眉/页脚高度计算，不能默认 16:9 原图直接铺满。

### 待本地一次性导出、放入 GitHub 的 Preflight Snapshot

在**开始可重建目标图生成之前**，在已配置的本地环境执行并记录：
- `slidepoise doctor`
- `slidepoise profile show`（若使用自定义 profile，应明确其实际 ID 和选用资源）
- 当前 presentation override/解析后的 full-slide size、enabled header/footer size、content canvas ratio、字体可用性、图像生成服务模式与版本
- 标准中文字体和英数/希腊符号字体、是否具备 LibreOffice/Poppler 的预览能力
- 是否可通过原生构造/后处理可靠写入与读取每页 PowerPoint Speaker Notes；这一项**未从现有 SlidePoise 官方资料确定**，必须一页实测

若 **content canvas 长宽比未核定**：聊天窗口只可生成「视觉方向草案」，不得贴 `accepted-slide.png`、不得声明已满足 SlidePoise reconstruction invariant。记录为 `concept_only`，本地需按正确画布重新编译请求/生成或经合规裁切审查。

### 推荐共有框架（须按本地能力落地）

| 角色 | 建议处理 | 全局检查 |
|---|---|---|
| 顶部主标题 | 结论式中文句子，原生 PPT 文字；如由 inherited header 承担，图片中不重复 | 同级内容页使用同一文字角色、字号、粗细和距主图区 |
| 可选章节/副标题 | 只在能帮助定位时出现；绝不代替主张 | 与主标题不冲突、不重复标题 |
| 主体内容 | 由 page-specific concept image 探索后映射为 native text/shapes/tables/connectors；必要照片等独立资源保留 | 不拉伸来源图，不把全页扁平化 |
| 引用/来源 | 统一底部引文带或主图紧邻的数据来源；不能与页脚、页码冲突 | 字号、对齐和可读性稳定；可追溯到具体原文 |
| 页码 | 全套封面 01/17、目录 02/17、结尾 17/17 | 统一 PowerPoint 页脚绘制，禁止图片内重复 |
| 边界注记 | 重要、影响本页结论的限定应放实质内容区；常规来源可放引用区 | 不把关键反证完全藏到讲者备注 |

> **标题归属必须先定。** 如果已安装 SlidePoise 的配置不能在 inherited header 放动态逐页主标题，就使用原生 PowerPoint 文字层实现统一标题角色，并为其预留区域；不能一边生成带标题图、一边由 PowerPoint 再加同一标题。

## C. 可读信息密度与字体设计

- 投影不是论文 PDF。每页从「一个主结论 + 一个有意义的主视觉 + 2–5 条必要解释」组织信息；如非常复杂，可使用主图 + 侧边解释，但不能重复同义内容。
- 字体和中文混排优先选择环境已有、Windows PowerPoint 与 LibreOffice 可较稳定替换/渲染的字体。没有核实字体前不要依赖罕见专有字体；禁打包、传播第三方字体文件。
- 参考而非机械验收门槛：大标题约 26–31 pt、正文约 14–18 pt、图中必要标记约 11–15 pt、引用约 9–11 pt。实际由页面的信息作用、字数与 100% 渲染结果判断；不靠「最小字号达标」冒充好设计。中文文本要避免英文排版产生的孤行、单字掉行。
- 视觉留白有明确职能：标题和证据图之间留出层级，右侧文本与流程图保持可追踪对应，底部留出引用/页码而非任意扩大黑洞。
- 相同职能的文字使用同一 `role` 样式：内容页标题、图内节点标题、注解、数值标签、表头、来源行、页码；跨页复核实际 PPT 对象字体与渲染，而不只比较图片美感。
- 图表数值加粗用于提示重要结果；勿通过巨大数字掩盖「最高值/测试条件」这些限定。

## D. 按内容选择主视觉，而不是让模板规定内容

| 页面 | 优先视觉结构 | 必须解决的阅读问题 |
|---|---|---|
| S01 | 克制的概念封面 | 研究对象、技术范围、规划窗口 |
| S02 | 四段章节导航 | 这份报告如何一步步得出判断 |
| S03 | 分层技术决策与跨层抽象 | 工程优先、储备、无证据硬件主押注有何不同 |
| S04 | Agent 生命周期环 / 条件反馈 | 工具结果验证与状态更新区别于单次推理 |
| S05 | 动态有向 Stage DAG | 哪些步骤并行、哪些依赖、为什么要阶段调度 |
| S06 | 分阶段比较 + 开销分解 | 为什么算子更快不一定端到端更快 |
| S07 | llm.npu 与 ShadowNPU 机制剖析 | 为什么 NPU 软件前沿会改变执行分工 |
| S08 | CPU 内部 SME2 技术结构 + 独立设备实验面板 | SME 属于 CPU；现有 ISA 优化收益边界 |
| S09 | DAG 调度与前台 DRAM 资源争用双视图 | HeRo 与 SERENO 回答的是两个互补问题 |
| S10 | 带判定与异常分支的工具执行流程 | API 成功 ≠ 真实效果已验证 |
| S11 | 软件可观察账本 vs 窄残余假设 | 什么已经能由软件得到、什么仍是猜想 |
| S12 | 跨层功能/所有权架构 | Agent、Runtime、OS、CPU/LLVM、XPU 怎么分工 |
| S13 | 三条差异化技术责任链 | 哪些能力可推进、交叉接口在哪里 |
| S14 | 强基线—证据缺口—升级门槛矩阵 | 为什么三项储备不是立项 |
| S15 | 年份×技术层矩阵路线 | 2027–2029 什么先做、什么条件性研究 |
| S16 | 证据/推断/未知分层 | 何以不能把单篇/单设备结果泛化 |
| S17 | 三项行动结论 + 重新评估条件 | 研究闭环为何是现实的技术决策 |

每页先按 [02-slide-contracts.md](02-slide-contracts.md)审图，阅读该页技术关系，再检索或制作与用途相符的视觉参考。**禁止把 17 页全部强制做成等宽三卡片**。

## E. 科学图表和真实资产使用规则

1. **真实论文图优先核原文**：核设备、模型、任务、坐标轴、单位、基线、误差线、图号与引用；未经核对不声明「来源于某篇论文的 Figure N」。
2. 论文图可采用「忠实重绘」为 PPT 原生表格/柱/折线/流程图；具有复杂原创视觉的论文截图可单独嵌入，但必须说明局部不可编辑，不能把整页 PNG 当 PPT。
3. **图像生成不得捏造图表数字。** 对需要精确数字的页，原始数值列表应来自证据锁定文件并进入原生图表构造。生成图里出现的数字只是候选，不是数据源。
4. 数据间的比较必须同设备/软件栈、同模型、同指标、明确基线；不把 PAPER-009 Snapdragon 8 Gen 3、SMEPilot Apple M4 Pro、ExecuTorch vivo X300 的实验合成「统一实测排名」。
5. S08 图形中 SME/SME2 属于 **CPU 核内 AArch64 指令与执行能力**；GPU/NPU 是 SoC 的其他计算引擎。架构图绝不并列「CPU 核 vs SME」。
6. 未授权或不明授权的 Logo/原论文图、产品图：先记录来源、用途与权限；不要生成「貌似某公司官方图」来替代。
7. 合法且有解释价值的自制 SVG 图可作为原生或矢量来源；不要以假三维芯片意象冒充真实微架构。可用局部高质量插画，但保持独立图层。
8. 正式 PowerPoint 内的引用格式统一（论文题目/作者或机构/会议年及来源入口）。截图旁最好保留图名或简短边界，讲者备注写清完整出处。

## F. 箭头/连接线语义规范（本项目高风险项）

### 画图之前先定义图结构
为 S05、S10、S12、S13、S15 等有关系线页面，先在 Slide Contract 中列出 `node_id`、`edge_id`、`from`、`to`、`edge_role`、`label`；例如：
- `E01: N1(Agent 计划) → N2(检索任务), edge_role=control_request`
- `E02: N2(检索结果) → N3(重排), edge_role=data_dependency`
- `E03: N4(实际效果验证) → N1(重新规划), edge_role=conditional_feedback`

### 视觉判定
- 实线：确定执行/数据依赖；虚线：条件路径、推断或未定接口（需图例）；双向线：仅在确有双向语义时使用，不能图形对称就画双向。
- 交叉线应有足够避让和连接点；端点必须落到预期节点（箭头不能悬空、压进文本或误接到邻框）。
- 同一条有折点的箭头要作为**连续可编辑 connector/polyline** 保持连接，不用 2–3 段断线装作一条路径。
- 箭头颜色不是唯一语义编码，必要时在线边标注「执行依赖」「数据更新」「反馈验证」「条件性跟进」。
- 构图模型若画错方向，不能因为整体很好看就进入重建；优先修正内容图与 semantic map，必要时重新生成。

## G. 图像生成、选版、语义重建的边界

### 聊天窗口前置（当前工作）
1. 对每页用 Slide Contract 固定论证、证据与不能外推的限制。
2. 拿到真实 Profile/preflight 的画布信息后编译每页图像 brief；选参考图需要说明其构图教会了什么，而不是仅按图库相关性排名选。
3. 先做 S03/S05/S08/S15 四张样页（可只制作概念稿，若内容画布尚未锁定），一页最多保留少量目的明确的候选，记录被否原因。
4. 任何选中的目标图必须有：`slide_id`、`version`、`sha256`、`canvas_width/height`、`master_frame_policy`、`source_contract_revision`、`known_defects`、`selection_rationale` 与明确状态（`concept_only` / `reconstruction_ready`）。
5. 图片经过目视、文字、数据、箭头审查后才允许标记为 `reconstruction_ready`。**仅上传到 GitHub 不代表通过审计**。正式 image target 必须与实际安装版 SlidePoise 的生成合同一致。

### 本地 Work 模式（之后）
严格遵循当时安装的 SlidePoise：接受的实质内容图 `accepted-slide.png` → 独立 `content_obligations` → `semantic-map.json` / `reconstruction-handoff.json` → OpenCV geometry/overlay → reconstruction contract → packaged scene renderer → native PPT → render-preview → 原图与 PPT 实质内容区对比 → 整套校准。
- 禁止绕开 SlidePoise、凭目测坐标直接用临时 python-pptx/PptxGenJS 重画整套，除非用户明确改工作流。未解析出合同或缺失脚本时报告阻碍，不静默换路线。
- **Native-first**：文字、框、表格、可编辑图表、箭头、编号、结论都应为 PowerPoint 对象；真实照片、复杂纹理和经核验论文原图可作为保留的独立图像资产。
- 逐张验证中文行距、文本 ink/基线、图形堆叠层级、箭头端点、图片裁剪；全套验收字体角色、页码、章节转场、统一来源区。
- 先证明 Speaker Notes 可写/可读，再批量写入 17 页；不因 Markdown 备注存在就说 PPTX 的备注已经嵌入。

## H. 三层质量审计和退出门槛

| Gate | 主要产物 | 必须审查 | 进入下一段的条件 |
|---|---|---|---|
| G1 内容与证据 | Outline、17 张合同、证据映射、风险边界 | 主张/机理/设备模型基线/证据等级/旧版状态 | 内容无阻断级冲突，来源映射完善 |
| G2 视觉样页 | 4 张样页的 brief、候选、选版、manifest | 冷读可懂、真实箭头、布局密度、科研图与真实资产、画布尺寸 | 每张有清晰图像目标和明确已知缺陷记录；本地重建就绪需要正确 content canvas |
| G3 PowerPoint 重建 | 单页 scene/PPT 渲染、整套 PPTX、讲者备注 | Native 可编辑率、文字溢出、连接线、同角色跨页样式、完整备注与来源 | 实际渲染逐页检查、独立审稿完成且无重大未解决错误 |

**所有 gate 的判断由实际人工/Agent 目视和事实审查做出，不得用对象数量、相似度分数或最小字号阈值代替专业审查。**

必须执行两次不同的实际阅读：
- **Blind read**：不给检查者作者意图，只看画面，要求其复述本页主张、数据含义、箭头关系；无法正确复述则设计需改。
- **Source/fidelity read**：提供合同、来源、候选图和 PowerPoint 实际渲染，检查漏写、错写、转化损失与排版故障。原始候选本身错误，不能因为重建忠实就算通过。

### 自动化可检查、但不能替代目视的事实
- 图片尺寸、哈希、文件存在、过期引用、PPTX ZIP 关系、可打开性；
- OCR/渲染文本回读仅辅助审稿（不依赖 OCR 作为唯一文字检查）；
- Native shape/text/chart/connector 数量与媒体来源清单；
- 引用 URLs/论文 IDs 覆盖、单页图片 vs 原生元素的归属记录。

### 坚决拒收的情况
- 箭头、流程、数据、设备基线与正文论证错位；
- 主标题只是问句或空主题，需听众猜结论；
- 图像生成的未经校验数字或研究中的历史废弃方向被当成现行事实；
- S08 把 SME2 误画成 CPU 之外的新处理器；
- 17 页主体被当 17 张 PNG 粘到 PPT；
- 声称备注写入了 PPTX，但无法通过保存、导出后读取或 PowerPoint 实际打开核验；
- 完成图像但未保存其元数据、哈希、已知缺陷及 GitHub 真实路径。

## I. GitHub 归档与版本协定

预期目录（后续阶段建设；本文件创建不意味着这些目录已存在）：

```text
slidepoise-prep/
  01-deck-outline.md
  02-slide-contracts.md
  03-evidence-map.md
  04-risk-boundaries.md
  05-visual-spec.md
  06-sample-slides-manifest.md
  07-work-mode-handoff.md
  qa/
  prompts/
  generated-images/
```

- 每张可交付图像按 `S05-substantive-v02.png` 这类稳定 ID 命名；不要用页码做唯一标识。
- 每张 PNG 与同名 `*.md` 审计记录、图像生成 brief、选版说明、源主张修订号关联；通过 GitHub 实际文件 URL 与校验和追溯。
- 概念图不可直接命名 `accepted-slide.png`，只有 SlidePoise 输入条件满足且已明确选定后才能在该运行目录作为正式 target。
- 工作区内的高频中间文件由 SlidePoise 维护；GitHub 优先保存最终选版、必要参考资产、可复原设计合同、QA 结论与正式输出。避免把临时缓存整仓提交造成混乱。
- 任何图像或 PPT 的主张变更，都须追溯到 02 内容合同和 03 证据表；只调整图形布局，不应在无审核下改数值和正式方向。
- 归档完成的判断是实际存在并可打开的 GitHub URL/Release 资产，而不是仅在 README 中声明「已归档」。

## J. 本轮决议与未决事项

- 本文为**聊天阶段视觉规范 v0.1**；尚无实际演示截图，也没有对本地 Profile、render-preview、Speaker Notes 实测。
- 下一步先完成来源映射和风险边界，再以四张难页的内容概念稿验证。**正式用于 SlidePoise 重建的图片必须等 Profile/content canvas 信息核定**；若现在生成，只能是 `concept_only`。
- 视觉规范允许以后根据真实样页做局部调整，但不可因此改动科学事实、颠倒技术关系或悄然调整已批准内容。
