# PAPER-062 — Portable Performance on Asymmetric Multicore Processors (WASH)

## Source
- ACM CGO 2016
- DOI: https://doi.org/10.1145/2854038.2854047
- Open PDF: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/06/paper-cameraready-1.pdf
- Authors: Ivan Jibaja, Ting Cao, Stephen M. Blackburn, Kathryn S. McKinley
- Implementation: high-performance Java VM / Jikes RVM research ecosystem
- Hardware: AMD Phenom II x86 with per-core DVFS configured as asymmetric big/small cores
- Priority: P0

## Q1 — Problem + target mapping

AMP systems need schedulers to reason about:
- which threads are on the critical path;
- which threads benefit from big cores;
- load balance;
- application/VM thread priorities;
- non-scalable messy parallelism.

Generic OS schedulers see threads and utilization but do not know managed-runtime semantics such as locks, VM helper roles, application priorities and parallelism class.

Project mapping:
This is direct prior art for the pattern:
> runtime-internal semantic/behavioral state → automatically inferred compact control facts → heterogeneous CPU placement.

It is not smartphone/Agent evidence.

## Q2 — Novelty / new-regime relevance

WASH's contribution is a runtime that automatically:
- classifies applications as sequential/scalable/non-scalable;
- identifies bottleneck threads holding contended locks;
- measures core sensitivity;
- respects thread priorities;
- adapts thread placement across big/small cores.

Prior critical-path schemes often relied on programmer hints or new hardware. WASH moves that inference into software/runtime analysis.

Classification: **generic runtime semantic/behavioral inference for heterogeneous scheduling**.

## Q3 — Falsifiable hypothesis

Core hypothesis:
> A managed runtime has enough semantic and dynamic execution information to automatically identify critical/bottleneck work and core sensitivity, and can use that information to outperform semantics-oblivious or narrower AMP schedulers.

Falsifiers:
- runtime cannot identify bottleneck threads robustly;
- lock waiting is a poor proxy for criticality;
- core-sensitivity prediction is inaccurate;
- affinity updates cost too much;
- OS interference destroys runtime decisions;
- workload classification is unstable.

Evaluated results support the hypothesis on the paper's Java benchmark/AMP setup.

## Q4 — Research lineage / competing route

Competing/prior routes include:
- oblivious Linux round-robin scheduling;
- proportional core-sensitive fair scheduling (PFS);
- bindVM: helper threads→small, application threads→big;
- programmer-hint critical-path acceleration;
- hardware-assisted critical-thread detection;
- IPC/performance-counter-based core-sensitivity predictors.

WASH's key difference is automatic runtime-level bottleneck identification plus joint criticality/core-sensitivity/load-balancing logic.

## Q5 — Key mechanism / control point

### Automatic workload classification
Runtime monitors scaling/progress to distinguish:
- sequential;
- scalable multithreaded;
- non-scalable multithreaded.

### Bottleneck/critical-thread inference
Runtime tracks contended locks and prioritizes threads by cumulative waiting time imposed on other threads.

### Core-sensitivity profiling
Runtime monitors how threads respond to big vs small cores and uses predictive/core-sensitivity information.

### Placement action
Runtime communicates decisions to OS via thread affinity and proportionally allocates big/small cores.

### Project interpretation
WASH shows that **automatic extraction** of useful resource-control facts from runtime semantics/behavior is already established prior art.

Therefore H-SCL cannot claim novelty merely for 'automatically derive criticality/placement hints from rich runtime state.'

## Q6 — Experiment design

Benchmarks:
- 14 DaCapo/Java workloads;
- sequential, scalable and messy non-scalable categories;
- multiprogrammed adversarial background workload tests.

Hardware:
- AMD Phenom II x86;
- per-core frequency scaling used to emulate asymmetric big/small core capability;
- real hardware, not cycle simulation.

Baselines:
- Linux oblivious scheduler;
- PFS;
- bindVM;
- prior core-sensitive approaches.

Headline results:
- ~20% average performance improvement;
- ≥9% average energy improvement;
- up to 27% performance benefit as asymmetry increases;
- ~15% average improvement on especially difficult messy non-scalable workloads in one reported comparison.

## Q7 — Data / artifact / reproducibility

Strengths:
- CGO peer review;
- detailed algorithm/evaluation;
- real hardware;
- established benchmark suite;
- Jikes RVM research archive availability noted by authors.

Limitations:
- AMP behavior is emulated through frequency-scaled homogeneous x86 cores rather than a production ARM big.LITTLE smartphone;
- Java managed-runtime semantics differ from Agent runtimes;
- no NPU/GPU/memory/thermal control;
- no smartphone QoE.

This project did not independently reproduce the implementation.

## Q8 — Evidence vs hypothesis

### [FACT]
Within the evaluated managed-runtime workloads, WASH automatically identifies bottleneck/critical threads and reports performance/energy improvements over the compared scheduling baselines.

### [OBSERVATION]
Runtime layers can infer useful scheduling facts from synchronization, progress and workload semantics that are not directly visible to a generic OS scheduler.

### [INFERENCE — project]
Automatic extraction of scheduling criticality/placement facts from rich upper-layer runtime state is mature prior art at the conceptual level.

### Not established
- Agent-specific fact extraction;
- smartphone transfer;
- CPU↔NPU placement;
- cross-resource Agent control;
- hardware/uArch need.

## Q9 — Real contribution to project decision

### H-SCL
**NARROW TO RESIDUAL / likely merge, not new Direction.**

WASH removes another possible novelty claim:
> automatic inference of criticality/placement hints from runtime semantics/behavior.

Combined with AutoDroid-V2, MUSched and Syrup, the surviving H-SCL white space is no longer an architectural pattern.
It is only a target-specific residual question:
> Is there an Agent-specific fact that strong runtimes/generic semantic schedulers cannot reconstruct, and that produces cross-resource smartphone SYSTEM_VALUE?

That question overlaps heavily with A (information value) and C (system-control residual).

### A
Conceptual baseline strengthening only.
A must assume runtime-derived criticality can be inferred automatically from rich execution state where mechanisms expose it.

### C
Generic control baseline strengthening only.
C cannot claim differentiated value for automatic critical-thread identification or heterogeneous core placement.

### R3
Remain BLOCKED. WASH obtains value without new hardware.

## Q10 — Next action

1. KEEP PAPER-062 as P0 prior art.
2. Use it as decision-grade evidence that automatic semantic/behavioral inference for resource scheduling is old prior art.
3. Do not create a separate H-SCL Direction from the current evidence.
4. Fold H-SCL's surviving questions into A/C unless a future Agent-specific cross-resource mechanism proves distinct.
5. Keep Interactive Context for Mobile OS Resource Management as a pending mobile-specific corroboration target; do not use it for decision until full text is available.

## Decision footer
- **New-regime relevance:** generic runtime/heterogeneous scheduling prior art
- **Evidence maturity:** SYSTEM_VALUE in evaluated managed-runtime AMP scope; STRUCTURAL_SIGNAL for mobile-Agent transfer
- **Decision impact:** further narrows H-SCL; strengthens A/C baseline
- **A impact:** no lane/score change
- **C impact:** no lane/score change
- **R3 impact:** remain BLOCKED
- **Open questions:** Agent-specific non-reconstructible facts, smartphone cross-resource value, production ARM transfer
- **Primary source:** https://doi.org/10.1145/2854038.2854047
