# TXN-20261006-FRONTIER-ROUND3-01 — Agent-specific residual audit

## Question
Which of four surviving Agent-specific residuals remain credible after strong Agent-runtime and workflow-serving prior art?

## Residuals
- cancel/discard/commit legality;
- RequiredProgress;
- state-reuse identity;
- foreground-impact budget.

## Sources completed with full 10Q
- PAPER-063 — Speculative Actions — ICLR 2026 / P0;
- PAPER-064 — Sherlock — arXiv preprint 2025 / P1;
- PAPER-065 — KVFlow — NeurIPS 2025 / P0.

## Canonical objects added
- CLM-AGENT-006;
- EC-PTA-005-A;
- EC-PTA-005-B;
- CLM-AGENT-007;
- EC-A-007-A;
- DEC-PTA-002;
- DEC-A-005.

## Direction/experiment changes
- PT-A contract now explicitly includes speculative effect class, commit guard, rollback/compensation and lineage.
- A B4-TX now includes verification/provisional state, legality/rollback scope, workflow topology, STE and reuse-distance proxies.
- EXP-A-001 now requires DemandState/RequiredProgress to beat these stronger proxies.

## Decisions
### Cancel/discard legality
NARROW as independent opportunity. Strong Agent-runtime capture exists. Retain as PT-A platform field and A baseline.

### State-reuse identity
NARROW as independent opportunity. Workflow topology/STE already drives state-retention and prefetch in KVFlow.

### RequiredProgress
KEEP inside A. Exact residual remains unresolved, but must beat topology/criticality/verification/legality/reuse proxies.

### Foreground-impact budget
OPEN as analysis hypothesis `H-FIB`; highest-priority next second-Bet probe.
No Direction/promotion yet.

## Portfolio
No lane or score changes.

## Next smallest useful step
Pressure-test H-FIB against direct mobile/persistent-Agent evidence and Sereno/MUSched/TimelyLLM/generic self-throttling baselines.

## Anti-drift note
This round does not search for new scheduler architecture or new uArch ideas.
It asks only whether Agent-specific marginal-value/tolerance information changes a real smartphone resource-control decision.