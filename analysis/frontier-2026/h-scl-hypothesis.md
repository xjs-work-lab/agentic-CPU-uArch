# H-SCL — Semantic Control Lowering

Status: **ANALYSIS HYPOTHESIS / NOT A DIRECTION**
Updated: 2026-10-06

## Why this hypothesis exists
The first frontier round showed several high-level Agent facts can affect system value:
- progress/criticality state;
- useful-by time;
- control/data-flow state;
- persistent variables and belief state;
- foreground QoE constraints;
- heterogeneous stage/operator characteristics.

But PAPER-053, PAPER-054, PAPER-003 and PAPER-056 also show large value can already be captured in application/runtime software.

Round 2 adds PAPER-058 AutoDroid-V2, which materially narrows the hypothesis further:
> generic semantic-to-program/code lowering is **not white space**.

## Killed broad formulation
Do **not** pursue H-SCL as:
> 'take rich Agent semantics and compile them into an executable plan/script.'

AutoDroid-V2 already demonstrates this pattern strongly at the application layer on evaluated smartphone GUI-Agent workloads.
AgentProg also demonstrates rich program/control/data-flow/belief-state ownership in the Agent runtime.

## Surviving formulation
Test only the narrower hypothesis:

> **A portable compiler/runtime boundary can lower rich, framework-specific Agent state into a small cross-framework set of reusable resource-control facts that existing generic OS/runtime/CPU/NPU mechanisms can consume, yielding incremental system value beyond both strong application-specific Agent runtimes and generic resource control.**

Candidate low-level facts are hypotheses, not a fixed ABI:
- critical-path / required-progress class;
- useful-by / latest-useful time;
- release / cancel / discard legality;
- foreground-impact budget;
- state-reuse / continuation identity;
- heterogeneous-stage placement constraints.

## What makes it potentially differentiated
The proposed value is **not** representing Agent semantics.
The proposed value would have to come from one or more of:
1. multiple Agent frameworks expose different rich state but need the same lower-level resource decision;
2. application-specific runtimes cannot observe or coordinate a shared resource at the required scope/timescale;
3. generic OS/runtime controls lack one compact fact that is expensive or impossible to reconstruct;
4. a reusable lowering layer avoids bespoke per-framework control logic while preserving measurable end outcome.

## Strongest baselines
H-SCL must beat at least:
- PAPER-058 AutoDroid-V2: task-level code/script lowering + app documentation + reusable static prefix;
- PAPER-056 AgentProg: program/control/data-flow + belief state;
- PAPER-054 TimelyLLM: useful-time/slack-aware serving;
- PAPER-003 Sereno: generic foreground-QoE-aware resource control;
- A B4-TX;
- C G1_GENERIC_OPTIMIZED.

## Kill criteria
Kill H-SCL as a separate Direction if any of the following holds:
- the useful facts are already fully reconstructible by strong Agent runtimes or generic schedulers;
- a common lowering loses too much semantic precision relative to bespoke runtime mechanisms;
- cross-framework common facts do not recur across representative Agent workloads;
- incremental end-outcome gain over B4-TX/G1 is <~5% under matched QoE/budget;
- the useful portion is already cleanly owned by A, C or PT-A and creates no distinct control point.

## Promotion criteria
Only consider a canonical Direction if evidence shows:
1. the same compact fact recurs across at least two materially different Agent frameworks/workload styles;
2. application-specific upper-layer baselines cannot capture the same value;
3. the fact maps to a reusable control surface in compiler/runtime/OS scope;
4. target-relevant SYSTEM_VALUE is plausible/testable;
5. the mechanism is distinct from A DemandState and generic C resource control.

## Next prior-art search
Search older/non-Agent vocabulary in ASPLOS/OSDI/SOSP/PLDI/CGO:
- application-informed / application-aware scheduling;
- task-graph criticality;
- deadline/slack propagation;
- workflow-aware resource management;
- compiler/runtime hints;
- QoS contract lowering;
- heterogeneous task runtime metadata;
- semantic information flow into schedulers.

The goal is to **kill or sharply delimit H-SCL**, not to validate it by keyword matching.
