# Round15N：第 7 页 SMEPilot — 纯蓝色可编辑 PPT 样板、技术解释与 QA

日期：2026-10-08。**第 7 页已实际制作 PPTX 与 16:9 PNG，基础技术/文件 QA 通过；当前仍待用户审阅，不能写为“正式定版”。** 第 4 页 V3、第 5 页 V3 blueonly 是本轮纯蓝色学术视觉参考；页码统一为 `07 / 15`。

## 领导阅读的中心结论

**修订后的建议标题（架构层级修正）**：**SMEPilot 协同利用 CPU 的通用计算与 SME 矩阵计算能力，通过分块并行、流水重叠和数据复用减少执行开销。**

主前提：**SME 是 CPU 内部的矩阵计算扩展，不是独立 SoC NPU。** SME 矩阵计算与 CPU 核通用/向量计算能够互补，但共享内存带宽；某个任务最适合谁执行，取决于算子的计算量、输入形态和内存流量。

**主模块结论**：先按算子特点选择 CPU-only、SME-only 或混合执行，进一步通过三项不同机制解决空间空闲、执行等待、重复数据打包。

## 三项机制必须讲清楚“为什么→怎样→解决什么”

| 机制 | 真实技术难点 | 论文方法在图中的解释 | 预期减少的损失 |
|---|---|---|---|
| ① Tile-level partition | 大型计算密集 GEMM 完全交给 CPU 核或 SME，可能闲置另一类计算资源 | 将矩阵工作拆成独立 tiles（小块），按实际吞吐能力划分给两方并行执行 | 减少一方闲置，提升矩阵吞吐 |
| ② Phase-aware pipeline | Attention 内矩阵阶段和 softmax/reduction 阶段偏好的执行资源不同，串行安排会出现空档 | SME 计算后续 tile 的矩阵阶段时，CPU 核同时处理已就绪 tile 的 Softmax；以满足依赖为前提 | 减少等待和空泡，避免误画成同一 tile 的依赖被突破 |
| ③ Layout-aware runtime | SME kernel 喜欢 packed layout，每次调用时重新转换浪费搬运/带宽 | 静态权重提前打包、KV-cache 在产生时形成可复用布局，下游再使用时尽可能无需反复转换 | 减少重复 packing / memory traffic |

这三个机制解决不同问题，**不是必须 ①→②→③ 顺序执行的一条流水线**。图中三个方法卡并列，分别给出简化数据示意。

## 可核对的论文数据

