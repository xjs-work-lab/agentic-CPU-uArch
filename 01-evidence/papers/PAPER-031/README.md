+++
id = "PAPER-031"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Learning Agent Execution for KV-Cache Management in Agentic Serving"
primary_url = "https://arxiv.org/abs/2608.14624"
priority = "P0"
evidence_role = "strong history-only reuse baseline"
origin_paths = ["03-academic/paper-10q/PAPER-031.md"]
origin_blobs = ["801122351161cec63a5725b3c075d0ed0c33c530"]
authors = ["Rui Zhang", "Chaeeun Kim", "Shaoting Feng", "Kuntai Du", "Yuhan Liu", "Yi Zhong", "Cheng-Wei Ching", "Junchen Jiang", "Liting Hu"]
venue = "arXiv preprint · 2026"
+++

# PAPER-031 — Learning Agent Execution for KV-Cache Management in Agentic Serving

## 30-second read
- **Why it matters:** A lightweight first-order Agent transition model already captures substantial KV reuse without explicit semantic ABI fields.
- **What it establishes:** History-only prediction can materially improve Agent KV retention/prefetch.
- **Boundary:** Server/GPU serving; mobile transfer unproven.

## Migration fidelity
- frozen V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- transform: `STRUCTURAL_REPACK`
- detailed V1 interpretation is preserved in [deep.md](deep.md).
- source independence remains `UNKNOWN`.
