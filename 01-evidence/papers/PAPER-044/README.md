+++
id = "PAPER-044"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "ProAgentBench: Evaluating LLM Agents for Proactive Assistance with Real-World Data"
primary_url = "https://arxiv.org/abs/2602.04482"
priority = "P0"
evidence_role = "strong long-history real-world B4 demand-prediction baseline"
origin_paths = ["03-academic/paper-10q/PAPER-044.md"]
origin_blobs = ["81f6645a9f73b02f9a4f8eb3ec4b7a053bc49035"]
authors = ["Yuanbo Tang", "Huaze Tang", "Tingyu Cao", "Lam Nguyen", "Anping Zhang", "Xinwen Cao", "Chunkang Liu", "Wenbo Ding", "Yang Li"]
venue = "arXiv preprint · 2026"
+++

# PAPER-044 — ProAgentBench: Evaluating LLM Agents for Proactive Assistance with Real-World Data

## 30-second read
- **Why it matters:** Long real-world behavioral history materially improves When-to-Assist prediction.
- **What it establishes:** A strong generic history-based baseline can infer a substantial fraction of demand.
- **Boundary:** Primarily desktop workflows; wall-clock history is not phone CPU/NPU active cost and When-to-Assist is not identical to continuation ground truth.
- **Primary source:** https://arxiv.org/abs/2602.04482

## Migration fidelity
- V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- Transform: `STRUCTURAL_REPACK`
- Detailed V1 interpretation is preserved in [deep.md](deep.md).
- Source independence remains `UNKNOWN` unless explicitly assessed later.
