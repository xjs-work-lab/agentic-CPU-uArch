+++
id = "CLM-CPU-005"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "INFERENCE"
status = "SUPPORTED"
scope = "dynamic Agent-flow/stage heterogeneous orchestration as CG-06 strongest baseline"
supersedes = []
+++

# CLM-CPU-005

## Proposition
For Agent workloads, CPU/NPU/GPU fast-path value must be evaluated after dynamic flow/stage-level heterogeneous orchestration, because static operator placement or single-model partitioning can leave substantial performance on the table when workflow dependencies, stage criticality and shared-memory contention evolve at runtime.

## Current interpretation
PAPER-097 Agent.xpu and PAPER-098 HeRo jointly raise the CG-06 strongest baseline from optimized per-model placement to **Agent-aware dynamic xPU orchestration**.

## Boundary
The two sources share research lineage and therefore establish a sustained mechanism trajectory rather than independent replication. They do not prove the CPU fast-path residual disappears.
