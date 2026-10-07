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
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
origin_paths = ["03-academic/paper-10q/PAPER-009.md"]
origin_blobs = ["b58711781ca457f10fd6afd05a67ff089c35759a"]
authors = ["Pu Li", "Jiawen Qi", "Qinyu Chen"]
venue = "arXiv preprint · 2026"
+++

# PAPER-009 — When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference

## 30-second read
- Direct Snapdragon 8 Gen 3 / Hexagon v75 measurements show that current CPU↔NPU performance can reverse by inference stage.
- The robust systems result is **stage/operator/implementation-dependent placement plus material dispatch/fallback overhead**, not an architecture-general “Prefill belongs on CPU” rule.
- Prefill CPU wins in the evaluated stack are partly explained by Hexagon backend maturity, VTCM constraints and unsupported-op fallback.
- Decode core MUL_MAT favors NPU substantially, but end-to-end gain shrinks because communication, lightweight-op scheduling tax and fallback remain.
- Primary source: https://arxiv.org/abs/2605.27435

See [deep.md](deep.md) for EDP v1 FULL_10Q.
