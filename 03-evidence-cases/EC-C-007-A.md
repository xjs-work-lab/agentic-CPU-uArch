+++
id = "EC-C-007-A"
type = "EVIDENCE_CASE"
record_state = "CURRENT"
relation = "SUPPORT"
target_kind = "CLAIM"
target_id = "CLM-C-006"
warrant = "Syrup directly evaluates a portable application-defined scheduling abstraction across kernel/thread/network/NIC hooks and shows cross-layer coordination outperforming single-layer scheduling in its evaluated KVS workloads."
scope = "PAPER-061 server/KVS/networking evaluation"
boundary = "Generic server cross-layer scheduling prior art; not smartphone/Agent SYSTEM_VALUE."
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-061"
locator = "SOSP 2021 design, Sections 5.2-5.5: policy expressiveness, cross-layer scheduling, hook portability and overhead"
+++

# EC-C-007-A

## Inference
PAPER-061 → **SUPPORT** → CLM-C-006

## Warrant
The evaluated framework demonstrates both portable policy expression and incremental benefit from coordinated multi-layer scheduling.

## Boundary
Transfer to smartphone Agent CPU/NPU/memory/thermal control remains unproven.
