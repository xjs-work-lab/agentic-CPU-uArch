# Agentic CPU µArch Research Refresh — 2026-11-09

本目录是 2026-11-09 对既有公开证据研究的定向更新。**不修改旧决策快照，不修改任何 PPT/PPTX。**

## 入口与阶段状态

- [Phase 1 仓库质量与当前性审计](repository-quality-audit-2026-11-09.md)
- [PAPER-122 EdgePace 深读卡](PAPER-122-EdgePace-2026-10-27.md)
- [PAPER-123 Tandem 深读卡](PAPER-123-Tandem-2026-10-19.md)
- [独立研究与反证综合报告（Consensus，原文保留引用）](Research%20task-%20independent%20validation%20and%20counter-evidence%20for%20two%20recent%20mobile.md)
- [PAPER-124 Is Your NPU Ready for LLMs](PAPER-124-Is-Your-NPU-Ready-2026-07-06.md)
- [PAPER-125 Compiler Fusion Power Bursts](PAPER-125-Compiler-Fusion-Power-Bursts-2026-07-17.md)
- [PAPER-126 sd.npu](PAPER-126-sd-npu-2025-12-17.md)
- [PAPER-127 MemGUI-Bench](PAPER-127-MemGUI-Bench-2026-02.md)
- [PAPER-128 Ripple — DGX Spark UMA CPU-GPU deadline scheduler](PAPER-128-Ripple-2026-10-31.md)
- [EdgePace/Tandem 全文二次核验（设备、基线、PMU开销、DMA cache coherence）](PAPER-122-123-crosscheck-2026-11-09.md)
- [EdgePace/Tandem/Android/QNN/既有工作比较、研究谱系与反证矩阵](comparison-lineage-counterevidence-2026-11-09.md)
- [VENDOR-027 Android NPU Manager / Qualcomm QAIRT 更新](VENDOR-027-android-npu-manager-qairt-update-2026-11-09.md)

## 本批初步判断（尚非正式决策）

- **C — STRENGTHEN:** 手机端 Agent/LLM 的 QoE、deadline/freshness、NPU 生命周期、state reuse 和异构调度已有更丰富软件证据。
- **CG-06 — STRENGTHEN:** CPU decode、host-side dispatch/polling/DVFS、PMU反馈与 phase-aware backend 选择更具体；应聚焦软件、编译器、kernel与Runtime协同，不是新ISA。
- **B-residual — NARROW:** 已有软件方案覆盖一部分状态复用、回滚、图切换与NPU生命周期；物理跨引擎状态有效性残差仍未测量。
- **A — KEEP CONDITIONAL/NARROW:** GUI memory问题真实，但ProgRouter/MemGUI说明软件工作流状态与记忆已有较强能力；仍无证据证明需要CPU私有RequiredProgress。
- **PT-A、R2 — NO DIRECT CHANGE:** 本批没有直接新证据。

## 重要审计发现

- EdgePace的91.3%是OnePlus 13相机前台任务deadline miss相对unmanaged inference的下降；它没有和SERENO做直接头对头比较。PMU读取成本主要在Jetson Orin Nano Super测量，不能当作OnePlus 13的开销。
- Tandem是独立作者团队、公开llama.cpp fork，并以llama.cpp最快NPU配置为主要基线；其主要结果是Qwen3.5 hybrid GUI Agent与OnePlus 13T/15特定环境。其DMA cache-coherence问题通过OS cache clean/invalidate处理，是B-residual的重要软件边界案例。
- AOSP Android 17 NPU Manager和Qualcomm QAIRT已公开部分priority、admission、work lifecycle、power-vote控制，但没有Agent语义进度/utility/freshness接口，也不代表所有OEM都实现相同能力。
- PAPER-124、PAPER-125、PAPER-126、PAPER-127均为本轮发现的高价值遗漏/补充证据；其中PAPER-124的POMACS出版状态需再从ACM publisher record核实。
- 本批共读了种子论文及4篇额外原始全文；Consensus 独立筛查报告是20篇摘要级筛查，不将摘要筛查等同于全文深读。

## 下一批

转向CPU微架构、AArch64/SME2/LLVM、手机SoC CPU/cache/interconnect/内存和厂商披露，重点重新评估CG-06与R2。完成前不更新正式投资组合，不重做PPT。
