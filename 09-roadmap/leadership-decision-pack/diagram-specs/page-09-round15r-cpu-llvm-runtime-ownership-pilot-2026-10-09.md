# Round15R · 正文第 9 页：CPU/LLVM、Runtime/OS 研发责任与执行路径

日期：2026-10-09。**当前状态：第 9 页可编辑 PPTX/16:9 PNG 已在本轮会话中实际制作并通过基础文件 QA，仍待用户视觉与内容审阅。** 本页遵守 [四章汇报结构](round15q-cover-agenda-and-chapter-map-2026-10-09.md) 和 [禁用商业化词汇的领导汇报文案合同](leadership-technical-wording-v2-2026-10-09.md)，是第三章第一张正文。

## 1. 页面要给领导的观点

**主标题**：**CPU 团队可先完善 LLVM/SME2 与微内核快速路径，再与 Runtime/OS 协同减少跨处理器执行开销。**

**副标题**：第 4–8 页已有研究表明，现有 CPU/NPU 软件栈仍有优化空间；本页区分哪些技术由 CPU 团队能直接推进，哪些需要协作。

**模块标题**：**编译器准备 CPU 执行能力；Runtime 决定每个阶段实际交给哪个处理器。**

这里的“准备 CPU 执行能力”是工程/编译阶段的代码生成和算子库集成，不等于 Runtime 已经把此阶段派给 CPU。“Runtime 决定执行路径”描述软件控制；具体平台可能由委托执行后端、驱动和 OS 共同参与，**不是一个统一的跨厂商真实 API**，也不是编译器直接操控 NPU 的物理电路。

## 2. 技术机制：两条链路严格区分

### A. CPU 实现准备（编译/开发阶段）

需求：模型矩阵算子的尺寸、精度和目标 CPU 特性。

1. **LLVM/MLIR**：以分块、向量化及 ArmSME lowerings 等技术将适合 CPU 的运算映射到已有指令能力。MLIR 官方 ArmSME 文档提供了 `linalg.matmul → Arm SME FMOPA` 的真实示例；不声称所有模型自动得到同样效率。
2. **调用边界**：LLVM AArch64SME 官方文档规定 streaming mode / ZA 状态在函数调用边界的 ABI 处理，包括 `PSTATE.SM` 和 `PSTATE.ZA` 对寄存器/函数属性的影响。这是确保 SME 代码正确且可组合的已有软件支持；**并未测出手机平台 SM 切换固定时延**。
3. **CPU 微内核**：通过 Neon/SVE/SME2 与 Arm KleidiAI 等优化函数为不同负载准备执行候选。配合数据打包/布局复用，避免计算时间获益被数据整理抵消。KleidiAI 提供具体 kernel 与 packing 方法，但不表示任何给定 Agent 工作流必然提升。

**产出**：可被 Runtime/后端选择的、经功能与性能测试验证的 CPU 算子实现/调用路径。

### B. 运行时执行放置（Runtime/OS 运行阶段）

- Runtime 根据阶段所需算子、精度、实时资源状态/前台响应要求等，选择 CPU 路径或者当前平台软件后端可用的 GPU/NPU 路径；并非固定每个子阶段三个处理器同时执行。
- CPU 路径使用已经准备好的可执行代码/微内核，GPU/NPU 路径由各自受支持的执行栈承担。
- OS/驱动负责通用资源/执行状态支持，配合 Runtime 阶段放置和完成状态观察；双方关系是软件体系抽象，**不是公开验证过的单一统一接口**。
- 如果 NPU 后端不支持某算子，可能采用 CPU fallback，造成额外计算和数据/同步开销；已在 [第 4 页 V3](page-04-round15m-v3-cpu-fallback-explained-2026-10-08.md) 解释过，**此页未制造新的实测比例或加速数据**。

## 3. 三项责任分工与建议的实验验证

| 建议工作 | 主要责任层 | 要解决的技术问题 | 首轮客观验收 |
|---|---|---|---|
| LLVM SME lowering、SM/ZA ABI 正确性、微内核与 packed 布局复用 | CPU/Compiler 团队为主 | CPU 现有 ISA 能否支撑低额外开销的短阶段与矩阵算子 | 同机相同精度的 kernel timing、packing/状态边界成本与正确性 |
| 算子支持矩阵、fallback/copy/sync 成本监测、CPU/NPU 放置规则 | Runtime/NPU 软件协作 | NPU 算子加速为什么不总能传到阶段整体耗时 | 同版本同模型阶段时延与能耗、回退构成 |
| 前台响应和资源争用约束、授权工具动作与真实结果检查 | OS/Agent 平台主责，CPU 需配合 | 用户任务完成受动态优先级、权限和外部副作用影响 | 真实用户任务成功/失败/撤销情况与前台 QoE |

