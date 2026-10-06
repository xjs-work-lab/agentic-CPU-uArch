> Exact V1 Stage16A C matrix copied from frozen baseline.

# Stage 16A — C Agent Control-Path Experiment Matrix

Updated: 2026-10-05  
Lifecycle: CURRENT  
Stage: Stage16A Pass 3  
Canonical role: frozen control-path matrix for Candidate C

## Decision question

> After strong generic runtime/accelerator tuning, is there still a reusable >=~5% Agent-specific control-path residual?

The experiment must not credit generic RPC/NPU/backend problems to Candidate C.

---

## 1. Fixed phase taxonomy

Every measured control path uses:

1. planner
2. runtime_dispatch
3. serialization
4. rpc
5. accelerator_queue
6. accelerator_execute
7. sync
8. result_delivery
9. permission

Anything else:
`other`

No new phase name is added without updating the Stage16A schema.

---

## 2. Workload classes

### C0 — inference-only control
No Agent loop.

Purpose:
measure ordinary runtime/accelerator overhead.

### C1 — single Agent, no external tool stall
One Agent loop where all required local stages are immediately runnable.

Purpose:
measure orchestration overhead without tool blocking.

### C2 — single Agent, deterministic tool stalls
10 logical steps.
External/tool waits injected after logical steps:
- 3
- 7

Purpose:
create repeatable blocked→ready transitions.

### C3 — four concurrent Agents
Each Agent executes the C2 10-step pattern.

Purpose:
test slot/queue/control pressure and stall redistribution.

### C4 — real/public trace replay
Use only when an external artifact exposes enough timing/state to reproduce the path.

Purpose:
external-validity check.

Synthetic C2/C3 are harness tests, not product evidence.

---

## 3. Configuration ladder

### G0 — DEFAULT
Normal platform/runtime behavior.

### G1 — GENERIC_OPTIMIZED
Must use all feasible generic improvements before Candidate C is credited:
- persistent runtime/session;
- RPC/connection reuse;
- precompiled graphs;
- zero-copy/shared buffers where supported;
- asynchronous dispatch;
- batching/coalescing where appropriate;
- worker/thread reuse;
- affinity/topology tuning;
- avoidable serialization removal;
- avoidable fallback removal.

No Agent-native DemandState or effect/commit semantics.

### A1 — AGENT_AWARE_CONTROL
G1 plus Agent execution-state control such as:
- active / blocked / ready state;
- stall-aware suspend/yield;
- Agent-slot redistribution;
- per-Agent queue/control coordination.

To keep Candidate C distinct from A:
**A1 must not use DemandState / REQUIRED-OPTIONAL-SPECULATIVE as an input.**

If DemandState is added later, report it as a separate A×C experiment.

---

## 4. Timing / trace protocol

### Timing
Per workload/config:
- warmup: **10**
- measured: **30**
- if CV >3%: measured = **100**
- tracing disabled/minimal

### Phase trace
Per workload/config:
- warmup: **3**
- measured: **5**
- phase instrumentation enabled

Do not use traced E2E latency as the primary timing result unless trace overhead is shown negligible.

---

## 5. Required matrix

| Workload | G0 | G1 | A1 |
|---|---:|---:|---:|
| C0 inference-only | Required | Required | Not applicable |
| C1 single Agent / no stall | Required | Required | Required |
| C2 single Agent / stalls | Required | Required | Required |
| C3 four Agents / stalls | Required | Required | Required |
| C4 public/real trace replay | When available | When available | When available |

Minimum controlled matrix:
- C0: 2 configs
- C1–C3: 3 configs each
- **11 required workload/config cells**

---

## 6. Required outputs

### Per phase
- count;
- duration;
- share of E2E;
- backend;
- queue/wait where observable.

### Per run
- E2E latency;
- useful/required progress if meaningful;
- foreground QoE if a foreground workload is present;
- energy if available.

### Derived
```text
RawControlPathShare
GenericCapture
AgentAwareResidual
AgentSpecificFraction
```

Where possible:
```text
GenericCapture =
(G0_control - G1_control) / G0_control
```

Agent-aware end-outcome increment is evaluated:
```text
A1 vs G1
```
not A1 vs G0 alone.

---

## 7. Agent-specificity sanity gate

Candidate C should not be promoted solely because G1 is better than G0.

Evidence becomes meaningfully Agent-specific when:
- A1 beats G1 by >=~5% on an end outcome in representative Agent workloads;
- gain appears in more than one Agent workload regime;
- the mechanism is tied to Agent blocked/ready/concurrency state;
- C0 does not show the same benefit from the same “Agent-aware” mechanism.

This is a pre-device experimental gate, not yet a product claim.

---

## 8. Strong negative interpretations

### DOWNGRADE C if
- nearly all control-path gain is G0→G1;
- A1→G1 is consistently <~5%;
- the same benefit appears in inference-only C0;
- gain is caused mainly by avoidable backend fallback/serialization.

### Keep C as Enabler if
generic optimization is highly valuable but Agent-specific residual remains weak.

### Consider Primary-Bet promotion only if
- Agent-specific residual survives;
- smartphone/target-system transfer is demonstrated later;
- control point is reusable and independent enough from A/PT-A.

---

## 9. Canonical input

Normalized phase CSV:
```text
run_index,phase,start_us,duration_us,backend,...
```

Adapter:
`../analysis/stage16a/harness/control_phase_to_stage16a.py`

Run manifest:
`../prototype/contracts/stage16a_run_manifest.schema.json`
