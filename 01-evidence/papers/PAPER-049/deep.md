# PAPER-049 — Affinity Tailor: Dynamic Locality-Aware Scheduling at Scale

## Source
- Paper: https://arxiv.org/abs/2604.27915
- Authors: Jin Xin Ng, Ori Livneh, Richard O'Grady, Josh Don, Peng Ding, Samuel Grossman, Luis Otero, Chris Kennelly, David Lo, Carlos Villavieja
- Affiliation: Google
- Venue/status: arXiv preprint, 2026
- Target: production Linux multicore scheduling
- Project relevance: R2 strongest generic software locality baseline
- Priority: P0

## Q1 — Problem + target mapping
Linux work-conserving load balancing spreads workloads across cores, causing loss of cache, branch-predictor and prefetcher locality.

This maps directly to the non-Agent-specific part of R2.

## Q2 — Novelty / new-regime relevance
Affinity Tailor provides **soft affinity**:
- userspace estimates workload CPU demand;
- assigns topologically compact preferred cores;
- minimizes LLC-domain spread;
- kernel treats the set as an affinity hint rather than a hard partition;
- workload may burst outside the set when required.

The key idea is preserving locality without permanently stranding capacity.

## Q3 — Falsifiable hypothesis
Dynamic, permeable preferred-core regions should retain microarchitectural warmth while preserving work-conservation better than ordinary CFS load balancing or hard cpusets.

## Q4 — Research lineage / competing route
For R2 this is a strong generic competing route.

It shows that cache/branch/prefetcher locality can be captured with:
- demand prediction;
- topology;
- soft affinity;
- no Agent semantics;
- no new CPU microarchitecture.

## Q5 — Mechanism / control point
Inputs:
- online CPU demand;
- hardware topology / LLC domains;
- current placement.

Actuator:
- cgroup preferred-core soft affinity.

No Agent semantic contract is required.

## Q6 — Experiment
Deployed across thousands of Google machines.

Reported:
- geomean per-CPU throughput +12% on chiplet systems;
- +3% on non-chiplet systems over Linux CFS;
- per-GB throughput +3–7%.

## Q7 — Artifact / reproducibility
Public paper available.
Production deployment is strong operational evidence, but exact production workloads/infrastructure are not reproducible as a phone experiment.

## Q8 — Evidence vs hypothesis
**[FACT]** Generic locality-aware software scheduling can recover meaningful cache/branch/prefetcher value in production.

**[BOUNDARY]** Datacenter topology and scale differ substantially from smartphones.

## Q9 — Project contribution
Raises the R2 software-sufficiency baseline.

R2 cannot compare against default scheduler or hard pinning.
It must beat dynamic, soft, topology-aware affinity plus generic shared cache.

## Q10 — Next action
- KEEP as P0 R2 baseline/constraint evidence.
- Do not promote Agent-specific locality without phone PMU residual.
- Measure SoftwareLocalityCapture before any uArch design.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for generic datacenter locality scheduling; STRUCTURAL_SIGNAL for mobile transfer
- Decision impact: NARROW / DOWNGRADE R2
- Open questions: smartphone transfer; Agent-specific residual
- Primary source: https://arxiv.org/abs/2604.27915
