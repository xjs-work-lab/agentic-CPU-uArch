# PAPER-091 — Fine-Tuning a 3B-Parameter LLM on a Smartphone: Characterizing Sustained Training

## Source
- arXiv:2610.06325
- submitted 2026-10-05
- iPhone 17 Pro
- code/data publicly linked by the paper
- Priority: P0 direct smartphone measurement

## Q1 — Problem + target mapping
Prior mobile-training studies often measure only individual steps.
This paper asks whether complete multi-billion-parameter fine-tuning runs are practical on a phone and what memory, thermal, energy and runtime bottlenecks dominate.

For the project this is the first direct evidence that a sustained local-learning phase can materially affect phone thermals, battery and runtime behavior.

## Q2 — Novelty / new-regime relevance
The novelty is measurement depth:
- complete 3B-model adapter runs;
- energy;
- sustained thermal behavior;
- time decomposition;
- personalization quality;
- runtime/kernel audit.

Classification:
**GENERIC ENABLING / direct smartphone SYSTEM_VALUE**.
Not Agent-specific by itself.

## Q3 — Falsifiable hypothesis
If multi-billion-parameter on-device fine-tuning is feasible but currently inference-runtime-limited, complete runs should finish within realistic battery/memory limits while exposing sustained throttling and backward-path inefficiency.

The reported measurements support this.

## Q4 — Research lineage / competing route
Competing routes:
- server-side fine-tuning;
- retrieval-only personalization;
- smaller models;
- forward-only/zeroth-order training;
- single-step mobile training studies;
- burst/pause scheduling;
- specialized backward kernels.

## Q5 — Key mechanism / control point
The dominant path is not the small LoRA adapter itself.
The frozen base model is traversed during every training step, and most step time is in the backward pass over quantized weights.

The paper reports that nine of ten audited alternative runtimes lacked an accelerated path for this direction at the time of audit.

## Q6 — Experiment design
- iPhone 17 Pro;
- 3B-parameter model, 4-bit base weights;
- complete per-user adapter training runs;
- memory, per-step timing, thermal behavior, energy and personalization measured.

Reported observations:
- sustained throughput falls to roughly half initial rate under thermal throttling;
- tested pausing/burst schedules did not restore initial throughput;
- training cost scales approximately linearly with tokens;
- about 0.01 s and 0.04 J per training token in the reported setup;
- 405-record history costs about half a battery charge;
- 987-record history can exhaust a charge before completion;
- repaired backward kernel: 1.47× faster and about one-third less energy.

## Q7 — Data / artifact / reproducibility
Strengths:
- direct commercial smartphone;
- whole-run energy + thermal measurement;
- complete training rather than isolated kernels;
- personalization outcome checked against server-trained adapters;
- code/data released.

Limitations:
- preprint;
- one phone family / Apple stack;
- not mixed with active Agent foreground serving;
- one model/training regime cannot establish broad product economics.

## Q8 — Evidence vs hypothesis
### [FACT]
Sustained mobile LLM fine-tuning is feasible on current phone hardware.

### [FACT]
Thermal throttling and backward-path efficiency are first-order in the tested setup.

### [FACT]
The repaired runtime kernel materially improves both speed and energy.

### [OBSERVATION]
Mobile OS/runtime stacks are still inference-centric.

### [INFERENCE — project]
This establishes real smartphone SYSTEM_VALUE for training as a workload, but not a differentiated Agent control point.

## Q9 — Real contribution to project decision
Positive for H-CAL:
- removes the objection that sustained phone training is purely hypothetical;
- gives real battery/thermal stakes.

Negative:
- bottleneck is strongly generic and software/kernel-capturable;
- no evidence that Agent semantics are needed for the kernel/layout problem.

## Q10 — Next action
1. KEEP P0 direct phone evidence.
2. Use its energy/thermal facts as the physical baseline for any Agent-contiguous-learning experiment.
3. Require mixed foreground inference + background adaptation traces before creating a new lane.
4. Separate generic backward-kernel work from Agent-specific control.

## Decision footer
- **Evidence maturity:** SYSTEM_VALUE for generic sustained phone training
- **Decision impact:** strengthens workload reality, not differentiation
- **Open questions:** concurrent Agent serving, update cadence, Android/Adreno/Mali transfer, user-QoE impact
- **Primary source:** https://arxiv.org/abs/2610.06325
