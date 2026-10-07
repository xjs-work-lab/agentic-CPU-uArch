+++
id = "PAPER-044"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "INDEPENDENT_GROUP"
title = "ProAgentBench: Evaluating LLM Agents for Proactive Assistance with Real-World Data"
primary_url = "https://arxiv.org/abs/2602.04482"
priority = "P0"
evidence_role = "real-world long-history personalized demand-prediction baseline"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
authors = ["Yuanbo Tang", "Huaze Tang", "Tingyu Cao", "Lam Nguyen", "Anping Zhang", "Xinwen Cao", "Chunkang Liu", "Wenbo Ding", "Yang Li"]
venue = "arXiv preprint · 2026"
+++

# PAPER-044 — ProAgentBench

## 30-second read
- 17 participants, 28,528 events, 500+ hours, with time-ordered per-user histories.
- Real-world SFT materially improves When-to-Assist over zero-shot/synthetic training; longer history helps, with diminishing returns for intent prediction beyond ~5 minutes.
- Evaluation isolates each user's history and uses time-based splits, so this is a strong personalized-history baseline rather than a clean cross-user generalization result.
- Ground truth is anchored to observed help-seeking/LLM-use triggers, not direct access to intrinsic Agent RequiredProgress.
- Primary source: https://arxiv.org/abs/2602.04482

See [deep.md](deep.md) for EDP v1 FULL_10Q.
