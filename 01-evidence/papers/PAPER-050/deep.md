# PAPER-050 — TomasuLLM — EDP v1 FULL_10Q

Re-reviewed: 2026-10-07

## Q1 — Problem + target mapping
Coding Agents serialize on long tool observations.
Can future tool actions execute early while preserving serial task semantics?

A mapping:
tests whether Effect/Commit legality requires privileged Agent semantic truth or can be reconstructed/enforced by runtime tracing.

## Q2 — Novelty / new-regime relevance
TomasuLLM combines:
- action drafting;
- observation drafting;
- COW speculative sandboxes;
- conservative dependency/effect tracing;
- in-order validation/commit frontier.

Agent-specific because the main Agent remains canonical authority over actions.

## Q3 — Falsifiable hypothesis
Out-of-order tool execution can be reused without outcome drift if the runtime validates action identity, dependency freshness, observation integrity and effect safety against committed state.

## Q4 — Research lineage / competing route
HKUST-led systems line; independent from Cordon and PAPER-013.

Neighboring routes:
- speculative action prediction;
- shell/script speculative execution;
- semantic transactions;
- serial coding-agent runtime.

## Q5 — Mechanism / control point
Each speculative execution leaves Trace IR.

Reuse requires:
- Vact — action identity;
- Vdep — dependency freshness/lineage;
- Vrecord — observation integrity/canonicalization;
- Veffect — effect safety.

Prediction itself is never commit evidence.

Opaque bash is traced conservatively with Riker.
If dependencies/effects cannot be proved complete, the call is a speculation barrier and executes serially.

Irreversible or unsuitable effects are barriers.

## Q6 — Experiment design + results
Reported:
- 100 SWE-bench Verified tasks: 1.31×;
- 28 Terminal-Bench 2.0 tasks: 1.35×;
- 18 SWE-Marathon sessions: 1.27× arithmetic-mean matched progress.

SWE-bench outcome:
both Serial Pi and TomasuLLM resolve mean 41.7%; difference 0.0 points, 95% CI [-4.3,+4.3].

Validation audit:
- one-in-ten sampling over paired SWE-Marathon executions;
- 4,010 commit-validation records;
- zero false accepts;
- reads/writes 100% accepted when valid;
- read-only bash ~99%;
- tests ~98%;
- invalid/stale cases are rejected and rerun serially;
- 390 additional barrier records run serially.

Primitive overhead:
- read-only fork around 0.08 s;
- tests needing private data copy ~3–5.5 s.

## Q7 — Artifact / reproducibility
Primary paper is public and implementation details are unusually explicit.

Current audit does not establish a public code release suitable for direct reproduction.

The 4,010 validation records are a sampled audit, not exhaustive proof of zero-error semantics.

## Q8 — Evidence vs alternatives
Strongly demonstrated within the measured coding-tool scope:
runtime can reconstruct substantial dependency/effect legality without trusting model rationale.

Boundary is equally important:
- untraceable effects;
- irreversible external actions;
- service restarts/checkpoints/final submissions;
- dependencies outside traced process scope
become barriers.

Thus “all Effect/Commit legality is runtime-derived” would be false.

## Q9 — Decision contribution
Strong support for CLM-AGENT-003 and B4-TX.

A loses differentiated credit for generic Effect/Commit legality wherever runtime mediation/tracing is sufficient.

A's core must remain DemandState / RequiredProgress residual.

## Q10 — Next action
KEEP P0.

EXP-A-001 baseline should assume TomasuLLM/Cordon-class legality when feasible.
Only opaque/irreversible/non-mediated residual semantics remain candidate privileged information.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for coding/tool Agent runtime; indirect for smartphone
- Decision impact: NARROW A; strengthen B4-TX
- Open questions: phone effect surfaces; tracing cost; non-mediated semantics
- Primary source: https://arxiv.org/abs/2609.38201
