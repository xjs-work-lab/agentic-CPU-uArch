+++
id = "AO-1"
type = "ARCHITECTURE_OPPORTUNITY"
record_state = "CURRENT"
title = "Agent Execution Fabric — heterogeneous CPU/GPU/NPU orchestration"
opportunity_stage = "DISCOVERY"
coverage_state = "EVIDENCE_MAPPED"
priority_rank = 1
research_question = "How should the mobile execution fabric change when Agent work repeatedly crosses orchestration, tool execution, model stages and heterogeneous engines?"
claim_links = [
  { claim_id = "CLM-AO1-001", role = "PROBLEM_SIGNAL" },
  { claim_id = "CLM-AO1-002", role = "PROBLEM_SIGNAL" },
  { claim_id = "CLM-AO1-004", role = "PRODUCT_SIGNAL" },
  { claim_id = "CLM-AO1-003", role = "STRONG_BASELINE" },
  { claim_id = "CLM-AO1-005", role = "PRIOR_ART_BOUNDARY" },
  { claim_id = "CLM-AO1-006", role = "OPEN_GAP" },
  { claim_id = "CLM-AO1-007", role = "ARCH_HYPOTHESIS" }
]
related_trends = ["T2", "T5"]
related_directions = ["C", "CG-06", "R2", "CG-01"]
related_capabilities = ["CAP-ARM-C2-SME2-CPU-AI", "CAP-QUALCOMM-ORYON-FLEX-CACHE"]
related_actors = ["ACT-ARM", "ACT-QUALCOMM"]
+++

# AO-1 — Agent Execution Fabric

## Current judgment
**KEEP / HIGH-PRIORITY CO-DESIGN OPPORTUNITY — EVIDENCE_MAPPED.**

The opportunity is not "CPU beats NPU."

The evidence supports a broader shift: Agent execution increasingly behaves as a long-lived, mixed-criticality, stateful workflow that repeatedly crosses CPU-side orchestration/tools and heterogeneous AI engines.

## Evidence skeleton

### Problem Signal
CLM-AO1-001:
reactive + proactive personal-Agent flows create different latency/throughput priorities and dynamic prefill/decode interleavings.

Primary anchor: PAPER-113 / Agent.xpu — FULL_10Q.

CLM-AO1-002:
tool/orchestration CPU work, accelerator inference, state residency and phase handoff can jointly determine the critical path.

Primary anchors:
- PAPER-114 / MARS — FULL_10Q;
- PAPER-115 / CPU-Centric Agentic AI — FULL_10Q;
- PAPER-008 — prior FULL_10Q corroboration.

### Product Signal
CLM-AO1-004:
Arm, MediaTek and Qualcomm publicly frame Agentic mobile compute at subsystem/fabric level: CPU orchestration, heterogeneous accelerators, shared/coherent memory/cache, larger local state and specialized domains.

Key sources:
- VENDOR-017;
- VENDOR-019;
- VENDOR-001;
- VENDOR-023.

Boundary: vendor product disclosures are strong direction signals; vendor performance numbers are not independent proof.

### Strongest Baseline
CLM-AO1-003:
software/runtime already captures a large fraction of the problem through:
- flow-aware accelerator binding;
- stage elasticity;
- fine-grained preemption;
- admission control;
- CPU/KV pressure coordination;
- priority-aligned state retention;
- role-aware CPU pools;
- dynamic soft affinity.

Primary anchors: PAPER-113 / 114 / 115 / 008 / 049.

### Prior-Art Boundary
CLM-AO1-005:
generic heterogeneous placement, cache-aware migration and planner/workflow-to-resource scheduling are crowded.

Direct-claim anchors:
- PATENT-024;
- PATENT-030.

Therefore "Agent-aware scheduler" is not enough to constitute a differentiated architecture Bet.

### Open Gap
CLM-AO1-006:
after software capture and broad prior art, the coherent residual is the execution-fabric boundary itself:
- cross-xPU command / synchronization / dispatch overhead;
- shared-memory and bandwidth contention between stages;
- persistent context/state residency across short Agent phase transitions;
- low-cost mixed-criticality preemption/cancellation;
- timely visibility of stage/priority/state to the execution fabric.

This is a credible public-evidence opportunity, not yet a proven hardware bottleneck.

### Architecture Hypothesis
CLM-AO1-007 remains OPEN.

Candidate mechanisms include:
- lower-latency xPU command/synchronization paths;
- persistent execution contexts;
- flexible shared/coherent state residency;
- cheaper accelerator preemption/cancellation;
- lightweight cross-layer stage/priority/state metadata.

These are hypotheses, not proposed silicon features.

## Important negative evidence
AO-1 is explicitly narrowed by:
- Agent.xpu using an AI-PC rather than smartphone platform;
- PAPER-009 showing current CPU-NPU crossover partly depends on backend/operator maturity;
- MARS/Agora/Affinity Tailor showing large software-capturable value;
- generic scheduling/cache-aware prior art.

## Round 15A conclusion
AO-1 has enough evidence to remain a high-priority Architecture Opportunity.

It does not yet justify a new ISA, new cache architecture, new accelerator queue primitive or hardware metadata protocol.

## Remaining gaps
1. more direct smartphone evidence covering full Agent pipelines, not only LLM stages;
2. public documentation of CPU-NPU/GPU queue, memory, coherence and preemption costs on modern mobile SoCs;
3. sustained academic lineage around heterogeneous Agent execution;
4. multi-vendor convergence on shared-state/execution-fabric mechanisms;
5. explicit comparison between software-visible state and lower-layer state that software cannot cheaply reconstruct.