其中第三行**不属于 CPU 团队单独拥有的交付责任**。这些都是技术建议而非已经获批准的团队分工、项目预算或性能指标。

## 4. 可靠来源

- [LLVM: Support for AArch64 SME](https://llvm.org/docs/AArch64SME.html) — SM/ZA IR 属性、ABI 和 streaming mode 处理。
- [MLIR: ArmSME Dialect](https://mlir.llvm.org/docs/Dialects/ArmSME/) — `linalg.matmul` lowering、tile/ZA 操作与示例。
- [Arm KleidiAI](https://github.com/ARM-software/kleidiai) — CPU 微内核与数据打包。
- [第 4 页 Snapdragon CPU/NPU 真实数据合同](page-04-stage-benchmark-data.md)、[第 7 页 SMEPilot 修订](page-07-round15n-v2-cpu-isa-hierarchy-pilot-2026-10-08.md)、[第 8 页 HeRo V6](page-08-round15k-v6-leadership-readable-copy-2026-10-08.md) — 研究脉络与适用边界。

**图的性质：** 本页为跨来源、基于公开编译和 Runtime 机制的架构综合示意。未引用某一论文的原系统图，也没有构造实验时延数据。不把 LLVM 画成与 CPU/NPU 并列的硬件引擎，且不把 SME 画为独立 SoC 加速器。

## 5. 页面结构和交付

- 16:9，背景与已认可的第 4–8 页相同纯蓝色系，沿用已有右上角芯片装饰图。
- 上部双 panel：**A 开发/编译阶段 → CPU 执行代码** 与 **B Runtime/OS 执行阶段 → CPU 或 GPU/NPU**；内部流程只画明确定义的箭头；两 panel 没有不真实的跨层硬件直连箭头。
- 下部三项工程责任：CPU/LLVM 可直接推进、Runtime/NPU 共同优化、OS/Agent 平台主要负责。
- 页脚明确边界：“优先用好现有 CPU 编译与执行能力；不由本页推断 Agent 专用 ISA 的独立收益。”
- 页码统一 `09 / 15`，标题和文本均为原生 PowerPoint 对象，来源短标签带真实超链接。

本轮实际生成的会话产物：
- `/mnt/data/round15r_slide09/slide09_llvm_runtime_blue_editable.pptx`
- `/mnt/data/round15r_slide09/slide09_llvm_runtime_blue_preview.png`（从同一 PPTX 经 LibreOffice/PDF 导出）
- `/mnt/data/round15r_slide09/make_slide09.js`（用于修改和重建的可追溯源码）
- `/mnt/data/round15r_slide09/header_art.png`（独立芯片插画）

**上述二进制文件与源码当前在对话附件空间，未确认上传到 GitHub**；此 GitHub 记录不冒称包含二进制。

## 6. 已执行 QA 与未完成验收

- PPTX ZIP 完整，**1 张 16:9** 幻灯片，可编辑 XML 具有 **62 个普通 PowerPoint shapes/text 元素**和 1 张独立装饰图片。
- **09 / 15**、LLVM、MLIR、SME2、KleidiAI、Runtime、CPU Fallback、GPU/NPU 等重要词均能从 PPTX 原生文本读取。
- PPTX slide relationship 中含三个真实官方来源的超链接（LLVM、MLIR、KleidiAI）；没有“投资”禁用文字。
- 同源 PDF 1 页，960×540 pt；预览 PNG **1921×1080 px**，基本是 16:9；人工查看正文图形、卡片字号和来源，无越界。
- 首次渲染发现三个责任卡文本/编号重叠，**已实际调整源脚本并二次导出修复**；不存在未处理的该项问题。
- 尚待用户视觉评审、实际 Microsoft PowerPoint 打开与链接点击、正式全 17 页统一合并/逐页页码与投影可读性最终检查。**不能因此宣称第 9 页已经最终定版。**

建议用户优先审阅“两个时段划分是否容易懂，三项工程责任是否表达自然”；第 10 页随后应转到**可信工具动作与跨引擎派生状态的两类不同有效性**，避免误认为 CPU 提供全部 Agent 安全功能。
