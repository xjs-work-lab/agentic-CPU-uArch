+++
id = "EC-A-007-A"
type = "EVIDENCE_CASE"
record_state = "CURRENT"
relation = "SUPPORT"
target_kind = "CLAIM"
target_id = "CLM-AGENT-007"
warrant = "KVFlow directly uses Agent Step Graph topology and steps-to-execution to predict future KV reuse, guide fine-grained eviction and prefetch, and improve serving performance over strong prefix-cache baselines."
scope = "PAPER-065 NeurIPS 2025 server-GPU multi-Agent workflows"
boundary = "Agent-workflow software evidence; not mobile or CPU/uArch cache evidence."
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-065"
locator = "Agent Step Graph, STE propagation, cache eviction/prefetch and evaluation"
+++

# EC-A-007-A

## Inference
PAPER-065 → **SUPPORT** → CLM-AGENT-007

## Boundary
Supports reconstructible workflow-derived reuse distance, not a claim that all RequiredProgress/DemandState semantics are reconstructible.