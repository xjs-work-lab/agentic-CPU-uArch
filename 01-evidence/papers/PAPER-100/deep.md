# PAPER-100 — Jev-Mobile

## Source
- arXiv:2609.30186, 2026 preprint
- AndroidWorld full task suite
- Priority: P1 software architecture baseline

## Q1 — Problem + target mapping
Step-wise GUI Agents often invoke an expensive VLM for every action.

Jev-Mobile asks:
> can a high-level VLM delegate a local goal and let a cheaper typed executor perform several observation-grounded actions before returning control?

## Q2 — Novelty / new-regime relevance
The system decomposes control:
- VLM: interpret screenshot/tree/task and issue local goal;
- program: enumerate executable candidates from the current accessibility tree;
- Jev: choose candidate ID or DONE/BLOCKED;
- after each action: re-observe and rebuild candidates.

Classification:
**GENERIC/Agent enabling hierarchical execution baseline**.

The paper itself notes hierarchical/lightweight execution is not broadly novel; its narrower contribution is typed decision-model execution over live candidates.

## Q3 — Falsifiable hypothesis
If low-level GUI action selection is simpler than high-level task interpretation, typed local decisions should reduce expensive VLM use with limited success loss.

Falsifiers:
- handoffs dominate;
- accessibility-tree coverage is poor;
- cheap executor errors compound;
- a small VLM performs equally well;
- remote service latency/cost offsets fewer VLM calls.

## Q4 — Research lineage / competing route
Competing routes:
- step-wise VLM;
- SeeAct-V visual grounding;
- Mobile-Agent planning/reflection decomposition;
- Hi-Agent / EcoAgent high-low or edge-cloud split;
- script/action-plan compilation;
- lightweight GUI policies.

## Q5 — Key mechanism / control point
- live accessibility-tree candidate enumeration;
- typed ID selection;
- DONE/BLOCKED handoff;
- stale-ID validation before execution;
- action-history handoff instead of model-written summaries.

This makes executability and handoff explicit software state.

## Q6 — Experiment design
Benchmark:
- full AndroidWorld suite.

Compared systems:
- Step-wise VLM;
- SeeAct-V adaptation;
- Jev-Mobile.

General VLM:
- Qwen3.8-Max in the reported setup.

Reported aggregate results:
- success: 0.84 Step-wise VLM, 0.78 SeeAct-V, 0.79 Jev-Mobile;
- mean total time per successful trajectory: 197.21s vs 162.63s vs 132.67s;
- mean executor-model time: 94.30s vs 12.37s vs 5.16s;
- model API cost per successful trajectory is reported substantially lower, including a 73.4% reduction versus Step-wise VLM in the paper’s comparison.

## Q7 — Data / artifact / reproducibility
Strengths:
- full benchmark;
- independent terminal evaluator;
- explicit accounting of time/cost;
- action IDs tied to fresh observations;
- failure categories separated into coverage/selection/handoff.

Limitations:
- Jev is remote, not on-device;
- only three complete-system comparators;
- SeeAct-V uses a substituted grounder;
- tree-missing visual targets are inaccessible;
- no small-local-VLM executor ablation.

## Q8 — Evidence vs hypothesis
### [FACT]
Multiple low-level GUI actions can be executed under one high-level VLM delegation in the tested system.

### [FACT]
Fresh-tree candidate rebuilding prevents stale IDs from silently binding to changed UI nodes.

### [OBSERVATION]
High-level semantic planning and low-level executable action selection can operate at different cadences.

### [INFERENCE — project]
A must compare against hierarchical software decomposition; per-step VLM reasoning is no longer a credible strongest baseline.

## Q9 — Real contribution to project decision
Jev-Mobile strengthens existing ownership:
- A: high-level semantic progress may be delegated less frequently;
- PT-A: executable action candidates and handoff status are explicit runtime state.

It does not create a new lane:
- mechanism is upper-layer;
- no on-device compute evidence;
- no CPU/NPU hardware residual.

## Q10 — Next action
1. KEEP as A/PT-A strongest software baseline.
2. Do not credit per-step reasoning reduction as new differentiation.
3. Use only as workload/control decomposition evidence, not mobile hardware evidence.
4. No score/lane change.

## Decision footer
- **Evidence maturity:** STRUCTURAL_SIGNAL / software benchmark
- **Decision impact:** raises A/PT-A baseline
- **Open questions:** on-device executor, small-VLM comparison, accessibility-tree coverage
- **Primary source:** https://arxiv.org/abs/2609.30186
