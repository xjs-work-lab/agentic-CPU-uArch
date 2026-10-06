+++
id = "PAPER-033"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "LOCAL: Enabling Learning On-device Contiguously for Agent LLMs"
primary_url = "https://arxiv.org/abs/2608.15241"
priority = "P0"
evidence_role = "version-aware Agent KV validity baseline"
origin_paths = ["03-academic/paper-10q/PAPER-033.md"]
origin_blobs = ["fe55dc1e4c695785e1ee45d39d98c35e61ebad7d"]
authors = ["Xinxin Liu", "Jiaxin Li", "Zibo Wang", "Yun Ji", "Zhangqi Zhu", "Qing Hu", "Zhibin Wang", "Rong Gu", "Sheng Zhong", "Chen Tian"]
venue = "arXiv preprint · 2026"
+++

# PAPER-033 — LOCAL: Enabling Learning On-device Contiguously for Agent LLMs

## 30-second read
- **Why it matters:** Shows adapter/version identity can directly govern KV validity and multi-Agent preparation.
- **What it establishes:** Version-aware KV/runtime state is already an active Agent systems mechanism.
- **Boundary:** 24 GB single-GPU evaluation; not smartphone SYSTEM_VALUE.

## Migration fidelity
- frozen V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- transform: `STRUCTURAL_REPACK`
- detailed V1 interpretation is preserved in [deep.md](deep.md).
- source independence remains `UNKNOWN`.
