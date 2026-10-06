+++
id = "C"
type = "DIRECTION"
record_state = "CURRENT"
title = "Efficient System-Control Substrate"
direction_class = "STRATEGIC_ENABLER"
investment_lane = "STRATEGIC_ENABLER"
score_context = 72.0
evidence_maturity = "STRUCTURAL_SIGNAL"
maturity_scope = "direct smartphone generic control/QoE tax is established; EdgeAgent shows Agent-aware incremental value on Apple M4; target-phone Agent-specific residual beyond strong generic tuning remains unestablished"
strongest_baseline = "G1_GENERIC_OPTIMIZED"
related_claims = ["CLM-MOBILE-001", "CLM-MOBILE-002", "CLM-MOBILE-003", "CLM-AGENT-008", "CLM-C-001", "CLM-C-002", "CLM-C-003", "CLM-C-004", "CLM-C-005", "CLM-C-006", "CLM-C-007", "CLM-C-008", "CLM-C-EXP-001"]
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

PAPER-051 supplies pressure for this layer on Apple M4; target-phone transfer remains open.

PAPER-060 / CLM-MOBILE-002 further raises the bar: generic interaction semantics can already be converted into deployable scheduler-visible priority/dependency state on commercial phones.
PAPER-061 / CLM-C-006 additionally shows that portable application-defined policy and cross-layer scheduling coordination are mature prior-art patterns in server systems.
PAPER-062 / CLM-C-007 shows that automatic runtime criticality inference and heterogeneous CPU placement are also mature prior-art patterns.
PAPER-066 / CLM-AGENT-008 shows Agent workflow structure and per-request SLOs can already drive model/hardware/resource orchestration in a strong software control plane.
PAPER-067 / CLM-MOBILE-003 shows personalized background usefulness can already drive smartphone allow/suppress decisions.
PAPER-068 / CLM-C-008 shows graded task utility and low-value abort are foundational resource-scheduling concepts.

C only earns differentiated credit for a target-phone Agent-specific residual that is not reproduced by these generic and Agent-aware upper-layer controls.

## Current lane
Keep as **Strategic Enabler**.

**Second-Bet watch is closed on current evidence.**

The H-FIB pressure test did not reveal a distinct C-owned architectural/control pattern. Any surviving value signal is now an A→C transfer question: A must first prove Agent-specific semantic information beyond SLO/TUF/history/topology proxies; C can then test whether that information improves target-phone control.

The direct phone foreground-QoE evidence strengthens the problem, but the effectiveness of software-only SERENO-like control also raises the baseline.

Therefore:
**no Primary-Bet promotion from PAPER-003.**

## Promotion gate
EXP-C-001 must show:
- A1 vs G1 >=~5% meaningful end-outcome residual;
- >1 representative Agent workload regime;
- mechanism tied to Agent blocked/ready/concurrency/criticality;
- same benefit not reproduced in inference-only C0;
- target-phone transfer;
- distinct reusable control point.

## Hardware boundary
No uArch promotion unless:
1. target-phone C reaches SYSTEM_VALUE;
2. SERENO-like, MUSched-like, Syrup-like, WASH-like, HUSH-like, TUF/ReUA-like, Murakkab-class + other best software/runtime controls are exhausted;
3. a causal hardware-timescale/visibility/control residual remains.
