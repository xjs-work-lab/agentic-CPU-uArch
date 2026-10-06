+++
id = "PAPER-028"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management"
primary_url = "https://arxiv.org/abs/2605.06472"
priority = "P0"
evidence_role = "strong workflow/history/semantic reuse-prediction baseline"
origin_paths = ["03-academic/paper-10q/PAPER-028.md"]
origin_blobs = ["e61e4f8bb700f456bedea1fab5147e2551c5d434"]
authors = ["Haoyu Zheng", "Fangcheng Fu", "Jia Wu", "Binhang Yuan", "Yongqiang Zhang", "Hao Wang", "Yuanyuan Zhu", "Xiao Yan", "Jiawei Jiang"]
venue = "arXiv preprint · 2026"
+++

# PAPER-028 — Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management

## 30-second read
- **Why it matters:** PBKV occupies broad future-Agent-reuse-guided KV retention/prefetch space.
- **What it establishes:** Rich workflow/history signals can drive future KV reuse management without proving a cross-tier phone semantic contract is needed.
- **Boundary:** Server/GPU KV hierarchy; not smartphone S2/S3 or CPU-local proof.

## Migration fidelity
- frozen V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- transform: `STRUCTURAL_REPACK`
- detailed V1 interpretation is preserved in [deep.md](deep.md).
- source independence remains `UNKNOWN`.
