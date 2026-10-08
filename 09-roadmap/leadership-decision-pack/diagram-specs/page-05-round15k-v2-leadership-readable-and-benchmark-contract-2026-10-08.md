# 第 5 页 ShadowNPU V2：领导可读性与科学基线双重锁定合同

日期 2026-10-08。**替代** [V1 样板记录](page-05-round15k-visual-pilot-status-2026-10-08.md) 作为第 5 页当前制图输入。修复用户连续指出的：执行分工不清、CPU/GPU 开销表述模糊、两论文来源不显性、论文性能数据没有基线、Graph Bucketing 与 Head-wise Pipeline 不知支撑哪步，以及术语密度超出领导阅读需求。仍为**待用户视觉/语言验收的样板**。

## 一、这页只传达一个结论

**主标题**：ShadowNPU 让 NPU 筛选重要 Token，CPU/GPU 只精算关键部分。

**论证目标**：展示手机 LLM 在已有 NPU 上，仍能通过编译、量化和跨处理器的执行分工减少 CPU/GPU 全量计算；这支持 CPU 与 NPU 协同演进，**不直接证明 Agent 专用 ISA 的价值**。

解释句：Attention 用于计算当前内容与上下文的关联；由于完整计算对 INT8 量化误差敏感，在 2025 年 llm.npu 的实现中仍主要由 CPU 处理。Token 是模型处理的文本片段。

## 二、两个研究方案必须在画面里看得出来

