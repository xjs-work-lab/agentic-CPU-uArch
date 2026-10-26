# S07｜讲者备注：优化后的 NPU 软件才是 CPU 的真实强基线

**本页观点。** CPU 与 NPU 不是永久固定的胜负关系。NPU 软件改进静态图、低精度和子图放置后，会重新定义 CPU 的可保留工作；CPU/GPU 对控制、精度敏感的残差、top-k 和 fallback 仍可能必要。

**左侧 llm.npu（PAPER-059，ASPLOS 2025）**：Prompt 分块映射静态图、NPU INT8 主干矩阵运算与 CPU/GPU outlier 计算、按后端亲和度的子图部署。论文在特定 Snapdragon 手机与模型/应用任务上给出平均 Prefill 22.4×、平均能耗节省因子30.7×及最高应用端到端32.8×，但这些值有各自基线和测量口径，未在投影画面混用。

**右侧 ShadowNPU（PAPER-057，MobiSys 2026）**：在 Prefill Attention 中用 NPU 低精度估计重要 token，再由 CPU/GPU 作 top-k 与稀疏高精注意力残差；Decode 的完整 Attention 仍有 CPU/GPU 路径。不能称为“所有 Attention/Decode 已转给 NPU”。

**来源支持与边界。** 原文：https://arxiv.org/abs/2407.05858 和 https://arxiv.org/abs/2508.16703。两项研究存在技术谱系关联，并非完全独立复验；不能把性能倍数相乘、不能由某模型测试推出全手机 NPU 普遍优势。

**对 CPU/LLVM 的意义。** 现有 ISA 优化要对标优化后的异构软件基线，寻找控制、回退、低延迟算子和精度协同真实剩余空间，不凭朴素 NPU 比较直接推动新 ISA。
