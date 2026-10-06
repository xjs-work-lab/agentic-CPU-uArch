# Frontier Round 2 Synthesis — 2026-10-06

## Decision question
After pressure-testing the first frontier synthesis with stronger software, mobile-scheduler and cross-layer prior art, does a credible second differentiated Primary Bet emerge?

## Decision-grade Sources reviewed
- PAPER-058 — AutoDroid-V2 (MobiSys 2025)
- PAPER-059 — Fast On-device LLM Inference with NPUs / llm.npu (ASPLOS 2025)
- PAPER-060 — MUSched (OSDI 2026)
- PAPER-061 — Syrup (SOSP 2021)

All four received full Paper Insight 10Q review before decision use.

## What this round kills or narrows

### 1. Generic semantic → executable-program lowering
**Crowded / not white space.**

AutoDroid-V2 shows that stable mobile-GUI Agent semantics can already be compiled into:
- app/task documentation;
- a task-level executable script;
- reusable static prefix/KV state;
- exception-triggered replanning.

Implication:
A/H-SCL cannot claim value simply because rich Agent semantics can be converted into executable control flow.

### 2. Generic semantic → mobile CPU scheduling
**Crowded / not white space.**

MUSched shows that mobile interaction-critical semantics can already be lowered into:
- bounded VIP classes;
- critical-thread annotations;
- Binder/lock dependency-priority propagation;
- user-space-updatable scheduling policy.

Implication:
A/C/H-SCL must beat a strong generic semantic-aware mobile scheduler.

### 3. Portable application-defined cross-layer control
**Crowded / not white space.**

Syrup demonstrates:
- compact application-defined scheduling policy;
- deployment across thread/network/NIC hooks;
- cross-layer shared control state;
- coordinated multi-layer scheduling.

Implication:
H-SCL cannot claim novelty for a portable user-defined cross-resource control API or policy substrate alone.

### 4. NPU limitations as fixed hardware boundaries
**Rejected as a default assumption.**

llm.npu + ShadowNPU show a sustained software trajectory:
- prompt/static-graph reconstruction;
- quantization/outlier decomposition;
- block/sub-operator scheduling;
- NPU↔CPU/GPU pipelining.

Implication:
CG-06 must beat a moving NPU-OPT/HETERO-OPT frontier.

## Surviving H-SCL hypothesis
H-SCL remains **analysis-only / not a Direction**.

Only the following narrow proposition survives:

> Can a compiler/runtime layer **automatically derive** a small cross-framework set of genuinely Agent-specific facts from rich Agent state, and can those facts provide incremental smartphone **cross-resource** value beyond application-specific Agent runtimes and strong generic controls?

The novelty cannot be:
- semantic-to-code lowering;
- semantic priority/class;
- user-defined cross-layer policy;
- generic heterogeneous placement.

A surviving control fact must be:
1. genuinely Agent-specific;
2. recurring across materially different Agent frameworks;
3. hard/expensive for generic software to reconstruct;
4. useful across CPU/NPU/memory/thermal or equivalent shared resources;
5. measurably valuable beyond B4-TX/G1 on target-relevant workloads.

## Portfolio impact
| Direction | Round-2 impact | State |
|---|---|---|
| A | B4-TX strengthened with task-level code lowering + generic semantic scheduling | PRIMARY_BET / 82.5 unchanged |
| C | G1 strengthened with MUSched-like semantic scheduling + Syrup-like cross-layer policy | STRATEGIC_ENABLER / 72 unchanged |
| CG-06 | NPU-OPT lineage strengthened by llm.npu → ShadowNPU | INVEST / 86.5 unchanged |
| R1 | no new promotion | CONDITIONAL_RESERVE unchanged |
| R3 | software-first evidence strengthened again | BLOCKED unchanged |

## Key negative evidence retained
- AutoDroid-V2 loses efficiency advantages when UI/task structure is too dynamic and requires regeneration.
- MUSched shows little benefit on already highly optimized games and can slightly worsen current/temperature.
- Syrup's cross-layer portability is server evidence; smartphone transfer is not automatic.
- llm.npu/ShadowNPU are lineage-overlapping, not independent replication.

## Next highest-risk prior art
**Interactive Context for Mobile OS Resource Management (IEEE TMC 2020)** is the next P0 candidate because its abstract indicates:
- application-transparent inference of user-interaction context;
- propagation through UI/syscall/IPC mechanisms;
- use for CPU scheduling and power control on smartphones.

It is **not decision-grade yet**. Full text + 10Q are required before it can alter H-SCL/A/C.

Secondary candidate:
- WASH / Portable Performance on Asymmetric Multicore Processors (CGO 2016), for automatic critical-thread inference from managed-runtime semantics.

## Current conclusion
**No second differentiated Primary Bet is justified.**

Round 2 reduces false whitespace further. The remaining research gap is increasingly specific:
> not whether semantic context can drive resource management, but whether there is a **genuinely Agent-specific, automatically derivable, cross-framework, cross-resource fact** with smartphone SYSTEM_VALUE beyond strong generic semantic controls.


## Round-2B — automatic semantic inference pressure test

### PAPER-062 — WASH (CGO 2016)
Full 10Q completed.

Decision-grade effect:
- automatic runtime extraction of critical/bottleneck work from synchronization/progress/runtime state is established prior art;
- heterogeneous big/small-core placement driven by those inferred facts is established prior art;
- no programmer hints or new hardware are required in the evaluated system.

### H-SCL convergence
**Do not promote H-SCL to a separate Direction.**

Its broad architectural components are already occupied:
- semantic→program lowering — AutoDroid-V2;
- semantic→mobile CPU scheduling — MUSched;
- portable application-defined cross-layer policy — Syrup;
- automatic runtime criticality inference — WASH.

The only surviving questions are folded into:
- **A** — does genuinely Agent-specific information retain measurable value beyond B4-TX?
- **C** — does that surviving information create target-phone cross-resource SYSTEM_VALUE beyond G1?

H-SCL may only be reopened as a separate Direction if later evidence reveals a distinct reusable mechanism not cleanly owned by A or C.

### Pending mobile corroboration
Interactive Context for Mobile OS Resource Management (IEEE TMC 2020) remains PENDING_FULLTEXT and is not decision-grade.
