> Evidence Rescue Round 1 re-read under EDP v1 on 2026-10-07.
> V1 provenance remains the frozen baseline; this page is the current mechanism-level interpretation.

# PAPER-052 — SMEPilot

## Q1 — Problem + target mapping
SME-enabled CPUs contain both ordinary vector cores and matrix-extension resources, but LLM operators vary sharply in arithmetic intensity, shape and layout requirements.

Project mapping:
- CG-06 CPU-local AI feasibility;
- LLVM/runtime/operator placement;
- CPU-side strongest baseline before proposing new ISA/uArch.

## Q2 — Novelty / new-regime relevance
SMEPilot is not Agent-specific.

It introduces a CPU-internal heterogeneous execution engine choosing:
- CPU-only;
- SME-only;
- cooperative SME+CPU

per operator shape.

Classification: **generic enabling / competitive baseline**.

## Q3 — Falsifiable hypothesis
A roofline/shape-aware runtime coordinating SME and CPU vector cores should outperform conventional CPU inference that treats matrix extensions as a simple replacement kernel.

The ablation supports this on evaluated SME platforms.

## Q4 — Competing route
Relevant competing routes:
- llama.cpp CPU baseline;
- GPU inference;
- NPU-first / CPU-NPU heterogeneous systems;
- static SME-only kernels.

Critical project boundary:
SMEPilot does not directly evaluate phone CPU vs NPU.

## Q5 — Mechanism / control point
Mechanism chain:

`operator shape + arithmetic intensity → roofline placement → CPU / SME / cooperative execution`

Three implementation gaps:
1. **spatial utilization** → tile-level CPU+SME partition;
2. **temporal bubbles** → pipeline SME matrix work with CPU vector/softmax phases;
3. **layout compatibility** → layout becomes runtime state; static weights pack off-path and reusable activations/KV state use producer-side packed layout.

## Q6 — Experiment design + results
Platforms:
- Apple M4 Pro CPU;
- MediaTek Dimensity 9500 smartphone SoC;
- KunPeng 920 server CPU.

Models:
- Llama-3.2-3B;
- Qwen3-4B;
- Qwen3-30B-A3B, with 4-bit weights for the large MoE configuration.

Workloads include long-context processing, QA and long generation.

Baseline:
- llama.cpp default CPU backend.

Reported across evaluated configurations:
- up to **3.94×** end-to-end speedup;
- removing tile partition increases GEMM latency **1.46×**;
- removing attention pipeline increases prefill-attention latency **2.07×**;
- naive on-path packing increases cited decode GEMV latency **0.52 ms → 1.71 ms**.

Power:
- measured on Apple M4 Pro / Qwen3-4B / Ruler-4K;
- energy **482.813 J → 233.931 J**, about **0.485×** baseline.

GPU comparison:
- Apple M4 Pro only;
- SMEPilot reaches roughly **0.72–0.96×** GPU performance in the reported comparison.

## Q7 — Data / artifact / reproducibility
Strengths:
- phone + PC + server platforms;
- dense + MoE models;
- explicit ablations;
- real SME/SME2 implementations using KleidiAI/ACLE.

Limits:
- energy measured only on M4 Pro;
- no direct smartphone NPU baseline;
- no Agent workload;
- sustained phone thermal behavior not established;
- headline “up to” speedup must not be assigned to every device/workload.

## Q8 — Evidence vs alternative explanations
### Demonstrated
CPU matrix extensions plus runtime/layout co-design can materially improve CPU LLM inference.

### Not demonstrated
- CPU wins over smartphone NPU;
- Agent fast path is CPU-resident;
- new ISA beyond existing SME is needed.

Indeed, the paper is evidence that **software/runtime exploitation of existing ISA is a strong baseline**.

## Q9 — Project decision contribution
KEEP CLM-CPU-002:
> existing CPU matrix acceleration can materially expand the CPU-local AI region.

NARROW interpretation:
CG-06 is not justified by SMEPilot alone.
Its competitive-gap case depends on combined evidence and the future crossover experiment.

The key positive opportunity is partly compiler/runtime:
- operator placement;
- tile partition;
- phase pipelining;
- persistent layout state.

## Q10 — Next action
- KEEP as P0.
- Treat SMEPilot-class optimization as a mandatory CPU baseline.
- Require optimized NPU/HETERO comparison on the same target phone.
- Do not propose new matrix ISA until existing SME-class software capture is exhausted.

## Decision footer
- Evidence maturity: **SYSTEM_VALUE for CPU inference; STRUCTURAL_SIGNAL for Agent transfer**
- Decision impact: **narrow CPU-vs-NPU interpretation; no lane/score change**
- Open questions: target-phone CPU/NPU crossover, phone energy/thermal, Agent stage mix
- Primary source: https://arxiv.org/abs/2606.16332
