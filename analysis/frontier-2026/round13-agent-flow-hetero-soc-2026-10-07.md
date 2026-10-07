# Frontier Round 13 — Agent-Flow Heterogeneous SoC Orchestration — 2026-10-07

## Question
Does Agent-native dynamic execution structure on real smartphone heterogeneous SoCs reopen differentiated C/CG-06 whitespace?

## FULL_10Q set
- PAPER-097 — Agent.xpu
- PAPER-098 — HeRo
- PAPER-099 — MobileExplorer
- PAPER-100 — Jev-Mobile

## Strongest positive evidence
HeRo is the material new fact.

On commercial Snapdragon phones, Agentic RAG creates:
- multiple heterogeneous model/stage types;
- stage–accelerator affinity;
- non-linear shape sensitivity;
- a partially observed/evolving workflow DAG;
- shared-memory-bandwidth contention across concurrent stages.

Its online scheduler reports material end-to-end improvements, including up to ~1.5× over a static multi-xPU mapping in the reported evaluation.

This closes C's prior target-phone Agent-aware SYSTEM_VALUE gap.

## Strongest negative / baseline pressure
The same family reduces differentiated whitespace.

Agent.xpu already shows:
- reactive/proactive flow priority;
- stage-elastic heterogeneous execution;
- fine-grained preemption;
- bandwidth-aware NPU/iGPU coordination.

HeRo adds:
- dynamic partial-DAG criticality;
- shape-aware partitioning;
- phone xPU affinity;
- bandwidth-aware concurrency.

These are software-visible control variables.

Therefore:
**SYSTEM_VALUE passes; SOFTWARE_INSUFFICIENCY does not.**

## GUI cross-check
### MobileExplorer
Reasoning latency can be used for speculative UI probes if rollback restores the main trajectory.

Decision:
- keep as PT-A speculative-effect/rollback workload;
- no new lane.

### Jev-Mobile
High-level VLM planning can run at lower cadence than typed local action selection.

Decision:
- add to A/PT-A strongest software baseline;
- do not use step-wise VLM as strongest baseline;
- no mobile hardware conclusion.

## Portfolio decision
| Lane | Round-13 result |
|---|---|
| A | baseline ↑; 82.5 unchanged |
| PT-A | workload evidence ↑; 80.0 unchanged |
| C | **evidence maturity → SYSTEM_VALUE**; 72.0 unchanged |
| CG-06 | strongest baseline ↑ / whitespace narrows; 86.5 unchanged |
| New Direction | none |
| Second Primary Bet | unfilled |
| uArch candidate | none |

## Mechanism-level conclusion
Round 13 confirms an important distinction:

> Agent workflow structure is valuable on real phones, but value of a software-visible signal is not the same as differentiated ownership of that signal.

The next promotion step for C or CG-06 would require a residual that survives Agent.xpu/HeRo-class dynamic orchestration and cannot be reconstructed from workflow/runtime/hardware profiling state.

## Next
Resume frontier reset outside already-covered dynamic scheduling/orchestration families.
