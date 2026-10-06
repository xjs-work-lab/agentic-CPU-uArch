+++
id = "EXP-CG06-001"
type = "EXPERIMENT"
record_state = "CURRENT"
status = "READY"
title = "CG-06 strong-baseline CPU↔NPU crossover experiment"
direction_ids = ["CG-06"]
tests_claim_ids = ["CLM-CG06-EXP-001"]
input_source_ids = ["PAPER-009", "PAPER-052", "PAPER-057", "PAPER-059", "TOOL-012", "TOOL-013"]
evidence_target = "SYSTEM_VALUE"
+++

# EXP-CG06-001 — Strong-baseline CPU↔NPU crossover

## Decision question
Where, if anywhere, does CPU-resident execution beat a **strong optimized NPU-centric path** for latency-critical Agent-relevant AI stages after dispatch, communication, fallback, layout, precision, graph-specialization and state-reuse costs are counted?

## Required paths

### CPU-VECTOR
Best available CPU vector/SIMD implementation.

### CPU-MATRIX
Best available CPU matrix implementation using existing ISA/compiler/runtime capability.

### NPU-BASE
Conventional NPU execution with realistic launch/communication/fallback costs.

### NPU-OPT
Strongest feasible optimized NPU-centric path, including where applicable:
- prompt chunking/static-graph reconstruction;
- quantization-aware operator/sub-operator placement;
- sparse float residual CPU/GPU work;
- graph bucketing/specialization;
- out-of-order/cross-engine pipeline/fusion;
- minimized transfer and fallback.

### HETERO-OPT
Selective mixed CPU/NPU execution if neither monolithic path is strongest.

## Required accounting
- stage/operator/sub-operator shape;
- precision / accuracy constraint;
- dispatch and synchronization;
- layout/data movement;
- CPU/NPU resource occupancy;
- foreground QoE externality;
- energy / thermal;
- state reuse / cacheability;
- full Agent critical-path contribution, not kernel-only speed.

## Pass condition
A CPU-fast-path region only counts if it survives the NPU-OPT/HETERO-OPT baseline on meaningful end outcome, not merely against NPU-BASE.

## State
READY / WAITING-FOR-DATA.

## Boundary
Existing hardware + compiler/runtime paths first.
This is not a new-ISA experiment.
PAPER-059 and PAPER-057 strengthen the comparator; they do not pre-decide the winner.

The frozen V1 matrix remains preserved in deep.md.
