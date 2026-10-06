> V1 semantic source copied from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.
> The compact README owns the V2.2 Source metadata.

# PAPER-051 — EdgeAgent: Orchestrating On-Device LLM inference for End-User Multi-Agent Systems on CPU-GPU Unified Memory Architectures

## Source
- Paper: https://arxiv.org/abs/2610.03394
- Authors: Yuhai Long, Yuanxin Wei, Kai Wu, Jinhui Wei, Dan Huang, Jiangsu Du
- Venue/status: arXiv 2026-10-02; ASPLOS 2027 proceedings metadata reported on paper page
- Target: end-user edge multi-Agent LLM inference on CPU-GPU UMA
- Hardware: Apple M4 SoC
- Project relevance: C / M1 / R3 pressure; CPU matrix-extension and heterogeneous runtime route
- Priority: P0

## Q1 — Problem + target mapping
Concurrent multi-Agent inference on a single end-user device is fragmented by:
- different drafting difficulty;
- tool-induced stalls;
- CPU/GPU shared-memory bandwidth contention;
- graph-runtime constraints on zero-copy heterogeneous execution.

This is directly relevant to the project's Agent system-control substrate, though the evaluated M4 platform is not a smartphone.

## Q2 — Novelty / new-regime relevance
The paper co-designs:
- UMA-aware CPU-GPU tensor execution;
- SME-optimized CPU kernels;
- Agent-aware speculative budget allocation;
- stall-aware suspend/yield and slot redistribution.

The workload irregularity is Agent-amplified/native, while zero-copy UMA execution is a generic systems mechanism.

## Q3 — Falsifiable hypothesis
Cross-layer Agent-state-aware scheduling plus architecture-aware CPU/GPU execution should outperform static/batched edge inference when multi-Agent requests are heterogeneous and frequently blocked by tools.

## Q4 — Research lineage / competing route
Strong competing/supporting route for:
- C Efficient System-Control Substrate;
- generic heterogeneous execution;
- R3 semantic-to-hardware-interface speculation.

It does **not** require a new Agent-specific CPU microarchitecture.

## Q5 — Key mechanism / control point
Execution layer:
- asymmetric CPU/GPU memory layouts;
- zero-copy shared output buffers;
- custom graph barriers;
- SME micro-kernels.

Scheduling layer:
- Historical Accepted Length as drafting-difficulty proxy;
- dynamic draft budget;
- tool-stall detection;
- cooperative suspend/yield;
- redistribute vacated slots.

## Q6 — Experiment
Reported on Apple M4:
- UMA-aware execution alone: 1.29x over batched speculative decoding;
- full system: up to 1.77x under extreme tool-use stall settings.

The paper also reports CPU/GPU UMA bandwidth contention can erase co-run benefit on large memory-bound matrices.

## Q7 — Artifact / reproducibility
Public arXiv paper available.
Code artifact was not verified in this round.

## Q8 — Evidence vs hypothesis
**[FACT]** Cross-layer edge multi-Agent orchestration can create material end-to-end value on an end-user UMA platform.

**[BOUNDARY]**
- Apple M4 is not a Huawei smartphone;
- part of the gain comes from generic UMA/SME/compiler/runtime engineering;
- it does not prove a new CPU-uArch feature is necessary.

## Q9 — Decision contribution
Strengthens Candidate C from a mostly instrumentation/substrate hypothesis toward a **second-Bet watch**, but does not promote it.

It also changes the CPU-role thesis:
> future Agent CPUs may combine orchestration/control with selective local AI compute, rather than acting only as a control plane.

R3 remains blocked because the demonstrated value is achievable with runtime scheduling + existing SME/UMA mechanisms.

## Q10 — Next action
- KEEP as P0.
- Include in Portfolio Re-score 3.0 for C.
- Add strong cross-layer runtime baseline before any semantic-hardware proposal.
- Benchmark phone-transfer conditions: UMA/shared memory, tool stalls, concurrent Agent count, CPU matrix capability.

## Decision footer
- Evidence maturity: SYSTEM_VALUE on edge Apple M4; smartphone transfer not yet established
- Decision impact: strengthen C; no R3/uArch promotion
- Open questions: phone transfer, energy/thermal, NPU comparison, generic-vs-Agent contribution
- Primary source: https://arxiv.org/abs/2610.03394
