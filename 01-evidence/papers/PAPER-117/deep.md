# PAPER-117 — Cordon — FULL_10Q

## Q1 — Problem + target mapping
Tool-using Agents execute multi-step tasks whose effects cross files, APIs, services and authority boundaries, but most runtimes expose tools as isolated RPCs. Per-call checks cannot reason about the composed task-level effect.

AO-2 mapping: explicit commit/abort, lineage and effect authority across a multi-step Agent transaction.

## Q2 — New-regime relevance
Agent-native / Agent-amplified. The unit of correctness changes from individual call validity to the semantic transaction representing an Agent task.

## Q3 — Falsifiable hypothesis
A task-level transaction boundary with effect staging and result lineage should catch unsafe cross-step compositions that per-call guardrails miss while preserving benign completion.

## Q4 — Strongest baseline / competing route
Compared against ordinary Agent execution, per-call/adapter defenses and rollback/recovery approaches without task-level semantic lineage.

## Q5 — Mechanism / control point
Semantic transaction binds task scope/intents, read anchors, derived result objects and lineage, reversible local writes/deletes, staged external effects, delegated authority and audit metadata.

Runtime components: transaction manager, shadow-state engine, effect outbox and recovery log. Lifecycle: prepare, validate composed flow, then commit or abort.

## Q6 — Experiment design + results
Key reported anchors:
- 45 risk-bearing workflows;
- plain execution exposes the risky effect in all 45;
- compared existing-defense strategy blocks 14/45 before commit and misses or acts too late on 31;
- Cordon intercepts 45/45 before commit in the reported suite;
- benign workflows remain viable with modest approval/runtime overhead;
- rollback tests report millisecond-scale local recovery and successful resumption in the tested deterministic trajectories.

## Q7 — Artifact / limitations
Operations must be mediated/observable by Cordon. Opaque plugins/effects outside the runtime boundary are not rollback-safe. Already released external effects may require compensation. No smartphone/accelerator evaluation.

## Q8 — Evidence vs hypothesis
FACT: task-level Agent transaction semantics can be represented and enforced in software.
FACT: cross-step lineage/effect reasoning catches failures missed by per-call checks in the evaluated suite.
FACT: effect authority can be staged before release.
NOT ESTABLISHED: hardware transaction support, xPU queue tags, or mobile value.

## Q9 — Decision contribution
Strong AO-2 MECHANISM and STRONG_BASELINE evidence. Broad novelty around Agent commit/rollback/effect staging is crowded at software/runtime level.

## Q10 — Next action
Compare with Atomix and Versioned Execution for authority/version, progress frontiers, compatible-state inheritance and irreversible-effect gating.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for evaluated runtime/security setting
- Decision impact: strengthen AO-2 while narrowing broad novelty
- Open questions: mobile state/execution propagation, opaque effects, distributed progress
- Primary source: https://arxiv.org/abs/2606.17573