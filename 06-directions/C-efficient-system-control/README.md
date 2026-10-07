+++
id = "C"
type = "DIRECTION"
record_state = "CURRENT"
title = "Efficient System-Control Substrate"
direction_class = "STRATEGIC_ENABLER"
investment_lane = "STRATEGIC_ENABLER"
score_context = 72.0
evidence_maturity = "SYSTEM_VALUE"
maturity_scope = "direct commercial-phone Agent-aware heterogeneous orchestration SYSTEM_VALUE is established by HeRo; differentiated residual beyond strongest generic/Agent-aware software orchestration and Huawei target transfer remain unestablished"
strongest_baseline = "G2_AGENT_AWARE_HETERO_ORCHESTRATION"
related_claims = ["CLM-MOBILE-001", "CLM-MOBILE-002", "CLM-MOBILE-003", "CLM-AGENT-008", "CLM-C-001", "CLM-C-002", "CLM-C-003", "CLM-C-004", "CLM-C-005", "CLM-C-006", "CLM-C-007", "CLM-C-008", "CLM-C-009", "CLM-C-EXP-001"]
related_capabilities = ["CAP-HUAWEI-GENERIC-RESOURCE-CONTROL"]
+++

# C — Efficient System-Control Substrate

## 30-second decision
**STRATEGIC_ENABLER / 72.0**

C is the runtime/OS/system-control seam around Agent execution and heterogeneous accelerators.

## Three-layer evidence model

### 1. Generic control / QoE tax
Real smartphone evidence establishes two distinct generic costs:
- CPU↔NPU communication/scheduling/fallback overhead can materially change execution economics;
- background NPU LLM inference can severely harm foreground QoE through shared-memory-bandwidth contention.

PAPER-003 / CLM-MOBILE-001 is direct commercial-phone evidence for the second problem.

### 2. Generic capture — G1
Strong runtime/system mechanisms must be applied before C receives differentiated credit:
- persistent sessions / RPC reuse;
- zero-copy/shared buffers;
- async dispatch / batching;
- affinity/topology;
- serialization/fallback removal;
- foreground-QoE-aware contention sensing;
- fine-grained inference yielding/preemption;
- elastic verification/batching;
- throughput guardrails;
- existing Huawei public generic QoS/resource/inference-control primitives;
- interaction-critical scenario annotation, bounded semantic scheduling classes and IPC/lock dependency-priority propagation (MUSched-like control);
- portable application-defined cross-layer scheduling/control policies and shared control state across system layers (Syrup-like control);
- automatic runtime inference of critical/bottleneck work and heterogeneous big/small-core placement (WASH-like control);
- personalized background-work usefulness/suppression based on app/user history (HUSH-like control);
- explicit time/utility-function and utility-aware low-value work suppression/abort (TUF/ReUA-like control).

SERENO-like control, MUSched-like semantic-aware CPU scheduling, Syrup-like portable cross-layer policy, HUSH-like background usefulness suppression, and TUF/ReUA-like utility-aware scheduling are explicitly strongest-baseline mechanisms, not differentiated C value.

### 3. Agent-aware residual
Only incremental value tied to Agent blocked/ready/concurrency/criticality state beyond G1 counts toward differentiated C value.

PAPER-051 supplies pressure for this layer on Apple M4.

PAPER-097 / Agent.xpu then shows that reactive/proactive Agent flows can drive large software-only gains through stage-elastic NPU/iGPU coordination, bandwidth-aware dispatch and fine-grained preemption on a commodity shared-memory hetero-SoC.

PAPER-098 / HeRo closes the **target-phone transfer gap**: on commercial Snapdragon phones, dynamic Agentic-RAG workflow state, stage–PU affinity, shape sensitivity and shared-memory contention support material online scheduling value.

Therefore C now reaches **SYSTEM_VALUE**, but this is an evidence-maturity upgrade rather than differentiated-lane promotion.

PAPER-060 / CLM-MOBILE-002 further raises the bar: generic interaction semantics can already be converted into deployable scheduler-visible priority/dependency state on commercial phones.
PAPER-061 / CLM-C-006 additionally shows that portable application-defined policy and cross-layer scheduling coordination are mature prior-art patterns in server systems.
PAPER-062 / CLM-C-007 shows that automatic runtime criticality inference and heterogeneous CPU placement are also mature prior-art patterns.
PAPER-066 / CLM-AGENT-008 shows Agent workflow structure and per-request SLOs can already drive model/hardware/resource orchestration in a strong software control plane.
PAPER-067 / CLM-MOBILE-003 shows personalized background usefulness can already drive smartphone allow/suppress decisions.
PAPER-068 / CLM-C-008 shows graded task utility and low-value abort are foundational resource-scheduling concepts.

### G2 — Agent-aware heterogeneous orchestration baseline
The strongest baseline now also includes:
- Agent.xpu-class reactive/proactive flow priority and preemption;
- prefill/decode stage elasticity;
- dynamic xPU binding under accelerator affinity;
- partial/evolving workflow-DAG criticality;
- shape-aware sub-stage partitioning;
- shared-memory-bandwidth-aware concurrency control;
- HeRo-class online stage-to-CPU/GPU/NPU mapping.

C only earns differentiated credit for a target-phone Agent-specific residual **beyond G2** that is not reproduced by these generic and Agent-aware software controls.

## Current lane
Keep as **Strategic Enabler**.

**Second-Bet watch is closed on current evidence.**

The H-FIB pressure test did not reveal a distinct C-owned architectural/control pattern. Any surviving value signal is now an A→C transfer question: A must first prove Agent-specific semantic information beyond SLO/TUF/history/topology proxies; C can then test whether that information improves target-phone control.

The direct phone foreground-QoE evidence strengthens the problem, but the effectiveness of software-only SERENO-like control also raises the baseline.

Therefore:
**no Primary-Bet promotion from PAPER-003.**

## Promotion gate
EXP-C-001 must show:
- A1 vs G2 >=~5% meaningful end-outcome residual;
- >1 representative Agent workload regime;
- mechanism tied to Agent blocked/ready/concurrency/criticality;
- same benefit not reproduced in inference-only C0;
- target-phone transfer;
- distinct reusable control point.

## Hardware boundary
No uArch promotion unless:
1. target-phone C reaches SYSTEM_VALUE;
2. SERENO-like, MUSched-like, Syrup-like, WASH-like, HUSH-like, TUF/ReUA-like, Murakkab-class, Agent.xpu-class and HeRo-class controls are exhausted;
3. a causal hardware-timescale/visibility/control residual remains.
