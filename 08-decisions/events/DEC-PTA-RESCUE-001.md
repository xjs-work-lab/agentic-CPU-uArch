+++
id = "DEC-PTA-RESCUE-001"
type = "DECISION_EVENT"
subject_kind = "DIRECTION"
subject_id = "PT-A"
event_type = "REFRAME_CONTEXT_BOUND_ACTUATION_KEEP_PLATFORM_TRACK"
effective_date = "2026-10-07"
transaction_id = "TXN-20261007-EVIDENCE-RESCUE-R1A-01"
trigger_claims = ["CLM-PTA-001", "CLM-PTA-002", "CLM-PTA-003", "CLM-PTA-006", "CLM-PTA-EXP-002"]
trigger_experiments = ["EXP-PTA-002"]
+++

# DEC-PTA-RESCUE-001 — Reframe PT-A around context-bound actuation

## Previous state
PT-A emphasized heterogeneous API/CLI/MCP/GUI routing, explicit effect metadata, outcome verification and bounded recovery.

## New state
PT-A remains **PLATFORM_TRACK / 80.0 / SYSTEM_VALUE**, but its execution contract is strengthened to include:
- capability/authority-aware routing;
- fresh target/context binding before actuation;
- OutcomeReceipt;
- post-action verification and bounded recovery.

## Why
Deep reading changes three assumptions:
1. PAPER-038's CLI advantage partly relies on benchmark/ADB privilege, so action-surface value must be capability/authority scoped.
2. PAPER-039 shows that exposing more action surfaces without learned/selective routing can reduce accuracy.
3. PAPER-101 shows verification/recovery after action is not sufficient when observation and action recipient can diverge.

PAPER-102 simultaneously confirms that generic action-effect verification is a strong software baseline.

## Portfolio consequence
- PT-A does not become a differentiated Primary Bet.
- Score remains 80.0.
- Evidence maturity remains SYSTEM_VALUE.
- No CPU/uArch candidate.
- The new residual is routed to EXP-PTA-002 and must first survive software/OS baselines.
