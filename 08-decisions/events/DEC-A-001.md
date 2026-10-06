+++
id = "DEC-A-001"
type = "DECISION_EVENT"
subject_kind = "DIRECTION"
subject_id = "A"
event_type = "PORTFOLIO_LANE_CONFIRM"
effective_date = "2026-10-05"
transaction_id = "TXN-STAGE15D-FREEZE"
trigger_claims = ["CLM-AGENT-001", "CLM-AGENT-002", "CLM-AGENT-003", "CLM-MOBILE-001", "CLM-A-001"]
trigger_experiments = []
+++

# DEC-A-001 — A retained as Primary Bet

## Change
A is retained/frozen as the differentiated Primary Bet after narrowing the differentiating core to DemandState / RequiredProgress over B4-TX.

## Why
The user-facing mobile foreground-protection problem is real, generic baselines are strong, demand can be partially inferred from history, and runtime-derived Effect/Commit legality is a strong B4-TX component. The surviving discriminating question is `CLM-A-001`.

## Boundary
This imported event records the Stage15D state. It does not claim the open hypothesis has already passed SYSTEM_VALUE.

## Origin
- `06-opportunities/stage15-portfolio-rescore-3.md`
- `08-roadmap/stage15-pre-device-roadmap-freeze.md`
