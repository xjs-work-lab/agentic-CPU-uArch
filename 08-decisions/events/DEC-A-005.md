+++
id = "DEC-A-005"
type = "DECISION_EVENT"
subject_kind = "DIRECTION"
subject_id = "A"
event_type = "LEGALITY_REUSE_PROXY_BASELINE_STRENGTHEN_NO_LANE_CHANGE"
effective_date = "2026-10-06"
transaction_id = "TXN-20261006-FRONTIER-ROUND3-01"
trigger_claims = ["CLM-AGENT-006", "CLM-AGENT-007"]
trigger_experiments = ["EXP-A-001"]
+++

# DEC-A-005 — A baseline strengthened by legality and workflow-derived reuse proxies

## Change
A remains:
- PRIMARY_BET;
- score context 82.5;
- SIMULATION_SUPPORT.

No promotion or demotion.

B4-TX and EXP-A-001 now explicitly include reconstructible proxies for:
- Effect/Commit legality;
- verifier-pending / verified state;
- rollback/discard scope;
- workflow topology and criticality;
- future invocation distance / STE;
- shared-prefix / reusable-state identity;
- topology-driven retention/prefetch.

## Why
PAPER-063/PAPER-064 show that legality and provisional-state semantics can already drive Agent-runtime speculation/rollback.
PAPER-065 shows that Agent workflow topology can reconstruct future-use/reuse-distance information and drive cache decisions.

Therefore A cannot receive differentiated credit for signals that are equivalent to these upper-layer proxies.

## Surviving A residual
RequiredProgress remains open only insofar as it captures decision-relevant information that **cannot be reproduced by topology, slack/criticality, verification vulnerability, legality or future-reuse proxies** and still yields >=~5% end-outcome value over B4-TX.

## Boundary
No target-phone SYSTEM_VALUE or hardware promotion is established.