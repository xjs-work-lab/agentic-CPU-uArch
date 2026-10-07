# PAPER-113 — Agent.xpu — FULL_10Q

## Q1 — Problem + target mapping
The paper asks how a resource-constrained shared-memory heterogeneous SoC should execute personal-Agent LLM flows when foreground reactive work and background proactive work coexist.

The key mismatch is not simply low NPU utilization. Existing on-device engines largely assume isolated, single-shot inference, whereas the Agent workload contains concurrent stateful flows, mixed priorities and unpredictable phase interleaving.

Target mapping:
- AO-1 Agent Execution Fabric;
- T2 heterogeneous Agent AI execution;
- T5 state lifecycle/locality.

## Q2 — New-regime relevance
Classification: Agent-native / strongly Agent-amplified.

The paper explicitly separates:
- reactive flows: bursty, user-facing, latency-sensitive;
- proactive flows: long-running, background, throughput-oriented.

It argues that ordinary static inference assumptions break because these flows coexist and repeatedly enter prefill/decode phases with different priorities.

## Q3 — Falsifiable hypothesis
If ordinary single-accelerator or static heterogeneous inference were sufficient, flow-aware priority, preemption, stage elasticity and accelerator coordination would add little end-to-end value.

The evaluated mixed workloads show the opposite under the tested SoC.

## Q4 — Competing routes / strongest baseline
Baselines include:
- OpenVINO iGPU serving with continuous batching;
- llama.cpp CPU serving;
- serial NPU-iGPU inference with tuned tensor partition.

Important stronger competing route:
future NPU software may remove some current dynamic-shape/operator limitations.

Therefore the paper does not establish a permanent CPU/iGPU/NPU ownership split.

## Q5 — Mechanism / control point
Agent.xpu uses:

1. Heterogeneous Execution Graph
- operator groups;
- NPU/iGPU affinity;
- precompiled static NPU chunks;
- dynamic iGPU kernels;
- profiling-guided latency and bandwidth annotations;
- elastic late binding.

2. Flow-aware stage elasticity
- prefill and decode decoupling;
- contention-aware NPU/iGPU dispatch;
- adaptive batching;
- reactive-first arbitration.

3. Fine-grained preemption
- kernel/layer-boundary preemption;
- shared-memory copy-free context switching;
- KV/progress/activation tracking.

4. Slack-aware piggybacking
- proactive work fills compute or bandwidth slack without violating reactive objectives.

## Q6 — Experiment design + results
Platform:
- ASUS NUC 14 Pro+;
- Intel Core Ultra 5 125H;
- Intel Arc iGPU;
- Intel AI Boost NPU;
- 64 GB DDR5;
- Ubuntu 24.04;
- OpenVINO 2025.2 lineage.

Models:
- Llama-3.2-3B-Instruct;
- Llama-3.1-8B-Instruct;
- W8A16.

Workloads include:
- ProactiveBench;
- SAMSum;
- CNN/DailyMail;
- LMSys-chat-1M;
- MTRAG;
- Berkeley Function Call Leaderboard.

Reported anchors:
- proactive-only throughput: 2.0–2.4x over OpenVINO iGPU for some 3B workloads;
- up to 3.9x over CPU and 4.9x over serial NPU-iGPU baselines;
- mixed-load reactive mean-latency reduction: about 91–97% vs OpenVINO iGPU across reported rates;
- proactive latency improvements remain positive but shrink at heavier mixed load;
- overall iGPU utilization reduced by 32.5% vs serial NPU-iGPU and 37.1% vs OpenVINO iGPU;
- energy/token 26.8% lower than OpenVINO iGPU.

## Q7 — Artifact / reproducibility / limitations
Strengths:
- full implementation;
- operator/task-level profiling;
- realistic reactive/proactive workload composition;
- explicit energy and graphics-resource consideration;
- runtime breakdown.

Limits:
- AI PC, not smartphone;
- Intel NPU/iGPU stack, not mobile Qualcomm/MediaTek/Arm SoC;
- central focus is local LLM flow, not full tool-execution Agent pipeline;
- assumes moderate request density without memory overflow;
- NPU dynamic-shape and compilation limits are platform/software-generation dependent;
- vendor/backend maturity can move the crossover.

## Q8 — Evidence vs hypothesis
FACT:
mixed-criticality Agent flows create distinct scheduling objectives on the tested heterogeneous SoC.

FACT:
software/runtime co-design can recover very large value without changing silicon.

FACT:
shared-memory contention and accelerator-affinity matter.

NOT ESTABLISHED:
- smartphone magnitude;
- permanent NPU limitations;
- need for new ISA/uArch;
- benefit of Agent semantic metadata beyond reactive/proactive priority.

## Q9 — Decision contribution
Strongly supports AO-1 as an Architecture Opportunity.

It changes the framing from CPU-vs-NPU benchmarking to:
flow-aware heterogeneous execution, preemption, state retention and shared-memory coordination.

At the same time, it raises the strongest software baseline substantially.

## Q10 — Next action
Use as a P0 AO-1 anchor.

Search for:
- mobile/phone corroboration;
- cross-xPU command/handoff cost;
- shared-memory bandwidth/coherence behavior;
- persistent state handoff;
- product architecture signals;
- strong generic preemption and heterogeneous-scheduling prior art.

## Decision footer
- Evidence maturity: SYSTEM_VALUE on evaluated consumer hetero-SoC; STRUCTURAL_SIGNAL for smartphone transfer
- Decision impact: KEEP / strengthen AO-1, narrow away from CPU-vs-NPU framing
- Open questions: phone transfer, software-sufficiency boundary, state/control hardware assist
- Primary source: https://arxiv.org/abs/2506.24045
