+++
id = "PAPER-049"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Affinity Tailor: Dynamic Locality-Aware Scheduling at Scale"
primary_url = "https://arxiv.org/abs/2604.27915"
priority = "P0"
evidence_role = "strong generic software locality baseline using soft preferred cores"
origin_paths = ["03-academic/paper-10q/PAPER-049.md"]
origin_blobs = ["5276d5f7b562c6b4a70d271b208449dda1289508"]
authors = ["Jin Xin Ng", "Ori Livneh", "Richard O'Grady", "Josh Don", "Peng Ding", "Samuel Grossman", "Luis Otero", "Chris Kennelly", "David Lo", "Carlos Villavieja"]
venue = "arXiv preprint · 2026"
+++

# PAPER-049 — Affinity Tailor

- Dynamic soft / permeable preferred-core regions preserve cache, branch-predictor and prefetcher locality without hard partitioning.
- V1 reports geomean per-CPU throughput +12% on chiplet and +3% on non-chiplet systems; per-GB throughput +3–7%.
- **Decision use:** R2 must beat strong topology-aware software locality, not a default scheduler.
- **Boundary:** datacenter production evidence, not smartphone Agent PMU evidence.

Exact frozen V1 interpretation is preserved in [deep.md](deep.md).
