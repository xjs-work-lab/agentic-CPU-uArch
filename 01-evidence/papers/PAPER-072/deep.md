# PAPER-072 — CD-ANN: Scalable Approximate Nearest Neighbor search on client-side devices

## Source
- Journal of Systems Architecture, Vol. 175, 2026, 103771
- DOI: https://doi.org/10.1016/j.sysarc.2026.103771
- Authors: Chaoxia Qin, Yixiong Tang, Bing Guo, Kan Zhong, Duo Liu
- Evaluated client hardware: Apple M4 Pro / 48 GB in the reported setup
- Priority: P1

## Q1 — Problem + target mapping
ANN indices on personal/client devices face:
- high memory/storage overhead;
- expensive dynamic insertion/update;
- growing local datasets;
- client/cloud consistency/integrity concerns.

This overlaps the persistent-Agent-memory frontier, especially the assumption that frequent insert/update is a new workload.

## Q2 — Novelty / new-regime relevance
CD-ANN partitions a monolithic HNSW index into adaptive independent segments and stores only frequently needed segments on the client.

Classification:
**generic dynamic client-side ANN**, not Agent-native.

The important project consequence is negative:
dynamic vector growth is not sufficient evidence of an Agent-specific systems opportunity.

## Q3 — Falsifiable hypothesis
If graph operations are localized into segments and cold segments need not remain resident, then dynamic insertion and retrieval can scale under limited client memory with lower update cost.

Falsifiers:
- segmentation destroys recall;
- segment routing adds excessive overhead;
- working sets touch too many segments;
- update churn forces constant repartition;
- remote/on-demand fetch dominates latency.

The evaluated results support the hypothesis within the client/server simulation scope.

## Q4 — Research lineage / competing route
Competing/baseline families:
- HNSW;
- IVF-HNSW / IVFPQ-HNSW;
- DiskANN;
- static ANN indexes;
- LEANN compute-for-storage;
- MUSE mobile heterogeneous execution.

CD-ANN primarily addresses **dynamic growth + client memory**, while LEANN emphasizes storage minimization and MUSE emphasizes real mobile heterogeneous execution.

## Q5 — Key mechanism / control point
### Adaptive segmented HNSW
K-means partitions the dataset; each cluster maintains an independent HNSW segment.

### Incremental growth
New vectors route to the nearest centroid; segment growth is handled locally rather than rebuilding one monolithic graph.

### On-demand storage/cache
Only frequently used graph segments remain client-resident.

### Verification
Merkle/blockchain anchoring verifies freshness/integrity in cloud-edge use, but this is not central to our current hardware decision.

### Project interpretation
The generic software baseline already includes:
> segmented dynamic index + demand-paged/cached index state.

## Q6 — Experiment design
The paper evaluates multiple vector datasets and compares memory, query and insertion behavior against existing ANN solutions.

Public paper metadata reports:
- client-memory reductions spanning roughly 10–82% depending setting;
- incremental insertion latency reductions around 70–97%;
- stronger long-tail retrieval in evaluated cases.

The article text also summarizes somewhat different aggregate numbers in its conclusion, so strategic use should rely on the qualitative result rather than a single exact percentage.

## Q7 — Data / artifact / reproducibility
Strengths:
- peer-reviewed 2026 journal paper;
- dynamic insertion explicitly evaluated;
- client memory modeled directly;
- multiple datasets/baselines.

Limitations:
- reported client hardware is Apple M4 Pro with 48 GB, not a smartphone;
- system includes simulated cloud/blockchain components;
- not Agent memory;
- energy/thermal/heterogeneous CPU-NPU behavior is not the focus;
- no direct personal-Agent outcome.

## Q8 — Evidence vs hypothesis
### [FACT]
Segmented ANN indexing can substantially reduce dynamic insertion cost and client-resident memory in the evaluated systems.

### [OBSERVATION]
Frequent updates and limited local memory are generic dynamic-index concerns, not uniquely Agentic.

### [INFERENCE — project]
A persistent-Agent-memory candidate must show either:
- a different operation mix/semantic constraint; or
- a direct mobile heterogeneous execution residual beyond segmented/on-demand ANN.

### Not established
- smartphone SYSTEM_VALUE;
- Agent-specific semantics;
- CPU/NPU/DRAM mechanism;
- hardware insufficiency.

## Q9 — Real contribution to project decision
### Memory frontier
**Strong generic dynamic-index baseline / narrowing.**

CD-ANN weakens any candidate framed only as:
- frequent inserts;
- growing local vector store;
- limited resident memory;
- index maintenance overhead.

### B-residual
Integrity/freshness concepts overlap conceptually with provenance, but CD-ANN's cryptographic freshness is not semantic dependency validity.

### Hardware
No promotion.

## Q10 — Next action
1. KEEP as P1 baseline.
2. Include segmented/on-demand dynamic ANN in strongest software baseline.
3. Search for Agent-specific operation semantics: consolidation, forgetting, semantic revision, multimodal acquisition, graph traversal.
4. Require direct phone evidence before assigning systems maturity.

## Decision footer
- **New-regime relevance:** generic enabling
- **Evidence maturity:** SYSTEM_VALUE in evaluated client-side ANN scope; not smartphone Agent
- **Decision impact:** narrows dynamic-index novelty
- **Hardware impact:** none
