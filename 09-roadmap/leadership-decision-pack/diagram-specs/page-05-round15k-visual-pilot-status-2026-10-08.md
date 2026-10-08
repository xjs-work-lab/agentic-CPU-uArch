# Round15K 第 5 页 ShadowNPU / llm.npu：可编辑 PPT 试制与领导可读性检查

日期：2026-10-08。**状态：V1 样板已制作并进行文件 QA，待用户实际视觉与内容验收**。不把生成成功等同最终通过。继承已基本获认可的 [第 6 页 SME2 数据页](page-06-round15k-visual-pilot-status.md)、[第 8 页 HeRo V6 叙事要求](leadership-readability-gate-v1-2026-10-08.md) 的浅蓝学术风格，具体图形布局按第 5 页自身机制确定。

## 核心消息与正式内容

**页面标题**：ShadowNPU 让 NPU 快速找出重要 Token，CPU/GPU 只精算少量内容，减少 Attention 回退开销。

**一行背景**：Token 是模型处理的文字片段；Attention 计算它们之间的关联权重；整段 Attention 直接使用低精度 INT8 容易损伤数值准确率，因而已有 NPU-centric 框架往往回退到 CPU/GPU。

**模块标题**：软件重新分工：NPU 负责“找重点”，CPU/GPU 负责“算准确”。

**领导第一次阅读的路径**：
1. 旧情况（以 llm.npu 的 Attention 放置为例）：其他适配模型算子在 NPU，Attention 主要在 CPU/GPU 高精度计算，增加通用处理器负荷与执行交接成本。
2. ShadowNPU / shadowAttn：**NPU 用 INT8 Q·K 快速估计各 Token 的重要性**，输出一个近似分数（不是最终准确 Attention）。
3. **CPU/GPU Top-k 选出重要 Token 的位置索引**，再仅对选定 Token 做高精度 Sparse QKV，合成 Attention 输出（不是说只须搬运索引、无需读取 Q/K/V 数据）。
4. 为什么有意义？确定 Token 排序对低精度近似相对更稳健；真实 Attention 的高精度数据计算只需覆盖重要子集。
5. 软件支持：离线 graph buckets 预编译若干量化 scale / 图配置，在线匹配；head-wise pipeline 让不同 attention heads 的 NPU 估计与 CPU/GPU 计算错峰重叠，减少等待。RoPE 等仍由 CPU/GPU 处理，不能声称所有 Attention 步骤彻底 NPU-only。

**论文分离**：底部单独给出 2025 ASPLOS 的 llm.npu 与 2026 MobiSys 的 ShadowNPU 两条记录。llm.npu 本身的关键技术是 chunk-sharing graph、shadow outlier execution、out-of-order subgraph scheduling；这不是 ShadowNPU 的 Figure 5 所画的同一算法。两篇作者存在研究链联系，不能当成互相独立复现，更不能将速度倍数相乘。

**经验数据与实验范围**：ShadowNPU 论文对 Snapdragon 8 Gen3/8 Gen2 商用手机、指定 Qwen2 与 PhoneLM 以及数据集进行测试，报告在 CPU/GPU 资源受限等受测配置下，端到端提升 **最高 4.5×**、能耗下降 **最高 7.7×**，平均精度下降 **0.4 percentage points**。对应论文本身的受测设计备选/基线；不能当作所有手机或 Agent 任务的通用收益。

**投资解释**：CPU 的高精度 fallback 价值确实存在，但 NPU 软件栈可不断改变其工作范围；宜加强 CPU/GPU 残差算子、layout/precision 数据合同与跨引擎接口，不支持因此直接批准独立 Agent 专用 CPU 指令/硅片预算。

## 科学出处和图形性质

- [ShadowNPU / shadowAttn 原始论文，arXiv 2508.16703 v4](https://arxiv.org/pdf/2508.16703)，§3.1–3.4、Figure 5、实验结果，MobiSys 2026。
- [llm.npu / Fast On-device LLM Inference with NPUs 原文](https://xumengwei.github.io/files/ASPLOS25-NPU.pdf)，ASPLOS 2025。
- 早期技术逻辑：[第 5 页图合同](page-05-npu-software-path.md)。

本页**依据论文方法文字和 Figure 5 图注简化重绘，不是 Figure 5 原图逐像素缩绘**。外部 web PDF 截图调用报错（页面 4、5），无法声明已经逐元素图像核验；正文 Figure 5 方法、图注和原始算法描述则已复核。未从 Fig. 5 中另造硬件物理互联。

## 本轮制作与程序 QA

在当前会话的 `/mnt/data/round15k_shadownpu/` 已制作：
- `round15k_slide05_shadownpu_editable.pptx` — 可编辑 PPTX，一页宽屏 16:9；
- `round15k_slide05_shadownpu_preview.png` — 从同一 PPTX 经 LibreOffice/PDF 导出的 PNG；
- `make_slide05.js` — PPT 原生图元、标签、流程连接线和备注的生成脚本；
- `header_art.png` — 早期 Image Generator 的已认可装饰性素材（在当前目录独立副本，避免引用其他页的绝对路径）。

本轮 **实际验证**：
- PPTX ZIP 完整，无损。
- 一页 PPTX；**65 个原生可编辑形状/文字图元**，**1 张装饰图片**，技术图不是整页 PNG。
- 可编辑文本检出 `ShadowNPU`, `llm.npu`, `Top-k`, `Sparse QKV`, `Graph Bucketing`, `Head-wise Pipeline`，以及 **4.5× / 7.7× / 0.4** 等完整数据。
- PPTX 超链接关系中包含 ShadowNPU 原文 PDF 与 llm.npu 官方论文 PDF；脚本按逻辑图元绘制**三条从左到右的连接线**，没有杂乱回环。
- PNG **1921×1080**（约 16:9），已人工观察文本与卡片、原文链接、论文间的分隔和最终结论均在页内。所有 PPT 图元通过脚本的页面边界检查；这不等于 Microsoft Office 字体和链接点击已测试。

## 尚需通过的验收

1. 用户能否不听讲解，看出“为什么以前回退 CPU/GPU”和“为什么 NPU 估分 + CPU/GPU 稀疏精算有价值”；如果仍有困惑，需要扩充文本或独立拆页，不能缩字硬塞。
2. NPU 图 Bucketing、head pipeline 的解释是否足够清楚且仍准确；如果不够，优先展示真实适配参数而非抽象术语。
3. 4.5×、7.7× 和 0.4 pp 是否需要在正式页标出对应实验模型/对照系统完整名称；当前对照限定在页脚和备注。
4. Microsoft PowerPoint 原生打开后的真实排版/超链接功能；论文 Figure 5 原始图逐元素视觉对照未完成。
5. **最终用户审阅尚未通过，不能宣称第 5 页正式定稿**。用户若认可，可用本页演示的“前后对照 + 三步可读技术机制 + 独立论文关系 + 单页证据/启示”方法推广到其余机制页。
