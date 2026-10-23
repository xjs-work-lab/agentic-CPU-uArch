# S15 Speaker Notes｜未来三年技术路线（研究建议）

**本页首先讲的结论**：这页不是厂商量产发布计划、也不是内部预算已批准的研发排期。根据当前公开证据，我们优先建设现有 CPU ISA 与 LLVM/AArch64、异构 Runtime/OS、Agent 可信工具、内存/状态以及主动低功耗能力；新增 Agent 专用 CPU 硬件，目前没有预算级主押注证据。

**横向按年解释：** 2027 以复用现有硬件/软件能力打基础：SME2/Neon/SVE 的 CPU 内核路径，LLVM lowering、tile、packing、布局复用；动态 DAG 调度和共享 DRAM QoE；权限、目标绑定、OutcomeReceipt 式效果验证与有界恢复；缓存 provenance/版本/有效期；跟进 CHRE/AOP/Sensing Hub 的成熟接口。2028 强化跨层合同：能力感知 CPU/NPU 放置与 ABI，模型准入/取消/回收、公平资源策略、跨 App 可信动作，以及派生状态与模型/后端版本兼容、低功耗唤醒/隐私/帮助价值。2029 现有 ISA/Runtime/Agent 软件仍应持续优化；状态保留、CPU continuation locality、额外低功耗域或语义 ISA **只有在出现新公开、可独立复核的手机物理残余证据且强软件基线无法吸收时才重新研判**。

**纵向责任：** CPU/LLVM 主要管编译、微内核和轻量控制；Runtime/OS 主要管动态 DAG、异构资源、前台 QoE、取消/恢复；Agent 平台与应用/OS 主要管权限和工具效果；内存主题跨软件/系统管理层；低功耗优先复用已经公开的硬件/OS 能力，谨慎对待误唤醒和用户价值。不能把这五层画成五颗新芯片或五个已批准项目。

**证据如何支撑：** 2026-10-20 研究终稿第十三章给出技术层×三年建议；正式 current.md 和 DEC-PORTFOLIO-002、DEC-A-008 决定现行三项优先工程/平台、三项条件研究储备以及没有获充分证据支持的独立硬件 Primary Bet。SMEPilot/ExecuTorch 支撑已有 CPU/SME 工程优化空间；llm.npu/ShadowNPU、HeRo、SERENO 支撑异构系统软件/DAG/QoE 问题；LAS/ProgRouter 支持软件可观察进度及强软件基线；官方 NPU 管理/Session/shared buffer 文档证明平台能力，**不等于真实手机通用收益与低成本状态一致性**。

**不能推出：** “2029 必定出现新 Agent ISA/缓存硬件/专用低功耗域”；“某厂商已承诺量产”；“用户的内部团队或预算已批准”；“不同论文倍数可直接相乘或构成统一硬件提升率”。整个报告基于公开来源研究，没有真机实验。
