+++
id = "DEC-H-CAL-001"
type = "DECISION_EVENT"
subject_kind = "ROADMAP"
subject_id = "ROADMAP-CURRENT"
event_type = "OPEN_NARROW_ANALYSIS_HYPOTHESIS_NO_DIRECTION"
effective_date = "2026-10-07"
transaction_id = "TXN-20261007-FRONTIER-ROUND11-01"
trigger_claims = ["CLM-CAL-001", "CLM-CAL-002", "CLM-CAL-003"]
trigger_experiments = []
+++

# DEC-H-CAL-001 — Open Contiguous Agent Learning only as a narrow analysis hypothesis

## Previous state
No active second-Bet frontier was assigned after proactive/always-on coverage was integrated into CG-07.

## New state
**H-CAL — ANALYSIS HYPOTHESIS / NARROWED / NOT A DIRECTION.**

## Why
- PAPER-089 exposes an Agent-native stable-weight break: adapter updates affect live KV validity while serving continues;
- PAPER-091 proves sustained phone training can be battery/thermal significant;
- PAPER-090 / 092 / 093 show strong generic software capture for layout, memory and mobile training runtime.

## Surviving residual
Only the smartphone-specific combination of live Agent serving, repeated adaptation, versioned model/KV state and mixed foreground/background resource use is worth one more residual test.

## Boundary
No Direction. No score. No hardware candidate. Generic on-device training is not rebranded as Agent-specific.
