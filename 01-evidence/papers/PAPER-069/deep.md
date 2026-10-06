# PAPER-069 — MUSE: A Heterogeneity-Aware Multimedia Search Engine for Mobile SoCs

## Source
- ACM Multimedia 2026, accepted paper
- arXiv: 2511.19192 v2
- v1 title: *AME: An Efficient Heterogeneous Agentic Memory Engine for Smartphones*
- v2 title: *MUSE: A Heterogeneity-Aware Multimedia Search Engine for Mobile SoCs*
- Evaluation: commercial Snapdragon 8-series mobile SoCs
- Workload: high-dimensional multimodal vector retrieval + continuous ingestion + index maintenance
- Priority: P0

## Q1 — Problem + target mapping
Persistent personal Agents increasingly depend on semantic access to continuously growing personal data: screenshots, audio, video, text, memories, and derived embeddings.

MUSE targets the lower-level systems problem that appears when this data plane runs locally:
- high-dimensional embeddings;
- interactive queries;
- continuous background ingestion;
- index construction/update;
- tight bandwidth/on-chip-storage limits;
- heterogeneous CPU/GPU/NPU execution.

This maps directly to the project's new frontier:
> does long-lived Agent memory create a new smartphone CPU/system workload beyond inference?

## Q2 — Novelty / new-regime relevance
MUSE's key insight is that server vector-search assumptions mismatch mobile SoCs in two ways:

1. **hardware mismatch**
   - small local memories;
   - strict bandwidth/power/thermal limits;
   - NPU-preferred data types/layouts;
   - fixed accelerator invocation/adaptation costs;

2. **workload mismatch**
   - interactive query must coexist with background insertion and index maintenance.

The workload is highly relevant to persistent Agents, but MUSE deliberately generalizes it to multimedia retrieval.

Classification:
**Agent-amplified / generic mobile retrieval substrate**, not uniquely Agent-native.

## Q3 — Falsifiable hypothesis
If mobile vector-search/index operations are restructured to fit accelerator execution/data-layout constraints and routed to the right compute engine by workload shape, then heterogeneous SoC execution should outperform naïve CPU/NPU mapping under realistic hybrid query/update loads.

Falsifiers:
- query/update rate is too low to matter;
- CPU-only optimized ANN remains better;
- NPU fixed costs dominate;
- format/layout conversion erases accelerator gains;
- thermal/energy pressure removes throughput benefit;
- storage/index software dominates instead of SoC execution.

The reported results support the hypothesis in the evaluated Snapdragon scope.

## Q4 — Research lineage / competing route
Strong competing routes include:
- optimized CPU ANN/vector search;
- HNSW / IVF / product quantization;
- Faiss-style CPU/GPU implementations;
- low-storage personal-device indices such as LEANN;
- segmented/on-demand client-side ANN such as CD-ANN;
- generic heterogeneous runtime scheduling;
- cloud/server vector databases.

Important lineage rule:
AME v1 and MUSE v2 share arXiv ID and mechanism/result lineage; do not count them twice.

## Q5 — Key mechanism / control point
### 1. NPU-centric asynchronous pipeline
MUSE overlaps:
- DMA transfer;
- HVX data conversion/layout packing;
- HMX dense similarity compute;
- result unpack/writeback.

### 2. Zero-copy host/accelerator sharing
Shared dma-buf/ION mappings reduce host-side duplication and CPU/memory-bandwidth overhead.

### 3. Hardware-aligned IVF
Index parameters and batch shapes are aligned to matrix-engine tile granularity so centroid routing/candidate scoring map to regular dense kernels.

### 4. Workload-aware heterogeneous scheduling
Different operation classes go to different processors:
- small latency-sensitive interactive work can remain on CPU;
- continuous ingestion can use CPU/GPU;
- throughput-friendly dense scoring uses NPU;
- index maintenance is scheduled to avoid destructive interference.

### Project interpretation
The potential control point is not "Agent memory" as a label.

It is:
> **operation-shape-aware mapping and data movement for a continuously mutating semantic-memory substrate.**

