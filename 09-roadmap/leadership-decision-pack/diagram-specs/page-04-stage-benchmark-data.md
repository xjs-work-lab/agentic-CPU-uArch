# 第 4 页：Snapdragon CPU/NPU 实测的可视化数据合同（原文复核）

**原文**：[When NPUs Are Not Always Faster](https://arxiv.org/pdf/2605.27435) §III–IV，Table II–V、Fig. 2–3。设备 Snapdragon 8 Gen 3 / Hexagon v75 / Android 15 / llama.cpp tag b7588 / 6 CPU threads / 四款 Q4_0 模型。结果不应外推 2029 最强 NPU 栈。

## 图一：Table III 每次 MUL_MAT 调用的时间（µs；越小越好）

| 模型 | Prefill CPU | Prefill NPU call-usec | NPU/CPU | Decode CPU | Decode NPU call-usec | CPU/NPU |
|---|---:|---:|---:|---:|---:|---:|
| Llama-3.2-3B | 5896 | 9541 | 1.62× | 348 | 208 | 1.67× |
| Llama-3.1-8B | 16085 | 20378 | 1.27× | 646 | 404 | 1.60× |
| Qwen3-4B | 7181 | 10352 | 1.44× | 324 | 210 | 1.55× |
| Qwen3-8B | 12033 | 18444 | 1.53× | 589 | 359 | 1.64× |

**高优先级纠错**：Table III 的 NPU 值是 `call-usec`，**包括 CPU↔NPU 通信等调用总耗时**。因此不得在主图标为“纯 NPU Kernel 计算时延”。可展示“NPU 每次调用”与“CPU 每次调用”对照，同时注明 NPU 的总调用口径。

## 图二：Table IV NPU Pipeline 开销比例（%）

Decode communication：Llama-3.2-3B 13.0；Llama-3.1-8B 10.5；Qwen3-4B 12.7；Qwen3-8B 9.9。都是作者 OPMASK 差分方案中的执行路径比例，不是所有厂商 NPU 的静态比例。

## 图三：Table V Decode Aggregated Operator Latency

| 模型 | CPU 路径 (ms) | NPU operators (ms) | CPU fallback (ms) | NPU 路径合计 (ms) | CPU/NPU 合计比 |
|---|---:|---:|---:|---:|---:|
| Llama-3.2-3B | 19597 | 11844 | 5360 | 17204 | 1.14× |
| Llama-3.1-8B | 40011 | 24583 | 8858 | 33441 | 1.20× |
| Qwen3-4B | 23889 | 15767 | 6966 | 22733 | 1.05× |
| Qwen3-8B | 41285 | 25827 | 9839 | 35666 | 1.16× |

**高优先级纠错**：Table V 标题是 **Decode-stage aggregated operator latency**。它支持“整体阶段的加速被非 NPU 算子与回退压缩”这一推断，但不能把这个表头改为“完整 Agent 任务端到端墙钟延时”。单位原文使用 ms；报告应以原论文说明精确定义，不自造误差条。

## 图片制作要求
三个 panel 各自有原表名、单位、比值方向；无需将三种统计口径放在同一数轴。原论文 Fig. 2 另是不同 ngl 的 **throughput (tokens/s)**，不得混用为每调用 latency。图片底部要有论文原文超链接，PPTX 可点击。图形宽度按真实值线性缩放。
