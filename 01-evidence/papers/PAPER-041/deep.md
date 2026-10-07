> Evidence Rescue Round 1 re-read under EDP v1 on 2026-10-07.
> V1 provenance remains the frozen baseline; this page is the current mechanism-level interpretation.

# PAPER-041 — Cordon: Semantic Transactions for Tool-Using LLM Agents

## Q1 — Problem + target mapping
Per-tool RPC safety checks do not provide a task-scoped boundary for cross-step state/effect composition.

Cordon asks whether an Agent task can be executed as one semantic transaction with commit/abort/recovery semantics.

Project mapping:
- A strongest baseline for reconstructible/enforceable Effect/Commit legality;
- PT-A substrate for explicit effects, validation and bounded recovery.

## Q2 — Novelty / new-regime relevance
Cordon binds:
- tool intents;
- runtime-tracked result lineage;
- shadow local state;
- pending external effects;
- delegated authority;
- audit/recovery metadata.

Classification: **Agent-native runtime containment**, but not smartphone-specific.

## Q3 — Falsifiable hypothesis
Cross-step validation at a task-level transaction boundary should catch correlated risks missed by point defenses while preserving benign task completion and practical recovery.

The evaluation supports this within Cordon's mediated runtime boundary.

## Q4 — Competing route
Compared conceptually/evaluatively against boundaries such as:
- prompt/tool point checks;
- sandbox/process isolation;
- per-effect guards;
- post-hoc recovery.

For this project it also competes with any claim that Effect/Commit legality must be supplied as irreducible Agent semantic state.

## Q5 — Mechanism / control point
Mechanism chain:

`mediated tool call → task-scoped intent → lineage + authority + staged state/effect → composed validation → commit / abort / approval / audit-compensation`

Key components:
- transaction manager;
- result lineage;
- shadow state;
- effect outbox;
- authority state;
- recovery log.

Crucial boundary:
Cordon **does not create policy or authority from nothing**.
Its guarantees depend on relevant effects being mediated/observable and the required policy/authority/effect metadata being available.

## Q6 — Experiment design + results
Evaluation includes:
- 45 risk-bearing multi-tool workflows across nine defense-boundary categories × five transaction-level risk families;
- five deterministic rollback trajectories;
- τ-bench and Terminal-Bench benign sanity checks.

Reported:
- plain execution commits policy-violating effects in 45/45 constructed risk workflows;
- strategy adapters intercept 14/45 before commit;
- Cordon intercepts 45/45 before commit;
- excluding approval wait, transaction-mediated execution reduces mean task time 24.6–27.9% in the reported risky-workflow setup, largely because unsafe chains terminate earlier;
- token use falls 23.6–28.4%;
- median rollback primitive latency 4.17 ms;
- 15/15 resume checks pass;
- transaction-control path accounts for roughly 22.2–23.4% of measured time in the cited breakdown.

These numbers must not be interpreted as a universal “transactions are faster” claim.

## Q7 — Data / artifact / reproducibility
Strengths:
- explicit risk taxonomy;
- benign benchmarks plus adversarial workflows;
- recovery tests;
- detailed runtime cost decomposition.

Limits:
- risk suite is constructed rather than production trace distribution;
- approval behavior materially affects wall time;
- guarantees require tool/runtime mediation;
- opaque external effects can only enter audit/compensation after the boundary is crossed.

## Q8 — Evidence vs hypothesis
### Demonstrated
A runtime can enforce substantial task-level commit discipline when it controls and observes the relevant effect path.

### Not demonstrated
- universal semantic correctness;
- universal derivability of effect legality;
- complete rollback of already-observed external actions;
- smartphone system value.

## Q9 — Project decision contribution
Previous wording “Effect/Commit legality can be runtime-derived” was too broad if read unconditionally.

Correct baseline:
> substantial Effect/Commit legality can be **constructed/enforced where mediation, observability, policy/authority and effect metadata exist**.

A's B4-TX remains strong, but only “where available.”
Any semantic fact outside that mediated/observable boundary cannot be assumed reconstructible.

## Q10 — Next action
- KEEP as P0 strongest runtime baseline.
- Narrow CLM-AGENT-003.
- Preserve A's differentiated question around RequiredProgress rather than generic transaction handling.
- Use PT-A experiments to expose opaque/unmediated effect paths rather than assume complete rollback.

## Decision footer
- Evidence maturity: **SYSTEM_VALUE for Agent runtime containment; phone transfer unproven**
- Decision impact: **NARROW strongest-baseline wording; no lane/score change**
- Open questions: production workload mix, smartphone overhead, opaque tool/effect paths
- Primary source: https://arxiv.org/abs/2606.17573
