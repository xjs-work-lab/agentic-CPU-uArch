+++
id = "CG-06"
type = "DIRECTION"
record_state = "CURRENT"
title = "CPU-Resident Latency-Critical Agent AI Fast Path"
direction_class = "COMPETITIVE_GAP"
competitive_action = "INVEST"
score_context = 86.5
evidence_maturity = "STRUCTURAL_SIGNAL"
maturity_scope = "direct phone evidence supports current-stack stage/operator/numerical-role dependent heterogeneous execution; representative Agent crossover, optimized target-phone NPU comparison and Huawei target-system value remain unproven"
related_claims = ["CLM-CPU-001", "CLM-CPU-002", "CLM-CPU-003", "CLM-CPU-004", "CLM-CPU-005", "CLM-HUAWEI-001", "CLM-CG06-EXP-001"]
related_capabilities = ["CAP-ARM-C2-SME2-CPU-AI"]
+++

# CG-06 — CPU-Resident Latency-Critical Agent AI Fast Path

## 30-second decision
**INVEST / 86.5 / Adaptation + Differentiation**

Strategic control point:
**stage/operator/sub-operator placement + numerical precision role + dispatch/fallback/layout/state reuse across CPU and NPU paths.**

## Evidence synthesis
- CLM-CPU-001: CPU↔NPU winner is workload-stage/operator/implementation dependent in direct phone evidence; PAPER-009 must not be read as an architecture-general “Prefill belongs on CPU” result.
- CLM-CPU-002: CPU matrix acceleration materially expands the CPU-local region under evaluated settings; PAPER-052 is a CPU/runtime result and does not establish phone CPU>NPU superiority.
- CLM-CPU-003: Arm publicly productizes CPU+SME2 for responsive Agentic/local AI.
- CLM-CPU-004: strong NPU-centric co-design can reclaim CPU/GPU fallback work through prompt/tensor/block and sub-operator numerical-role decomposition.
- CLM-HUAWEI-001: equivalent Huawei smartphone CPU matrix-AI fast path is not publicly established in the reviewed source set.

## Strongest baseline update
PAPER-059 / llm.npu (ASPLOS 2025) and PAPER-057 / ShadowNPU (MobiSys 2026) form a sustained optimized-NPU lineage.

llm.npu shows that prompt shape, quantization residuals and block scheduling are movable software boundaries.
ShadowNPU extends that trajectory into attention using low-precision NPU importance estimation plus sparse high-precision CPU/GPU residual work.

Because the two papers share an author/group lineage, they are used as **trajectory/mechanism evidence**, not counted as independent replications.

Round 13 raises the baseline again:
- PAPER-097 / Agent.xpu adds dynamic reactive/proactive flow scheduling, stage elasticity, preemption and bandwidth-aware NPU/iGPU coordination;
- PAPER-098 / HeRo transfers workflow-level orchestration to commercial Snapdragon phones with partial/evolving Agentic-RAG DAGs.

Agent.xpu and HeRo also share a PKU research lineage, so they establish a sustained mechanism trajectory rather than independent replication.

CG-06 must not compare CPU paths only against naive/full NPU offload.
A strong NPU baseline must include, where applicable:
- prompt/static-graph reconstruction;
- operator/sub-operator partition;
- mixed precision / quantization-aware placement;
- sparse residual CPU/GPU work;
- graph bucketing / specialization;
- persistent/batched dispatch and improved operator coverage;
- out-of-order or pipelined cross-engine execution;
- minimized CPU/GPU residual resource use;
- dynamic flow/stage criticality and partial-DAG scheduling;
- shape-aware sub-stage partitioning;
- stage–accelerator affinity;
- shared-memory-bandwidth-aware concurrency;
- reactive/proactive priority and fine-grained preemption where applicable.

This strengthens the heterogeneous-control-point thesis while **narrowing the CPU-resident whitespace**.

## Boundary
- Strategic gap / adaptation route, not global novelty.
- Agent-specific value is not established by generic LLM/operator placement.
- PAPER-009 crossover is current-stack evidence and may shrink as NPU software/operator coverage improves.
- PAPER-052 proves strong existing-ISA CPU optimization, not phone CPU>NPU superiority or need for new matrix ISA.
- No inference of Huawei internal absence.
- No new ISA/uArch conclusion.
- Exhaust existing compiler/runtime/ISA and optimized-NPU paths first.

## Next discriminating gate
EXP-CG06-001 asks whether a representative CPU-fast-path region remains after both:
1. all CPU-side matrix/layout/state optimizations, including SMEPilot-class placement/pipelining/layout reuse;
2. strong NPU-OPT/HETERO-OPT techniques including improved dispatch/operator coverage, llm.npu/ShadowNPU plus Agent.xpu/HeRo-class dynamic flow/stage orchestration where applicable.

## Portfolio state
No lane/score change:
- INVEST;
- 86.5;
- STRUCTURAL_SIGNAL.
