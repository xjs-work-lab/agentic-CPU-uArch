+++
id = "PAPER-009"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference"
primary_url = "https://arxiv.org/abs/2605.27435"
priority = "P0"
evidence_role = "direct smartphone CPU↔NPU stage/operator crossover evidence"
origin_paths = ["03-academic/paper-10q/PAPER-009.md"]
origin_blobs = ["b58711781ca457f10fd6afd05a67ff089c35759a"]
authors = ["Pu Li", "Jiawen Qi", "Qinyu Chen"]
venue = "arXiv preprint · 2026"
+++

# PAPER-009 — When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference

## 30-second read
- **Why it matters:** Direct measurements show CPU/NPU winner reverses by inference stage and overhead regime.
- **What it establishes:** For the evaluated phone/models, heterogeneous winner depends on stage/operator economics rather than a universal NPU-first rule.
- **Boundary:** Specific software/driver/NPU generation and evaluated models; not a universal constant.
- **Primary source:** https://arxiv.org/abs/2605.27435

## Migration fidelity
- V1 baseline: `960abb4ef50a8f5b0bd357c067f08346025d`
- Transform: `STRUCTURAL_REPACK`
- Detailed V1 interpretation is preserved in [deep.md](deep.md).
- Source independence remains `UNKNOWN` unless explicitly assessed later.
