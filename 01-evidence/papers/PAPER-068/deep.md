# PAPER-068 — Energy-Efficient, Utility Accrual Scheduling under Resource Constraints for Mobile Embedded Systems (ReUA)

## Source
- ACM EMSOFT 2004
- DOI: https://doi.org/10.1145/1017753.1017768
- Open PDF: https://www.cs.york.ac.uk/rts/docs/EMSOFT-2004-2005/docs04/p64.pdf
- Extended TECS 2006: https://doi.org/10.1145/1165780.1165781
- Priority: P0 foundational prior art

## Q1 — Problem + target mapping
Classical deadlines are binary: finish before the deadline or fail.
But many soft real-time activities have **graded value as a function of completion time**.

ReUA asks how a mobile/embedded scheduler can:
- respect shared-resource dependencies;
- provide statistical timeliness guarantees;
- maximize accrued utility;
- improve system-level energy efficiency.

This directly challenges any broad H-FIB claim that exposing 'how valuable completion is under delay' to a resource manager is novel.

## Q2 — Novelty / new-regime relevance
ReUA builds on Time/Utility Functions (TUFs):
> utility to the system as a function of an activity's completion time.

A classical deadline is just a step-shaped TUF.

ReUA combines this utility model with:
- statistical cycle-demand estimation;
- shared-resource constraints;
- DVS;
- utility/energy ratio scheduling;
- infeasibility/low-value abort.

Classification: **foundational generic soft-real-time / mobile-embedded utility scheduling**.

## Q3 — Falsifiable hypothesis
If application value varies with completion time and workload demand is uncertain, a scheduler using utility curves plus demand statistics/resource constraints can make better value/energy decisions than deadline-only or utility-oblivious scheduling.

Falsifiers:
- utility curves are unavailable/wrong;
- overhead exceeds savings;
- resource dependencies dominate scheduling freedom;
- workload statistics are inaccurate;
- utility is not separable per task.

The paper analytically/simulated evaluates this model; it is not a modern product deployment.

## Q4 — Research lineage / competing route
Lineage includes:
- Jensen time/utility functions;
- utility-accrual real-time scheduling;
- EDF/deadline scheduling;
- DVS energy-aware scheduling;
- resource-constrained real-time scheduling.

Important project implication:
generic task value, deadlines, graded utility and low-utility abort have decades of prior art.

## Q5 — Key mechanism / control point
### TUF
Each task has an application-specific utility curve vs completion time.

### Utility accrual objective
Scheduler maximizes system-wide accrued utility rather than only deadline success.

### UER
Utility-and-energy ratio provides a combined ordering/efficiency criterion.

### Statistical demand allocation
Cycle demand is estimated from mean/variance to allocate enough execution for probabilistic timeliness bounds.

### DVS
Unused/slack cycles are exploited by adjusting CPU speed for system-level energy efficiency.

### Abort
Jobs deemed infeasible or with poor utility can be aborted rather than consuming resources with little expected value.

## Q6 — Experiment design
The paper provides analytical properties plus simulation experiments across:
- load levels;
- resource contention/dependencies;
- demand uncertainty;
- multiple scheduling baselines.

Reported qualitative result:
ReUA improves system-level energy efficiency while meeting statistical timeliness bounds when feasible, and prioritizes higher utility/energy work under overload.

This evidence is foundational/mechanistic, not directly comparable to smartphone Agent end outcomes.

## Q7 — Data / artifact / reproducibility
Strengths:
- peer-reviewed embedded-systems venue;
- explicit mathematical task/utility/resource model;
- analytical guarantees/properties;
- simulation comparisons;
- expanded later journal version.

Limitations:
- simulation-based;
- legacy CPU/DVS context;
- no smartphone app/Agent workload;
- utility functions are supplied by the application model rather than learned from rich Agent state;
- no NPU/memory-bandwidth/thermal interference.

## Q8 — Evidence vs hypothesis
### [FACT]
TUF/utility-accrual scheduling explicitly represents graded task value over time and can abort low/infeasible work under resource constraints.

### [OBSERVATION]
Resource scheduling based on application-specific utility/tolerance is mature prior art, including mobile-embedded energy-aware variants.

### [INFERENCE — project]
H-FIB cannot claim novelty for 'marginal-value curve', 'delay tolerance', 'utility budget' or 'abort low-value background task' in generic form.

### Not established
- automatic derivation of utility from Agent semantic progress;
- Agent RequiredProgress as a distinct information variable;
- target-phone QoE benefit;
- cross-resource mobile SoC control;
- hardware/uArch need.

## Q9 — Real contribution to project decision
### H-FIB
**Broad utility-budget concept killed as novelty.**

Surviving question is not whether a utility curve can guide scheduling.
It is:
> can Agent semantic state produce a **better, automatically derived dynamic utility function** than deadlines/TUFs/history/workflow/SLO proxies, and does that improve real smartphone end outcome?

### A
This actually strengthens A's conceptual importance: the novelty, if any, is the information source/RequiredProgress semantics, not utility-aware scheduling itself.

### C
Treat utility-aware scheduling as generic prior art. C receives no differentiated credit for the scheduler pattern alone.

## Q10 — Next action
1. KEEP as P0 foundational prior art.
2. Add canonical utility-scheduling Claim.
3. Add ReUA/TUF to H-FIB/C strongest baseline.
4. Reframe H-FIB into an A→C transfer question rather than a separate scheduler architecture.

## Decision footer
- **New-regime relevance:** generic foundational prior art
- **Evidence maturity:** STRUCTURAL_SIGNAL/SYSTEM_VALUE for modeled embedded real-time scheduling; not smartphone Agent SYSTEM_VALUE
- **Decision impact:** broad H-FIB utility-budget novelty killed
- **A impact:** clarifies differentiation lies in semantic information value
- **C impact:** generic utility-aware scheduler baseline
- **Open questions:** automatic Agent-derived utility, target-phone transfer, cross-resource control
- **Primary source:** https://doi.org/10.1145/1017753.1017768