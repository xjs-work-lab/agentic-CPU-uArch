+++
id = "PAPER-013"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Speculative Interaction Agents: Building Real-Time Agents with Asynchronous I/O and Speculative Tool Calling"
primary_url = "https://arxiv.org/abs/2605.13360"
priority = "P1"
evidence_role = "speculative/discardable Agent work semantics"
origin_paths = ["03-academic/paper-briefs/PAPER-001-020.md"]
origin_blobs = ["71be54fd3d91d7c516a9dbaef224541b68e8a437"]
authors = ["Coleman Hooper", "Minwoo Kang", "Suhong Moon", "Nicholas Lee", "Eric Wen"]
venue = "arXiv preprint · 2026"
+++

# PAPER-013 — Speculative Interaction Agents: Building Real-Time Agents with Asynchronous I/O and Speculative Tool Calling

## 30-second read
- **Why it matters:** Shows Agent runtimes can generate work before it is necessarily committed/required.
- **What it establishes:** Speculative Agent execution creates ready work whose value/necessity can differ from mere executability.
- **Boundary:** Agent-runtime semantics; indirect for smartphone CPU/system value.
- **Primary source:** https://arxiv.org/abs/2605.13360

## Migration fidelity
- V1 baseline: `960abb4ef50a8f5b0bd357c067f08346025d`
- Transform: `STRUCTURAL_REPACK`
- Detailed V1 interpretation is preserved in [deep.md](deep.md).
- Source independence remains `UNKNOWN` unless explicitly assessed later.
