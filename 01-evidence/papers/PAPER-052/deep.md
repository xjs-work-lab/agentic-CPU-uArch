> V1 semantic source copied/repacked from frozen baseline `960abb4ef50a8f5b0bd357c067f08346025d`.
> Do not reinterpret this page as V2.2 metadata authority; the compact README owns the Source object.

# PAPER-052 — SMEPilot: Characterizing and Optimizing LLM Inference with Scalable Matrix Extensions

## Source
- Paper: https://arxiv.org/abs/2606.16332
- Authors: Feiyang Chen, Haibo Chen
- Affiliation: IPADS, Shanghai Jiao Tong University
- Venue/status: arXiv preprint, 2026-06-15
- Target: LLM inference on SME-enabled CPUs
- Evaluated platforms include MediaTek Dimensity 9500 phone, Apple M4 Pro, and KunPeng 920 server
- Project relevance: CPU-resident Agent AI fast path; LLVM/runtime/operator placement; competitor-gap CG-06
- Priority: P0

## Q1 — Problem + target mapping
Modern CPUs increasingly include matrix extensions, but LLM operators differ in arithmetic intensity, vector behavior, layout needs and memory pressure. Blindly using matrix units is not optimal.

This maps directly to a possible smartphone CPU role beyond orchestration:
> low-latency / small-shape AI execution on CPU matrix extensions.

## Q2 — Novelty / new-regime relevance
SMEPilot is not an Agent-specific architecture.
It is a runtime for choosing:
- CPU-only;
- SME-only;
- cooperative SME+CPU

per operator/shape, while retaining packed layout state.

For this project it is primarily **competitive/adaptation evidence**, not global Agent novelty.

## Q3 — Falsifiable hypothesis
Phase/operator-aware placement between ordinary CPU cores and SME should outperform one-size-fits-all CPU execution for LLM inference.

## Q4 — Research lineage / competing route
Competes with:
- NPU-first inference;
- GPU offload;
- conventional vector CPU inference;
- static SME-only execution.

It raises the bar for any thesis that the CPU should only orchestrate AI engines rather than execute AI stages.

## Q5 — Mechanism / control point
- roofline-guided placement;
- tile-level work partitioning;
- SME matrix phases + CPU vector phases;
- inter-phase pipelining;
- layout-state reuse to avoid repeated packing.

This is highly compatible with compiler/runtime expertise.

## Q6 — Experiment
Across Llama-3.2-3B, Qwen3-4B and Qwen3-30BA3B on phone/PC/server platforms, the paper reports up to **3.94x** end-to-end improvement.

Important comparison:
the same logical operator may prefer CPU, SME or mixed execution depending on phase and shape.

## Q7 — Artifact / reproducibility
Public arXiv paper available.
SMEPilot's own research artifact/code is still not established in the current source set.

Independent engineering reproducibility is now stronger:
- TOOL-012 PyTorch/ExecuTorch reported SME2 speedups on a vivo X300 smartphone for SqueezeSAM;
- TOOL-013 Arm SME2 ExecuTorch Profiling Kit provides a public SME2-on/off Android/macOS profiling workflow with ETDump CSV/operator breakdown generation.

PyTorch/ExecuTorch reported:
- INT8 556 ms -> 304 ms (1.83x);
- FP16 1163 ms -> 298 ms (3.90x).

## Q8 — Evidence vs hypothesis
**[FACT]** CPU matrix extensions can materially change the feasible region for on-device AI.

**[BOUNDARY]**
SMEPilot is LLM inference, not an end-to-end Agent benchmark; the up-to number is not a universal speedup.

## Q9 — Decision contribution
Creates a new strategic-gap candidate:

> **CG-06 — CPU-Resident Latency-Critical Agent AI Fast Path**

This should not be framed as globally novel.
It is retained because:
- Arm is productizing SME2 explicitly for mobile Agentic AI;
- real phone measurements show large CPU inference acceleration;
- equivalent Huawei smartphone CPU matrix-AI capability is not publicly established in the current source set;
- CPU/compiler/runtime is within the team's controllable scope.

It also corrects the project thesis from “CPU mainly control substrate” to a **dual-role CPU**:
1. orchestration/system control;
2. selective latency-critical/local AI execution where CPU startup/data-locality/shape economics win.

## Q10 — Next action
- KEEP as P0.
- Add CG-06 to competitive-gap map.
- Do not propose new matrix ISA before checking Huawei public capability and existing Arm/Qualcomm/MediaTek prior art.
- Design a strongest-baseline phone experiment versus NPU offload including launch/transfer/sync/energy/thermal/QoE.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for SME-enabled CPU inference; STRUCTURAL_SIGNAL for Agent fast-path transfer
- Decision impact: new Adaptation/Differentiation candidate; refine CPU-role thesis
- Open questions: Huawei phone capability; exact Agent stage mix; CPU-vs-NPU crossover
- Primary source: https://arxiv.org/abs/2606.16332
