+++
id = "EC-CAL-003-C"
type = "EVIDENCE_CASE"
record_state = "CURRENT"
relation = "SUPPORT"
target_kind = "CLAIM"
target_id = "CLM-CAL-003"
warrant = "MeSP reduces LoRA activation memory with explicit structured recomputation while preserving exact gradients, showing that training-memory pressure is substantially software-reducible."
scope = "PAPER-093 ACL 2026 Industry"
boundary = "Memory baseline, not phone-wide energy or Agent-runtime evidence."
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-093"
locator = "structured backward pass, 49% average memory reduction, exact gradients"
+++

# EC-CAL-003-C

PAPER-093 → **SUPPORT** → CLM-CAL-003.

Boundary: software memory baseline; not a full-phone Agent evaluation.
