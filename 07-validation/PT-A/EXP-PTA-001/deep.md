> Exact V1 PT-A interface/baseline specification copied from frozen baseline.

# Stage 15 — PT-A Interface and Baseline Specification

Updated: 2026-10-04

## Objective

Define a stable 2027 platform contract for:

> **PT-A — Heterogeneous Verified Agent Actuation Runtime**

PT-A is a **Platform Track**, not a differentiated Primary Bet.

Its job is to give Agent runtimes a reliable, measurable execution substrate across heterogeneous phone action surfaces.

---

# 1. Architecture

```text
Planner / Agent runtime
       │
       ├─ action intent
       ├─ A semantic policy
       │
       ▼
PT-A Router
       │
       ├─ Capability Registry
       ├─ Effect / Retry metadata
       ├─ Backend cost/history
       ├─ Permission / precondition
       │
       ▼
Backend Adapters
 ┌────────┬────────┬──────────┬──────────────┬───────────┐
 │ API    │ CLI    │ MCP/tool │ Typed Exec   │ GUI Agent │
 └────────┴────────┴──────────┴──────────────┴───────────┘
       │
       ▼
Outcome / Verification Layer
       │
       ├─ success
       ├─ failed
       ├─ unknown
       ├─ state changed
       ├─ evidence
       └─ recovery permission
       │
       ▼
Agent runtime / A controller
```

---

# 2. Canonical ActionDescriptor

Required fields:

- `ActionID`
- `CapabilityID`
- `IntentClass`
- `BackendClass`
- `RequiredPermission`
- `Precondition`
- `ExpectedPostcondition`
- `EffectClass`
- `IdempotenceClass`
- `RetrySafety`
- `ExpectedLatencyClass`
- `ExpectedEnergyClass`
- `VerificationMethod`

Optional:
- model requirement;
- network requirement;
- foreground requirement;
- app/package target;
- data-sensitivity class;
- compensation action.

---

# 3. BackendClass

Initial enum:
- `SYSTEM_API`
- `APP_API`
- `CLI_COMMAND`
- `MCP_TOOL`
- `TYPED_EXECUTOR`
- `GUI_AGENT`
- `DIRECT_UI`
- `UNKNOWN`

Do not encode one universal preference order into the schema.

Routing policy is separate.

---

# 4. Effect contract

## EffectClass
- READ_ONLY
- REVERSIBLE
- IRREVERSIBLE
- UNKNOWN

## IdempotenceClass
- IDEMPOTENT
- NON_IDEMPOTENT
- CONDITIONAL
- UNKNOWN

## RetrySafety
- SAFE
- SAFE_WITH_VERIFICATION
- COMPENSATION_REQUIRED
- UNSAFE
- UNKNOWN

PT-A should expose these fields to A.

A may use them in Effect/Commit legality decisions.

---

# 5. OutcomeReceipt

Every backend invocation should return or be wrapped into:

- `ActionID`
- `AttemptID`
- `BackendClass`
- `StartTimestamp`
- `EndTimestamp`
- `OutcomeState`
- `StateChanged`
- `ObservedPostcondition`
- `VerificationConfidence`
- `EvidenceHandle`
- `PartialProgress`
- `RetryAllowed`
- `CompensationRequired`
- `FailureClass`

OutcomeState:
- SUCCESS
- FAILED
- PARTIAL
- UNKNOWN
- TIMEOUT
- CANCELED

A textual LLM statement such as “done” is not sufficient verification.

---

# 6. Verification classes

## V0 — backend return code
Weakest.

## V1 — structured API/tool result
Machine-readable direct result.

## V2 — state observation
Re-read target state after action.

## V3 — invariant/postcondition verification
Evaluate declared postcondition.

## V4 — external evidence
Receipt, message ID, system event, transaction/result handle.

Each ActionDescriptor should declare the minimum acceptable verification class.

---

# 7. Baseline routing policies

## P0 — GUI-only
Use GUI Agent / direct UI whenever possible.

Purpose:
legacy/control baseline.

## P1 — deterministic-first
Prefer structured API/CLI/MCP/typed executor when capability matches; otherwise GUI.

This is the primary strong static baseline.

## P2 — reliability-history routing
Route based on:
- capability match;
- recent success;
- historical latency;
- recovery frequency.

No privileged Agent semantics.

## P3 — cost-aware generic routing
Adds:
- current foreground state;
- load;
- energy/thermal;
- expected latency/cost.

No DemandState or effect/commit semantic priority beyond generic metadata.

## P4 — A-integrated semantic routing
PT-A receives A's derived legal/policy facts.

