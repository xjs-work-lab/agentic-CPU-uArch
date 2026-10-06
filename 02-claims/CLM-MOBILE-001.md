+++
id = "CLM-MOBILE-001"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "smartphone foreground/background QoE baseline"
supersedes = []
+++

# CLM-MOBILE-001

## Proposition
Strong generic foreground-protection mechanisms can capture a large portion of foreground-interference value in mobile background-AI concurrency.

## Current interpretation
SERENO directly shows severe mobile LLM interference and large recovery from generic/shared-resource control, making generic protection part of the strong baseline for A.

## Boundary
Not a full Agent workload and does not prove DemandState has no incremental value.

## Migration
- V1 baseline: `960abb4ef50a8f5b0bd357c067f08346025d`
- Transform: `STRUCTURAL_REPACK`
