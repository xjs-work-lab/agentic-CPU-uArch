# 09｜正式 16:9 幻灯片母版与正文内容区合同（2026-10-23）

> 状态：**真实本地 `run resolve` 依据已验证；母版设计规范待本地 packaged render 验收**。  
> 输入：[用户上传的脱敏预检](../slidepoise-config/slidepoise-preflight-export.json)；Profile `academic-cpu-insight`；Profile revision `c330fa78476cd5d74298edb608b3fcedde4b90c6f8175905316588b95ea779d6`。  
> 重要：这里的全页 16:9、页眉页脚高度与生成区位置都来自**用户上传的真实已解析运行配置**，不是默认模板推断。已归档的 1600×900 四张图片仍是旧版概念图；[10 的新样页](10-formal-content-region-samples.md)按真实正文内容区重绘。

## 1. 唯一尺寸真值（像素是设计坐标，不是 PPTX 图片铺底）

| 层 | 整页绝对坐标 | 宽 × 高 | 由谁在最终 PPTX 中构造 | 允许元素 |
|---|---|---|---|---|
| PowerPoint 16:9 整页 | `x=0,y=0` | **2048×1152** | SlidePoise packaged renderer 的 full slide | 背景/母版+正文 |
| Inherited header | `x=0,y=0` | **2048×41** | PPT 母版/共享 frame | 项目短标签、轻量分隔线；没有逐页大标题 |
| **Substantive content** | `x=0,y=41` | **2048×1070** | 正式图像目标/原生 text/shape/connector | 每页结论标题、说明、主图、数据、重要限定、来源带 |
| Inherited footer | `x=0,y=1111` | **2048×41** | PPT 母版/共享 frame | 固定保密/资料属性、原生页码、轻量分隔线 |

验证：`2048/1152 = 1.777777...`，即标准 **16:9**。  
`41 + 1070 + 41 = 1152`；`2048/1070 = 1.91401869...` 与本机上报 `derived.generation_aspect_ratio=1.914019` 一致。

**不要**把 2048×1070 当 PPT 纸张尺寸，也不要为了把 1600×900 旧概念图塞进去而关闭 inherited frame 或强制拉伸。母版填的是页面设计结构，并不是「给截图补条空白」。

## 2. 统一框架（16:9 全页）

### 母版页眉（41 px）
- 左：`Agentic CPU µArch Insight`；右：`2027–2029 · 公开证据`，深蓝/冷灰小字、浅蓝下分割线。
- **目前配置里的 `header.left_text/right_text` 是空字符串**。上面的字样只是已设计的**建议写入 run session override**，并非已经发生的本地配置更新。
- 项目名/时间的静态信息属于共享母版；逐页长结论式标题留在 substantive region，不能让 41px 页眉承担它。

### 正文内容区（2048×1070；页面本地坐标）
- 页面相对 `x=60–1988` 有效宽区；初始结论标题建议从 `x=84,y=75` 起，基线最终以渲染和统一标题角色决定。
- 共用正文设计网格：**标题区 y≈65–156；解释/状态条 y≈165–215；主图区 y≈245–925；引用/边界区 y≈960–1030**。
- 主标题推荐约 49–58 设计 px（当前 Profile 的 `nominal_size_px=76` 是配置源值，原生实际标题字号/换行需要校准），不是在 41px 页眉内画 76px 标题。
- 正文内容区的右边要留足页边距；来源放在内部**独立引文带**，因为共享 footer 只有 41px，放不下多篇论文的设备/基线限制。
- 内部图表自绘要保存 node/edge IDs；箭头连线不是装饰，方向+条件必须对应 Slide Contract。

### 母版页脚（41 px）
- 统一页码用本地配置中 `native_slide_number_field_on_master`，计入封面/目录，共 17 页。
- 左侧可用静态文本 `技术路线研判 · 公开资料`，右侧母版页码；**每页详尽参考文献/边界不应放在通用页脚**。
- 本地配置 `footer.slide_number.format="{slide_number}"` 当前只声明单数字；`03/17` 样式需在实际 packaged frame/native renderer 支持下单独验证，不能擅自在正文重复页码。不能直接承诺自动以 `{slide_number}/17` 显示。

## 3. 背景与对比色

- 整页母版背景白色 `#FFFFFF`；正文可使用 `#F7F9FD` 轻微结构分区。
- 主张深蓝 `#102C55`；标题与高级线条 `#174478`；箭头/重点 `#2473B6`；弱面板 `#E7F2FD`；引用线 `#C9DBEA`。
- 中文所有功能角色按已生效的 `Microsoft YaHei` 作为预期；实际可用性及 PowerPoint/LibreOffice 字体回退**尚未经真机字体渲染检查**。
- 不把 Consulting Profile 中橙色、Georgia 标题、装饰性芯片图加回来。

## 4. 哪些归母版 / 哪些归正文

| 元素 | 归属 | 理由 |
|---|---|---|
| 全局项目简称、公共报告属性 | inherited header | 所有内容页相同 |
| 内容页动态结论大标题 | **substantive / 原生 PPT 文本** | 长度随页变化；统一标题角色可编辑 |
| DAG/CPU-SME2/路线图/状态卡 | **substantive / 原生对象** | 重要信息不可被生成器随意变形 |
| 真实实验数字/设备、论文短引 | **substantive / 原生文本和图表** | 需要逐页绑定来源 |
| 项目共用来源性质、细分隔线 | inherited footer | 稳定字段，不能占大正文 |
| PowerPoint 页码 | inherited footer | 原生页码字段，避免重复 |
| Speaker Notes | 每页 PPT speaker notes 元数据 | 暂未验证 SlidePoise 写入/回读，不属页内截图 |

## 5. 正式生成与接受条件

- 本轮新 SVG 必须**精确宽 2048、高 1070、viewBox 0 0 2048 1070**；不含通用母版页眉/页脚文字、页码或全页底部装饰。
- SVG **只是已知坐标的矢量设计参考**，真正 SlidePoise `accepted-slide.png` 须依本地 `prepare_generation.py` 编译的 request 和 packaged workflow 经真实候选审查、尺寸确认后创建；不能把自画 SVG 假装为该管线产物。
- 已有的 1600×900 旧图不得直接拉伸，不能回写覆盖；版本放在 `generated-images/formal-content-v02/`。
- 任何图形一旦修改数值、边连接或机制须按 [03 evidence map](03-evidence-map.md) 和 [04 risk boundaries](04-risk-boundaries.md)重新验。
- **尚缺的 Gate**：实际 SVG→PNG 的文字/碰撞/箭头目视验证、SlidePoise master/frame 在 PPTX 内构造、Speaker Notes 写入/回读、真实 editable native PPTX 端到端渲染。

## 6. 与本机配置的一致性记录

| 来源字段 | 读取的值 |
|---|---|
| `profile_id` | `academic-cpu-insight` |
| `design.full_slide_px` | `[2048,1152]` |
| `frame.header.enabled,height_px` | `true,41` |
| `frame.footer.enabled,height_px` | `true,41` |
| `derived.generation_region_px` | `[2048,1070]` |
| `derived.generation_offset_y_px` | `41` |
| `derived.generation_aspect_ratio` | `1.914019` |
| `style.body_font` | `Microsoft YaHei` |
| `style.accent_colors` | `#102C55 / #174478 / #2473B6...` |
| `speaker_notes_write_readback` | `NOT_TESTED` |
