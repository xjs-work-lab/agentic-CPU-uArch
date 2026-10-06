+++
id = "PAPER-062"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "INDEPENDENT_ACADEMIC"
title = "Portable Performance on Asymmetric Multicore Processors"
primary_url = "https://doi.org/10.1145/2854038.2854047"
priority = "P0"
evidence_role = "prior art for automatic runtime critical-thread inference and semantic-aware placement on asymmetric big/small cores; H-SCL/A baseline pressure"
authors = ["Ivan Jibaja", "Ting Cao", "Stephen M. Blackburn", "Kathryn S. McKinley"]
venue = "ACM CGO 2016"
+++

# PAPER-062 — WASH

## 30-second read
- **Why it matters:** Demonstrates that a managed runtime can automatically infer critical-thread/resource-placement facts unavailable to a generic OS/hardware scheduler and use them to place work on asymmetric big/small cores.
- **What it establishes:** Runtime-visible locks, priorities, parallelism, thread progress and core sensitivity can be analyzed dynamically to identify bottlenecks and guide heterogeneous CPU scheduling without programmer hints or new hardware.
- **Reported anchors:** ~20% average performance improvement and ≥9% energy improvement over prior approaches across evaluated AMP configurations; up to 27% performance advantage as asymmetry grows.
- **Portfolio meaning:** Strong old prior art against claiming novelty for automatic semantic/behavioral fact extraction followed by heterogeneous CPU placement.
- **Boundary:** Java/server-style managed workloads on frequency-scaled x86 AMP hardware, not smartphones/Agents and not CPU↔NPU cross-resource control.
- **Primary source:** https://doi.org/10.1145/2854038.2854047

See [deep.md](deep.md) for the full Paper Insight 10Q.
