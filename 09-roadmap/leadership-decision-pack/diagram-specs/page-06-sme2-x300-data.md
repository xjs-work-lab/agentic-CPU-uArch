# 第 6 页：vivo X300 单 CPU 核 SME2 开关对比的可视化数据合同（官方来源复核）

**原文**：[PyTorch / ExecuTorch 与 Arm 技术博客](https://pytorch.org/blog/accelerating-on-device-ml-inference-with-executorch-and-arm-sme2/)，2026-01-29；Fig. 1、Table 1、Table 2。真实设备 vivo X300；SqueezeSAM 图像分割；ExecuTorch + XNNPACK + KleidiAI；Normal mode 默认电源策略；**单个 CPU 核、model-only latency**；不是 Agent 工作流，不是 CPU/NPU 横向对比。

## 主图：同机 on/off 成对水平柱（ms，低为好）

| 精度 | SME2 关闭 | SME2 开启 | 作者报告加速 |
|---|---:|---:|---:|
| INT8 | 555.8 ms | 304.1 ms | 1.83× |
| FP16 | 1163.0 ms | 298.2 ms | 3.90× |

注：Fig. 1 与 Table 1 使用整数近似显示，**Table 2 提供本文采用的一位小数**；所有标签必须声明同一 measurement mode。

## 辅图：优化后 Data Movement 比例（Table 2）

| 精度 | Data Movement ms | SME2 开启后占比 |
|---|---:|---:|
| INT8 | 125.8 | 41.4% |
| FP16 | 119.1 | 39.9% |

这是 SqueezeSAM 的算子分类占时，部分来自 layout transpose；非 GPU↔NPU 拷贝份额，也非任何 Agent 应用通用比例。

**关键机制**：文章指出约 85% 的数据搬运时间来自 transpose，指向 NCHW↔NHWC 格式反复转换；这是文章中具体视觉模型和 XNNPACK 路径的问题。可用小型 *layout转换示意图*，不可画成已测量的 CPU L1↔L2 总线时序。

**边界**：作者包括 Arm 人员；性能不代表独立学术复现，也不意味着“CPU 必胜 NPU”。来源链接必须作为 PPTX 可点击引用。
