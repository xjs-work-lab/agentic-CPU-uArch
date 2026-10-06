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
origin_paths = ["03-academic/paper-10q/PAPER-052.md"]
origin_blobs = ["3b30d53e4a812546c1edd4f93dbdacddbeaa8c80"]
authors = ["Feiyang Chen", "Haibo Chen"]
venue = "arXiv preprint · 2026-06-15"
+++

# PAPER-052 — SMEPilot: Characterizing and Optimizing LLM Inference with Scalable Matrix Extensions

## 30-second read
- **Why it matters:** Shows CPU matrix extensions can materially change the feasible region for on-device AI and that operator/shape/layout determine the best CPU path.
- **What it establishes:** CPU matrix acceleration can materially expand CPU-local AI viability under evaluated settings.
- **Boundary:** LLM inference, not end-to-end Agent; up-to speedup is not universal and does not by itself compare Huawei CPU vs NPU.
- **Primary source:** https://arxiv.org/abs/2606.16332

## Migration fidelity
- V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- Transform: `STRUCTURAL_REPACK`
- Detailed V1 interpretation is preserved in [deep.md](deep.md).
- Source independence remains `UNKNOWN` unless explicitly assessed later.
