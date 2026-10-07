+++
id = "PAPER-108"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "T6_SANDBOX_LIFECYCLE_STRONGEST_SOFTWARE_BASELINE"
independence_assessment = "INDEPENDENT_MULTI_INSTITUTION_RESEARCH"
title = "SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving"
primary_url = "https://arxiv.org/abs/2607.23933"
priority = "P0"
evidence_role = "strong server-side Agent sandbox lifecycle baseline; negative pressure on standalone T6 CPU residual"
authors = ["Yihui Zhang", "Tianyu Wo", "Jinghao Wang", "Xiaoyang Sun", "Menghao Zhang", "Cangzhou Yuan", "Li Li", "Chunming Hu", "Albert Y. Zomaya", "Renyu Yang"]
venue = "arXiv preprint v2, revised 2026-08-05"
+++

# PAPER-108 — SpecBox

## 30-second read
- Agent sandbox cold-start/residency is a real latency-memory tradeoff.
- Mechanisms: intent prediction, prewarm, cross-step prefetch, semantic result cache, mmap shared-memory transport.
- Evaluation: 16-core / 256 GiB server, Docker, 32 sandbox environments, 200 multi-turn traces.
- Reported up to 2.9× lower P99 E2E and 45.9% lower peak memory vs key baselines.
- No smartphone/JIT/code-cache evidence.
- T6 impact: strongest software-sufficiency pressure; maps to C + T5/B-residual.

See [deep.md](deep.md).
