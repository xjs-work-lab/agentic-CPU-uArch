> V1 semantic source copied/repacked from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.
> Do not reinterpret this page as V2.2 metadata authority; the compact README owns the Source object.

# PAPER-041 — Cordon: Semantic Transactions for Tool-Using LLM Agents

## Source
- Paper: https://arxiv.org/abs/2606.17573
- Authors: Zheng Chen, Hanqing Liu, Duling Xu, Dong Dong, Jialin Li, Bangzheng Pu, Jidong Zhai
- Venue/status: arXiv preprint, 2026
- Target: tool-using Agent runtimes
- Project relevance: effect/commit/rollback; second-Bet audit
- Priority: P0

## Q1 — Problem
Per-tool RPC boundaries do not provide task-scoped commit, rollback, recovery or audit across multi-step Agent workflows with real side effects.

## Q2 — Novelty
Cordon introduces semantic transactions spanning tool intents, result lineage, reversible state, staged external effects and audit metadata.

## Q3 — Hypothesis
A task-level transactional containment boundary can reduce irreversible-effect failures while preserving benign task completion.

## Q4 — Competing route
Directly pressures any broad project proposal around:
> Agent transaction / effect-safe commit / rollback runtime.

## Q5 — Mechanism
- transaction manager;
- shadow state;
- effect outbox;
- lineage tracking;
- validation before commit;
- recovery metadata.

## Q6 — Experiment
The paper reports adversarial/benign workflow evaluation and reduced irreversible-effect failures with modest overhead; exact normalized system numbers should be re-read before quantitative final-report comparison.

## Q7 — Artifact
Artifact status not yet verified.

## Q8 — Evidence vs hypothesis
**[FACT]** transactional Agent execution is already a concrete systems research line.

## Q9 — Project contribution
Stage 15C strengthens this paper's role.

Effect/Commit Safety remains required for Candidate A correctness, but Cordon demonstrates that a strong runtime can **construct and enforce** substantial effect/commit legality from:
- task-scoped transaction state;
- runtime lineage;
- shadow state;
- staged effect outboxes.

Therefore:
> Effect/Commit should not automatically be counted as uniquely Agent-supplied semantic information.

The differentiated semantic burden shifts toward **DemandState / required-progress value**, while transaction-derived legality becomes part of the strongest B4-TX runtime baseline.

Generic transactional Agent runtime still does not qualify as an independent second Bet.

## Q10 — Next action
- KEEP as P0 negative evidence.
- Fold effect/commit semantics into A correctness/runtime requirements.
- Do not open a separate transaction Bet unless phone-specific residual appears.

## Decision footer
- Evidence maturity: SYSTEM_VALUE/STRUCTURAL evidence for Agent runtime; phone transfer unproven
- Decision impact: kill generic transactional-runtime second Bet
- Open questions: smartphone-specific side-effect path
- Primary source: https://arxiv.org/abs/2606.17573
