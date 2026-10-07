+++
id = "PAPER-075"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "PREPRINT_AGENT_MEMORY_SYSTEM"
title = "SwiftMem: Fast Agentic Memory via Query-aware Indexing"
primary_url = "https://arxiv.org/abs/2601.08160"
priority = "P1"
evidence_role = "strong software baseline for temporal/semantic query routing and semantic co-consolidation/locality in agentic memory retrieval"
authors = ["Anxin Tian", "Yiming Li", "Xing Li", "Hui-Ling Zhen", "Lei Chen", "Xianzhi Yu", "Zhenhua Dong", "Mingxuan Yuan"]
venue = "arXiv preprint 2026"
+++

# PAPER-075 — SwiftMem

## 30-second read
- **Why it matters:** Directly pressures H-PAM's remaining idea that temporal/semantic memory semantics might require a new lower-level layout mechanism.
- **What it establishes:** Query characteristics can be used in software to route retrieval into temporal or semantic subspaces, while embedding/tag co-consolidation periodically reorganizes vector blocks to improve locality.
- **Strong-baseline point:** dense baselines already use HNSW; SwiftMem's gain comes from candidate-space narrowing and layout organization, not from beating a naïve linear scan.
- **Reported anchors:** ~10.8 ms/query on LoCoMo and ~12.8 ms/query on LongMemEval_S in the public artifact, with large latency reductions versus HNSW-backed memory systems while maintaining competitive quality.
- **Portfolio meaning:** temporal/semantic routing and semantic co-consolidation are software-capturable; H-PAM must look beyond these patterns.
- **Boundary:** server/cloud memory benchmark and API-based embeddings/LLMs; no smartphone CPU/NPU/energy/thermal evidence.
- **Primary source:** https://arxiv.org/abs/2601.08160
- **Artifact:** https://github.com/EdwardTex/SwiftMem

See [deep.md](deep.md) for full Paper Insight 10Q.