# PAPER-088 — Perceive Before Reasoning: A Pre-Reasoning Perception Framework for Efficient and Reliable Proactive Mobile Agents

## Source
- arXiv:2606.03236, 2026 preprint
- evaluation: ProactiveMobile
- training hardware: NVIDIA H20 96GB; total training reported ~2,817 GPU-hours
- Priority: P0 strongest software baseline

## Q1 — Problem + target mapping
A proactive Agent has asymmetric objectives:
- `when` — conservatively decide whether intervention is warranted;
- `how` — perform broad multimodal reasoning to generate useful assistance.

Running one heavy VLM for both on every observation wastes compute and can increase false interventions.

Target mapping:
> before considering a dedicated always-on AI domain, how much proactive-Agent cost can be removed by a lightweight software/model gate?

## Q2 — Novelty / new-regime relevance
PRPF separates the pipeline:

### MPP — Multimodal Proactive Perceptor
- lightweight multimodal front end;
- short-/long-term context pathways;
- intervention/no-intervention gate;
- predicts top intent scenarios;
- compresses the function pool.

### PAR — Proactive Agent Reasoner
- invoked only for gate-accepted observations;
- performs heavier multimodal reasoning and executable recommendation generation.

Classification:
**Agent-specific workload optimization / strong software baseline**.

## Q3 — Falsifiable hypothesis
If the conservative `when` decision can be separated from the generative `how` decision, a lightweight front-end should suppress unnecessary heavy-model calls while improving false-trigger behavior and preserving/improving success.

Falsifiers:
- gate false negatives destroy useful assistance;
- gate itself costs nearly as much as the reasoner;
- function-pool compression removes needed tools;
- no-action observations are too rare;
- real-phone sensing/encoding dominates instead of reasoning.

Benchmark results support the hypothesis in the evaluated setting.

## Q4 — Research lineage / competing route
Strong baselines:
- unified VLM proactive reasoning;
- model routing;
- early exit;
- region/context selection;
- lightweight always-on classifiers;
- shared NPU/CPU power gating;
- CG-07's existing shared-domain baseline.

Strategic point:
PRPF shows the always-on workload can be **algorithmically sparsified before expensive reasoning**.

## Q5 — Key mechanism / control point
### Intervention gate
No-intervention observations bypass PAR.

### Candidate-function compression
MPP reduces the 63-function pool to <=~20 candidates on average in the reported benchmark, shortening the heavy reasoner's prompt/search space.

### Decomposition
The gate optimizes for conservative intervention; PAR optimizes for rich reasoning.

### Project interpretation
The strongest CG-07 baseline must now include:
> lightweight context/perception gating + candidate compression + shared compute domain.

A hardware domain only earns value on the **residual after this sparsification**.

## Q6 — Experiment design
Metrics:
- Success Rate;
- False Trigger Rate;
- TFLOPs per sample;
- peak GPU memory;
- end-to-end latency.

Reported vs ProactiveMobile 7B baseline:
- SR: **20.82% → 41.15%**;
- FTR: **13.76% → 7.21%**;
- expected compute: **−69.3%**;
- E2E latency: **−60.1%**;
- peak memory: **+12.0%** for full PRPF 9B setup.

Ablation:
- gating alone contributes roughly **−24.6% compute / −29.8% latency**;
- candidate-function filtering alone contributes roughly **−57.1% compute / −50.5% latency**;
- combined PRPF gives the largest savings.

## Q7 — Data / artifact / reproducibility
Strengths:
- directly targets proactive `when/how` decomposition;
- detailed ablations separate gating and compression;
- uses the canonical ProactiveMobile benchmark;
- reports latency/compute/memory rather than accuracy alone.

Limitations:
- preprint;
- no commercial phone evaluation;
- efficiency is measured in GPU benchmark setting, not battery/SoC rails;
- no real always-on context arrival process;
- 9B PAR is larger than the 7B baseline, complicating simple hardware-transfer interpretation;
- expected compute reduction depends on benchmark intervention distribution.

## Q8 — Evidence vs hypothesis
### [FACT]
Lightweight proactive gating and candidate compression substantially reduce heavy-model execution in the benchmark.

### [FACT]
Separation improves both SR and FTR in that evaluation.

### [OBSERVATION]
A large fraction of prospective proactive compute can be captured before any special always-on hardware is considered.

### [INFERENCE — project]
CG-07's residual duty cycle may be much smaller than a naïve 'continuously run Agent AI' assumption.

### Not established
- phone energy savings;
- wake/idle transition cost;
- shared NPU vs dedicated domain break-even;
- thermal/foreground-QoE value.

## Q9 — Real contribution to project decision
### CG-07
**NARROW / strongest baseline raised; no score change.**

Positive:
- proactive workload makes low-duty-cycle observation/gating strategically relevant.

Negative:
- software/model gating captures a very large fraction of nominal compute before hardware;
- therefore dedicated always-on domain must be compared against the residual after PRPF-class sparsification.

### C / A
Generic scheduling remains C territory; semantic demand overlap does not create a new A claim.

## Q10 — Next action
1. KEEP P0 baseline with preprint boundary.
2. Update CG-07 strong baseline to include proactive pre-reasoning gating.
3. Add an experiment input for real intervention rate/context arrival/wake cost.
4. Do not promote CG-07 until target-phone measured data exists.

## Decision footer
- **Evidence maturity:** software SYSTEM_VALUE on benchmark/GPU; not phone SYSTEM_VALUE
- **CG-07 impact:** strong baseline pressure + better workload definition
- **score impact:** none
- **hardware impact:** none
- **Primary source:** https://arxiv.org/abs/2606.03236