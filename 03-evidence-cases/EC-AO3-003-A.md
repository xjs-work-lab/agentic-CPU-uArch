+++
id = "EC-AO3-003-A"
type = "EVIDENCE_CASE"
record_state = "CURRENT"
relation = "SUPPORT"
target_kind = "CLAIM"
target_id = "CLM-AO3-003"
warrant = "MobiMem's validated replay, PBKV's predicted reuse, CacheScout's history-only prediction, PLACEMEM's typed state/provenance capsules and Invalidation Contracts' scoped invalidation show substantial value captured through software rather than an Agent-specific hardware memory invention."
scope = "strong software/runtime baseline for reuse, prediction and correctness"
boundary = "Comparisons span different workloads/platforms; no single system implements every feature and no phone cross-engine counterfactual is shown."
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-103"
locator = "replay checks against UI hierarchy, failure fallback and CPU-only Snapdragon action reuse"
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-028"
locator = "multi-step Agent-KV prediction and hierarchical eviction/prefetch, server GPU tests"
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-031"
locator = "online transition-count-based cache prediction on vLLM"
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-034"
locator = "semantic/provenance/version capsules with vLLM sidecar"
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-035"
locator = "version and dependency invalidation contract evaluation"
+++

# EC-AO3-003-A

## Inference and role
**SUPPORT** → CLM-AO3-003.

## Warrant
MobiMem's validated replay, PBKV's predicted reuse, CacheScout's history-only prediction, PLACEMEM's typed state/provenance capsules and Invalidation Contracts' scoped invalidation show substantial value captured through software rather than an Agent-specific hardware memory invention.

## Scope and counterweight
strong software/runtime baseline for reuse, prediction and correctness

## Boundary
Comparisons span different workloads/platforms; no single system implements every feature and no phone cross-engine counterfactual is shown.
