+++
id = "CLM-C-003"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "SOURCE_CLAIM"
status = "SUPPORTED"
scope = "Huawei public generic control capability"
supersedes = []
+++

# CLM-C-003

## Proposition
Huawei publicly exposes generic task/thread QoS, resource-management and on-device inference-control primitives relevant to C's lower system-control baseline.

## Current interpretation
VENDOR-006 documents the public Kernel Enhance/Gewu control surface used as the existing Huawei baseline.

## Boundary
Official public capability claim; it does not establish Agent-native semantic propagation.

## Migration
- V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- Transform: `STRUCTURAL_REPACK`
