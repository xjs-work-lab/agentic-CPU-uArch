+++
id = "PAPER-039"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "INDEPENDENT_GROUP"
title = "HybridCUA: Learning to Orchestrate GUI and CLI for Computer-Use Agents"
primary_url = "https://arxiv.org/abs/2609.38008"
priority = "P0"
evidence_role = "learned GUI↔CLI routing strongest software baseline"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
authors = ["Tongbo Chen", "Junbo Niu", "Zhengxi Lu", "Niu Lian", "Fei Tang", "Yuchen Yan", "Yike Hong", "Yong Du", "Yizhou Liu", "Bofan Chen", "Yongliang Shen"]
venue = "arXiv preprint · 2026-09-29"
+++

# PAPER-039 — HybridCUA

## 30-second read
- Strong software baseline for learning **when and how** to use GUI vs CLI.
- Merely exposing CLI hurts the untrained base model: 38.8% GUI-only → 18.4% GUI+CLI on OSWorld.
- After mixed SFT + CLI-aware RL, GUI+CLI reaches 53.6% vs 50.4% for the comparably trained GUI branch and uses fewer steps.
- This means PT-A value is not “more tools”; it is selective, capability-aware routing and reliable execution.
- Desktop/computer-use evidence, not phone-system evidence.
- Primary source: https://arxiv.org/abs/2609.38008

See [deep.md](deep.md) for EDP v1 FULL_10Q.
