+++
id = "PAPER-100"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "HIERARCHICAL_GUI_EXECUTION_SOFTWARE_BASELINE"
independence_assessment = "PREPRINT_REMOTE_EXECUTOR_NOT_ON_DEVICE"
title = "Jev-Mobile: Jev as an Executor for Mobile GUI Agents"
primary_url = "https://arxiv.org/abs/2609.30186"
priority = "P1"
evidence_role = "hierarchical mobile GUI baseline separating low-frequency VLM goals from high-frequency typed execution over live accessibility-tree candidates"
authors = ["Linghua Zhang"]
venue = "arXiv preprint 2026"
+++

# PAPER-100 — Jev-Mobile

## 30-second read
- **Mechanism:** one VLM call delegates a local goal; a typed decision service repeatedly chooses live accessibility-tree actions until DONE/BLOCKED.
- **Reported result:** 79% AndroidWorld success vs 84% step-wise VLM, with successful-trajectory mean time 132.67s vs 197.21s and model cost substantially lower.
- **Critical boundary:** Jev is a remote service; “local goal” does **not** mean on-device executor.
- **Project impact:** raises A/PT-A software baseline for hierarchical delegation and observation-bound action execution; no mobile hardware conclusion.

See [deep.md](deep.md) for full Paper Insight 10Q.
