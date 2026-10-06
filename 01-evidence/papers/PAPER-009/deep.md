> V1 semantic source copied/repacked from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.
> Do not reinterpret this page as V2.2 metadata authority; the compact README owns the Source object.

# PAPER-009 — When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference

## Source
- Paper: https://arxiv.org/abs/2605.27435
- Authors: Pu Li, Jiawen Qi, Qinyu Chen
- Affiliation: Leiden University / LIACS
- Venue/status: arXiv preprint, 2026
- Target: Snapdragon 8 Gen 3 / Hexagon v75 / Android 15
- Project relevance: M1 / M2
- Priority: P0

## Q1 — What problem is the paper solving, and how does it map to smartphones?
The paper asks whether NPU offload is always beneficial for mobile LLM inference. It directly measures stage-level CPU/NPU trade-offs on a smartphone-class SoC.

## Q2 — Is the problem/new mechanism actually new?
Heterogeneous placement is old; the new evidence is that **mobile LLM stage granularity and invocation overhead can reverse the expected winner**.

Classification: Agentic-amplified / generic enabling.

## Q3 — What falsifiable hypothesis is being tested?
**Hypothesis:** optimal CPU/NPU placement depends on inference stage and operation granularity; maximal NPU offload can worsen latency/energy.

## Q4 — What is the research lineage / competing route?
Competes with “NPU-first” inference design and static offload policies. Complements CORE/PowerBench.

## Q5 — What is the key technical mechanism / control point?
Stage-aware heterogeneous placement based on:
- compute intensity;
- invocation overhead;
- communication;
- energy.

## Q6 — How is the experiment designed?
Direct mobile measurements on Snapdragon 8 Gen3/Hexagon v75.

Reported anchors:
- prefill: 6-core CPU 1.27–1.62× faster than tested NPU setup;
- decode: NPU 1.05–1.2× faster;
- communication can be ~9.9–13.0% of decode;
- lightweight op call overhead can be 8–22× actual op time;
- more NPU offload can consume up to 51% more energy in tested cases.

## Q7 — What data/artifact/reproducibility support exists?
Primary preprint public. Artifact availability not currently verified.

## Q8 — Do the results actually support the hypothesis?
Yes for evaluated models/stages/device.

Boundary: software/driver stack and NPU generation matter; results are not universal constants.

## Q9 — What is the real contribution / technology control point for us?
Important warning for M1:
> “Agent = send everything to NPU” is not a valid system strategy.

CPU can be the better executor for certain short/control stages, reinforcing the need to distinguish planner/model compute from lightweight executor/control work.

## Q10 — What should we do next?
- Keep as P0 heterogeneous-placement evidence.
- Use stage/invocation overhead in M1 reframe.
- Avoid assuming accelerator use is always optimal.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for evaluated mobile LLM stages
- Decision impact: KEEP M1 heterogeneous executor question
- Open questions: artifact; next-gen NPU transfer
- Primary source: paper above
