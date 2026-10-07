+++
id = "PAPER-113"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-08"
decision_critical = true
decision_use = "AO1_PERSONAL_AGENT_HETERO_SOC_FLOW_AWARE_EXECUTION"
independence_assessment = "ACADEMIC_PREPRINT_INTEL_HETERO_SOC_NO_SMARTPHONE"
title = "Agent.xpu: Efficient Scheduling of Agentic LLM Workloads on Heterogeneous SoC"
primary_url = "https://arxiv.org/abs/2506.24045"
priority = "P0"
evidence_role = "direct personal-agent heterogeneous-SoC mixed-criticality execution evidence"
authors = ["Xinming Wei","Jiahao Zhang","Haoran Li","Jiayu Chen","Haoning Guan","Rui Qu","Maoliang Li","Xiang Chen","Guojie Luo"]
venue = "arXiv preprint · v2 2026-01-06"
+++

# PAPER-113 — Agent.xpu

## 30-second read
- Full-text reviewed, not abstract-only.
- Targets personal Agent execution on an Intel Core Ultra heterogeneous SoC with CPU, iGPU and NPU sharing memory.
- The Agent-specific operating regime is concurrent reactive foreground and proactive background LLM flows with different latency/throughput objectives.
- Identifies operator-to-accelerator affinity, shared-DDR contention, stage-divergent batching and the absence of flow-aware runtime abstractions.
- Implements a Heterogeneous Execution Graph, NPU-iGPU stage elasticity, kernel/layer-boundary preemption and slack-aware piggybacking.
- Reports up to 2.4x proactive throughput over the iGPU serving baseline and 91–97% lower reactive mean latency under mixed load; energy/token is reported 26.8% lower than OpenVINO iGPU.
- Strong evidence for an Agent Execution Fabric problem, but the evaluated platform is an AI PC, not a smartphone, and the paper proves a software/runtime solution rather than hardware necessity.

See deep.md.
