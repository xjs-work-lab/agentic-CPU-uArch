+++
id = "PAPER-098"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "TARGET_PHONE_AGENTIC_HETERO_ORCHESTRATION_SYSTEM_VALUE"
independence_assessment = "DAC_2026_SAME_LINEAGE_AS_AGENT_XPU"
title = "HeRo: Adaptive Orchestration of Agentic RAG on Heterogeneous Mobile SoC"
primary_url = "https://arxiv.org/abs/2603.01661"
priority = "P0"
evidence_role = "direct commercial-phone Agentic RAG orchestration evidence across CPU/GPU/NPU with dynamic dependencies and shared-memory contention"
authors = ["Maoliang Li", "Jiayu Chen", "Zihao Zheng", "Ziqian Li", "Xinhao Sun", "Guojie Luo", "Chenchen Liu", "Xiang Chen"]
venue = "DAC 2026 / arXiv manuscript"
+++

# PAPER-098 — HeRo

## 30-second read
- **Direct phone evidence:** Redmi K80 / Snapdragon 8 Gen 3 and OnePlus 13 / Snapdragon 8 Elite-class platform.
- **Agentic workload:** dynamic multi-stage RAG with query rewriting, retrieval, reranking and generation; the execution DAG is only partially known at runtime.
- **Control points:** shape-aware sub-stage partition, criticality + accelerator affinity mapping, bandwidth-aware concurrency.
- **Reported value:** up to 10.94× over GPU-only and up to ~1.5× over an Ayo-like static multi-xPU mapping.
- **Project impact:** closes C’s “no direct target-phone Agent-aware system value” gap, but still does not prove differentiated residual beyond the strongest generic/Agent-aware software baseline.

See [deep.md](deep.md) for full Paper Insight 10Q.
