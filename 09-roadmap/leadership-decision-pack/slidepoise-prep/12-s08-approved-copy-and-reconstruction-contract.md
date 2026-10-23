# 12｜S08 CPU/SME2 目标图、证据与 native 重建合同（2026-10-23）

> 状态：**SOURCE-BOUNDED PNG RENDERED / IMAGE2.5 ASSET INCORPORATED / USER VISUAL SIGNOFF PENDING**。  
> 这里的 S08 正文 PNG 是在独立 Image2.5 生成的蓝色 CPU 概念插画基础上，重新用可审查的矢量文字、架构关系和精确图表构成的；**不是把 Image2.5 自行画出的性能数字直接接受为真**。  
> 内容来源：[02-S08 合同](02-slide-contracts.md)、[03-S08 证据映射](03-evidence-map.md)、[04 风险边界](04-risk-boundaries.md)及官方原始 [PyTorch/Arm 文章](https://pytorch.org/blog/accelerating-on-device-ml-inference-with-executorch-and-arm-sme2/)。

## 页面结论与不可改变的图形层级

**标题：SME2 是 CPU 内部矩阵能力，编译与布局协同仍有优化空间**

**技术层级：**

```text
Mobile SoC
├─ AArch64 CPU core
│  ├─ scalar / control
│  ├─ SIMD / vector
│  └─ SME / SME2 architectural matrix extension
│      └─ streaming mode + ZA state, subject to implementation/ABI
├─ GPU (a separate engine)
└─ NPU (a separate engine)
```

图中右上方的 Image2.5 芯片插画是**无数据意义的科技素材**，标注“非真实 CPU 布局”。不要依此图推断芯片内部 microarchitecture、面积、物理 tile 阵列个数、互连或制程参数。

## 实验数据闭环（手机，单核，Normal mode）

- 设备：**vivo X300**；工作负载：**SqueezeSAM 视觉分割**；ExecuTorch / XNNPACK / KleidiAI；**1 个 CPU 核**，正常手机功耗策略，model-only 延迟。
- **INT8**：SME2 关 **555.8 ms** → SME2 开 **304.1 ms**（约 **1.83×**）。
- **FP16**：SME2 关 **1163.0 ms** → SME2 开 **298.2 ms**（约 **3.90×**）。
- 统一采用 **0–1200 ms 的绝对时间横轴**；不能把两个精度的原基线都画成相同长度而不说明归一化。
- SME2 开启后数据搬运占比：INT8 **41.4%**、FP16 **39.9%**，属于**同一设备/模型/单核设置**，不是所有手机 CPU 的普遍结构比例。
- 官方原始数值来自 [PyTorch 2026-01-29 文章](https://pytorch.org/blog/accelerating-on-device-ml-inference-with-executorch-and-arm-sme2/) 中 Table 2，实际图像和源代码可独立复核。

## 左栏「编译/ISA 优化路径」的证据范围

- 形状/精度→tile/packing→AArch64 SME2 只是**研究人员综合的工程方法示意**，不是宣称 SqueezeSAM 已使用某个具体 LLVM SME lowering pass。
- SMEPilot 针对 LLM 研究 operator-aware CPU+SME 协作、tile granularity、attention pipeline 和 packing 复用；最高 3.94× 是该论文**特定评估平台**的上限，**未与右侧 vivo X300 图混合**。
- LLVM/MLIR 官方 SME/ArmSME 文档说明架构状态/编译约束；没有直接证明 SqueezeSAM 测量或 Agent 端到端性能。
- 不写 Apple M4 Pro 482.813→233.931J 的数字到此手机页；更不比较 NPU 相对 CPU 的默认胜负。

## 投影中的三项可操作结论

1. **SME2 计算路径**：按形状选择 tile、pipeline 和 packing 复用。
2. **布局转换与内存搬运**：关注 NCHW↔NHWC、transpose 和非矩阵算子。
3. **性能剖析驱动优化**：用 ETDump / 算子归因寻找新的 latency bottleneck。

其中第二、三项由 PyTorch/Arm 官方案例中的算子级 profile 直接支撑；第一项同时受 SMEPilot 的研究机理支持。

## 给 Work 的不可协商规范

- **Content image**：2048×1070，先消费 `S08-controlled-content-v01.png`；2048×1152 的完整页面仅是母版参考图，**不得拿它代替正文 accepted target**。
- **PowerPoint native**：所有标题、子标题、CPU 内部能力框、基线/SME2 on 柱形、数值标签、来源与结论带需原生可编辑；复杂芯片概念插画可保持图片素材，但应可替换且不承载实验数据。
- **图表数据**：必须从本合同/manifest 的数值重建，不能从图片柱形宽度或 OCR 猜测；统一 0–1200ms 横轴。
- **备注顺序**：先讲本页结论；解释 CPU 内 SME2 与 GPU/NPU 不同层级；介绍官方 vivo X300 设备、模型、单核/Normal mode、INT8/FP16 数据；讲数据移动瓶颈；最后解释 SMEPilot 的机制与局限、LLVM 状态/ABI、不能外推 Agent 与 CPU-NPU。
- **禁止**：新 Agent ISA 已被证明需要、SME 是独立 NPU、手机电池能耗结论、全 Agent 任务加速、跨论文直接倍率比较。
- SlidePoise 的原生 master/header/footer 与 Speaker Notes 仍必须经 packaged renderer/真实 PowerPoint 打开后验收，不能因 PNG 已生成就宣称 native PPTX 已完成。

## 当前交付路径与状态

- **实物**：在本次聊天生成 `S08-controlled-content-v01.png`、`S08-16x9-frame-preview-v01.png`、`S08-controlled-content-v01.svg`、Image2.5 小插画素材和 `S08-controlled-source-and-PNG-v01.zip`。
- **GitHub**：[机器可读 manifest](generated-images/formal-content-v02/S08-controlled-png-v01.manifest.json)、[Round07 审计报告](qa/round07-s08-image2p5-and-measurement-audit-2026-10-23.md) 已归档。
- **二进制状态**：GitHub 连接暂未直接提交 PNG 字节；现在在聊天可下载完整 ZIP，manifest 只登记 SHA-256，不声称图片已在 GitHub。
- **G2**：技术与实际 PNG 初步视觉审查通过，等待使用者最终审美认可；
- **G3**：SlidePoise packaged accepted target、native editable PowerPoint 和 Speaker Notes 实测尚未开始。
