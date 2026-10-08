# PPT 多语言制图与视觉交付规范 v1.0

> 2026-10-08。适用于 2027–2029 Agentic CPU-uArch 技术领导汇报的所有正文与附录技术图。**本规范取代“所有逻辑图默认 Mermaid”的操作习惯，不取代研究结论、正文锁定文案或已审计图中的技术事实。**
>
> 配套：[逐页选型表](page-visual-language-routing.md) · [Round15J 验证状态](validation-round15j-2026-10-08.md) · [原始内容蓝图](../content-storyboard-v1-2026-10-08.md)。

## 1. 从“要表达什么”开始，而不是从“要用什么工具”开始

每张图开工前，写出五条不会被外观替代的信息：
1. **本图技术问题**：领导看到这张图，要回答哪一个具体问题？模块标题应显式表达目的/因果/结果，而非只有“机制结构”等空泛名称。
2. **事实边界**：直接源自论文图/数据、依据论文方法简化、跨来源系统推断、概念示意四类只能择其恰当声明，不允许默默升级证据。
3. **节点/组件清单**：名称、唯一 ID、实际层级（编译时软件、Runtime、OS、CPU、GPU/NPU、共享数据、外部 App 等）。
4. **关系合同**：对每条连线确定起点 ID、终点 ID、边类型、方向、条件/载荷、是否可选；决策图定义所有 Yes/No/Unknown 去向和各类终态。
5. **阅读和媒体**：左→右、上→下或泳道/矩阵的明确方向；需要可编辑 PPT 形状、SVG、原论文图片还是精确数值图；底部注明精确来源和局限。

逻辑真值的权威来自**内容 Markdown + 原始公开来源 + 页面节点关系合同**。Mermaid/PlantUML/DOT/SVG 等只是一种**编写和呈现关系的格式**；改变语言不得改变原始逻辑。

## 2. 工具与表达任务路由

| 格式/工具 | 优先使用情形 | 不适用/警戒 |
|---|---|---|
| Mermaid | 简单 Flowchart、几条有条件分支、基本状态转移；仓库直接浏览方便 | 技术泳道并发、严格端口布局、复杂交叉 DAG 或高精度图不强用 |
| PlantUML | Agent↔Runtime↔OS↔Tool **时序/消息/生命周期**、带条件/并发的交互、组件部署关系 | UML 语义不与真实系统对应时不可硬套；正式图必须注明概念抽象 |
| Graphviz DOT | 节点/边众多、层级 DAG、可控 cluster、读图顺序清楚的依赖网络 | 复杂 UML 时序不如 PlantUML；布局器能减交叉但不保证最优 |
| Direct SVG | 必须精准保留架构层次、分区、总线/数据路径、复杂箭头、学术布局 | SVG 视觉位置并不自动证明语义正确；需附文本节点关系清单 |
| Excalidraw | 与设计人员快速讨论粗线框、早期概念与白板注释 | 草图不是权威关系规范；正式原生格式是 scene JSON（.excalidraw），不要假设统一“Excalidraw Markdown”标准 |
| PowerPoint SmartArt | 少量节点的并列、层级、无复杂交叉的关系，需直接在 Office 编辑 | 不是通用流程图代码语言；复杂多向反馈/条件分叉易失真 |
| PPT 原生 shapes/connectors | 最终精确文字、点击链接、可编辑框和较简单的有向图 | 必须和文本合同/关系合同做比对，不能只靠肉眼拖线 |
| PPT/Plotly/Matplotlib 原生数据可视化 | 论文实测曲线、对照、误差、消融、比例等，需真实轴和尺度 | **不使用** Image Generator 杜撰量化图；多设备/不同任务的结果不拼出虚假可比结论 |
| 原始论文 Figure | 系统方法难用简单图完整表达，原图可读，图号/引用/使用条件已核对 | 原图字小、版权限制、单图超出主张范围时要改为独立重绘并说明 |

**推荐组合**：内容 Markdown（结论、文字、证据） + 适配的逻辑源（如 DOT/PlantUML） + Direct SVG/PPT 原生图层（精确落地） + Image Generator（视觉语言、配色、技术图标、背景装饰）。不把 Image Generator 当作节点/数值/文字的权威生产者。

## 3. 语义合同与绘图代码分离

