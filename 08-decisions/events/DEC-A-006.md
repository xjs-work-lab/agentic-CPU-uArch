+++
id = "DEC-A-006"
type = "DECISION_EVENT"
subject_kind = "DIRECTION"
subject_id = "A"
event_type = "UTILITY_SLO_HISTORY_BASELINE_STRENGTHEN_NO_LANE_CHANGE"
effective_date = "2026-10-06"
transaction_id = "TXN-20261006-FRONTIER-ROUND4-01"
trigger_claims = ["CLM-AGENT-008", "CLM-MOBILE-003", "CLM-C-008"]
trigger_experiments = ["EXP-A-001"]
+++

# DEC-A-006 — A strongest baseline strengthened by Murakkab, HUSH and utility-accrual prior art

## Change
A remains:
- PRIMARY_BET;
- score context 82.5;
- SIMULATION_SUPPORT.

No lane/score promotion or demotion.

B4-TX / EXP-A-001 now explicitly assume reconstructible or application-supplied:
- workflow/per-request quality, latency and cost SLOs;
- profile-derived resource demand;
- personalized app/user-history background usefulness;
- time/utility functions and graded delay value;
- low-value/infeasible-work abort.

## Why
PAPER-066 demonstrates strong Agent-aware workflow/SLO/resource orchestration.
PAPER-067 demonstrates personalized smartphone background usefulness suppression.
PAPER-068 establishes utility-aware/tolerance-aware mobile-embedded scheduling as foundational prior art.

## Surviving A differentiation
A is no longer testing whether utility-aware scheduling is useful.
It tests whether **Agent semantic execution state itself contains a non-reconstructible RequiredProgress/value signal** beyond SLO/TUF/history/topology/legality/reuse proxies.

## Boundary
No target-phone SYSTEM_VALUE or hardware/uArch promotion.