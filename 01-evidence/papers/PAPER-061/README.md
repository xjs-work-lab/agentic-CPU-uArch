+++
id = "PAPER-061"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "INDEPENDENT_ACADEMIC"
title = "Syrup: User-Defined Scheduling Across the Stack"
primary_url = "https://doi.org/10.1145/3477132.3483548"
priority = "P0"
evidence_role = "strong prior art for portable application-specific cross-layer scheduling policy and C/H-SCL baseline"
authors = ["Kostis Kaffes", "Jack Tigar Humphries", "David Mazières", "Christos Kozyrakis"]
venue = "ACM SOSP 2021"
+++

# PAPER-061 — Syrup: User-Defined Scheduling Across the Stack

## 30-second read
- **Why it matters:** Direct prior art for a portable, declarative interface that lets applications express workload-specific scheduling policies across multiple system layers.
- **What it establishes:** Matching-function policies can be deployed across thread scheduling, networking and programmable NIC hooks, exchange state through a Map abstraction, and outperform default/single-layer scheduling on evaluated server workloads.
- **Reported anchors:** up to 8× application-performance improvement in evaluated policy examples; cross-layer request+thread scheduling supports ~60% higher load than the best single-layer scheduling case at the paper's target tail-latency regime.
- **Portfolio meaning:** Broad 'portable cross-resource scheduling/control interface' is not H-SCL white space. C must treat cross-layer user-defined policy mechanisms as generic prior art.
- **Boundary:** Datacenter KVS/networking workloads, not smartphone/Agent workloads; does not establish Agent-specific semantic extraction or mobile SYSTEM_VALUE.
- **Primary source:** https://doi.org/10.1145/3477132.3483548

See [deep.md](deep.md) for the full Paper Insight 10Q.
