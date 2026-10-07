+++
id = "PAPER-052"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "SMEPilot: Characterizing and Optimizing LLM Inference with Scalable Matrix Extensions"
primary_url = "https://arxiv.org/abs/2606.16332"
priority = "P0"
evidence_role = "CPU matrix/operator placement + layout-state reuse evidence for CG-06"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
origin_paths = ["03-academic/paper-10q/PAPER-052.md"]
origin_blobs = ["3b30d53e4a812546c1edd4f93dbdacddbeaa8c80"]
authors = ["Feiyang Chen", "Haibo Chen"]
venue = "arXiv preprint · 2026-06-15"
+++

# PAPER-052 — SMEPilot

## 30-second read
- Directly evaluates SME-enabled CPUs on Apple M4 Pro, MediaTek Dimensity 9500 and KunPeng server hardware.
- The core contribution is **within-CPU heterogeneous execution**: CPU-only vs SME-only vs cooperative SME+CPU selected by operator shape/arithmetic intensity.
- Tile partitioning, phase-aware attention pipelining and layout-state reuse each have explicit ablation support.
- The paper proves CPU-matrix/runtime viability versus CPU baselines; it does **not** prove smartphone CPU superiority over NPU.
- Reported energy measurement and GPU comparison are on Apple M4 Pro, not the phone.
- Primary source: https://arxiv.org/abs/2606.16332

See [deep.md](deep.md) for EDP v1 FULL_10Q.
