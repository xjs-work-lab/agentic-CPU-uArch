# Round15K — 第 8 页 HeRo 高保真视觉试制与 QA（2026-10-08）

## 用户视觉基准与页面目标

用户已表示第 6 页 SME2 样板“基本就可用了”，因此继承第 6 页的浅蓝色学术风格、精确中文叠字、芯片页眉与 16:9 版面标准。第 8 页改用**复杂 DAG 软件系统架构 + 原始论文消融数据**两栏，主张是“动态 Agent DAG 的异构资源调度具有工程价值，而非新增 Agent 专用 ISA 的直接证据”。

**交付状态**：本轮实际制作了单页 16:9 `round15k_slide08_hero_preview.png` 和可编辑 `round15k_slide08_hero_editable.pptx`，放置于聊天会话的生成文件区；**GitHub 当前仅归档 DOT 逻辑和审计记录，不代表仓库已储存二进制 PPT/PNG**。第 8 页仍待用户目视审阅与真实 Office 打开检验。

## 严格来源与素材

- [原论文 HeRo](https://arxiv.org/abs/2603.01661)；[本仓库已核对的机制合同](page-08-hero-runtime.md)。
- Graphviz DOT 骨架保存在 [hero-semantic-graph.dot](hero-semantic-graph.dot)，已在当前运行环境执行 `dot -Tsvg` 与 `dot -Tplain`，输出成功；因使用 `splines=ortho` 同时给部分边设置标签，Graphviz 对边标签有 orthogonal layout 警告。警告不影响本轮图结构输出，但原始 DOT 并不是 PPT 精确视觉图层。
- PowerPoint 页中的关键节点、箭头、图表、中文标签都是**原生可编辑形状**；并非把 DOT 的 SVG 原封不动压成整页图片。Image Generator 仅提供与第 6 页同一组装饰性芯片横幅。
- 概念图以 Agentic RAG 请求 → 部分就绪 DAG → 在线调度器为主路径；shape/离线剖析、动态关键性、共享 DRAM 带宽为调度依据；CPU/GPU/NPU 为**可选异构执行路径**，不是固定同时执行，也不是 CPU 对 NPU 的直接硬件控制。

## 原始数值与展示

论文 Table 3 的两组消融场景分别展示，单位秒，越少越好：

| 论文消融配置 | 对照方案 | HeRo | 同组延时比 |
|---|---:|---:|---:|
| C1 | 5.79 s | 3.82 s | 1.52× |
| C2 | 17.23 s | 5.38 s | 3.20× |

数值标签放在 native PPT 文本框，**柱长按组内自身基线归一化**；故左右两组不可比较绝对 bar 长度，不能将两个倍数相乘或归并到原论文 `up to 10.94×` headline。正式使用前仍须确认原论文具体 C1/C2 模型与 workflow 标注是否需要在页脚展开，且图中“对照方案”标签应与 Table 3 的精确定义吻合。

## 本轮完成的检查

- PowerPoint 导出 PDF 再转 PNG：尺寸为 **2134×1200 px**，16:9 宽高比约 1.7783。
- PPTX XML 中发现 **90 个普通 `p:sp` 图形元素**和一张 `p:pic` 装饰插画；复杂机制图以原生形状绘制。
- PPTX 中存在关键数值 `5.79`、`3.82`、`17.23`、`5.38`、`1.52×`、`3.20×`，并存在 CPU、GPU、NPU、共享 DRAM、在线调度器等关键标签。
- PowerPoint 关系文件包含 [HeRo 原文](https://arxiv.org/abs/2603.01661) 的可点击源链接。
- 已人工检查页面 PNG 一轮并修订：消融组标题避免断行，调度器到 CPU/GPU/NPU 的分支避开因子框和图题，新增虚线状态反馈路径，三项调度约束汇总到调度器。

## 仍未完成的验收

1. 用户对第 8 页视觉密度与科研解释是否满意（当前无明确意见）。
2. 在真实 PowerPoint 中打开并测试链接、字体、箭头及布局。
3. Graphviz DOT 原生 SVG 的全部边标签存在 layout warning，正式 DOT 图若作为可交付 SVG 需要进一步移除警告或调整布局。
4. 本页是依据 HeRo 论文的**机制简化重绘**，不是论文 Figure 4 原图逐像素核验，也不是手机真实任务 trace。

下一样板按计划制作第 5 页 ShadowNPU/llm.npu 软件增强机制；应将两篇论文作为独立路径而非一条伪综合执行流水。
