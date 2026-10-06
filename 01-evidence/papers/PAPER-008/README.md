+++
id = "PAPER-008"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Architectural Implications of Agentic AI Workflows"
primary_url = "https://arxiv.org/html/2608.04458"
priority = "P0"
evidence_role = "Agentic server CPU locality/context-switch structural signal; indirect mobile transfer"
origin_paths = ["03-academic/paper-10q/PAPER-008.md"]
origin_blobs = ["a41d685e7f3e071c52c0720c66af98aac0f95b93"]
authors = ["Jirong Yang", "Peizhe Liu", "Chaojie Zhang", "Jovan Stojkovic"]
venue = "arXiv preprint · 2026"
+++

# PAPER-008 — Architectural Implications of Agentic AI Workflows

- Direct Agentic CPU/system characterization shows context-switch growth and cache/branch locality pressure under concurrency.
- V1 anchors: IPC ~1.2–1.6; backend stalls ~43–47%; L1D MPKI ~14–20; SWE-Agent involuntary context switches ~71/s→~660/s as concurrency rises 1→32.
- Role-aware pooling/pinning can reduce tool CPU demand by up to ~46%.
- **Boundary:** server/datacenter evidence; cannot establish smartphone R2 SYSTEM_VALUE.

Exact frozen V1 interpretation is preserved in [deep.md](deep.md).