复杂图在页面 Markdown 写一张**节点表**与一张**边表**，再附 `mermaid`/`plantuml`/`dot`/`svg` 源码或者原生 PPT/Excalidraw 资产位置；简单图允许直接在源码中登记所有节点和关系。分支与例外必须清楚：

| 示例字段 | 含义 |
|---|---|
| node_id | 页面内稳定唯一 ID，正文不显示 |
| display_name | PPT 锁定中文名称 |
| category | CPU/LLVM/Runtime/OS/状态/工具/决策等 |
| edge_id、from、to | 唯一可定位的箭头和两端 |
| relation | 请求、放置、结果、数据、编译支撑、使能、时序、条件 |
| condition | 是/否/未知、是否可选、触发事件 |
| evidence | 原论文/官方资料或“本报告概念示意” |
| authoring_format | 本图所选主编辑格式和落地资产路径 |

复杂图禁止使用“上图”“两类引擎”“这几个阶段”等未绑定的代词作箭头终点。编译时因果边不可画为运行时硬件控制信号；同一 CPU 的 SME 不与手机 NPU 并列成独立处理器。

## 4. 格式不能混淆的特别说明

- **Mermaid / PlantUML / DOT 是文本图形描述语言**，有各自的解析器与语法；语法能成功解析 ≠ 科学机制正确。
- **Direct SVG 是可渲染矢量绘图格式**，既可以手写，也可以由布局生成，但图中的文本必须与锁定文案一致。
- **SmartArt 是 PowerPoint 内置图形对象**，可由 Office 界面/受支持的 Office 能力编辑，并不是约定好的 Markdown 语法。
- **Excalidraw 的 `.excalidraw` 文件是场景 JSON**。若用户提到“Excalidraw Markdown”，先区分具体应用的 Markdown 包装、链接嵌入或插件扩展，不擅自承诺互通/可解析。
- **论文真实统计图不是流程图**：数据、单位、比较对象、基线和方向必须从原始表或论文数字锁定。论文截图或矢量重绘都不能改变实验结果。
- **PNG 不可点击**：PPTX 中保留可点击原文和 GitHub 超链接；静态 PNG 展示简短来源文字，不承诺图内能点击。

官方格式参考：[Graphviz DOT](https://graphviz.org/doc/info/lang.html) · [PlantUML](https://plantuml.com/) · [Excalidraw Scene JSON](https://docs.excalidraw.com/docs/codebase/json-schema/) · [Microsoft SmartArt](https://support.microsoft.com/en-us/office/graphics-visuals/choose-a-smartart-graphic)。

## 5. 五道分离的质量 Gate

**Gate A — 科学**：引文和论文 Methods/Figure 一致；公开直接事实与综合推断分离。强 NPU 软件基线与 CPU/SME 数据不能换分母。

**Gate B — 拓扑**：节点定义齐备，边起终点存在，控制/数据/反馈类型对得上，状态机分支与终态语义闭合。复杂时做静态边集核验。

**Gate C — 工具解析**：对 Mermaid/PlantUML/DOT 真正使用对应引擎渲染；SVG 需在矢量/浏览器渲染检查；SmartArt/Excalidraw 需用实际兼容工具打开。静态字符串检查不能冒充官方解析成功。

**Gate D — 视觉**：Image Generator 的漂亮图不是终稿。检查图的阅读方向、字号与可读性、图标一致、连接线准确、符号与颜色含义，没有伪装实测的比例或假数量。

**Gate E — 交付**：PPTX 的文字/技术公式/形状尽可能可编辑，原始论文与仓库超链接实际可点击；PNG 与 PPTX 同步，保证图文合同和最终显示一致。

每页交付标注独立状态：设计待核 / 结构已核 / 论文源已核 / 渲染已核 / 视觉已核 / PPTX 验收。**不因选择语言更新而自动提升现有页状态。**

## 6. 对现有工作如何迁移

- 已经建立的 Mermaid **保留**，除非另一种表达明确减少错误或增强阅读；不机械重写历史文件。
- 正式选型记录于 [逐页路由表](page-visual-language-routing.md)，每页选**逻辑表达**与**最终呈现**两种不同产物。
- 对第 5、7、8、9 页继续遵守 [Round15J 论文方法核对](validation-round15j-2026-10-08.md) 和独立页面规格；没有完成原图/实际解析/可编辑 PPT 检查之前，仍标“待验收”。
- 对第 10–15 页下一轮逐页深化；为 Data/Matrix 类页面创建表格/数字合同，而不是冗余 Mermaid。
