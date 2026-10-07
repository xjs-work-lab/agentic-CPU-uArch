+++
id = "PAPER-104"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "T5_VERSIONED_STATE_AND_T7_MULTI_AGENT_SHARED_RUNTIME_PRESSURE"
independence_assessment = "PREPRINT_SINGLE_NJU_GROUP_NO_TARGET_PHONE_REPLICATION"
title = "LOCAL: Enabling Learning On-device Contiguously for Agent LLMs"
primary_url = "https://arxiv.org/abs/2608.15241"
priority = "P0"
evidence_role = "single-GPU Agent serving-plus-learning runtime with version-aware KV, foreground/background scheduling and cross-agent pre-prefill"
authors = ["Xinxin Liu", "Jiaxin Li", "Zibo Wang", "Yun Ji", "Zhangqi Zhu", "Qing Hu", "Zhibin Wang", "Rong Gu", "Sheng Zhong", "Chen Tian"]
venue = "arXiv preprint, submitted 2026-08-15"
+++

# PAPER-104 — LOCAL

## 30-second read
- **New-regime signal:** foreground Agent inference, delayed judging, LoRA training, adapter publication and KV maintenance share one model instance and one memory budget.
- **Correctness state:** reusable KV is keyed by token span + context namespace + logical adapter + adapter version.
- **Important T7 boundary:** Agent identity is provenance, not necessarily a hard cache key; different Agents may share KV when the actual validity tuple matches.
- **Cross-Agent signal:** pending communication can trigger speculative pre-prefill for a future consumer; reported TTFT p99 improves 21.9%.
- **Scheduling value:** foreground-first reduces queue-wait p95 3.1× vs FIFO while completing 34 training commits; interruptible training lowers p95 TTFT 1.55× vs non-preemptible training.
- **State-lifecycle value:** staged-version hot-prefix prefill lowers post-publish first-hit prefill p99 25.6%.
- **Memory coupling:** evaluated passing configurations peak at 21.6–23.5 GB on an RTX 3090-class 24 GB GPU.
- **Boundary:** this is not a smartphone/mobile-SoC experiment; no official public code artifact was verified during review.
- **Project impact:** strongly strengthens T5 software/runtime baseline and further narrows standalone T7 differentiation; no uArch implication.

See [deep.md](deep.md) for the FULL_10Q decision card.