Examples:
- do not start optional irreversible action under pressure;
- prefer deterministic low-cost backend for speculative work;
- preserve required path even if more expensive;
- retry only when effect semantics permit.

P4 is not required to prove PT-A platform value.
It tests A+PT-A integration.

---

# 8. Verification / recovery baseline

Every policy variant must define:

### On SUCCESS
- verify at required verification class;
- publish receipt.

### On FAILED
- if RetrySafety=SAFE → retry within budget;
- if SAFE_WITH_VERIFICATION → verify state before retry;
- if COMPENSATION_REQUIRED → invoke compensation path or escalate;
- if UNSAFE/UNKNOWN → stop and replan/escalate.

### On UNKNOWN/TIMEOUT
Never blindly repeat irreversible actions.

First:
- verify state;
- recover outcome if possible;
- then decide retry/replan.

---

# 9. Metrics

## Reliability
- task success;
- action success;
- silent failure rate;
- false-success rate;
- duplicate-effect rate;
- unrecovered unknown-outcome rate.

## Efficiency
- action count;
- Agent/model calls;
- tokens;
- backend transitions;
- wall time;
- CPU time;
- NPU time;
- energy;
- network use.

## Recovery
- retry count;
- verification count;
- compensation count;
- recovery latency;
- successful recovery rate.

## Routing
- backend distribution;
- per-backend success;
- per-backend latency;
- per-capability preferred backend;
- routing regret against offline best-known backend.

---

# 10. Workload coverage

PT-A should cover:

### System/device operations
Best case for structured/deterministic paths.

### Tool-assisted workflows
Mixed MCP/API/CLI.

### Single-app GUI tasks
Likely GUI-heavy.

### Cross-app workflows
Mixed action surfaces.

### Irreversible/side-effect tasks
Messaging, calendar, upload, delete-like synthetic or safe-test actions.

### Asynchronous actions
launch, download, background completion, permissions.

---

# 11. Safety/correctness test patterns

Use non-destructive test doubles where possible.

Required classes:
- duplicate-submit prevention;
- timeout with unknown outcome;
- reversible failure;
- irreversible pre-commit abort;
- post-commit cancellation attempt;
- permission denied;
- app state drift;
- asynchronous delayed completion;
- backend unavailable;
- backend returns success but postcondition fails.

PT-A must distinguish:
`backend returned`
from
`desired effect verified`.

---

# 12. Integration seam with A

A supplies:
- DemandState;
- derived CancelPermission;
- derived ReleasePermission;
- effect/commit legality.

PT-A supplies:
- capability options;
- effect metadata;
- backend cost/history;
- outcome receipt;
- verification evidence.

Stable interaction:

```text
A: Should this work proceed now?
        ↓
PT-A: Which backend can execute it?
        ↓
PT-A: What actually happened?
        ↓
A: Continue / cancel / retry / replan?
```

This loop is more important than sharing raw framework semantics with lower layers.

---

# 13. Shared trace fields with A

Every actuation event should include:

- ActionID
- ContinuationID
- BackendClass
- PolicyID
- EffectClass
- CommitState
- Start/End
- OutcomeState
- VerificationClass
- VerificationResult
- RetryCount
- FailureClass
- CPU active interval
- NPU interval if applicable
- foreground state
- energy/thermal if available

This permits C control-path analysis later.

---

# 14. 2027 platform success criteria

PT-A is considered successful as a Platform Track if it delivers:

1. one common backend contract;
2. one common outcome receipt;
3. reproducible GUI/structured mixed-action benchmark;
4. lower silent-failure / false-success rate than GUI-only;
5. measurable model-call/step reduction for deterministic-capable tasks;
6. safe bounded recovery;
7. A integration path.

No novelty claim is required.

---

# 15. Primary-Bet promotion gate

PT-A should only become a differentiated Bet if a new control point emerges that:

- is not generic hybrid routing;
- is not ordinary verification/retry;
- is not generic transaction handling;
- gives >=~5% meaningful residual over ClawMobile/PhoneHarness/HybridCUA/UIAnchor-class strong baselines;
- is controllable by our stack.

Otherwise remain Platform Track.

---

# 16. Implementation sequence

### Sprint P0
ActionDescriptor + OutcomeReceipt schema.

### Sprint P1
Two deterministic adapters + one GUI adapter.

### Sprint P2
P0/P1/P2 routing baselines + verification.

### Sprint P3
Recovery/failure-injection suite.

### Sprint P4
A integration.

### Sprint P5
Phone measurement:
- success;
- steps;
- model calls;
- latency;
- energy;
- control-path trace.

No PT-A-specific hardware work is planned.
