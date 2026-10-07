+++
id = "PAPER-114"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-08"
decision_critical = true
decision_use = "AO1_CPU_GPU_TOOL_KV_UNIFIED_CONTROL_STRONG_SOFTWARE_BASELINE"
independence_assessment = "ACADEMIC_PREPRINT_SERVER_H100_H200_OPENHANDS"
title = "MARS: Efficient, Adaptive Co-Scheduling for Heterogeneous Agentic Systems"
primary_url = "https://arxiv.org/abs/2604.26963"
priority = "P0"
evidence_role = "strong software baseline for coupled CPU-tool/GPU-inference/KV control"
authors = ["Yifei Wang","Hancheng Ye","Yechen Xu","Cong Guo","Chiyue Wei","Qinsi Wang","Dongting Li","Tingjun Chen","Hai Helen Li","Danyang Zhuo","Yiran Chen"]
venue = "arXiv preprint · v2 2026-06-15"
+++

# PAPER-114 — MARS

## 30-second read
- Full-text reviewed.
- Treats Agent execution as repeated GPU LLM rounds interleaved with CPU-side tool execution rather than a continuous decode stream.
- Introduces a Unified Information Stream across GPU KV pressure and CPU tool pressure, an external admission-control plane, and an internal Agent-centric scheduler.
- Couples execution priority with KV retention/eviction and warm resumption.
- H100/H200 + OpenHands server evidence, not mobile.
- Reports up to 5.94x controlled-testbed mean end-to-end latency improvement and 1.20–1.87x full OpenHands task-completion speedup over strongest compared baselines.
- Ablations show priority coordination, admission control and opportunistic state management each matter.
- Strong evidence that a large portion of AO-1 can be captured in software if cross-layer state is visible.

See deep.md.
