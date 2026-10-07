+++
id = "PAPER-031"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "B_RESIDUAL_HISTORY_ONLY_REUSE_PREDICTION_STRONG_BASELINE"
independence_assessment = "PREPRINT_SERVER_VLLM_NO_TARGET_PHONE"
title = "Learning Agent Execution for KV-Cache Management in Agentic Serving"
primary_url = "https://arxiv.org/abs/2608.14624"
priority = "P0"
evidence_role = "strong history-only reuse baseline"
authors = ["Rui Zhang", "Chaeeun Kim", "Shaoting Feng", "Kuntai Du", "Yuhan Liu", "Yi Zhong", "Cheng-Wei Ching", "Junchen Jiang", "Liting Hu"]
venue = "arXiv preprint · 2026"
+++

# PAPER-031 — CacheScout

## 30-second read
- Learns Agent execution transitions online from observed requests.
- Requires neither predefined workflow DAGs nor explicit semantic annotations.
- Uses learned survival/reuse probability for predictive eviction and background prefetch.
- Implemented on vLLM.
- Reports +10–18 pp KV hit rate, 18–45% lower mean TTFT, 29–38% lower mean per-turn latency and up to 57% higher peak throughput.
- Strongest direct pressure on semantic ReuseHint/StateAffinity necessity.
- Server evidence, not smartphone evidence.

See [deep.md](deep.md).
