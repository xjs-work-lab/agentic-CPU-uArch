# PAPER-098 — HeRo: Adaptive Orchestration of Agentic RAG on Heterogeneous Mobile SoC

## Source
- arXiv:2603.01661
- listed by the authors’ IF-Lab publication page as DAC 2026
- Peking University-led lineage
- commercial Snapdragon phones
- Priority: P0

## Q1 — Problem + target mapping
Agentic RAG no longer resembles a fixed two-stage retrieve→generate pipeline.

Specialist agents may:
- rewrite/decompose queries;
- trigger multiple searches;
- rerank/refine documents;
- generate variable-length responses;
- conditionally skip or add stages.

Therefore the execution graph is multi-model, partially observable and dynamically materialized.

Target mapping:
> can Agent workflow state materially improve heterogeneous mobile SoC scheduling beyond static accelerator placement?

## Q2 — Novelty / new-regime relevance
HeRo moves optimization from:
- single-model operator placement
to:
- **workflow-stage / sub-stage scheduling across a dynamic DAG**.

It explicitly models:
- stage–PU affinity;
- workload-shape sensitivity;
- shared DRAM contention;
- partial future dependency.

Classification:
**AMPLIFIED / Agentic-RAG-native execution structure.**

The primitives are generic DAG scheduling, profiling and contention control, but the partially evolving workflow is directly caused by Agent decisions.

## Q3 — Falsifiable hypothesis
If dynamic Agentic RAG graph structure matters on phones, online affinity/criticality/contention-aware orchestration should beat:
- GPU-only execution;
- NPU-only execution;
- static multi-xPU mapping.

Falsifiers:
- static mapping is near-optimal;
- online scheduling overhead removes gains;
- benefits arise only from one unusually favorable model/device;
- a generic dynamic DAG scheduler with identical signals matches HeRo.

The paper supports the first comparison but does not fully close the last one.

## Q4 — Research lineage / competing route
Baselines/prior art include:
- llama.cpp GPU execution;
- Powerserve-NPU;
- Ayo-like static multi-xPU mapping;
- HeteroInfer / mllm.npu single-model heterogeneous execution;
- HedraRAG CPU-GPU workflow graph optimization.

HeRo and Agent.xpu share authors/group lineage, so they establish sustained capability rather than independent replication.

## Q5 — Key mechanism / control point
1. **Shape-aware sub-stage partition** chooses batches/token groups based on profiled PU behavior.
2. **Criticality-affinity mapping** combines observed DAG critical path with a prior over likely future stages.
3. **Bandwidth-aware concurrency control** selectively delays parallel work when shared DRAM interference would hurt critical progress.
4. **Online partial-DAG scheduling** reacts as Agent decisions reveal new nodes/edges.

## Q6 — Experiment design
Devices:
- Redmi K80 — Snapdragon 8 Gen 3-class CPU/GPU/NPU, 12 GB LPDDR5X;
- OnePlus 13 — Snapdragon 8 Elite / Gen-4-class CPU/GPU/NPU, 24 GB LPDDR5X.

Workflows:
- three Agentic RAG workflows of increasing complexity;
- four datasets including FinQA, TruthfulQA, HotpotQA and 2WikiMultihopQA;
- Qwen3-family and BGE + Llama-family configurations.

Baselines:
- llama.cpp GPU;
- Powerserve NPU;
- Ayo-like manual/static xPU mapping.

Reported:
- up to **10.94×** end-to-end improvement over GPU-only;
- up to about **1.5×** over Ayo-like static xPU mapping;
- ablation case C1: 5.79s baseline → 3.82s all techniques (1.52×);
- ablation case C2: 17.23s baseline → 5.38s all techniques (3.20×).

## Q7 — Data / artifact / reproducibility
Strengths:
- direct commercial smartphones;
- two SoC generations;
- CPU/GPU/NPU shared-memory system;
- multiple workflow complexities / datasets / model families;
- mechanism ablation.

Limitations:
- primarily average single-query latency, not foreground app coexistence;
- baselines do not include every strong generic scheduler in C’s G1 set;
- traces with abnormal latency are filtered in reported methodology;
- same lineage as Agent.xpu;
- public artifact maturity is less established than peer-reviewed systems with full AE.

## Q8 — Evidence vs hypothesis
### [FACT]
Agentic RAG stages show different PU affinities and shape sensitivity on the evaluated phones.

### [FACT]
Shared DRAM contention changes the benefit of concurrent stage execution.

### [FACT]
HeRo beats static/single-accelerator deployment baselines on the evaluated commercial phones.

### [OBSERVATION]
Workflow complexity increases the value of adaptive scheduling in the reported experiments.

### [INFERENCE — project]
C now has **direct target-phone Agent-aware SYSTEM_VALUE**, but differentiated information/control beyond strong software baselines remains unproven.

## Q9 — Real contribution to project decision
This source changes C’s evidence maturity:
- before: target-phone Agent-aware value absent;
- after: direct target-phone Agentic RAG scheduling value exists.

It does **not** reopen C as a second Primary Bet because:
- criticality, partial DAG state, affinity and bandwidth are software-visible;
- Murakkab/HedraRAG/Agent.xpu establish strong upper-layer orchestration prior art;
- HeRo’s strongest comparison is not against all C G1/G2 controls.

For CG-06:
- static operator-level CPU/NPU comparison is no longer sufficient;
- CPU fast-path value must survive workflow-level xPU orchestration.

## Q10 — Next action
1. UPGRADE C evidence maturity to SYSTEM_VALUE.
2. Keep C lane/score unchanged.
3. Add Agent.xpu/HeRo-class orchestration to the strongest baseline.
4. Narrow CG-06 whitespace; no score change.
5. Do not create a new Direction.

## Decision footer
- **Evidence maturity:** SYSTEM_VALUE on commercial phones
- **Decision impact:** C evidence upgrade / no lane promotion; CG-06 baseline raised
- **Open questions:** strongest generic-dynamic scheduler, foreground QoE, Huawei target transfer
- **Primary source:** https://arxiv.org/abs/2603.01661
