+++
id = "EXP-CG01-001"
type = "EXPERIMENT"
record_state = "CURRENT"
status = "READY"
title = "CG-01 phone continuation-locality benchmark"
direction_ids = ["CG-01"]
tests_claim_ids = ["CLM-CG01-EXP-001"]
input_source_ids = ["VENDOR-001"]
evidence_target = "SYSTEM_VALUE"
+++

# EXP-CG01-001 — Phone continuation-locality benchmark

## Decision question
After strong software locality and generic shared/coherent cache baselines, is there still a material phone Agent continuation-locality residual that justifies Huawei-specific adaptation/differentiation?

## Required comparisons
1. default scheduling;
2. strong affinity/pooling/warm-core policy;
3. generic coherent/shared-cache baseline where observable;
4. candidate adaptation only if a residual remains.

## Measure
- core handoff / migration;
- L1/L2/LLC locality / MPKI where available;
- TLB/predictor warmup proxies where available;
- continuation latency;
- CPU burst cost;
- energy / thermal;
- foreground QoE.

## State
READY / WAITING-FOR-DATA.

## Boundary
No experiment was executed during migration.

This Experiment is the CG-01 benchmark gate, not an R2 promotion result.