| 研究 | 原论文、公开年度 | 明确采用什么技术 | 确切边界 |
|---|---|---|---|
| **llm.npu** | [ASPLOS 2025 原始 PDF](https://xumengwei.github.io/files/ASPLOS25-NPU.pdf) | 分块共享计算图、量化离群项的 shadow execution、乱序子图调度，使 QKV Linear、FFN 等适配算子在 NPU 高效执行 | 其 Attention 主要在 CPU；不能说所有框架或所有 Attention 永久只能由 CPU 执行 |
| **ShadowNPU / shadowAttn** | [MobiSys 2026 原文](https://arxiv.org/html/2508.16703v4) | NPU INT8 重要性估计，CPU/GPU Top-k 后只对少量关键 Token 做高精度 Sparse QKV；再增加 Graph Bucketing、Head-wise Pipeline | 不是 NPU-only Attention；RoPE 等步骤仍可能由 CPU/GPU 执行；不能把两论文拼成一条执行流水 |

**关系**：ShadowNPU 的端到端测试将 shadowAttn 集成到 llm.npu 框架中；两个研究有技术链条联系，不能当作独立复现，更不能跨论文相乘 speedup。

## 三、主流程节点与箭头

| 图内 ID | 展示文字 | 为什么这么做 | 传给下一步什么 |
|---|---|---|---|
| S1 | **NPU 快速估分**：用 INT8 Q·K 粗筛 | 选重要 Token 所需的相对排序，比完整注意力输出的绝对精度更适合低精度估计 | 每个 Token 的近似重要性评分 |
| S2 | **CPU/GPU 选重点**：Top-k 选择重要 Token | 只保留可能显著影响当前输出的 Token，减少后续高精度工作 | 被选 Token 的索引/位置 |
| S3 | **CPU/GPU 精算**：只处理被选 Token 的 Attention | 避免 CPU/GPU 对全部 Token 执行完整高精度 Attention | 高精度 Attention 输出 |

**连线**：S1→S2 是近似评分；S2→S3 是选出的索引（高精度阶段还需访问所需 Q/K/V 数据，不得暗示只传索引就完成计算）；无未经证实的 CPU↔NPU 直接硬件物理链路。

### 两项系统优化必须接到明确的步骤

| 技术 | **必须显示的支撑范围** | 带入正文的因果解释 |
|---|---|---|
| **Graph Bucketing** | **支撑 S1**（NPU 估分前的运行时计算图选型） | 离线准备多套量化 scale/输入长度适配的 NPU 图；运行时选择更匹配当前 Q/K 的一套，避免固定配置下估分误差变大 |
| **Head-wise Pipeline** | **覆盖 S1–S3**（不同 Attention Head 的跨阶段执行安排） | 让不同 Head（不同组 Attention 计算）的 NPU 估分与 CPU/GPU Top-k/精算交错进行，减少互相等待 |

两项都不是全新的独立处理器、不是同等位置的业务步骤。正式展示中要写“支撑步骤①”“贯穿步骤①–③”，不放没有归属的孤立小字。

## 四、数字只有写清楚基线才允许出现

ShadowNPU §5 Table 6/Fig. 11/Table 8。**三个指标不是一个实验：**

| 结果 | 明确对照 | 设备与测量口径 | 限制 |
|---|---|---|---|
| **端到端推理最高 4.5× 加速** | 对 `C/G-Full`：CPU/GPU 上完整 FP32 Attention | MI14 / Snapdragon 8 Gen 3，shadowAttn 集成 llm.npu，指定 Qwen2/PhoneLM 模型及 ArxivSum、DroidCall、Octopus 等任务；论文平均 2.9× | 默认 CPU/GPU 资源受限为一个 CPU 中核；仅论文受测配置 |
| **单个 Attention kernel 能耗最高约 7.7× 降低** | 对 `C/G-Full` | Redmi K60 冠军版 / Snapdragon 8 Gen 2，输入 1024 的单 kernel 能耗，Table 8 的最大改善约 7.66× | **不能**说成完整 LLM/Agent 工作流的端到端能耗 |
| **平均准确率下降 0.4 个百分点** | 对 `C/G-Full` 完整 FP32 Attention | 四种模型×三个任务数据集，Table 6，平均 36.8 → 36.4 | 具体任务 accuracy 的百分点，不是“性能下降 0.4%” |

**基线注释统一**：`C/G-Full = CPU/GPU 完整 FP32 Attention`。不将“C/G-Sparse”“NPU-Full”和 C/G-Full 混用为同一基线；不同设计方案还存在准确率差异。

## 五、制作方案和外观边界

- 页面上部：陈述句主标题 + 首次出现的 Attention/Token 解释。
- 主体：**左 llm.npu 2025 旧分工，右 ShadowNPU 2026 新方案三步**；两篇论文有独立年份、论文名和真实链接。
- 主图下：Graph Bucketing 支撑 ①；Head-wise Pipeline 贯穿 ①–③。说明具体动作、解决的阻碍，不堆没有解释的名词。
- 数据栏：三列不同测量指标，各自附正确设备/层级/基线；不画跨实验可比的伪 bar。
- 页底：与 CPU/LLVM、NPU/Runtime 协作的意义；一律不写已经获得 Agent 专用 CPU 指令的硬件新颖性证据。
- 统一浅蓝学术风格，技术框/文字为 PowerPoint 原生可编辑元素；Image Generator 装饰性背景不包含实验事实或固定文字。PNG 是由同一 PPTX 导出。

## 六、真正的“领导读懂”验收

1. 不看论文，能回答“2025 旧方案的 Attention 是谁算的，为什么？”。
2. 30 秒内读懂 “NPU 初筛 → CPU/GPU Top-k → CPU/GPU 稀疏精算” 每步输出及目的。
3. 能指出 Graph Bucketing 支撑 S1，Head-wise Pipeline 跨 S1–S3，并能说出各减少什么代价。
4. 能说出“4.5× 是什么指标，与谁相比；7.7× 为什么不是完整推理能耗”。
5. 能理解对 CPU 团队的结论，但不会从这里误推断“硬件专用 ISA 已证实”。

## 七、资产状态

本会话已生成如下**当前会话文件**；**没有**把二进制直接提交 Github，不能假称仓库可以下载二进制：
- `/mnt/data/round15k_shadownpu_v2/round15k_slide05_shadownpu_v2_editable.pptx`
- `/mnt/data/round15k_shadownpu_v2/round15k_slide05_shadownpu_v2_preview.png`
- `/mnt/data/round15k_shadownpu_v2/make_slide05_v2.js`

基础程序 QA：1 页；1920×1080 PNG；53 个 PowerPoint 原生可编辑形状/文字对象及 1 张装饰图片；S1→S2、S2→S3 两条独立水平箭头；正确包含两个原论文超链接、基线、分工术语和数值。**尚未**通过用户最终阅读审查或真实 Microsoft PowerPoint 环境字体/超链接测试。
