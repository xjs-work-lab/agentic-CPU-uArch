+++
id = "PAPER-051"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "EdgeAgent: Orchestrating On-Device LLM inference for End-User Multi-Agent Systems on CPU-GPU Unified Memory Architectures"
primary_url = "https://arxiv.org/abs/2610.03394"
priority = "P0"
evidence_role = "C system-control evidence: generic UMA/SME optimization plus incremental Agent-aware scheduling"
origin_paths = ["03-academic/paper-10q/PAPER-051.md", "analysis/stage16a/public_evidence/README.md", "analysis/stage16a/results/pass2-public-evidence-summary.md"]
origin_blobs = ["4fae7a001ce8c3aaeceabc85205eadf2950afc6d", "21c60cd65c7148b97792a62e7570100ff5657f1e", "0e505a7589f0f6469836d1a9f0cfa6add8d69b43"]
authors = ["Yuhai Long", "Yuanxin Wei", "Kai Wu", "Jinhui Wei", "Dan Huang", "Jiangsu Du"]
venue = "arXiv 2026-10-02; ASPLOS 2027 proceedings metadata reported on paper page"
+++

# PAPER-051 — EdgeAgent: Orchestrating On-Device LLM inference for End-User Multi-Agent Systems on CPU-GPU Unified Memory Architectures

## 30-second read
- **Why it matters:** Separates substantial generic heterogeneous-execution gains from an additional Agent-aware scheduling increment on an end-user multi-Agent edge platform.
- **What it establishes:** Generic cross-layer execution optimization can be material; Agent-aware stall/scheduling logic can add further value beyond that stronger execution layer in the evaluated M4 setting.
- **Boundary:** Apple M4/M4 Pro-class edge system, not a Huawei smartphone; does not prove a new CPU-uArch feature is required.
- **Primary source:** https://arxiv.org/abs/2610.03394

## Quantitative anchors preserved from V1 Stage16A
- Generic/cross-layer UMA-aware SME + zero-copy execution: up to **1.29x** over Batch-SD.
- Agent-aware HAL scheduling on top of that stronger configuration: **1.05–1.17x** additional speedup.
- V1 normalized equivalent time-reduction range for that incremental factor: approximately **4.76–14.53%**.

These numbers remain scoped to the evaluated Apple M4/M4 Pro-class EdgeAgent setting.

## Migration fidelity
- V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- Transform: `STRUCTURAL_REPACK`
- Detailed V1 interpretation is preserved in [deep.md](deep.md).
- Source independence remains `UNKNOWN`.
