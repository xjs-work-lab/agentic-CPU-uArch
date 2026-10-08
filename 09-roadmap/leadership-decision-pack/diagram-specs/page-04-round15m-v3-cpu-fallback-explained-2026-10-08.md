# Round15M / 第 4 页 V3：解释 CPU Fallback，补充“为什么收益缩小”

日期 2026-10-08。**当前状态：第 4 页 V3 PPTX 与 16:9 PNG 实物已制作，通过基础 ZIP/图形/数值/超链接测试，待用户视觉和内容审阅。** 对比之前的 [V2 制作记录](page-04-round15m-editable-pilot-2026-10-08.md) 与 [Table III–V 的数据合同](page-04-stage-benchmark-data.md)，V3 保留三幅定量图与用户认可的纯蓝配色，不从零重做。

## 本页面向非专业领导的完整观点

**主标题**：NPU 的单次 Decode 运算更快，CPU 回退与频繁调用却压缩了收益；因此要同时优化算子覆盖与跨处理器交接。

**开头背景**：同设备 Snapdragon 8 Gen 3，Qwen3-4B，6 CPU 线程；Prefill 一次处理输入提示词，Decode 逐个生成 Token。各图数值都是此型号和该软件后端的受测结果，不代表所有新 NPU 系统。

**主要证据三栏，不能合并不同量纲**：
- ① Table III Prefill 每次 MUL_MAT（μs）：CPU 7,181，NPU call-usec 10,352，**CPU 快 1.44×**。
- ② Table III Decode 每次 MUL_MAT（μs）：CPU 324，NPU call-usec 210，**NPU 快 1.55×**。
- ③ Table V Decode 聚合算子耗时（ms）：全 CPU 路径 23,889，NPU 路径中 NPU 执行 15,767 + CPU fallback 6,966 = 22,733，**汇总快 1.05×**。
- 每个栏内柱长按本栏统一实数尺度缩放，**不同栏柱长不互比**。①②的 NPU 数值包含调用、通信与同步开销，不能叫纯 NPU kernel timing；③是 aggregated operator latency，不能误写为完整 Agent 任务的端到端墙钟时间。

## 新增解读模块：CPU Fallback 不是 CPU/NPU 故障

论文 §II-A（运行时后端模型）和 §IV-D（Scheduling Overhead）明确指出：
- 软件 Runtime/后端根据算子支持情况，将支持的算子交给 NPU；不支持的算子交给 CPU。这就是 CPU fallback，**不是 NPU 先运行失败再临时重启 CPU**。
- 例：论文受测的 Hexagon backend 对 `FLASH_ATTN_EXT` 没有 native 支持，执行分派到 CPU；跨后端执行可能带来缓存一致性同步、Tensor reorder、Memory Copy 等额外成本。
- 此次在 V3 以**上下两条并列分支**展示 “后端支持→NPU 执行” 和 “后端不支持→CPU Fallback”。严禁把两条路径画成 CPU 与 NPU 之间固定的串行物理箭头，或 CPU 直接控制 NPU 的硬件通道。

## 两种额外成本如何影响整体收益

- **高频调用**：论文 Table IV 中 Qwen3-4B Decode 的 NPU communication 占 12.7%；许多小算子的纯计算很短，调度/通信可能累积成瓶颈。
- **CPU fallback**：Table V Qwen3-4B NPU 执行路径仍有 6,966 ms 是 CPU fallback 的算子耗时；论文 §IV-D 还讨论了跨后端同步、tensor rearrangement/copy 产生的额外成本。注意 6,966 ms 是 fallback 相关算子耗时汇总，并**非仅计算处理器切换开销**。
- **工程启示**：Prefill/Decode 需要分阶段选择执行路径；优化 NPU 的算子覆盖与 Dispatch；保留 CPU 可编程快路径并优化数据布局、同步和跨后端调用；不能仅据本实验决定新增 Agent 专用 CPU 指令。

## 依据、素材与制作状态

**来源**：[Li, Qi, Chen, *When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference* (2026)](https://arxiv.org/html/2605.27435)，§II-A / III / IV-B–D，Tables III–V。

本轮原生 PPTX 使用 [V2 JS](../../../leadership-decision-pack/diagram-specs/page-04-round15m-editable-pilot-2026-10-08.md) 的排版思路与当前已认可的纯蓝色芯片装饰素材，新增文案、两分支解读和实验解释；图内文字、技术数据和卡片为 PowerPoint 原生可编辑元素，一张芯片插画保留为独立图片。

**会话交付产物（未提交二进制到 Github）：**
- `/mnt/data/round15m_slide04_v3/slide04_snapdragon_cpu_npu_v3_editable.pptx`
- `/mnt/data/round15m_slide04_v3/slide04_snapdragon_cpu_npu_v3_preview.png`
- `/mnt/data/round15m_slide04_v3/make_slide04_v3.js`
- `/mnt/data/round15m_slide04_v3/header_art.png`

**实测制作检查**：
- PPTX ZIP 有效，1 页 16:9；导出预览 PNG 为 1921×1080。
- 68 个原生形状及文本对象、1 张芯片装饰图；文本里包含所有主要数值、CPU Fallback 的解释、论文原文可点击链接。
- 所有对象通过生成脚本的页界检查；当前已复核 PNG 页面排版和文字可见。
- 不将此文件称为已通过用户审阅、真实 Microsoft PowerPoint 环境验收或论文截图逐像素复刻。

## 制作经验与约束

必须让每个读者都能从页内完整回答：
1. CPU Fallback 是什么（NPU 不支持时 CPU 接手，而非故障）？
2. 两种成本分别指什么（高频调用通信 vs. CPU fallback 工作和交接）？
3. 三张图是在什么不同测量口径下得出结论？
4. 这对 CPU/Compiler/Runtime 应优先优化什么？

下一步等待用户对“实验图信息量、底部解释清晰度、投影字号、全页视觉密度”的审阅，再确定是否作为第 4 页当前视觉定版。
