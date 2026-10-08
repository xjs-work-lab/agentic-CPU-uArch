# Round15N 第 7 页 V2：SME 指令扩展与 CPU 执行路径的架构层级修订

日期：2026-10-08。用户指出 SME 是 CPU 指令集扩展，不能让“CPU 核与 SME”成为无解释、似乎平级的两个处理器。前轮 [第 7 页 V1](page-07-round15n-smepilot-editable-pilot-2026-10-08.md) 的信息量/视觉方向得到“比较清晰了”的反馈，但术语层级错误需要修复。本轮**已实际更新单页可编辑 PPTX 并从同一 PPTX 导出 16:9 PNG**，用户尚未审阅 V2，不能视为最终定版。

## 1. 新版锁定文案

- **主标题**：**SMEPilot 协同利用 CPU 的通用计算与 SME 矩阵计算能力，通过分块并行、流水重叠和数据复用减少执行开销。**
- **首屏解释**：**SME 是 Arm CPU 的矩阵指令扩展，并非独立 NPU；本文讨论的是 CPU 体系内不同执行资源的协同。**
- **主模块结论**：**同一 CPU 体系内选择合适的执行方式，并减少等待与数据整理开销。**

### CPU 内部可选的三种执行路径

| V1 模糊表述 | V2 领导可读表述 | 技术限定 |
|---|---|---|
| CPU-only | **常规 CPU 路径** | 主要使用 CPU 的通用标量/向量执行 |
| SME-only | **SME 指令路径** | 使用 CPU ISA 中的 SME 矩阵指令、具体硬件实现相关 |
| CPU + SME 协同 | **两类执行路径协同** | 仅在论文受测实现和执行/带宽条件支持时并行互补，不宣称两颗独立 SoC 处理器 |

**两个不同的抽象层次必须分清**：SME 是 ISA 扩展；SME 指令的矩阵运算可能由实现中特设的矩阵硬件资源承担。论文研究 CPU cores 与 SME unit 的协作，但其硬件布局不是 ARM ISA 的强制通用结构。三种**路径**属于受支持的 CPU 计算体系，不应画成 CPU/NPU 那样的芯片级异构资源横向分配。

## 2. 保留的三机制与实验

三卡片分别展示 tile-level partition（常规 CPU 核与 SME 矩阵资源分担 tile）、phase-aware pipeline（不同就绪 tile 上交错做矩阵/softmax）、layout-aware runtime（重用静态权重、KV-cache 适当的布局）。它们是不同优化策略，非 ①→②→③ 串行执行。

论文 [SMEPilot](https://arxiv.org/html/2606.16332) Figure 12 的 Apple M4 Pro 消融口径不变：
- 去掉分块协同，GEMM 时延 **1.46×**；
- 去掉 Attention 流水，Prefill Attention 时延 **2.07×**；
- 重复在线 packing 的 Decode GEMV **1.71 ms**，复用数据布局降低为 **0.52 ms**；
- Figure 9 的全体受测配置最高 3.94× **相对 llama.cpp 默认 CPU 后端**，仍只作为原论文受测条件的结果，不被画成所有手机固定提升。

## 3. 文件、验证与未通过项目

**会话实际产物（尚未作为二进制归档到 GitHub）**
- 可编辑 PPTX：`/mnt/data/round15n_slide07_v2/slide07_smepilot_v2_cpu_hierarchy_editable.pptx`
- 同源预览 PNG：`/mnt/data/round15n_slide07_v2/slide07_smepilot_v2_cpu_hierarchy_preview.png`
- 生成 JS：`/mnt/data/round15n_slide07_v2/make_slide07_v2.js`
- 装饰图片仍为独立素材：`/mnt/data/round15n_slide07_v2/header_art.png`

实际执行的 QA：
- ZIP 完整、单页 16:9；PNG **1920×1080**。
- **83 个 PPT 原生可编辑形状/文字元素**，与 V1 的数量一致；另 1 幅装饰性图片。
- 新标题、SME ISA 解释、三种执行路径均存在于 PPTX 可编辑文本中；旧的 `CPU-only` 字符串和易误读的原标题不再出现。
- `1.46×`、`2.07×`、`1.71→0.52 ms`、Apple M4 Pro、`07 / 15` 与 V1 保持一致。
- 论文 arXiv 链接、Speaker Notes 仍在 PPTX 内。LibreOffice/PDF 转 PNG 后进行了排版目视检查，五区布局与文字未见明显溢出。
- **待完成**：用户对 V2 架构层级与可读性的审阅；真实 Microsoft PowerPoint 字体兼容和链接点击验收；最终全套 15 页页码母版统一。

## 4. 下一阶段

一旦确认 V2，**第 4–8 页的技术证据样板可串联**（第 4 页真实 CPU/NPU 边界 → 第 5 页 NPU 软件扩展 → 第 6 页 CPU SME2 现有 ISA → 第 7 页 CPU 内执行与数据复用 → 第 8 页 Agent DAG 跨处理器调度）。此后优先制作 1–3 页完整故事开场，特别执行“可独立读懂 + CPU/NPU/SME 层级不混淆 + 逻辑箭头清晰 + 统一纯蓝母版与页码”的验收。
