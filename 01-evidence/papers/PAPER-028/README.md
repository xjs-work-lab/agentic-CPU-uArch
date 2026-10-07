+++
id = "PAPER-028"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "B_RESIDUAL_FUTURE_REUSE_PREDICTION_STRONG_BASELINE"
independence_assessment = "PREPRINT_SERVER_GPU_NO_TARGET_PHONE"
title = "Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management"
primary_url = "https://arxiv.org/abs/2605.06472"
priority = "P0"
evidence_role = "strong workflow/history/semantic reuse-prediction baseline"
authors = ["Haoyu Zheng", "Fangcheng Fu", "Jia Wu", "Binhang Yuan", "Yongqiang Zhang", "Hao Wang", "Yuanyuan Zhu", "Xiao Yan", "Jiawei Jiang"]
venue = "arXiv preprint · 2026"
+++

# PAPER-028 — PBKV

## 30-second read
- Predicts several future Agent invocations from call-graph topology, workflow-prefix history and a prefill hidden-state signal.
- Uses predictions for hierarchical KV eviction and conservative prefetch.
- Server testbed: 8× NVIDIA A6000 48 GB, 128 vCPUs, 512 GB host memory; Qwen3-14B/32B.
- Reports up to 1.85× lower workflow latency vs LRU on dynamic workflows and up to 1.26× vs KVFlow on static workflow.
- Lifecycle-aware eviction alone can improve hit rate substantially; semantic-signal incremental value is not isolated cleanly.
- Strong B-residual baseline: future reuse can be inferred in software without an explicit semantic ABI.
- No smartphone evidence.

See [deep.md](deep.md).