## Q6 — Experiment design
MUSE evaluates:
- commercial flagship Snapdragon 8-series SoCs;
- high-dimensional multimodal embeddings;
- query throughput / recall;
- index construction;
- concurrent insertion + query;
- hardware profiling;
- energy/thermal behavior.

Reported headline:
- up to **1.4×** query throughput at matched recall;
- up to **7×** faster index construction;
- up to **6×** higher insertion throughput under concurrent streaming;
- peak device temperature capped around **38°C**;
- up to **4.6×** lower total energy vs CPU-bound baselines.

A key negative result is strategically important:
> naïve NPU mapping is not automatically superior; irregular search/pointer-chasing, layout conversion and synchronization can make accelerator execution worse.

## Q7 — Data / artifact / reproducibility
Strengths:
- accepted ACM MM 2026;
- real commercial mobile SoCs;
- direct heterogeneous CPU/GPU/NPU evaluation;
- hybrid query/update workload;
- thermal + energy reporting;
- detailed mechanism descriptions.

Limitations:
- no public standalone production artifact identified in the current review;
- low-level Qualcomm interfaces may limit reproducibility/portability;
- not Huawei hardware;
- retrieval workload is broader than Agent memory;
- exact benefit depends on embedding dimension, batch size, index design, update rate, and accelerator API.

## Q8 — Evidence vs hypothesis
### [FACT]
Dynamic high-dimensional vector retrieval + ingestion/index maintenance can create significant execution/data-movement pressure on commercial smartphone SoCs.

### [FACT]
Heterogeneous operation placement and hardware-aligned data/index layout materially change performance/energy in the evaluated systems.

### [OBSERVATION]
Irregular graph/pointer-chasing work favors CPUs, while dense batched scoring maps better to mobile accelerators.

### [INFERENCE — project]
Persistent Agent memory is a credible new workload family for CPU/system research **only if real Agent workloads actually sustain this query/update/mutation mix**.

### Not established
- Agent-specific semantic operation that generic multimedia retrieval lacks;
- Huawei transfer;
- >=5% user end-outcome value;
- software insufficiency;
- a CPU-uArch-specific mechanism.

## Q9 — Real contribution to project decision
### New memory frontier
**KEEP as P0 structural seed.**

MUSE provides the strongest direct phone evidence so far that persistent semantic data can create:
- CPU control/irregular work;
- accelerator dense work;
- DDR/TCM/layout pressure;
- foreground/background operation heterogeneity;
- insertion/index-maintenance duty cycle.

### B-residual
Only partial overlap.
B-residual is about semantic revision → safe lineage/coherence of derived artifacts.
MUSE is mainly **operational retrieval/update execution**, not semantic validity/provenance.

### R2 / CG-01
MUSE does not prove CPU continuation-locality or new cache hardware.
Its memory issue is vector/index/data-movement behavior, not thread continuation microstate.

### CG-07
MUSE does not prove a dedicated always-on AI domain; it may even favor distributing work across CPU/GPU/NPU.

### Hardware
No promotion. First exhaust generic ANN/index/data-layout/runtime mechanisms.

## Q10 — Next action
1. KEEP PAPER-069 as P0.
2. Treat AME→MUSE as one Source lineage.
3. Add a direct mobile dynamic-retrieval Claim.
4. Pressure-test with LEANN/CD-ANN and generic vector-index prior art.
5. Use M3-Agent/mobile-Agent memory evidence to determine whether the mutation/retrieval mix is genuinely Agent-amplified.
6. Do not create a hardware Direction yet.

## Decision footer
- **New-regime relevance:** Agent-amplified, not uniquely Agent-native
- **Evidence maturity:** SYSTEM_VALUE for evaluated mobile retrieval workload
- **Decision impact:** opens a structural memory-workload frontier, not a Bet
- **Hardware impact:** none
- **Open questions:** real Agent mutation mix, Huawei transfer, CPU share, memory-bandwidth/thermal duty cycle, semantic operation classes
