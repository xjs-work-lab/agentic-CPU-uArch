> Evidence Rescue Round 1 re-read under EDP v1 on 2026-10-07.
> V1 provenance remains the frozen baseline; this page is the current mechanism-level interpretation.

# PAPER-009 — When NPUs Are Not Always Faster

## Q1 — Problem + target mapping
The paper asks why mobile NPU offload does not always translate into end-to-end LLM benefit.

It directly targets a Snapdragon 8 Gen 3 smartphone with Hexagon v75 and decomposes Prefill and Decode rather than treating “LLM inference” as one homogeneous workload.

Project mapping:
- C: generic CPU↔NPU host/control-path cost;
- CG-06: current-stack placement crossover evidence.

## Q2 — Novelty / new-regime relevance
The contribution is a stage-aware benchmarking/decomposition methodology, not a new Agent mechanism.

Classification: **generic enabling / Agent-amplified**.

The paper's novelty for this project is empirical:
> current mobile CPU↔NPU placement economics are stage/operator/backend dependent.

## Q3 — Falsifiable hypothesis
If NPU compute throughput alone determines placement, more NPU offload should monotonically improve latency/energy.

Observed falsification:
- Prefill becomes slower on the evaluated NPU path;
- Decode core matrix-vector work benefits from NPU, but end-to-end acceleration is much smaller;
- full/greater offload can increase battery drain.

## Q4 — Competing route / lineage
Competing interpretations:
1. NPU-first static offload;
2. stage-aware CPU/NPU placement;
3. improved NPU software/operator coverage that removes today's crossover;
4. later systems such as llm.npu / ShadowNPU that reconstruct or repartition work to make NPU execution more competitive.

Therefore PAPER-009 is **not** a final strongest baseline by itself.

## Q5 — Mechanism / control point
Mechanism chain:

`LLM stage/operator shape → backend support + arithmetic intensity → dispatch/communication + quantization + compute + fallback → effective latency/energy`

OPMASK isolates:
- communication;
- dynamic quantization;
- NPU computation.

Important mechanisms:
- Decode lightweight operators pay repeated CPU↔NPU invocation tax;
- unsupported attention falls back to CPU and introduces synchronization/reordering/copy cost;
- Prefill performance is affected by backend kernel maturity and 8 MiB VTCM tiling constraints;
- Decode streaming GEMV can favor NPU scratchpad/DMA behavior.

## Q6 — Experiment design + results
Platform:
- Snapdragon 8 Gen 3;
- Hexagon v75;
- 16 GB RAM;
- Android 15;
- llama.cpp tag b7588.

Models:
- Llama-3.2-3B;
- Llama-3.1-8B;
- Qwen3-4B;
- Qwen3-8B;
- Q4_0 quantization.

Reported anchors:
- Prefill NPU path: 1.27–1.62× slower than 6-core CPU;
- Decode core MUL_MAT: NPU 1.55–1.67× lower latency;
- Decode end-to-end benefit: only about 1.05–1.20×;
- Decode communication: ~9.9–13.0% of NPU path;
- lightweight-op call-usec: 8–22× op-usec;
- fallback: roughly 1–1.5× penalty relative to native CPU execution for the cited path;
- Llama-3.2-3B battery-drain experiment: greater/full NPU offload reported +22%, +32%, +51% across increasing prompt lengths.

## Q7 — Data / artifact / reproducibility
Strengths:
- real smartphone;
- four models;
- operator and pipeline decomposition;
- multiple offload configurations;
- energy dimension.

Limits:
- one Snapdragon/NPU generation;
- one major runtime/backend lineage;
- current Hexagon operator coverage/kernel quality is part of the causal result;
- artifact status beyond public paper/thesis material remains not fully verified.

## Q8 — Evidence vs alternative explanations
### Demonstrated
Current CPU/NPU crossover and boundary overhead are material on the tested stack.

### Not demonstrated
- Prefill is intrinsically a CPU workload;
- future/optimized NPUs will preserve the same crossover;
- CPU wins specifically because of Agent semantics.

A major alternative explanation is **software/backend immaturity**, explicitly identified by the paper itself.

## Q9 — Project decision contribution
KEEP the following:
> CPU↔NPU winner is not universally NPU-first; current stage/operator/implementation overhead can reverse the winner.

REMOVE / avoid:
> “short/control Agent stages are therefore naturally CPU-resident.”

The paper's strongest direct CPU result is compute-intensive Prefill, not an Agent control-path workload.

CG-06 must therefore use PAPER-009 only as crossover/dispatch/fallback evidence and still beat llm.npu/ShadowNPU/Agent.xpu/HeRo-class optimized heterogeneous baselines.

## Q10 — Next action
- KEEP as P0 decision-critical source.
- Narrow CLM-CPU-001 boundary.
- Retain CLM-C-001.
- Do not promote architecture from PAPER-009.
- In EXP-CG06-001, explicitly test whether crossover survives improved NPU operator coverage/fusion/persistent dispatch.

## Decision footer
- Evidence maturity: **SYSTEM_VALUE for the evaluated current mobile stack**
- Decision impact: **NARROW wording; no lane/score change**
- Open questions: next-gen NPU transfer, optimized backend transfer, sustained thermal behavior
- Primary source: https://arxiv.org/abs/2605.27435
