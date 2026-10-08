# Round15M：第 4 页 Snapdragon CPU/NPU 实测的纯蓝色可编辑样板

日期：2026-10-08。**第 4 页试制已制作并通过基础文件与数据 QA，等待用户视觉/内容审阅；不得预先视为最终定版。**

## 本页要让缺少领域背景的领导读懂什么？

**修订后主标题（V2）：** NPU 单次运算更快，Decode 算子总耗时却只小幅下降；因此 CPU 回退和跨处理器通信同样值得优化。

**前提解释：** Prefill = 一次处理输入提示词；Decode = 逐个生成 Token。论文中 Prefill 属于 GEMM 类大矩阵阶段，Decode 以 GEMV 类矩阵-向量处理为主。

**结论：** 同一款模型在输入处理与逐字生成阶段，CPU/NPU 可能出现优势反转；即使单次 NPU 算子更快，CPU 回退及调用/通信成本也可能使较大范围内的实际收益缩小。**不能凭此推导所有平台上 CPU 总优于 NPU**。对 CPU-uArch 研究的价值是继续优化现有 CPU 计算快速路径，并与 NPU 软件/Runtime 联合降低回退和调用成本。

## 论文原始来源、设备与基线

[Li, Qi, Chen (2026), When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference, arXiv:2605.27435](https://arxiv.org/html/2605.27435)。

- Snapdragon 8 Gen 3 / Hexagon v75 NPU / Android 15 / 16 GB RAM / llama.cpp tag `b7588`。
- Q4_0 量化；CPU 线程数 6、默认 batch size 128、约 1,281 个提示词 token。作者每一配置重复 10–15 次，并用 IQR 做异常值过滤。
- 同一案例选择论文 **Qwen3-4B**，不要把多个不同模型的大小和速度拼成一条连续的“单次实测”；后续作者也研究其他 Llama/Qwen 模型。
- **Table III** 是单次 `MUL_MAT` 调用耗时 `μs`；NPU 的 `call-usec` **包括调度/通信/同步**，不能叫 NPU 纯 kernel 计算时间。
- **Table V** 是 **Decode-stage aggregated operator latency**，是算子耗时加总 `ms`，**不是完整 Agent 用户任务端到端墙钟时间**。
- **Table IV** 的通信百分比是作者用 OPMASK 控制分解测得的 NPU Pipeline 份额，仅能用于论文这个条件。

## 三张不同口径的证据图（均为同一 Qwen3-4B 模型）

| 栏位 | 图中表示的指标 | CPU 数值 | NPU 数值 | 图形结论 |
|---|---|---:|---:|---|
| ① Prefill | 单次 MUL_MAT 调用，μs | 7,181 | 10,352（含调用开销） | CPU 快约 1.44× |
| ② Decode | 单次 MUL_MAT 调用，μs | 324 | 210（含调用开销） | NPU 快约 1.55× |
| ③ Decode | 汇总多次算子耗时，ms | 23,889 | NPU 算子 15,767 + CPU fallback 6,966 = 22,733 | 汇总仅快约 1.05× |

**不可比性保护**：三个模块各自的条长按本栏最大值线性缩放，不能跨栏比较柱长；③ 另把 NPU 路径拆成两段真实堆叠数据。所有数值均来自原始论文表格；图中未添加假误差条、假比例或没有依据的 CPU/NPU 权重。

**为何收益缩小？**
- 论文 Table IV：Qwen3-4B Decode 的 NPU 通信占比 **12.7%**。处理器并非只执行纯计算，细碎工作每次调用会积累开销。
- 论文 Table V：NPU 路径算子总计中 **6,966 ms** 是仍回退到 CPU 的部分；说明现有软件后端算子覆盖对最终收益影响很大。

## 视觉和可编辑交付

- 继承用户最终认可的 **[第 5 页 ShadowNPU V3 纯蓝色视觉基准](page-05-round15k-v2-leadership-readable-and-benchmark-contract-2026-10-08.md)**：浅蓝底、深蓝大标题、浅蓝分区、右上芯片插画和蓝色文字层次；不用绿色和橙黄色模块。
- 本页采用原生 PowerPoint 形状、真实时延条、可编辑数字和来源链接；右上芯片插画单独作为装饰图层。
- 当前会话文件：`/mnt/data/round15m_slide04/slide04_snapdragon_cpu_npu_blue_editable.pptx` 和从同一 PPT 导出的 `/mnt/data/round15m_slide04/slide04_snapdragon_cpu_npu_blue_preview.png`；**目前没有确认二进制 PPTX/PNG 已存放在 GitHub**，GitHub 存储的是本制作说明和证据链接。
- 当前会话源脚本：`/mnt/data/round15m_slide04/make_slide04.js`，其中芯片装饰资源指向本地上一页的源素材路径，迁移工作环境时需要更新。

## 质量检查与剩余 Gate

本轮实际检查：
- 1 页宽屏 PPTX ZIP，61 个原生 `p:sp` 图形/文本，1 个独立装饰图片 `p:pic`。
- 所有关键数值 `7,181`, `10,352`, `324`, `210`, `23,889`, `22,733`, `15,767`, `6,966`, `12.7%` 均可从 PPTX 原生文本检出。
- PPTX 关系文件存在原始 [arXiv HTML](https://arxiv.org/html/2605.27435) 超链接，Speaker Notes 记录全部实验范围与四模型统计差异。
- 非蓝色旧风格关键十六进制如 `C8702D`, `078F88`, `FFF0E4` 未在幻灯片 XML 检出。
- PPT 通过 LibreOffice 转 PDF 再导出 PNG：**1921×1080 px（约 16:9）**；截图人工检查主标题、三个数据模块、开销原因、结论均显示。

仍未做：真实 Microsoft PowerPoint 打开后的兼容性、投影距离下字号、原论文可点击链接的人工点击、用户对技术可读性与设计风格的审阅。**本轮不得写“第 4 页已定版”。**

下一步建议：用户确认第 4 页后，按同样纯蓝色模板制作第 7 页 SMEPilot，并同步做相邻页面的叙事接续审查（4 → 5 → 6 → 7 → 8）。

## V2 用户反馈与制作修订（2026-10-08）

用户指出 V1 标题只陈述测量现象，没有说明对 CPU/NPU 技术投资的结论。V2 将页面主标题修改为：**NPU 单次运算更快，Decode 算子总耗时却只小幅下降；因此 CPU 回退和跨处理器通信同样值得优化。** 同时将原先的问句式辅助标题改为：**CPU 回退与通信开销，使单次算子提速未充分转化为阶段收益。**

本轮从原生 PPTX 生成的文件：`/mnt/data/round15m_slide04_v2/slide04_snapdragon_cpu_npu_v2_editable.pptx`，同源 PNG：`/mnt/data/round15m_slide04_v2/slide04_snapdragon_cpu_npu_v2_preview.png`。**仅修改 2 个标题**，原始数据、蓝色风格、图表和来源链接不变。程序化检查：ZIP 包完好；61 个可编辑形状；1921×1080 导出 PNG；新标题存在；全部关键数据未变。**仍待用户目视确认 V2。** 当前产物位于会话文件空间，尚未作为二进制资产提交 GitHub。
