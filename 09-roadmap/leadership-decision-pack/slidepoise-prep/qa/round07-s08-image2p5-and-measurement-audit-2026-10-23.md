# Round07｜S08 Image2.5 + 受控 CPU/SME2 图像审计（2026-10-23）

> **状态：实物 PNG 已生成并在当前会话中预览，内容与来源核对通过，仍待最终用户视觉签收和 native SlidePoise 验收。**
> 禁止将基于图像模型生成的芯片概念外观当成真实微架构图。

| Gate | 检查 | 结果 |
|---|---|---|
| 视觉素材来源 | Image2.5 生成蓝色概念芯片插画；本页实际放入一个标注为“非真实 CPU 布局”的小画面 | PASS |
| 严格文字/数据 | 标题、CPU 层级、延迟柱、来源由可审查 SVG 绘制 | PASS |
| 手机设备与设置 | vivo X300 / SqueezeSAM / 1 CPU 核 / Normal mode | PASS |
| INT8 | 555.8→304.1 ms；1.83×；PyTorch/Arm 第一方数据 | PASS |
| FP16 | 1163.0→298.2 ms；3.90×；相同设备及精度组外不进行无条件外推 | PASS |
| 数据搬运 | SME2 开启后 INT8 41.4%，FP16 39.9% | PASS |
| 绝对时间坐标轴 | 两组比较都使用 0–1200 ms | PASS |
| CPU/SME 层级 | SME/SME2 位于 CPU 核内；GPU/NPU 另是 SoC 的其他引擎 | PASS |
| 独立芯片 / Agent / 手机能耗错误外推 | 没有出现不受证据支持的推断 | PASS |
| 中文文本实际范围 | 在 Noto Sans CJK SC 字体下 55 个文字对象测量，发现 **0** 处超出画布 | PASS |
| 真 SVG→PNG / 16:9 预览 | 分别 2048×1070、2048×1152，真实打开检查过 | PASS |
| Microsoft YaHei Windows 字体 | 本地运行实际字体是 Noto Sans CJK；Windows 和 PowerPoint 字体替换尚未验证 | PENDING |
| GitHub PNG 字节 | GitHub 已写 QA/Manifest，**未写入二进制 PNG** | PENDING |
| PPTX 本地 native reconstruction | 尚未进行 | NOT_DONE |
| Speaker Notes 写/读回 | 尚未进行 | NOT_DONE |

**本轮修正**：最初 FP16 1163.0ms 标签贴于原基线柱内，已移至条形外侧；引用行将 SMEPilot CPU/SME 研究机理与 LLVM/MLIR 官方资料区分，避免把 LLVM pass 错归为 vivo 测试栈。

**来源适用边界**：官方发表日期 2026-01-29；文章 Table 2 测量 model-only latency、1 CPU core，Normal/default power，vivo X300。SMEPilot 为不同研究/设备集合；其 Apple M4 Pro 能耗数字不来自手机，故本页不使用。引用：`https://pytorch.org/blog/accelerating-on-device-ml-inference-with-executorch-and-arm-sme2/`、`https://arxiv.org/abs/2606.16332`。

**后续使用**：本页即使通过用户视觉审查，仍然只是 SlidePoise 的一个可提交生成目标的视觉候选，不能自动升格为已存在的 `accepted-slide.png` 或可编辑 PPTX。详见 [S08合同](../12-s08-approved-copy-and-reconstruction-contract.md)。
