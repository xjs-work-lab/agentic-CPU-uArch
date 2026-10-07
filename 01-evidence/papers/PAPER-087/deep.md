# PAPER-087 — ProactiveMobile: A Comprehensive Benchmark for Boosting Proactive Intelligence On Mobile Devices

## Source
- CVPR 2026, pp. 27503–27513
- official CVF Open Access version reviewed
- artifact: https://github.com/xiaomi-research/proactive-mobile
- benchmark: proactive mobile intelligence
- Priority: P0

## Q1 — Problem + target mapping
Reactive mobile Agents wait for an explicit command.
A persistent/proactive Agent must instead determine:
1. whether the current context warrants intervention;
2. what latent user intent is likely;
3. which executable function sequence should be proposed or executed.

This is a structural workload change for the project because the system may observe context continuously while expensive reasoning should happen only selectively.

## Q2 — Novelty / new-regime relevance
ProactiveMobile formalizes proactive intelligence over four context dimensions:
- **User Profile** — facts, habits, preferences;
- **Device Status** — hardware/battery/network/location/notifications and immediate state;
- **World Information** — weather/time/holidays/external state;
- **Behavioral Trajectory** — textual or GUI-screen sequence revealing evolving intent.

Output is not merely a text suggestion.
The benchmark requires executable function sequences, including a no-action/no-recommendation case.

Classification:
**DIRECT_AGENTIC / smartphone workload premise**.

## Q3 — Falsifiable hypothesis
If proactive mobile assistance is a specialized learnable capability, targeted training on latent-intent/context-to-action examples should materially outperform general-purpose models and reduce inappropriate action triggering.

Falsifiers:
- general models already solve the task well zero-shot;
- contextual dimensions add little beyond latest screen;
- no-action decisions are trivial;
- executable mapping does not reflect useful real-world assistance;
- personalized latent-intent inference is too ambiguous for repeatable evaluation.

The CVPR results show current general models perform poorly and targeted fine-tuning helps materially.

## Q4 — Research lineage / competing route
Related routes:
- reactive mobile GUI Agents;
- next-action prediction;
- recommender systems;
- intent prediction;
- contextual/personalized assistants;
- always-on sensing;
- proactive Agent benchmarks and intervention-timing work.

For this project the key distinction is:
> proactive workload introduces **when-to-intervene / when-to-remain-silent** as a first-class decision before expensive assistance reasoning.

## Q5 — Key mechanism / control point
ProactiveMobile itself is a benchmark, not a runtime mechanism.

It exposes the workload variables that a runtime may see:
- current behavior trajectory;
- device/world state;
- user profile;
- candidate intent/function space;
- no-action vs action decision.

Potential project implication:
the duty cycle of heavy Agent reasoning should depend on intervention probability rather than treating every context update as useful work.

## Q6 — Experiment design
Benchmark:
- more than 3,660 instances;
- 14 real-world scenario categories;
- 1–3 valid target actions per instance;
- multi-stage generated data plus expert auditing;
- executable function pool.

Peer-reviewed CVPR version reports:
- fine-tuned Qwen2.5-VL-7B-Instruct: **20.82% Success Rate**;
- o1: **17.02%**;
- GPT-5: **11.37%**.

Ablations show output/training format strongly affects False Trigger Rate; variants without explicit recommendation reasoning can produce very poor no-action behavior.

## Q7 — Data / artifact / reproducibility
Strengths:
- CVPR 2026 peer review;
- public benchmark/code;
- executable rather than text-only outcomes;
- explicit False Trigger Rate;
- context includes actual mobile-relevant state dimensions.

Limitations:
- data/context are benchmark constructions rather than months of passively collected real-user smartphone traces;
- model training uses large H20 GPU clusters;
- no real phone latency/power/thermal measurement;
- no measured context-arrival rate or intervention duty cycle;
- benchmark repo/paper versions show minor drift in API count and result numbers.

Version rule:
- use **20.82% / 17.02% / 11.37%** for the peer-reviewed CVPR 2026 paper;
- do not silently substitute later arXiv/repository values such as 19.15% or a 61-vs-63 API pool.

## Q8 — Evidence vs hypothesis
### [FACT]
Proactive mobile assistance requires an explicit no-action/intervention judgment in addition to intent/action generation.

### [FACT]
Targeted training materially improves the evaluated proactive task but absolute success remains low.

### [OBSERVATION]
A persistent Agent workload can contain many context observations for which expensive reasoning/action should not be triggered.

### [INFERENCE — project]
This is a credible workload premise for a low-duty-cycle always-on Agent front end.

### Not established
- actual phone context-update frequency;
- actual proportion of no-action observations in production;
- phone energy cost;
- need for a dedicated hardware domain.

## Q9 — Real contribution to project decision
### CG-07
**Strengthens workload relevance, not hardware promotion.**

CG-07 previously had strong vendor product signal but weak representative workload evidence.
ProactiveMobile supplies a concrete workload where selective always-on observation/gating is meaningful.

But it does not show that a dedicated low-power domain beats:
- software pre-gating;
- CPU/small-model path;
- shared NPU power gating/DVFS;
- batching/effective-wake reduction.

### A
Latent intent / intervention value is conceptually adjacent to semantic demand, but ProactiveMobile does not establish A's non-reconstructible RequiredProgress residual.

## Q10 — Next action
1. KEEP as P0 proactive workload seed.
2. Add proactive `when-to-intervene` workload to CG-07 experiment design.
3. Require strong lightweight gating baseline before any CG-07 promotion.
4. Search for real phone always-on/proactive duty-cycle and power measurements.

## Decision footer
- **New-regime relevance:** DIRECT_AGENTIC proactive workload
- **Evidence maturity:** workload/capability evidence, not phone SYSTEM_VALUE
- **CG-07 impact:** workload premise strengthened / no score change
- **hardware impact:** none
- **Primary source:** CVPR 2026 Open Access