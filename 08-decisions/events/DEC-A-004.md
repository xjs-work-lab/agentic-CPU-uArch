+++
id = "DEC-A-004"
type = "DECISION_EVENT"
subject_kind = "DIRECTION"
subject_id = "A"
event_type = "GENERIC_SEMANTIC_SCHEDULER_BASELINE_STRENGTHEN_NO_LANE_CHANGE"
effective_date = "2026-10-06"
transaction_id = "TXN-20261006-FRONTIER-ROUND2-01"
trigger_claims = ["CLM-MOBILE-002"]
trigger_experiments = []
+++

# DEC-A-004 — Generic semantic scheduler added to A baseline

## Change
A remains PRIMARY_BET / 82.5 / SIMULATION_SUPPORT.

B4-TX now explicitly includes generic mobile interaction-critical semantics and dependency-priority propagation of the type demonstrated by MUSched.

## Why
PAPER-060 shows that high-level mobile interaction context can already be converted into compact scheduler-visible control state with measurable commercial-phone QoE benefit.

Therefore A's DemandState/RequiredProgress hypothesis must add value beyond:
- generic interaction criticality;
- critical-path annotations;
- IPC/lock dependency propagation;
- bounded semantic priority classes.

## Boundary
MUSched is not an Agent workload and does not test CLM-A-001 directly.
No A score/lane change and no hardware conclusion.
