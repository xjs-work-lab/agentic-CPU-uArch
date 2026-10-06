# PAPER-070 — LEANN: A Low-Storage Overhead Vector Index

## Source
- MLSys 2026 — Best Paper Award
- arXiv: 2506.08276
- artifact: https://github.com/StarTrail-org/LEANN
- scope: personal-device/local semantic search and RAG
- Priority: P0

## Q1 — Problem + target mapping
Local semantic memory/search often duplicates the underlying personal data with:
- full high-dimensional embeddings;
- large graph/index metadata.

The paper reports examples where vector-index storage can exceed the raw source data by multiples, making local deployment unattractive.

This directly challenges the persistent-Agent-memory frontier:
> before asking for more cache/DRAM/hardware, can software simply avoid storing most embeddings?

## Q2 — Novelty / new-regime relevance
LEANN changes the storage/compute tradeoff:
- keep a compact graph/index structure;
- **do not persist every full embedding**;
- selectively recompute embeddings on demand;
- prune graph edges while preserving high-degree/important connectivity.

Classification:
**generic enabling personal-device retrieval**, not Agent-native.

It is relevant because Agent memory is one consumer of local semantic search, but the technique does not depend on Agent semantics.

## Q3 — Falsifiable hypothesis
If embedding inference is cheap enough relative to storage/memory pressure, and the graph can identify a small candidate set, then on-demand recomputation + compact graph structure should preserve retrieval quality while greatly reducing stored index size.

Falsifiers:
- recomputation latency/energy dominates;
- personal data is frequently queried with strict latency;
- dynamic update churn invalidates compact graph advantages;
- embedding model is too expensive on phone;
- memory pressure is not storage/index dominated.

The evaluated benchmarks support the storage-latency tradeoff in the paper's hardware scope.

## Q4 — Research lineage / competing route
Competing routes:
- HNSW storing vectors;
- IVF / DiskANN;
- product quantization/compressed embeddings;
- server vector databases;
- mobile heterogeneous acceleration such as MUSE;
- dynamic segmented client indexes such as CD-ANN.

LEANN attacks **capacity/storage overhead**, while MUSE attacks **execution/heterogeneity/update throughput**.
These are complementary strongest baselines, not direct substitutes.

## Q5 — Key mechanism / control point
### Graph-based selective recomputation
The graph narrows candidate search; embeddings for candidates are recomputed when needed rather than persistently stored.

### High-degree-preserving pruning
Redundant graph structure is removed while retaining connectivity important for search quality.

### Batched recomputation
Embedding generation is organized to recover practical latency.

### Project interpretation
The important baseline is:
> trade cheap/reusable compute for memory/storage capacity instead of introducing a new memory hierarchy mechanism.

## Q6 — Experiment design
Evaluation covers real retrieval/RAG datasets and compares against conventional vector-index baselines.

Public summaries report:
- index size below roughly **5% of raw source data**;
- up to about **50×** smaller index storage than conventional approaches;
- strong top-k retrieval quality;
- practical sub-few-second QA/RAG search behavior.

Public artifact supports local personal-data search and multiple ANN backends.

Hardware reported in paper/poster includes personal-device and GPU systems such as Apple M1 and NVIDIA A10-class setups; this is not a direct flagship-phone SoC evaluation.

## Q7 — Data / artifact / reproducibility
Strengths:
- MLSys 2026 Best Paper;
- open-source implementation;
- actively maintained artifact;
- real personal-data/RAG use cases;
- reproducible local indexing/search workflow.

Limitations:
- not direct smartphone CPU/NPU evaluation;
- current production repository has evolved beyond the paper;
- storage results should not be conflated with DRAM bandwidth/thermal behavior;
- update-heavy continuously mutating workloads are not the paper's primary contribution.

## Q8 — Evidence vs hypothesis
### [FACT]
Large vector indices can be compressed dramatically by avoiding persistent embedding storage and using selective recomputation.

### [OBSERVATION]
Local semantic memory pressure can be shifted from storage capacity to compute latency/energy.

### [INFERENCE — project]
Any persistent-Agent-memory opportunity must compare against a **compute-for-storage** baseline, not assume embeddings/indexes must remain fully resident.

### Not established
- smartphone energy benefit;
- high-rate insert/delete/index-maintenance behavior;
- Agent-specific memory semantics;
- cross-engine CPU/NPU placement;
- hardware necessity.

## Q9 — Real contribution to project decision
### Memory frontier
**Strong software baseline / white-space narrowing.**

LEANN means a candidate cannot earn differentiation simply because:
- embeddings are large;
- indexes consume storage;
- personal memory grows over time.

### B-residual
Strengthens the generic storage/provenance baseline but does not solve semantic revision validity.

### R2 / CG-01
No direct support for CPU-local continuation/cache hardware.

### Hardware
No promotion. It reinforces software-first pressure.

## Q10 — Next action
1. KEEP as P0 baseline.
2. Add a Claim that personal-device vector-memory capacity can be strongly reduced via software recomputation/index compression.
3. Compare MUSE dynamic update/heterogeneous pressure against LEANN capacity tradeoff.
4. Search for update-heavy/mobile-specific ANN systems such as CD-ANN.
5. Any new memory Direction must prove residual beyond compact/recomputed vector indexes.

## Decision footer
- **New-regime relevance:** generic enabling
- **Evidence maturity:** SYSTEM_VALUE in evaluated personal-device retrieval/RAG scope; not phone SYSTEM_VALUE
- **Decision impact:** narrows persistent-memory capacity novelty
- **Hardware impact:** negative baseline pressure
