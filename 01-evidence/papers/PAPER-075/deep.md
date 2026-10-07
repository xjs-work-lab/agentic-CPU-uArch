# PAPER-075 — SwiftMem: Fast Agentic Memory via Query-aware Indexing

## Source
- arXiv:2601.08160, 2026
- Artifact: https://github.com/EdwardTex/SwiftMem
- Datasets: LoCoMo, LongMemEval_S, LoCoMo Refined
- Public artifact includes memory manager, temporal index, semantic DAG-tag index, embedding retrieval, co-consolidation and evaluation pipeline
- Priority: P1 because peer-reviewed venue acceptance was not established in this review

## Q1 — Problem + target mapping
Agentic memory systems often send every query through a broad embedding index even when the query already contains strong temporal or semantic constraints.

SwiftMem asks whether the system can first infer *where* to search and only then invoke ANN/reranking.

For H-PAM this is highly relevant because several surviving candidate facts were:
- temporal memory semantics;
- semantic category/relationship;
- consolidation/locality;
- memory fragmentation.

SwiftMem directly attacks all four in software.

## Q2 — Novelty / new-regime relevance
SwiftMem uses three coordinated indexes:

1. **Temporal Index**
- per-user sorted timelines;
- global episode lookup;
- logarithmic range queries;
- explicit temporal-query routing.

2. **Semantic DAG-Tag Index**
- LLM-generated tags arranged in a DAG;
- bounded tag-neighborhood expansion;
- query-tag router narrows candidate space before dense retrieval.

3. **Embedding Index + Co-consolidation**
- embeddings remain available for similarity search;
- semantic tag clusters guide periodic vector-block reorganization;
- physically related memories are placed contiguously to improve cache locality and reduce fragmentation.

Classification:
**Agent-memory software/data-layout optimization**, not mobile systems/uArch evidence.

## Q3 — Falsifiable hypothesis
Core hypothesis:
> Query-aware temporal/semantic routing plus semantic co-consolidation can reduce memory search latency substantially without materially sacrificing retrieval/answer quality.

Falsifiers:
- query classification/routing is wrong too often;
- semantic tags add too much LLM overhead;
- HNSW alone already reaches the same latency;
- consolidation cost outweighs query savings;
- semantic drift breaks tag clusters;
- quality loss is unacceptable.

The public experiments support the hypothesis in the evaluated long-term conversation benchmarks.

## Q4 — Research lineage / competing route
Strong baseline families include:
- HNSW-backed dense retrieval;
- RAG;
- LangMem;
- Nemori;
- LightMem;
- EverMemOS;
- full-context processing.

Project relation:
- LEANN attacks storage capacity through selective recomputation;
- CD-ANN attacks dynamic growth/client residency;
- SwiftMem attacks query routing and semantic/temporal layout;
- MUSE attacks real mobile heterogeneous execution.

Together these form a much stronger generic memory-software baseline than ordinary vector search.

## Q5 — Key mechanism / control point
### Temporal routing
Queries with explicit temporal constraints use a sorted timeline and direct episode mapping instead of scanning the whole memory store.

### Semantic routing
Queries are mapped to a bounded set of relevant DAG tags; only those regions feed later retrieval/reranking.

### Co-consolidation
Tag relationships and co-occurrence define semantic clusters.
Embeddings for the same cluster are reorganized into contiguous blocks.

The system maintains a layout map for physical storage offsets and periodically consolidates when fragmentation/benefit criteria justify it.

### Project interpretation
This is important negative evidence for H-PAM:
> **semantic and temporal memory metadata can already drive software data layout and locality optimization.**

Therefore H-PAM cannot claim differentiation merely from 'memory semantics should influence placement'.

## Q6 — Experiment design
Public evaluation covers:
- LoCoMo;
- LongMemEval_S;
- LoCoMo Refined;
- strong memory systems with HNSW-backed dense retrieval.

Public artifact reports on LoCoMo with GPT-4.1-mini:
- SwiftMem search latency: **10.834 ms/query**;
- compared HNSW-backed systems: roughly **881.924–1231.332 ms/query**.

On LongMemEval_S:
- SwiftMem: **12.775 ms/query**;
- compared memory systems: roughly **913.948–1483.500 ms/query**.

Quality remains competitive but not uniformly best:
- on LoCoMo, EverMemOS has higher LLM-judge quality in the public table;
- SwiftMem trades some peak answer quality for very low search latency.

The arXiv abstract/version reports a ~47× headline speedup, while the later public artifact tables show larger per-query ratios in specific setups. We retain exact table values only with their benchmark scope and do not use a single headline multiplier for strategic scoring.

## Q7 — Data / artifact / reproducibility
Strengths:
- public code;
- HNSW-backed strong baselines;
- multiple long-term memory benchmarks;
- evaluation pipeline available;
- explicit indexing and consolidation implementation.

Limitations:
- preprint status;
- no smartphone hardware;
- embedding/LLM services are API-configurable and not representative of mobile-local cost;
- no CPU/NPU/DRAM/energy/thermal profiling;
- consolidation overhead is software-level and benchmark-dependent;
- long-term conversation retrieval may not match mobile GUI Agent memory duty cycles.

## Q8 — Evidence vs hypothesis
### [FACT]
Temporal and semantic query structure can be used to narrow Agent-memory search before ANN retrieval.

### [FACT]
Semantic tag structure can drive physical reorganization of embedding blocks to improve locality.

### [OBSERVATION]
Memory semantics can affect software storage/layout without requiring a new OS/hardware interface.

### [INFERENCE — project]
H-PAM's candidate residual must be narrower than temporal/semantic indexing, co-consolidation or generic locality-aware layout.

### Not established
- mobile Agent SYSTEM_VALUE;
- target-phone memory bandwidth/thermal behavior;
- CPU/NPU placement changes;
- inability of software to expose useful layout metadata;
- hardware/uArch need.

## Q9 — Real contribution to project decision
### H-PAM
**NARROW FURTHER / no promotion.**

Remove from H-PAM white space:
- temporal query indexing;
- semantic DAG-based query routing;
- semantic co-consolidation;
- semantic-cluster locality/layout optimization;
- fragmentation-triggered software reorganization.

Surviving H-PAM questions are now mostly about **runtime coupling and mobile execution**, not memory index architecture:
- foreground recall vs background maintenance contention;
- cross-representation coupling across raw media / vector / graph / action traces;
- suspend/resume state-loss and rebuild cost;
- lifecycle-phase urgency that changes heterogeneous placement or maintenance timing.

### B-residual
Semantic replacement correctness/lineage still belongs to B-residual.

### C
If SwiftMem-like semantics merely feed ordinary QoS/scheduling, that remains generic C territory.

### Hardware
No promotion. SwiftMem is another software-first capture path.

## Q10 — Next action
1. KEEP as P1 strongest-baseline evidence.
2. Add a canonical Claim for query-aware semantic/temporal indexing + co-consolidation software capture.
3. Strengthen H-PAM baseline.
4. Do not read more generic retrieval/index papers unless they expose a materially different lifecycle operation.
5. Next evidence must directly measure phone-side operation coupling, interference, or state-loss/rebuild economics.

## Decision footer
- **New-regime relevance:** Agent-memory software optimization
- **Evidence maturity:** SYSTEM_VALUE for evaluated memory-retrieval benchmarks; no mobile systems maturity
- **H-PAM impact:** NARROW
- **hardware impact:** none
- **Primary source:** https://arxiv.org/abs/2601.08160
- **Artifact:** https://github.com/EdwardTex/SwiftMem