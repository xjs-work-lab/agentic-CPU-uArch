# 07｜SlidePoise 本地 Work 模式执行交接（Handoff v0.1）

> **当前状态：BLUE_PROFILE_AND_16_9_CANVAS_VERIFIED / VECTOR_CONTENT_CANDIDATES_WRITTEN / VISUAL_RENDER_PENDING**。本交接用于未来用户主动切换 Work 模式时直接复制执行，避免从头阅读全部研究或重做视觉。  
> **注意**：2026-10-23 GitHub 保存的四个 SVG 是 \`concept_only\`，不是 \`accepted-slide.png\`，没有执行实际渲染，也不代表可编辑 PPTX 已生成。

## S03 已有总体判断页目标 PNG 与锁定内容（2026-10-23）

- 正文 PNG：`S03-controlled-content-v01.png`（2048×1070）；整页预览：`S03-16x9-frame-preview-v01.png`（2048×1152）。完整 ZIP 当前由聊天附件交付，含 PNG、SVG、QA、Notes、handoff 与构建脚本。
- 必须先读 `14-s03-approved-copy-and-reconstruction-contract.md`、`qa/round09-s03-decision-portfolio-audit-2026-10-23.md`、`generated-images/formal-content-v02/S03-controlled-png-v01.manifest.json` 和 `notes/S03-speaker-notes-2026-10-23.md`。
- 视觉语义锁定：实色蓝 = 三项优先工程/平台；浅蓝虚线 = 三项条件研究；大号 0 = 当前无证据充分的新硬件主押注，**不是永久否定 CPU 硬件价值**。
- 正式状态来源是 `current.md`、`DEC-PORTFOLIO-002`、`DEC-A-008`。A 已降为条件储备；旧 82.5 分不再是当前评分。不要在可见页面新增内部方向 ID 或旧分数。
- **GitHub 只存 S03 文本合同/QA/Notes/handoff/manifest；PNG、SVG、ZIP 二进制尚未提交 GitHub**，聊天 ZIP 是本轮可用素材。
- 用户视觉确认后，将 S03、S05、S08、S15 一起进入四页 SlidePoise native reconstruction 试制；必须检查对象可编辑、16:9 母版、字体、页码和 Speaker Notes 写入/读回。

## 最新（2026-10-23）：四页实物 PNG/ZIP 已补存到 ChatGPT Library，替代临时 sandbox

- 必须优先读取 [真实二进制获取与迁移说明](15-library-binary-handoff-and-github-archive.md)与 [SHA-256 Manifest](binary-assets/four-slide-pilot/library-assets-manifest.json)。
- ChatGPT Library 路径是 `/Agentic-CPU-uArch/slidepoise/four-slide-pilot/`，共12个真实文件，分别是四张正文 PNG、四张 full 16:9 preview 和四份源码 ZIP。已经在 Library list 核实12/12，并实际还原测试 S03 PNG 与 S08 ZIP 的哈希。
- Work 如果能使用 Library，请按此路径取得 PNG/ZIP 实际字节；如果 Work UI 或工具权限不能列 Library，须请求用户通过附件菜单从 Library 选择四 ZIP 附加给当前 Work 对话。**不得使用另一会话的 /mnt/data，亦不得据文本 manifest 伪造图片已存在。**
- 文件取得后先校验尺寸/哈希，然后将实际 PNG/ZIP 文件推送到 GitHub 固定目录 `09-roadmap/leadership-decision-pack/slidepoise-prep/binary-assets/four-slide-pilot/`，read-back 后再更改 GitHub 二进制状态。
- 四张正文 2048×1070 是可用于 SlidePoise 的内容区 PNG，2048×1152 的 16:9 preview 只作为母版/视觉对照。然后仅试制四页原生对象/Notes/母版，并进行渲染比较。
- 本最新规定**覆盖**本文件下方历史描述“仅聊天临时附件可用”的旧状态。
## S15 已有目标 PNG / 五层三年锁定路线（2026-10-23）

- 正文 PNG：`S15-controlled-content-v01.png`，2048×1070；整页 16:9 示意 PNG：`S15-16x9-frame-preview-v01.png`，2048×1152。当前聊天 ZIP 含二者+SVG+五个 Image2.5 图标+QA 脚本+完整 Notes；GitHub 目前仅存文本/哈希记录，不要误判二进制已存仓。
- 必须读取 `13-s15-roadmap-content-and-reconstruction-contract.md`、`qa/round08-s15-image2p5-and-roadmap-audit-2026-10-23.md`、`generated-images/formal-content-v02/S15-controlled-png-v01.manifest.json` 及 `notes/S15-speaker-notes-2026-10-23.md`。
- Image2.5 原始全页草图含 P0 不实的新硬件里程碑，**已拒收且被排除出 Work ZIP**。五个图标可作图片资产，但所有 Matrix/文字/年份/条件性状态必须 PowerPoint 原生可编辑对象，不能按原始草图 OCR/临摹。
- 2027 工程基础；2028 跨层接口；2029 持续工程＋条件研究，**非既定预算/团队排期/流片/量产时间表**。五条路线：CPU/LLVM、Runtime/OS、Agent 可信动作、内存/派生状态、主动低功耗。
- 在本地 packaged SlidePoise 流程中依真实 `academic-cpu-insight` 生成区接受目标 PNG、语义图/布局测量、原生 PPTX 重建、16:9/中文字体/页码渲染及 S15 speaker notes 写入回读；不得以图片好看代替对象可编辑性验收。

## S08 已有真实内容区 PNG 与源数据锁定合同（2026-10-23）

- 正文 PNG `S08-controlled-content-v01.png`，2048×1070；完整版预览 `S08-16x9-frame-preview-v01.png`，2048×1152。用户可从本轮聊天下载，**GitHub 目前只有 manifest 和 QA 合同，没有 PNG 二进制**。
- 必须一起读取 `12-s08-approved-copy-and-reconstruction-contract.md`、`generated-images/formal-content-v02/S08-controlled-png-v01.manifest.json`、`qa/round07-s08-image2p5-and-measurement-audit-2026-10-23.md`。
- Image2.5 的科技芯片插画是可保留的**复杂视觉资产**，其他主标题、实验图表、横轴、CPU 嵌套结构、数据说明必须 PPT native 重建，不能整页 PNG 当“可编辑”。
- 原始数据为 vivo X300/SqueezeSAM/1 CPU 核/Normal mode、INT8 555.8→304.1ms、FP16 1163.0→298.2ms；同一 0–1200ms 横轴；SME2 后数据移动占 41.4%/39.9%。严禁将 SME 当独立 NPU、将 Apple M4 Pro 能耗当手机数据、将 SqueezeSAM 当 Agent 端到端。
- Work 不要重新做科研或自行编造测试；先验证正式 packaged image target→semantic map→native PPTX→Windows/LibreOffice 实际渲染、中文字体与 Notes 写读回。

## S05 追加 P0 内容约束（2026-10-23，优先级高于 PNG 中的文字）

本轮审计发现 S05 的三次 Image2.5 视觉候选均存在**不受证据支持的加速/能耗/带宽比率**，以及将 Decode/Attention/MLP 绝对绑定 NPU 的倾向，**三张均技术拒收**。用户认可的是蓝白配色和分栏，不是数字。

必须读取：
- `11-s05-approved-copy-and-reconstruction-contract.md`：**最终逐字投影内容/禁止数据/每条箭头/来源/六项 Speaker Notes 必讲点**
- `generated-images/formal-content-v02/S05-locked-content-v03.json`：机器可读不可变文案与禁用数值
- `generated-images/formal-content-v02/S05-edge-contract-v02.json`：所有节点和 13 条有向边的语义
- `qa/round05-s05-imagegen-content-audit-2026-10-23.md`：三轮图片候选拒收的原因

**执行纪律**：未出现独立审定 `accepted-slide.png` 前，不能选择上述 Image2.5 候选进行 native reconstruction。Work 可参考候选配色/版式，但**禁止**复刻其中的柱状图、百分比、无根据的总吞吐/延迟收益和错误硬件映射。先用锁定内容合同完成 S05 目标图的 G2 事实/视觉审核，再使用 SlidePoise packaged 流程重建。PowerPoint 中所有节点、箭头、标题、数据等优先 native 可编辑；不能以“PNG 给了什么字”覆盖文字合同。

## 本轮最新生效配置：2026-10-23（覆盖下方历史预检阻断）

- 从 GitHub 实际读取已上传的 slidepoise-config/slidepoise-preflight-export.json。独立蓝色 Profile academic-cpu-insight **已在本地成功应用**；不需要再安装、创建或重复预检。
- **完整 PPT 页面 2048×1152，精确 16:9**；header 41px、footer 41px；正式 substantive canvas 2048×1070，y 偏移 41px。
- 09-frame-and-content-region-contract.md 锁定母版职责；10-formal-content-region-samples.md 保存四张 2048×1070 正文 SVG 和对应的 2048×1152 整页母版组合预览。八张 SVG 已静态检查，**未经真正 SVG/PNG 目视或 PowerPoint 渲染**。
- 本地已有 agentic-cpu-sample-df86e8 run。建议 frame 静态文案的 session override 在 profile-blue/academic-cpu-run-session-overrides.proposal.json，**尚未应用到 run**。
- 原生页码目前配置为 {slide_number}，组合示意中的 NN/17 为视觉参考，不代表已验证的 PowerPoint 字段。
- 下一个 Work 最小任务应是四张样页的真实渲染/内容审核及 packaged SlidePoise 重建试点（优先 S05），验证 native 对象、master、页码和 speaker notes，而不是重做 doctor。

## 以下为当时配置未完成时期的历史记录（不再是当前阻断状态）
## 重要：2026-10-23 本地配置核验后补充的阻断门槛

- 用户已将 `slidepoise-config/doctor.json` 和 `profile-show.json` 上传 GitHub。已确认当前激活 `consulting` 为橙色/Georgia/Arial 的**指定硬规则**，与我们已认可的蓝色中文研究视觉基线冲突。
- 进入正式图片生成或 native reconstruction **必须优先使用独立 Profile `academic-cpu-insight`**；其设计补丁见 `08-profile-adaptation-contract.md` 与 `profile-blue/academic-cpu-insight.profile-update.json`。补丁目前只是 GitHub 候选文件，**未在用户本机安装/运行**。
- `doctor` / `profile show` **不足以确认 substantive canvas**。要在选用独立 Profile 后获取真实 `run resolve` 的 `resolved-config.json`，核查 full-slide、header/footer 和 `derived.generation_region_px`，再决定图片尺寸。参考证据见 `qa/slidepoise-preflight-snapshot-2026-10-23.md`。
- 本地最小检查任务可以在普通终端完成，无需消耗 Work 令牌。只有完成 Profile / resolved canvas 核验才允许把当前 SVG 从 `concept_only` 推向正式图片 target 阶段。
- 如尚未做完这一步，**严禁以默认 Consulting Profile 先做四页再改色**，否则图像/Native PPT 样式会形成两套权威。

## 一、执行目标

用本地已安装的 **SlidePoise packaged workflow**，将基于 Agentic CPU 微架构研究的 **17 页中文学术型技术汇报**制作为真正可编辑的 16:9 PPTX，附带详细 Speaker Notes，并渲染、审核、保存归档。

用户希望把**论证、视觉和证据审稿**尽可能留在 ChatGPT 聊天阶段，**Work 模式只承担必须本地执行的有限确定性任务**：解析环境→实际内容画布与资源→SlidePoise 官方的生成/语义映射/测量/重建→真实 PPT 渲染与修复→备注写入/回读验证→文件交付/归档。

**不允许**：
- 从头做新一轮全网 Agentic 微架构研究或主动推翻当前正式决策；
- 把旧版 17 页备注按旧页码直接贴到新版 PPT；
- 擅自改变已审定论文数值、设备、基线或 NPU/CPU 关系；
- 用 17 张整页 PNG 假装生成 17 张可编辑 PPT；
- 在 SlidePoise 需要正式 substantive canvas 的地方直接喂入含页眉页脚的完整 1600×900 概念 SVG；
- 跳过 packaged SlidePoise reconstruction invariant，私下用 python-pptx/PptxGenJS 仿造流程。

## 二、唯一前置资料入口

仓库：\`xjs-work-lab/agentic-CPU-uArch\`，分支 \`main\`。

**源研究**：
- \`09-roadmap/agentic-cpu-uarch-detailed-research-summary-cn-2026-10-20.md\`
- \`09-roadmap/current.md\`
- \`08-decisions/events/DEC-PORTFOLIO-002.md\`
- \`08-decisions/events/DEC-A-008.md\`
- \`09-roadmap/management-final-public-evidence-2027-2029.md\`

**PPT 前置设计**：\`09-roadmap/leadership-decision-pack/slidepoise-prep/\`
- \`01-deck-outline.md\`：17 页稳定 S01–S17 顺序和叙事衔接
- \`02-slide-contracts.md\`：每页技术事实、内容、图形与拒收规则
- \`03-evidence-map.md\`：设备/论文/数字/基线/证据等级与不能外推内容
- \`04-risk-boundaries.md\`：16 个全局 P0/P1 关键技术禁区
- \`05-visual-spec.md\`：蓝色学术技术风格、图表、中文排版、引用、母版及 native 重建
- \`06-sample-slides-manifest.md\`：GitHub 中四张已存在的 SVG、真实路径和 blob SHA
- \`qa/round02-content-evidence-audit-2026-10-23.md\`
- \`qa/round03-visual-concept-audit-2026-10-23.md\`
- \`qa/slidepoise-local-preflight-minimal.md\`

**已存在的四张矢量概念设计（只能作设计参考，非重建输入目标）**：
1. \`generated-images/S03-overview-concept-v01.svg\`
2. \`generated-images/S05-dag-concept-v01.svg\`
3. \`generated-images/S08-sme2-concept-v01.svg\`
4. \`generated-images/S15-roadmap-concept-v01.svg\`

## 三、旧版 preflight 步骤（已完成，禁止无故重复执行）

1. 运行 \`slidepoise doctor\`、\`slidepoise profile show\`。使用本地实际可用 CLI，**不用再次执行 setup**。
2. 从实际 Profile + run overrides 确认完整幻灯片尺寸、header/footer 是否启用及尺寸、**substantive canvas 宽高与比例**、中文/拉丁字体、图像生成服务与 preview 能力。
3. 依本地版本读取 SlidePoise 官方 \`SKILL.md\`、\`references/deck-orchestration.md\`、\`workflow.md\`、\`reconstruction.md\`、\`human-approval.md\`。不要复制本文件成为替代品。
4. 以一页最小 PPTX 测试 Speaker Notes 写入与回读。若 packaged runtime 不提供此能力，只能在**不绕开其可编辑场景生成逻辑**的情况下采取独立、有记录的 notes 注入步骤，之后验收 PPTX 打开与 Notes 对应正确；未验证前报告阻断条件。
5. 将非敏感 preflight 结果（含所用 Profile ID、真实画布比例、preview 环境）存入 \`qa/slidepoise-preflight-snapshot-YYYY-MM-DD.md\`；不能把 \`TO_BE_CAPTURED\` 当实测。

**低 token 建议**：首次 Work 任务只做这一小段 preflight/notes 支持检查；把快照返回聊天窗口，再继续正式图片生成与审计。如果 user 已确认聊天窗口图片已按正式 substantive canvas 生成，则从交接包直接消费，但仍要核校合同与尺寸。

## 四、四张高风险样页的顺序

先跑 **S03 → S05 → S08 → S15**，每页执行同一条正式 SlidePoise 管线：

1. 消费逐页内容合同/证据与视觉规范；
2. 从真实 Profile、frame、视觉参考和意图**编译官方 generation request**（不能单独随手重写一个“差不多”的 prompt 代替）；
3. 生成/筛选仅覆盖**正文实质内容区**的 target image，检查文本、数字、连接方向并冻结 \`accepted-slide.png\`；
4. 独立编写必须保留的 \`content_obligations\`；
5. \`semantic-map.json\`、\`reconstruction-handoff.json\`、OpenCV 几何 evidence/overlay、reconstruction contract、native constructor scene；
6. 用 packaged \`slidepoise_runtime.py\` 组装和 render-preview；
7. 两种检查：**盲读真实幻灯片**（能否独立理解技术）与**原图/来源对比**（是否漏数值、失去布局、错连线或改变技术解释）；
8. 修正后重新 render，不以“程序执行成功”冒充人眼视觉验收。

**四页高风险硬限制**：
- S03：**三项工程/平台，三项条件储备，0 项证据充分的新 Agent 专用硬件**；不把 PIM/AI 加速器等未授权方向写进三储备。
- S05：关键有向边、可选查询拆分、并行检索、工具调用跳过、验证反馈和 CPU/GPU/NPU 资源池须表达正确；不是固定 CPU 硬件流程。
- S08：**SME2 属 CPU 内部 ISA 能力**；vivo X300 的 SqueezeSAM CPU 路径 INT8 555.8→304.1 ms、FP16 1163.0→298.2 ms；Apple M4 Pro 的研究不能伪装成手机能耗测试。
- S15：2027–2029 是规划建议，2029 新硬件只在有新增外部证据后才能评估；不要产生虚假量产承诺。

## 五、样页验收之后，再做其余 13 页

- 总共 17 页，含封面 01/17、目录 02/17、结尾 17/17；
- 最终中文结论式标题，非术语罗列、非问句、非研究内部编号；
- 每页主张与来源严格对应，引用不压正文；
- 主要文本、数值、表格、流程节点与箭头优先原生 PowerPoint，可编辑；
- 每页**完整讲者备注**：先解释画面/观点/机制，再逐条交代来源、论据、支持什么/不支持什么；旧版 17 页 Notes 只按主题重新映射；
- 全套单一视觉系统，保留不同叙事页的差异化构图；用真实页面照片/PNG 做交叉页校准；
- 不把不同设备/模型/基线的倍数放在同一无条件可比坐标轴。

## 六、版本交付与审计闭环

### 必交付
- 最终 \`.pptx\`（可编辑）
- \`.pdf\` 预览、每页 PNG 或同等逐页渲染截图
- 逐页 Notes（PPTX 内确实存在）及可供复核的 Notes Markdown
- 图片/版权/引用来源清单
- 17 页 QA 清单与 P0/P1 缺陷修复闭环
- 前置 SVG 与最终 PPT 设计的关键差异说明
- GitHub 存档入口与真实文件路径/版本/哈希

### 发布底线
\`pptx_exists\`、\`rendered_preview_inspected\`、\`native_content_verified\`、\`notes_written_and_read_back\`、\`sources_covered\` 和 \`no_unresolved_P0_P1\` 必须逐项满足，否则标记 \`NOT_ACCEPTED\`。不能因为目录里有 PPTX 就宣布已验收。

## 七、推荐复制到 Work 模式的最短执行提示

> 仓库 \`xjs-work-lab/agentic-CPU-uArch\`，读取 \`09-roadmap/leadership-decision-pack/slidepoise-prep/07-work-mode-handoff.md\` 及其 README 索引。我的本地 SlidePoise 已安装。**本轮只做最小预检**：doctor/profile/run 的 frame 与 substantive canvas 信息、中文字体/预览环境，以及一页 Speaker Notes 写入/回读可行性检查。不要重做研究，不要批量出图或生成全套 PPT。将非敏感配置与真正测试结果记录进 GitHub 的 QA 快照，并明确告知哪些条件阻断聊天窗口正式出图。

收到本地真实预检后，才用聊天窗口确定的样页方案生成正式 target，并启动后续四页重建任务。除非用户随后明确授权，不在一次 Work 任务中擅自从四页跳到 17 页。

## 八、研究主张变化的处理

- 只改美术/箭头位置时，保持原投影文案与 evidence map；
- 只改 Notes 时，不动投影内容；
- 真正需要改数据或技术结论时，先追溯 current.md/正式 decision/原证据卡，经过内容合同审批后再失效相应 downstream target；
- 保留原有视觉 SVG 与被拒版本的 QA 记录，不默默覆写历史；
- 前置资产文件夹与正式 deck output 目录保持分离，避免同名文件盖掉权威内容。
