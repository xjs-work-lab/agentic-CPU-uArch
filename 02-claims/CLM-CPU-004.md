+++
id = "CLM-CPU-004"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "optimized mobile NPU-centric heterogeneous inference baseline"
supersedes = []
+++

# CLM-CPU-004

## Proposition
On evaluated commercial Snapdragon phones, strong NPU-centric system/algorithm co-design can reclaim substantial attention work that otherwise falls back to CPU/GPU by decomposing low-precision ranking/estimation from high-precision sparse residual computation, materially reducing latency/energy and CPU/GPU dependence while preserving near-full-attention task accuracy.

## Current interpretation
PAPER-057 / ShadowNPU demonstrates that:
- full NPU attention is not the only NPU baseline;
- operator sub-roles with different precision semantics can be split across NPU and CPU/GPU;
- static-graph bucketing and cross-engine pipelining materially change the mobile execution frontier.

This is a **strong optimized-NPU baseline** for CPU↔NPU crossover research.

## Boundary
It does not establish:
- universal NPU superiority;
- Agent-semantic-aware placement;
- Huawei transfer;
- elimination of CPU/GPU from decode;
- CPU/uArch insufficiency.
