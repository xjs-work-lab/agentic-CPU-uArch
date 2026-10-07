+++
id = "PAPER-043"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "INDEPENDENT_GROUP"
title = "Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance"
primary_url = "https://arxiv.org/abs/2410.12361"
priority = "P0"
evidence_role = "human-annotated proactive-demand predictor baseline + false-alarm pressure"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
authors = ["Yaxi Lu", "Shenzhi Yang", "Cheng Qian", "Guirong Chen", "Qinyu Luo", "Yesai Wu", "Huadong Wang", "Xin Cong", "Zhong Zhang", "Yankai Lin", "Weiwen Liu", "Yasheng Wang", "Zhiyuan Liu", "Fangming Liu", "Maosong Sun"]
venue = "ICLR 2025"
+++

# PAPER-043 — Proactive Agent

## 30-second read
- ICLR 2025, not merely an arXiv preprint.
- Human activity is predictive enough to train proactive-assistance models, but even the best fine-tuned model reports ~50% false-alarm in the paper's metric table.
- Test set uses 233 real-world events; the 6,790-event Agent training set is generated/synthetic from the gym pipeline.
- This strongly raises B4-TX: observable behavioral history is a credible demand proxy, but does not equal intrinsic Agent RequiredProgress.
- Primary source: https://arxiv.org/abs/2410.12361

See [deep.md](deep.md) for EDP v1 FULL_10Q.
