# 06｜SlidePoise 四张优先样页图片清单（Visual Asset Manifest v0.1）

> 2026-10-23｜**4 张 UTF-8 SVG 已真实写入 GitHub main**。状态统一为 `concept_only / structural_checked / visually_not_yet_render_accepted`；不是官方 SlidePoise `accepted-slide.png`。  
> 这些 SVG 本身就是**可缩放的矢量图片**，每个文本、节点、条形和连线均是独立 SVG 对象；可直接在 GitHub 查看源码/预览。它们不是原生 PowerPoint，也未由本地 SlidePoise 的正式图像请求编译。

## 1. GitHub 已存的实际图片

| Stable slide ID | SVG 图像（可打开） | 主要表达 | 实际画布 | Git blob SHA | 当前状态 |
|---|---|---|---|---|---|
| S03 | [S03-overview-concept-v01.svg](generated-images/S03-overview-concept-v01.svg) | 三项工程/平台、三项储备、零项独立新硬件主押注；左侧跨层结构，右侧证据状态 | 1600×900 | `aee616f783529bbaf79ee65c619785e275018ab7` | CONCEPT_ONLY |
| S05 | [S05-dag-concept-v01.svg](generated-images/S05-dag-concept-v01.svg) | 动态工作流：任务规划、可选查询分解、并行检索、聚合、推理、工具、结果验证与条件反馈 | 1600×900 | `cb2a9e017e930c4a76d499a3f5a7ceb3c29db261` | CONCEPT_ONLY |
| S08 | [S08-sme2-concept-v01.svg](generated-images/S08-sme2-concept-v01.svg) | CPU 内 SME2 的正确层级、LLVM/MLIR 路线、vivo X300 指定单核模型的量化对照 | 1600×900 | `42ef4b96e3080986b34eb885ed466b9285598937` | CONCEPT_ONLY |
| S15 | [S15-roadmap-concept-v01.svg](generated-images/S15-roadmap-concept-v01.svg) | 2027–2029 年份×技术层路线，区分持续软件工程与需要额外公开证据的条件研究 | 1600×900 | `ad371316893f19a25e82fe65fdff44e8165dc63d` | CONCEPT_ONLY |

上述 Git blob SHA 是 GitHub 当前返回的**文件内容标识**，不是随意声称的 SHA-256；每个路径均已经从 GitHub 重新读取成功。

## 2. 画布 / Master Frame 的前置限制

当前 SVG 包含**演示用的顶部标题、页脚和页码**，只是为检查完整页面的视觉层级。**SlidePoise 真正的 ImageGen accepted target 通常应只包含扣除 inherited header/footer 后的 substantive region**；现阶段还不知道用户本地启用的 frame 高度及真实 canvas 比例。因此：
- 严禁把这四张 1600×900 整页 SVG 直接放入正式 `accepted-slide.png`，也不要拉伸成目标画布。
- 它们可以作为视觉设计参考/语义素材；正式生成请求必须从本地 run/profile 配置与 [02 内容合同](02-slide-contracts.md)、[05 视觉规范](05-visual-spec.md)编译。
- 画面中的标题、引用与页码只用于概念审查，在 native PPT 工作流中应按实际 header/footer 所有权重建，避免重复。
- 进入 Work 之前按 [最小预检清单](qa/slidepoise-local-preflight-minimal.md)采集真实参数。

## 3. 本轮质量状态

| Slide | 已完成的内容/结构检查 | 下一阶段必须进行的实际目视检查 |
|---|---|---|
| S03 | 官方决策对应：三项工程/平台，三项条件储备，0 个证据支持的新 Agent CPU 专用硬件主押注；无伪造加速数值 | 技术分层是否冷读可懂；左右两区有无拥挤；数据/控制箭头有无歧义 |
| S05 | 任务依赖与分支在源 SVG 中是单独路径；已修订“可选查询拆分旁路”“无需工具直接验证”“条件重新规划” | 实际渲染各边端点、交叉/遮挡；检查路径方向及关键路径是否易读 |
| S08 | SME2 被嵌套于 AArch64 CPU 核；vivo X300 数字与归档数据一致；INT8/FP16 各自归一化条长有注明；与苹果 M4 Pro 结果隔离 | 渲染数字、图形比例、标题和注释可读性；需确认各原始数据的基线语境 |
| S15 | 五技术层 × 三年；2029 保留软件持续推进与条件研究的区分；硬件选项需外部新增证据 | 逐格排版/行高/中文字体；2029 实线/虚线的沟通语义冷读检查 |

**已做的自动结构检查**：每张 SVG 的 1600×900 属性、标签闭合平衡、重复属性、未转义的 &、必需技术关键词及 GitHub 文件可读取性。  
**没做且绝不虚报的审查**：本地真实 SVG→PNG 渲染、手工像素对照、PPT 重建/字体/备注与 Windows PowerPoint 开启。参见 [Round03 QA](qa/round03-visual-concept-audit-2026-10-23.md)。

## 4. 第一轮自动图片候选拒收

生成器首轮返回了一张「S03/S05/S08/S15 四宫格位图」。它不是上述四张 SVG 的来源、也**不是任何一页的被认可图片**；审稿发现 **P0** 技术事实错误：
- 把专用加速器、存内计算和新存储/互连等当成本项目三项正式研究储备（实际储备为私有进度信息、跨引擎派生状态有效性、CPU 续执行局部性）。
- S08 的示例图使用没有独立来源绑定的性能柱状图。
因此**未提交为正式资产**；拒收事件记录于 Round03 QA。不得从首轮四宫格像素提取技术数字、节点或结论。

## 5. 后续更新规范

- 将图片状态从 `concept_only` 升级为 `reconstruction_ready` 必须有实际 SlidePoise ImageGen request、正确 substantive canvas、相应内容合同版本、设备/数值证据审稿、冷读视觉检查及明确选择理由。
- 正式被选中的 PNG 或相应原生候选必须另建文件与 manifest 记录；**不要覆盖本次 SVG**，保留已审计的设计探索历史。
- 任何 P0 技术错误出现时，先改 02/03/04 文本合同或重做图，再重新审核；不能仅换颜色或加一条脚注掩盖错误。
