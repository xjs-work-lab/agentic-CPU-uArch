# PAPER-122 — EdgePace: Deadline- and Freshness-Aware LLM Scheduling on Unified-Memory Platforms

- **Primary source:** https://arxiv.org/abs/2610.37307
- **Full text:** https://arxiv.org/html/2610.37307
- **Published:** 2026-10-27 (arXiv preprint)
- **Authors:** Teng Mei, Chengxuan Pei, Weijun Wang, Jie Wu, Marco Canini, Yunming Xiao
- **Affiliations:** CUHK-Shenzhen, Tsinghua AIR, Fudan, KAUST
- **Review date:** 2026-11-09
- **Status:** PREPRINT_FULL_TEXT_REVIEWED / PHONE_PLUS_JETSON
- **Decision relevance:** C (direct); CG-06 (direct systems/CPU-counter relevance); B-residual (shared-memory pressure boundary); A (limited).

## Q1 — Problem and target mapping

Concurrent sensor/foreground tasks and background LLM inference share physical DRAM on edge platforms. Compute utilization alone does not expose memory interference. Foreground processing has deadlines; LLM outputs must arrive before their source observations become stale. This is directly relevant to mobile Agent loops that observe, reason and act.

## Q2 — New-regime relevance

The mechanism is generic real-time edge scheduling, amplified by Agentic workflows where LLM feedback is part of a repeated observation/action loop. It is not an Agent-only CPU feature.

## Q3 — Falsifiable hypothesis

A runtime that combines foreground memory-demand/stall signals, deadline slack, and LLM-output freshness can reduce foreground deadline misses while retaining useful LLM throughput. It fails if monitoring/suspension overhead is high, signals mispredict interference, or pausing causes excessive lost work/late outputs.

## Q4 — Mechanism and strongest alternatives

Three main elements:
1. Safe sublayer suspension points in both Prefill and Decode to yield and resume without recomputing completed work.
2. Lightweight sampling of hardware counters on foreground CPU threads, combining memory-demand and stall signals rather than relying only on aggregate bandwidth.
3. Scheduler uses contention risk, foreground deadline slack, and remaining freshness window to decide continue/yield.

Relevant prior alternatives discussed by paper include FCFS/SJF, Sarathi-Serve chunked prefill, SERENO's speculative-decoding yield points, and bandwidth-threshold policies. Repository baselines to compare: PAPER-003 SERENO, PAPER-098 HeRo, VENDOR-027 Android NPU Manager and current accelerator runtime controls. This paper does not establish superiority against every optimized OEM scheduler.

## Q5 — Experimental setup

Evaluated on four platforms: three NVIDIA Jetson platforms and OnePlus 13 with Snapdragon 8 Elite. Workloads include multi-camera processing and robotic target tracking. The paper reports both synthetic memory traffic and Qwen2.5-1.5B background inference in a four-camera scenario. OnePlus is direct smartphone evidence; Jetson results are supporting edge evidence, not phone evidence.

## Q6 — Results

Against unmanaged inference, foreground deadline miss rates reduced by 24.1%–96.1%, while 64.9%–98.5% of LLM throughput is retained. Example OnePlus 13 camera workload: deadline misses decrease by 91.3% while 90.4% LLM throughput remains. All measured LLM outputs arrive within task-defined freshness windows. These are workload-specific results; do not report as general percentage improvement in phone Agent performance or battery life.

## Q7 — Measurement and reproducibility limits

The paper directly identifies unified-DRAM contention, not merely compute saturation. The available full text includes architecture, mechanisms and evaluation discussion. Before treating exact per-platform tables as decision-grade, re-check all tables/figures and artifact availability in the next review pass. No independent replication identified in this initial scan. arXiv preprint status must remain explicit.

## Q8 — Fact / inference / not established

- **[FACT]** Paper reports OnePlus 13 and Jetson evaluations, counter-informed runtime, safe prefill/decode suspension and deadline/freshness scheduling.
- **[FACT]** The OnePlus 13 example reports 91.3% fewer camera deadline misses with 90.4% LLM throughput retained vs unmanaged inference.
- **[INFERENCE]** C becomes more compelling as an OS/Runtime system-control track; CPU counters may serve as useful cross-engine QoE feedback for CG-06.
- **[INFERENCE]** The shared DRAM contention part of B-residual should be narrowed: software can observe and mitigate some contention without new physical state.
- **[NOT ESTABLISHED]** A new CPU structure, ISA, hardware scheduler or universal NPU preemption primitive is needed.
- **[NOT ESTABLISHED]** Results generalize to all smartphone SoCs, production apps, whole-day battery, or all Agent tasks.

## Q9 — Decision impact

**Preliminary: STRENGTHEN C; STRENGTHEN the software/control part of CG-06; NARROW B-residual.** No formal decision event yet. Compare with SERENO/HeRo and official Android NPU Manager before any portfolio update.

## Q10 — Next action

Read every relevant table/figure/appendix and inspect artifact/code status. Compare scheduling policy, counter availability, suspension granularity, CPU cost, energy accounting and device applicability against SERENO and Android NPU Manager. Search for independent replication and vendor implementation evidence.

## Evidence footer

- Source class: original arXiv preprint, full text read.
- Directness: OnePlus 13 smartphone + Jetson; multi-camera/robotic workflows.
- Independence: not yet established as independently replicated.
- Confidence: medium-high for mechanism existence and reported OnePlus experiment; medium for transfer to general mobile Agent workloads.
