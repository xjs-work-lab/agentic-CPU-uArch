# PAPER-097 — Agent.xpu: Efficient Scheduling of Agentic LLM Workloads on Heterogeneous SoC

## Source
- arXiv:2506.24045, v2 2026
- Peking University / University of Hong Kong lineage
- Intel Core Ultra heterogeneous SoC
- Llama 3-class 3B/8B workloads
- Priority: P0

## Q1 — Problem + target mapping
Personal Agents combine two execution classes:
- foreground **reactive** requests with strict latency sensitivity;
- background **proactive** work where throughput/energy matter more.

These flows repeatedly alternate prefill/decode and external stalls, so they are not well modeled as isolated one-shot LLM inference.

Target mapping:
> does Agent flow state create a reusable system-control signal for heterogeneous accelerators?

## Q2 — Novelty / new-regime relevance
Agent.xpu argues current on-device inference engines lack:
- flow-level concurrency;
- priority-aware preemption;
- coordinated NPU/iGPU control;
- stage-aware batching for mixed reactive/proactive demand.

Classification:
**AMPLIFIED / partially Agent-native.**

Foreground/background priority is generic, but the long-lived LLM flow structure, prefill/decode stage asymmetry and proactive/reactive coexistence are directly Agent-relevant.

## Q3 — Falsifiable hypothesis
If mixed Agent flows materially differ from static one-shot inference, flow-aware stage scheduling and preemption should outperform:
- iGPU-only serving;
- CPU-only serving;
- tuned static NPU-iGPU tensor partitioning.

Falsifiers:
- static placement performs similarly;
- preemption/context switching dominates gains;
- reactive priority destroys proactive throughput;
- benefits disappear when strong generic scheduling is applied.

The reported evaluation supports the hypothesis on its Intel platform.

## Q4 — Research lineage / competing route
Competing routes:
- OpenVINO/iGPU continuous batching;
- llama.cpp CPU serving;
- static NPU-iGPU partitioning;
- HeteroInfer / mllm.npu-style single-model heterogeneous execution;
- generic QoS/priority schedulers;
- SERENO-like interference control.

The same PKU lineage later appears in PAPER-098 HeRo, so the two papers are **trajectory evidence, not independent replication**.

## Q5 — Key mechanism / control point
1. **Heterogeneous Execution Graph (HEG)** encodes operator variants, accelerator affinity and elastic binding.
2. **Stage elasticity** decouples prefill and decode across NPU/iGPU.
3. **Bandwidth-aware dispatch** avoids harmful co-execution of memory-heavy kernels.
4. **Fine-grained preemption** uses shared memory / activation-buffer structure for low-copy context switching.
5. **Slack-aware piggybacking** fills reactive slack with proactive work while preventing starvation.

## Q6 — Experiment design
Hardware:
- Intel Core Ultra shared-memory SoC with CPU, iGPU and NPU.

Workloads:
- event handling;
- function calling;
- retrieval-augmented generation;
- proactive-only and mixed reactive/proactive arrival patterns.

Models:
- Llama 3-class 3B / 8B configurations.

Baselines:
- industrial OpenVINO iGPU serving;
- llama.cpp CPU;
- tuned serial/static NPU-iGPU inference.

Reported outcomes:
- proactive-only throughput: 1.2–2.4× over iGPU baseline and 1.4–4.9× over serial NPU-iGPU in reported settings;
- mixed flows: reactive latency reduced by roughly 91–97% while proactive throughput also improves in many settings;
- energy reduced by 26.8% in the reported comparison;
- iGPU utilization reduced by 32.5% in the cited comparison.

## Q7 — Data / artifact / reproducibility
Strengths:
- concrete hetero-SoC implementation;
- released LLM.xpu code path;
- mixed workload traces;
- operator/stage profiling;
- latency, throughput and energy dimensions.

Limitations:
- Intel Core Ultra is a personal-device SoC, not a commercial smartphone;
- no Android/iOS foreground app QoE;
- workload arrival process is benchmark-driven;
- strongest generic scheduler equivalence is not fully isolated.

## Q8 — Evidence vs hypothesis
### [FACT]
Reactive/proactive LLM flows create distinct latency/throughput objectives on the evaluated hetero-SoC.

### [FACT]
Shared-memory NPU/iGPU concurrency can cause asymmetric bandwidth interference.

### [FACT]
A flow-aware software runtime materially outperforms static/single-accelerator baselines in the reported setup.

### [INFERENCE — project]
Agent-aware heterogeneous orchestration is now a **strongest baseline** for C and CG-06; it is not evidence that new hardware is necessary.

## Q9 — Real contribution to project decision
Positive:
- demonstrates large software value from Agent flow state;
- strengthens C’s mechanism relevance;
- raises CG-06’s baseline from operator placement toward flow/stage orchestration.

Negative:
- no smartphone transfer;
- much of the control state is software-visible;
- no new C-owned information source beyond flow priority/stage state is proven.

## Q10 — Next action
1. KEEP as P0 strongest Agent-aware hetero-SoC baseline.
2. Pair with PAPER-098 for target-phone transfer.
3. Require CG-06 experiments to beat Agent.xpu-class dynamic xPU control.
4. Do not promote hardware from this source.

## Decision footer
- **Evidence maturity:** SYSTEM_VALUE on commodity personal-device hetero-SoC; not target smartphone
- **Decision impact:** raises C / CG-06 strongest baseline
- **Open questions:** phone transfer, foreground app coexistence, generic scheduler equivalence
- **Primary source:** https://arxiv.org/abs/2506.24045
