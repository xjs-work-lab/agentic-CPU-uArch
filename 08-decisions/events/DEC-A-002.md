+++
id = "DEC-A-002"
type = "DECISION_EVENT"
subject_kind = "DIRECTION"
subject_id = "A"
event_type = "BASELINE_STRENGTHEN_NO_LANE_CHANGE"
effective_date = "2026-10-06"
transaction_id = "TXN-20261006-PAPER056-10Q"
trigger_claims = ["CLM-AGENT-004"]
trigger_experiments = []
+++

# DEC-A-002 — A baseline strengthened after AgentProg review

## Change
A remains:
- **PRIMARY_BET**
- score context **82.5**
- evidence maturity **SIMULATION_SUPPORT**

No promotion or demotion.

`B4-TX` is strengthened to include reconstructible semantic execution state exposed by strong Agent runtimes:
- program/control-flow position;
- persistent task variables/data-flow;
- belief/environment state;
- step-specific history.

## Why
PAPER-056 shows these semantic representations can materially improve long-horizon mobile GUI Agent correctness in software.

Therefore semantic-state value itself cannot be credited to A's differentiated DemandState hypothesis.

## Boundary
This does not establish that DemandState has no residual value.
`CLM-A-001` remains OPEN and must be tested against the strengthened baseline.
No hardware/uArch conclusion.
