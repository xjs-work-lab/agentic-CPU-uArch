+++
id = "PAPER-049"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "R2_STRONG_GENERIC_SOFTWARE_LOCALITY_BASELINE"
independence_assessment = "GOOGLE_PRODUCTION_FLEET_DEPLOYMENT"
title = "Affinity Tailor: Dynamic Locality-Aware Scheduling at Scale"
primary_url = "https://arxiv.org/abs/2604.27915"
priority = "P0"
evidence_role = "strong generic software locality baseline using soft preferred cores"
authors = ["Jin Xin Ng", "Ori Livneh", "Richard O'Grady", "Josh Don", "Peng Ding", "Samuel Grossman", "Luis Otero", "Chris Kennelly", "David Lo", "Carlos Villavieja"]
venue = "arXiv preprint · 2026"
+++

# PAPER-049 — Affinity Tailor

## 30-second read
- Google production soft-affinity scheduler.
- Userspace predicts workload CPU demand; kernel steers threads to demand-sized, topologically compact Preferred Cores while preserving work conservation.
- Protects cache, branch-predictor and prefetcher locality without hard CPU partitioning.
- Deployed across thousands of machines.
- Reports +12% geomean per-CPU throughput on chiplet systems, +3% on non-chiplet systems, +3–7% per-GB throughput.
- P99 scheduling latency can increase up to 17%, showing locality benefit can outweigh immediate queueing reduction.
- Very strong generic R2 software baseline; not Agent-specific and not phone evidence.

See [deep.md](deep.md).
