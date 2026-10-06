# PAPER-008 — Architectural Implications of Agentic AI Workflows

## Source
- Paper: https://arxiv.org/html/2608.04458
- Authors: Jirong Yang, Peizhe Liu, Chaojie Zhang, Jovan Stojkovic
- Affiliations: UT Austin + Microsoft Azure context
- Venue/status: arXiv preprint, 2026
- Project relevance: M1 / M3
- Priority: P0

## Q1 — What problem is the paper solving, and how does it map to smartphones?
The paper characterizes CPU/system behavior of Agentic workflows whose execution is fragmented across orchestrators, runners, tools and accelerators.

It is not a smartphone paper, but directly investigates Agentic CPU architecture implications.

## Q2 — Is the problem/new mechanism actually new?
Agent workflows create a structurally new mix of:
- low average host load;
- sudden CPU bursts;
- role-specific code paths;
- higher context-switch activity;
- cache/branch locality degradation with concurrency.

Classification: **Agentic-native evidence, indirect mobile transfer**.

## Q3 — What falsifiable hypothesis is being tested?
**Hypothesis:** Agentic workflow structure creates CPU execution signatures sufficiently different from conventional inference/service workloads to justify role/affinity/state-aware architecture/system treatment.

## Q4 — What is the research lineage / competing route?
Builds on cloud microservice/serving CPU characterization, role-aware pools, cache affinity and heterogeneous scheduling.

Competing explanation: ordinary RPC/microservice fragmentation may explain most behavior.

## Q5 — What is the key technical mechanism / control point?
The paper proposes/analyses role pools, affinity, GPU-state preparation and control-path specialization around Agent roles.

## Q6 — How is the experiment designed?
Server/datacenter Agent workflows; measures host utilization, burstiness, context switching, cache/branch behavior and scaling with Agent concurrency.

## Q7 — What data/artifact/reproducibility support exists?
Primary preprint public. Public artifact/venue status remains to be verified.

## Q8 — Do the results actually support the hypothesis?

Quantitative anchors from the controlled/server study include:
- IPC around 1.2–1.6;
- backend stalls around 43–47% for several frameworks;
- L1-data MPKI around 14–20;
- SWE-Agent involuntary context switches rising from roughly 71/s to 660/s as concurrency increases 1→32.

The paper also reports that role-aware pooling/pinning can reduce tool CPU demand by up to ~46%.


They support Agent-specific server CPU signatures.

**Boundary:** magnitude and mechanism cannot be transferred directly to phones. This is precisely why our Mobile Transfer Test and Stage 12 exist.

## Q9 — What is the real contribution / technology control point for us?
It is the strongest source for the hypothesis that the CPU becomes an **Agent control/executor substrate** rather than only fallback compute.

It motivates M1/M3 but cannot justify mobile uArch by itself.

## Q10 — What should we do next?
- Keep as P0 architecture hypothesis source.
- Use its signatures as a checklist for device-free/mobile measurements.
- Require phone evidence before promoting to UARCH_CANDIDATE.

## Decision footer
- Evidence maturity: STRUCTURAL_SIGNAL
- Decision impact: KEEP M1/M3 hypotheses
- Open questions: phone transfer; artifact/venue
- Primary source: paper above
