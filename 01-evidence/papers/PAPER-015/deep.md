# PAPER-015 — PARE — EDP v1 FULL_10Q

Re-reviewed: 2026-10-07

## Q1 — Problem + target mapping
A proactive assistant must infer latent user goals, decide when to intervene, obtain approval and execute across apps.

PARE builds a stateful simulated mobile-phone environment so this interaction can be evaluated in closed loop.

A mapping:
Demand/authorization state exists before execution and is not equivalent to ordinary task readiness.

## Q2 — Novelty / new-regime relevance
PARE uses:
- finite-state-machine apps;
- active user simulation;
- asymmetric user/assistant interfaces;
- Observe-Execute proactive architecture.

This is Agent-native proactive interaction semantics.

## Q3 — Falsifiable hypothesis
A proactive assistant should improve user-goal completion while keeping proposal acceptance high; excessive proposal rate or premature proposals should hurt interaction quality.

## Q4 — Research lineage / competing route
UC Santa Barbara / Apple / University of Washington lineage; independent from P043/P044.

Competing routes:
- static proactive benchmarks;
- long-history demand classifiers;
- direct mobile GUI agents.

## Q5 — Mechanism / control point
Assistant modes:
1. Observe
2. Awaiting confirmation
3. Execute

Observe:
- read-only tools;
- wait;
- propose/send message.

If accepted:
- transition to Execute with full flat API over scenario apps.

If rejected:
- return to Observe; executor is not invoked.

Thus state-changing execution is structurally behind explicit user authorization.

## Q6 — Experiment design + results
Pare-Bench:
- 143 scenarios;
- communication/productivity/scheduling/lifestyle apps;
- 7 evaluated LLMs;
- 4 runs per scenario in the main setup;
- GPT-5-mini user simulator in the reported trajectory analysis.

Examples:
Claude 4.5 Sonnet:
- Success Rate 42.0% ±1.0
- Proposal Rate 12.8% ±0.4
- Acceptance Rate 78.2% ±0.8
- ~20.2 read actions

GPT-5:
- Success Rate 37.4% ±1.5
- Proposal Rate 28.1% ±0.3
- Acceptance Rate 70.2% ±1.0
- ~20.6 read actions

Proposal-outcome analysis:
Claude:
- direct accept 72.1%
- reject 7.8%
- gather context 17.8%
- truncated 2.3%

GPT-5:
- direct accept 64.1%
- reject 7.4%
- gather context 23.4%
- truncated 5.1%

Gather-context outcomes often remain unresolved because of the 10-turn cap.

## Q7 — Artifact / reproducibility
Public PARE repository exists.
Apps and proposal/acceptance mechanics are explicit and reproducible.

External validity limits:
- simulated user;
- FSM apps;
- assistant gets privileged flat APIs;
- no real phone scheduler, energy, thermal or jank data.

## Q8 — Evidence vs alternatives
Strongly demonstrates:
- proactive demand is not simply “work exists”;
- proposal timing and acceptance form real semantic states;
- users may need more context before accepting a proposal.

Does not demonstrate:
- effectful branch speculation before approval;
- frequency/cost of cancellable phone compute;
- incremental value of exporting DemandState below the Agent runtime.

## Q9 — Decision contribution
Supports CLM-AGENT-001 as **semantic ground truth**, not system-value proof.

It also strengthens B4:
Observe/read-only and authorization gating are already explicit runtime states.

Therefore A's residual must be incremental value from richer RequiredProgress/DemandState, not the existence of confirmation state itself.

## Q10 — Next action
KEEP P0.

Use PARE as a source of semantic labels and premature-intervention cases.
Do not use proposal fractions as phone compute prevalence.
EXP-A-001 should test whether internal DemandState adds information beyond observed history + proposal/confirmation/runtime state.

## Decision footer
- Evidence maturity: STRUCTURAL_SIGNAL
- Decision impact: KEEP / NARROW
- Open questions: target-phone mapping; real-user prevalence; lower-layer actuator value
- Primary source: https://arxiv.org/abs/2604.00842
- Artifact: https://github.com/deepakn97/pare
