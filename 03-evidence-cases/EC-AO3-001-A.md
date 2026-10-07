+++
id = "EC-AO3-001-A"
type = "EVIDENCE_CASE"
record_state = "CURRENT"
relation = "SUPPORT"
target_kind = "CLAIM"
target_id = "CLM-AO3-001"
warrant = "MobiMem demonstrates persistent mobile Agent profile/experience/action memory and replay; LOCAL demonstrates reusable KV/context bound to adapter/version state in one multi-Agent runtime. These establish multiple persistent state classes, not one homogeneous physical object."
scope = "long-lived, reusable Agent state classes"
boundary = "MobiMem's direct Snapdragon test uses CPU-only inference; LOCAL evaluates one 24GB discrete GPU, not a phone. Their results are not pooled into one device metric."
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-103"
locator = "Section 4 memory types; Sections 5-6 replay, 454 action-reuse tasks and Snapdragon experiment"
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-104"
locator = "versioned KV identity, cross-Agent pre-prefill and staged adapter publication; evaluation of one 24 GB GPU"
+++

# EC-AO3-001-A

## Inference and role
**SUPPORT** → CLM-AO3-001.

## Warrant
MobiMem demonstrates persistent mobile Agent profile/experience/action memory and replay; LOCAL demonstrates reusable KV/context bound to adapter/version state in one multi-Agent runtime. These establish multiple persistent state classes, not one homogeneous physical object.

## Scope and counterweight
long-lived, reusable Agent state classes

## Boundary
MobiMem's direct Snapdragon test uses CPU-only inference; LOCAL evaluates one 24GB discrete GPU, not a phone. Their results are not pooled into one device metric.
