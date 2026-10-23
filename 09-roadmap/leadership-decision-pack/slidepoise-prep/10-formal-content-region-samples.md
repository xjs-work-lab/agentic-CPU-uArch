# 10｜正式尺寸内容区四页 SVG 候选与 16:9 母版组合预览（v0.2）

> 2026-10-23｜**真实本地画布 2048×1152 / header41 / content2048×1070 / footer41 已核验**；本阶段为 `CANVAS_CORRECT_VECTOR_DESIGN_CANDIDATE`，**尚非 SlidePoise packaged `accepted-slide.png` 或已通过 PPTX 渲染的成品**。  
> 来源真值：[已上传的 sanitized preflight](../slidepoise-config/slidepoise-preflight-export.json)、[09 母版合同](09-frame-and-content-region-contract.md)、[正式内容合同](02-slide-contracts.md)、[证据边界](03-evidence-map.md)。 
> 两组 SVG 都由实际内容生成且独立存于 GitHub；上次 1600×900 的 `v01` 保留为历史设计，不做图像变形裁切。

## 1. 四张正式正文区 SVG

**正文区图像只包含动态结论标题、技术内容、重要边界和短引用；不包含母版页眉、页脚、页码。**

| Slide | 纯正文 2048×1070 SVG（可编辑矢量） | 整页 2048×1152 16:9 母版组合预览 | 信息职能 | 当前审核状态 |
|---|---|---|---|---|
| S03 | [正文图](generated-images/formal-content-v02/S03-overview-substantive-v02.svg) | [16:9 整页预览](generated-images/frame-preview-v02/S03-full-16x9-frame-mockup-v02.svg) | 三类状态与跨层职责 | SVG 源结构 PASS；实际渲染待验 |
| S05 | [正文图](generated-images/formal-content-v02/S05-dag-substantive-v02.svg) | [16:9 整页预览](generated-images/frame-preview-v02/S05-full-16x9-frame-mockup-v02.svg) | DAG 必要依赖/条件旁路与动态资源调度 | SVG 源结构 PASS；实际渲染待验 |
| S08 | [正文图](generated-images/formal-content-v02/S08-sme2-substantive-v02.svg) | [16:9 整页预览](generated-images/frame-preview-v02/S08-full-16x9-frame-mockup-v02.svg) | CPU 内 SME2 + vivo X300 指定 CPU 路径延迟 | SVG 源结构 PASS；实际渲染待验 |
| S15 | [正文图](generated-images/formal-content-v02/S15-roadmap-substantive-v02.svg) | [16:9 整页预览](generated-images/frame-preview-v02/S15-full-16x9-frame-mockup-v02.svg) | 2027–2029 规划建议与硬件研究门槛 | SVG 源结构 PASS；实际渲染待验 |

### SHA-256 与 GitHub blob 标识

本表中的 SHA-256 由 JavaScript 标准 SHA-256 运算按 UTF-8 **实际源字节内容**计算，并用已知 `abc` 测试向量验证实现；Git blob SHA 来自 GitHub 已返回的实际对象。二者是不同哈希体系。

| Slide | 正文 SVG SHA-256 | 正文 Git blob SHA | 整页预览 SHA-256 |
|---|---|---|---|
| S03 | `da02b9d759c0bc4556062082f837a229fef64936193c99911ef8ce23f910df22` | `123cdb0b206593a95d61ce0c7f7f78019a553f04` | `0f17ffe569452263599d511ad1d1712f7f39b66a8ed51848367b41d605eb8b75` |
| S05 | `189782a7336f4e2cc20f8977e76cc56e7585a53d3502c219eaaae688562d9948` | `f05b374d48f27c425ac64bccef236a7331dd22b3` | `ae0fbae5aa22bc79cb2d2cf71660d863e7b5fb03180e19562427884096d90e4e` |
| S08 | `f558739acc05dad4887ff6f3f1e158b3b09487e9c140cd22f3c061aa9a726caf` | `d5973643cbfd562f7fe2bddb40646b819d208b11` | `b92834b65d69ba5447d4905136407e8dc1ff7c79b72dbf2e8cd483b1f915b4fe` |
| S15 | `d3ede96db2788b38758b3f5b5338e3713fc9f8f715c87974a99cd48f5dfedbed` | `4288fdf8337d8b7a804885808e6d1a70216c2bba` | `8e4189a1c3a40d7acf03fd25d073230e010e9a052dc57f767b8f3f54a2a63c6c` |

