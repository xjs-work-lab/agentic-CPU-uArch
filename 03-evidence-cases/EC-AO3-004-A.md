+++
id = "EC-AO3-004-A"
type = "EVIDENCE_CASE"
record_state = "CURRENT"
relation = "SUPPORT"
target_kind = "CLAIM"
target_id = "CLM-AO3-004"
warrant = "Qualcomm explicitly links Oryon Flex Cache's dynamically shared CPU-core cache to multi-step Agent handoffs, while its Hexagon Agentic NPU disclosure reports expanded NPU-local shared memory for longer context/concurrent models."
scope = "official mobile CPU and NPU product-architecture signals"
boundary = "These are vendor product disclosures: Flex Cache is among CPU cores, whereas Hexagon shared memory is NPU-local. No unified CPU/NPU coherent Agent fabric is disclosed."
[[premises]]
ref_kind = "SOURCE"
ref_id = "VENDOR-001"
locator = "Oryon Flex Cache official Aug 25 2026 article: heterogeneous CPU cores share workload-adaptive cache pool"
[[premises]]
ref_kind = "SOURCE"
ref_id = "VENDOR-023"
locator = "Hexagon official Sep 10 2026 article: 50% larger NPU shared memory and Agentic execution"
+++

# EC-AO3-004-A

## Inference and role
**SUPPORT** → CLM-AO3-004.

## Warrant
Qualcomm explicitly links Oryon Flex Cache's dynamically shared CPU-core cache to multi-step Agent handoffs, while its Hexagon Agentic NPU disclosure reports expanded NPU-local shared memory for longer context/concurrent models.

## Scope and counterweight
official mobile CPU and NPU product-architecture signals

## Boundary
These are vendor product disclosures: Flex Cache is among CPU cores, whereas Hexagon shared memory is NPU-local. No unified CPU/NPU coherent Agent fabric is disclosed.
