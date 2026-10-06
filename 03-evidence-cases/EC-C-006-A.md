+++
id = "EC-C-006-A"
type = "EVIDENCE_CASE"
record_state = "CURRENT"
relation = "SUPPORT"
target_kind = "CLAIM"
target_id = "CLM-MOBILE-002"
warrant = "MUSched directly evaluates semantic annotation, VIP scheduling and dependency-priority propagation on a Snapdragon 8 Elite commercial phone and reports improved cold-start/QoE metrics with low scheduling overhead."
scope = "PAPER-060 laboratory commercial-phone evaluation; production deployment retained as vendor-reported operational context"
boundary = "Generic interaction-aware CPU scheduling; not Agent-specific or hardware-necessity evidence."
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-060"
locator = "OSDI 2026 Sections 4-7: scenario annotation, priority propagation, lab evaluation, overhead and production experience"
+++

# EC-C-006-A

## Inference
PAPER-060 → **SUPPORT** → CLM-MOBILE-002

## Warrant
The controlled commercial-phone evaluation demonstrates that compact interaction/dependency semantics can drive low-level scheduling actions with measurable end-to-end responsiveness benefit.

## Boundary
Large-scale production numbers are valuable operational context but remain vendor-reported in the current evidence set.