## 2. 母版不是“补上下空白”

```text
PowerPoint full slide: 2048 × 1152 = 16:9
+-----------------------------------------------------+
| 0..40          inherited header    (41 px)           |
+-----------------------------------------------------+
| 41..1110       substantive content (1070 px)         |
|                header/title in substantive area      |
|                scientific diagrams / table / notes  |
|                bottom source-and-boundary strip      |
+-----------------------------------------------------+
| 1111..1151     inherited footer    (41 px)           |
+-----------------------------------------------------+
```

- 上/下小区域属于 PowerPoint 母版：共用短标签、分隔线和原生页码。
- 内容区大标题属于可编辑的原生 slide object；正文 SVG 是视觉与语义参照，不能用它作为完整 PPT 背景。
- 整页预览的页眉/页脚为**尚未应用的建议配置**，并包含 `03/17` 一类说明性页码；上传的真实本机 run 中 header/footer 文字仍为空，页码原生格式为 `{slide_number}`，不是已验证 `XX/17`。不可将本预览冒充本机已渲染出的 PPT。
- 待 Work 执行时将 [建议 session override](profile-blue/academic-cpu-run-session-overrides.proposal.json) 用真实 run revision 应用，重新 resolve，实际生成共享 frame；若 `XX/17` 格式不受运行时支持，不得画一个假的内容区页码来掩盖。

## 3. 设计层面的纠偏与验收

- **S03**：归档的正式 current.md 对应「三项工程/平台、三项条件研究、零个新 Agent 专用 CPU 硬件 Primary Bet」；禁用 PIM/加速器等错误储备名单。
- **S05**：包含可选重写的 bypass 边、两条并行检索、聚合/生成、工具调用可跳过、结果验证与有条件重新规划；修复 SVG 顶部路径可能与节点/依赖边发生的交叉。
- **S08**：SME2 绝不能与 CPU 平级；INT8 为 555.8→304.1 ms，FP16 为 1163.0→298.2 ms，均为 vivo X300 SqueezeSAM CPU 路径；条长在每组精度内以“优化前”为 100% 缩放，不暗示跨精度 100% 时间一样长。
- **S15**：2027–2029 是建议而非已批准交付排期；2029 的持续软件工程与条件硬件研究通过文字状态而非单色虚线混为一谈。

## 4. G2/G3 严格边界

**已做**：
- 从用户上传的实际预检读取 full-slide/frame/derived 画布数值，验证 16:9 和 `41+1070+41=1152`；
- GitHub 保存全部 4 正文与 4 整页预览 SVG，源 SVG 可拆分文字、框、线、条形；
- 静态检查 SVG 标签闭合、属性重复、XML 转义、源坐标尺寸及基本估算文本边界；无明显异常。

**尚未做**：
- 用具有本机微软雅黑或等效字体的真实 SVG→PNG 渲染检查、人工全分辨率检查箭头/行距/光学重叠；
- 使用本地 SlidePoise 官方 `prepare_generation.py` 编译四页 ImageGen request、保存与审定 `accepted-slide.png`；
- semantic map / OpenCV measurement / native PPTX reconstruction、渲染差分、Notes 写入和回读；
- 确保整套 17 页的母版字体样式、页码格式、原生可编辑对象全部一致。

**当前状态定义**：`content_svg_dimensions_verified` ✓、`master_preview_dimensions_verified` ✓、`svg_static_structure_verified` ✓、`visual_render_pass` ⏳、`SlidePoise_accepted_target` ⏳、`native_editable_pptx` ⏳。

## 5. 后续正式生产

进入本地 Work 时以 [07-work-mode-handoff.md](07-work-mode-handoff.md) 和 [09-frame-and-content-region-contract.md](09-frame-and-content-region-contract.md) 为主线，**保留用户已创建的 `academic-cpu-insight` run**，不要重新设计研究或改回 Consulting。
正式出图/重建顺序 S03→S05→S08→S15；先真实渲染四页确认，再复制正确样式规则到其余 13 页。
