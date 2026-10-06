+++
id = "PAPER-035"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Invalidation Contracts for Cross-Episode Agent Memory"
primary_url = "https://arxiv.org/abs/2609.00243"
priority = "P1"
evidence_role = "dependency/version invalidation baseline"
origin_paths = ["03-academic/paper-briefs/PAPER-021-040.md"]
origin_blobs = ["e2af40f95a08c39744c46ae121f469647c435363"]
authors = ["Michael Wu", "Arquimedes Canedo"]
venue = "arXiv preprint · 2026"
+++

# PAPER-035 — Invalidation Contracts for Cross-Episode Agent Memory

## 30-second read
- **Why it matters:** Shows version stamps, dependency vectors and scoped invalidation can avoid broad over-eviction.
- **What it establishes:** Dependency-aware validity/invalidation is already a concrete Agent-memory control mechanism.
- **Boundary:** Application/protocol memory; not smartphone S2/S3 physical tiers.

## Migration fidelity
- frozen V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- transform: `STRUCTURAL_REPACK`
- detailed V1 interpretation is preserved in [deep.md](deep.md).
- source independence remains `UNKNOWN`.
