+++
id = "PAPER-029"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "B_RESIDUAL_STRONG_GENERIC_MOBILE_CONTEXT_LIFECYCLE_BASELINE"
independence_assessment = "PEER_REVIEWED_SENSYS_2026_COTS_PHONE"
title = "An Efficient Context Management System for On-Device LLMaaS"
primary_url = "https://doi.org/10.1145/3774906.3800479"
priority = "P1"
evidence_role = "direct mobile persistent-context/KV generic runtime-memory baseline"
authors = ["Wangsong Yin", "Mengwei Xu", "Yuanchun Li", "Xuanzhe Liu"]
venue = "SenSys 2026"
+++

# PAPER-029 — Libra / On-Device LLMaaS

## 30-second read
- Peer-reviewed SenSys 2026.
- Treats an LLM as a mobile OS service shared by multiple apps with persistent KV contexts.
- Libra uses chunk-wise compression, swap/recompute pipelining and chunk lifecycle management.
- Evaluated on COTS devices including an 8 GB MI14 smartphone with UFS 4.0, 8 CPU cores, Adreno GPU and Hexagon NPU.
- Reports up to 20× and 9.7× average context-switch latency reduction vs strong chunked baselines.
- Strong evidence that S2/KV physical lifecycle is a real phone problem, but also that generic runtime/memory management captures large value without Agent semantic lineage.
- B-residual impact: stronger generic baseline; no promotion.
- No CPU/uArch implication.

See [deep.md](deep.md).
