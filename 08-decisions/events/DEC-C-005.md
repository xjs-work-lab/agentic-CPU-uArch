+++
id = "DEC-C-005"
type = "DECISION_EVENT"
subject_kind = "DIRECTION"
subject_id = "C"
event_type = "AUTO_CRITICALITY_PRIOR_ART_BASELINE_STRENGTHEN_NO_LANE_CHANGE"
effective_date = "2026-10-06"
transaction_id = "TXN-20261006-FRONTIER-ROUND2B-01"
trigger_claims = ["CLM-C-007"]
trigger_experiments = []
+++

# DEC-C-005 — C baseline strengthened after WASH

## Change
C remains STRATEGIC_ENABLER / second-Bet watch / 72.0.

G1 now explicitly includes automatic runtime-derived criticality/bottleneck detection and heterogeneous big/small-core placement.

## Why
PAPER-062 shows that rich runtime state can be analyzed automatically to infer critical work and drive heterogeneous CPU placement without programmer hints or new hardware.

Therefore C/H-SCL cannot claim generic automatic criticality extraction or heterogeneous CPU placement as differentiated.

## Portfolio implication
H-SCL should not become a separate Direction on current evidence.
Its surviving questions are folded into:
- A: Agent-specific information-value residual;
- C: smartphone cross-resource control residual.

## Boundary
PAPER-062 is managed-runtime/x86 AMP evidence, not smartphone Agent SYSTEM_VALUE.
No C lane/score or hardware promotion.
