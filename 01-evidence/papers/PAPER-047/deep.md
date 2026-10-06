# PAPER-047 — Decoupling Readiness from Release for Tail-Aware Scheduling of Agentic LLM Workflows

## Source
- Paper: https://arxiv.org/abs/2609.10964
- Authors: Bochao Feng, Jianjiang Li, Haojie Wang, Lin Qiao, Yinghui Li, Yukun Yan, Jidong Zhai
- Venue/status: arXiv preprint, 2026-09-10
- Target: Agentic LLM workflow serving / release scheduling
- Project relevance: R1 post-ready timing; C1 E1 TemporalFlexibility
- Priority: P0

## Q1 — Problem + target mapping
Agentic workflows contain ready turns that are usually released immediately. Under contention, eager release can create released-but-unfinished work that the workflow scheduler can no longer reorder, harming tail flow time.

This maps directly to the project's R1 distinction:
**DependencyReady != Release**.

## Q2 — Novelty / new-regime relevance
The paper makes release itself a scheduling decision:
- choose which ready turn to release;
- control released-work budget;
- optimize workflow-level tail risk.

This is directly Agentic workflow scheduling.

## Q3 — Falsifiable hypothesis
A release scheduler that reasons about workflow tail risk, online work estimates and queue pressure should beat eager release under contention without hurting light-load behavior.

## Q4 — Research lineage / competing route
This is the strongest direct competing route found so far against broad R1 novelty.

It shows that decoupling readiness from release does **not** require:
- explicit LatestUsefulResume semantics;
- a new phone-specific ABI;
- hardware support.

## Q5 — Key mechanism / control point
Inputs:
- ready workflow turns;
- online work estimates;
- unfinished-work/tail-risk state;
- queue pressure.

Actuators:
- select next turn to release;
- adapt total released-but-unfinished work budget.

## Q6 — Experiment design
The abstract reports evaluation on real Agent execution traces from software-engineering tasks across:
- multiple LLMs;
- multiple workflow arrival rates.

Results:
- comparable to eager release under light load;
- up to **3.50x P95 workflow flow-time speedup** under contention.

## Q7 — Data / artifact / reproducibility
Public arXiv paper available.
Artifact/code availability was not established in this round.

## Q8 — Evidence vs hypothesis
**[FACT]** Ready/release decoupling is directly demonstrated as a useful Agent workflow scheduling primitive.

**[BOUNDARY]**
Server/workflow tail latency is not smartphone energy/QoE, and the paper does not establish that semantic LatestUsefulResume has zero residual value.

## Q9 — Decision contribution
Materially narrows R1.

Killed as strategic novelty:
- generic deferred-ready continuation state;
- generic ready/release decoupling;
- generic release budget.

Surviving residual:
> explicit Agent semantic timing bounds must add value beyond a strong generic release scheduler.

## Q10 — Next action
- KEEP as P0 negative/constraint evidence.
- Harden R1 B4 with workflow release scheduling.
- Measure GenericReleaseCapture before any R1 implementation.
- No uArch promotion.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for server Agent workflow release scheduling; STRUCTURAL_SIGNAL for smartphone transfer
- Decision impact: NARROW / DOWNGRADE R1
- Open questions: phone energy/QoE transfer; artifact; semantic-bound incremental value
- Primary source: https://arxiv.org/abs/2609.10964
