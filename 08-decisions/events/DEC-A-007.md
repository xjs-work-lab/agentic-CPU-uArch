+++
id = "DEC-A-007"
type = "DECISION_EVENT"
subject_kind = "DIRECTION"
subject_id = "A"
event_type = "EVIDENCE_RESCUE_REVALIDATE_NARROW_NO_LANE_CHANGE"
effective_date = "2026-10-07"
transaction_id = "TXN-20261007-EVIDENCE-RESCUE-R1B-01"
trigger_claims = ["CLM-AGENT-001", "CLM-AGENT-002", "CLM-AGENT-003", "CLM-A-001"]
trigger_experiments = ["EXP-A-001"]
+++

# DEC-A-007 — Rescue-1B revalidates A but narrows it to conditional information value

## Previous state
A was PRIMARY_BET / 82.5 / SIMULATION_SUPPORT with differentiation centered on DemandState / RequiredProgress beyond B4-TX.

## New state
**No lane/score/maturity change.**

A remains:
- PRIMARY_BET;
- 82.5;
- SIMULATION_SUPPORT.

The differentiating proposition is made stricter:
A receives credit only if explicit Agent-internal DemandState separates states that remain similar under the strongest observable/history/runtime baseline and produces >=~5% end-outcome value.

## Why
Deep reading shows:
- PAPER-013: speculation/cancel/commit state is substantially runtime-visible.
- PAPER-015: proactive demand/authorization states are real, but effectful execution is already confirmation-gated.
- PAPER-043: behavioral history is a credible learned demand predictor; metadata corrected to ICLR 2025.
- PAPER-044: long real per-user history and real-world training materially strengthen When-to-Assist prediction.
- PAPER-050: dependency/effect legality can often be traced and validated by runtime within an observable scope.

No source directly tests the residual in CLM-A-001.

## Decision
KEEP A as the sole differentiated Primary Bet **provisionally**.

Do not upgrade evidence maturity.
Do not infer hardware need.

EXP-A-001 is strengthened to a matched-observability conditional-information test.

## Reopen/downgrade trigger
If B4-TX reproduces the B6-Demand value under the strengthened experiment, downgrade or kill A as differentiated research.