原论文：[Feiyang Chen、Haibo Chen, *SMEPilot: Characterizing and Optimizing LLM Inference with Scalable Matrix Extensions* (2026)](https://arxiv.org/html/2606.16332)；§3.1–4.4、§5.2、§5.4、Figure 9 / Figure 12。

**Figure 12 消融实验，Apple M4 Pro CPU，三种不同算子，不能混成一条总加速：**
- 移除 tile-level work partitioning：GEMM 耗时相对完整 SMEPilot **增加 1.46×**。
- 移除 attention pipeline：Prefill Attention 耗时相对完整 SMEPilot **增加 2.07×**。
- Decode GEMV：重复在线 packing 为 **1.71 ms**，而 layout-aware 完整版本为 **0.52 ms**。这里使用绝对延时而不是将其和前两个倍数相乘。

**Figure 9 完整 LLM 推理**：在所测 Apple M4 Pro、MediaTek Dimensity 9500 手机平台与 KunPeng 服务器平台、特定模型和任务的组合中，相对 `llama.cpp` 默认 CPU 后端，端到端推理**最高 3.94×**；这个是跨测试配置的**最高值**，**不等于手机单独达到 3.94×**、也不能直接推成 Agent 工作流实测。幻灯片把它放在来源脚注而非三项消融主数据中。

**论文证据界限**：没有从一篇 SMEPilot 论文推出 Agent 专用新硬件需求。已有 SME ISA 与 CPU 编译/runtime 协作值得研究；不同执行单元仍共享内存带宽。

## 交付与实际 QA

本轮会话生成：
- `/mnt/data/round15n_slide07/slide07_smepilot_blue_editable.pptx` — 真实可编辑 PPTX；
- `/mnt/data/round15n_slide07/slide07_smepilot_blue_preview.png` — 由 PPTX 转 PDF 后导出的高清 PNG，1920×1080；
- `/mnt/data/round15n_slide07/make_slide07.js` — PptxGenJS 原生形状与文字生成脚本（依赖同目录 header_art.png），**尚未作为源脚本提交 GitHub**。

**实际文件 QA**：PPTX ZIP 完整；共 **83 个 PowerPoint 原生可编辑 shape/text 对象 + 1 张独立装饰插画**；Speaker Notes 存在；PPTX 原生文本检出标题、CPU-only/SME-only/CPU+SME、1.46×、2.07×、1.71/0.52 ms、`07 / 15`；PPTX 的 URL 关系文件包含 [论文原文](https://arxiv.org/html/2606.16332)；生成脚本检查全部元素均未越出 13.333×7.5 inch 页面；预览 PNG 1920×1080 为 16:9。制作过程观察了完整 PNG 并检查主流程、三项机制、三项消融、页码、底部结论与来源文字。

**尚待**：用户实际视觉审阅；真实 Microsoft PowerPoint 打开后字体、超链接与投影阅读测试；原论文全部 Figure 的逐像素比对。本 GitHub 文档为研究与制作记录，**不声称已将 PPTX/PNG 二进制上传至 GitHub**。

## 下一步

若用户认可，第 7 页与第 4/5/6/8 页可以组成连续技术证据链，进入 **第 1–3 页领导故事开场页**制作；最终将对 15 页统一页码、页眉、颜色、超链接及可编辑性做批量 QA。**不要因为本页输出成功就自动接受视觉稿。**

## 架构术语纠错：SME 是 CPU ISA 扩展，不是与 CPU 平级的处理器

2026-10-08 用户质疑：不能在 PPT 里直接写“让 CPU 核与 SME 更好分工”，因为 SME 首先是 Arm CPU 的指令集扩展。

**核对结论**：
1. Arm 官方 [SME 介绍](https://newsroom.arm.com/blog/scalable-matrix-extension) 将 SME 定义为 **Armv9-A CPU ISA 扩展**，引入矩阵类指令和架构状态；不是另一种与 CPU/NPU 平级的独立处理器。
2. [SMEPilot §3.1 与 Figure 1](https://arxiv.org/html/2606.16332) 研究的是 **支持 SME 的 CPU/CPU cluster 内的常规 CPU 核执行资源，与用于 SME 指令的专门矩阵执行资源**。在其研究的实现中，两者可同时贡献计算吞吐，但共享内存带宽；两种资源在**执行资源层**可以作为协作对象，在**芯片处理器层**不能把“CPU”和“SME”平列。
3. 硬件实现与具体芯片相关。Apple [XNU SME 文档](https://github.com/apple-oss-distributions/xnu/blob/main/doc/arm/sme.md) 也指出 SME 计算资源可能被多个 CPU 共享；不把任何单个示意图冒充 ARM 架构强制的物理组织。
4. 旧版标题被用户质疑后，当前**Markdown 修改为上面的建议标题**；此前已导出的 **V1 PPTX/PNG 尚未更新标题**，不得声称 PPT 已完成替换。

**视觉规范**：最外层大框必须明确标为“支持 SME 的 CPU / CPU Cluster”，其内并列小框标为“常规 CPU 核执行”和“SME 矩阵执行资源”；下方以“共享缓存/内存带宽”表示资源耦合。不再画“CPU → SME”硬件级跨处理器通信，也不写“CPU vs SME”而不说明是两种执行**路径**。
