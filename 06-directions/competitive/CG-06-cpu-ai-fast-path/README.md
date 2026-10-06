+++
id = "CG-06"
type = "DIRECTION"
record_state = "CURRENT"
title = "CPU-Resident Latency-Critical Agent AI Fast Path"
direction_class = "COMPETITIVE_GAP"
competitive_action = "INVEST"
score_context = 86.5
evidence_maturity = "STRUCTURAL_SIGNAL"
maturity_scope = "direct phone evidence supports stage/operator/numerical-role dependent heterogeneous execution; representative Agent crossover and Huawei target-system value remain unproven"
related_claims = ["CLM-CPU-001", "CLM-CPU-002", "CLM-CPU-003", "CLM-CPU-004", "CLM-HUAWEI-001", "CLM-CG06-EXP-001"]
related_capabilities = ["CAP-ARM-C2-SME2-CPU-AI"]
+++

# CG-06 — CPU-Resident Latency-Critical Agent AI Fast Path

## 30-second decision
**INVEST / 86.5 / Adaptation + Differentiation**

Strategic control point:
**stage/operator/sub-operator placement + numerical precision role + dispatch/fallback/layout/state reuse across CPU and NPU paths.**

## Evidence synthesis
- `CLM-CPU-001`: CPU↔NPU winner is workload-stage/operator dependent in direct phone evidence.
- `CLM-CPU-002`: CPU matrix acceleration materially expands the CPU-local region under evaluated settings.
- `CLM-CPU-003`: Arm publicly productizes CPU+SME2 for responsive Agentic/local AI.
- `CLM-CPU-004`: strong NPU-centric co-design can reclaim CPU/GPU fallback work by splitting quantization-tolerant estimation from high-precision residual computation.
- `CLM-HUAWEI-001`: equivalent Huawei smartphone CPU matrix-AI fast path is not publicly established in the reviewed source set.

## Strongest baseline update
`PAPER-057 / ShadowNPU` changes the comparator.

CG-06 must **not** compare CPU paths only against a naive/full NPU offload.
A strong NPU baseline must include, where applicable:
- operator/sub-operator partition;
- mixed precision / quantization-aware placement;
- sparsity;
- static-graph bucketing / specialization;
- cross-engine pipelining;
- minimized CPU/GPU residual resource use.

Therefore ShadowNPU both:
- strengthens the heterogeneous-control-point thesis;
- **narrows the CPU-resident whitespace**.

## Boundary
- Strategic gap / adaptation route, **not global novelty**.
- Agent-specific value is not established by generic LLM/operator placement.
- No inference of Huawei internal absence.
- No new ISA/uArch conclusion.
- Exhaust existing compiler/runtime/ISA and optimized-NPU paths first.

## Next discriminating gate
`EXP-CG06-001` now asks whether a representative CPU-fast-path region remains after **both**:
1. all CPU-side matrix/layout/state optimizations;
2. a strong optimized NPU-centric baseline including ShadowNPU-like techniques where applicable.

## Portfolio state
No lane/score change from PAPER-057:
- INVEST;
- 86.5;
- STRUCTURAL_SIGNAL.
