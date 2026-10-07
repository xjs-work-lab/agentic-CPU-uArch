+++
id = "PAPER-097"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "AGENT_FLOW_HETERO_SOC_BASELINE"
independence_assessment = "PREPRINT_COMMODITY_HETERO_SOC"
title = "Agent.xpu: Efficient Scheduling of Agentic LLM Workloads on Heterogeneous SoC"
primary_url = "https://arxiv.org/abs/2506.24045"
priority = "P0"
evidence_role = "Agent-native mixed reactive/proactive flow baseline for NPU-iGPU scheduling, preemption and shared-memory contention"
authors = ["Xinming Wei", "Jiahao Zhang", "Haoran Li", "Jiayu Chen", "Haoning Guan", "Rui Qu", "Maoliang Li", "Xiang Chen", "Guojie Luo"]
venue = "arXiv preprint, v2 2026"
+++

# PAPER-097 — Agent.xpu

## 30-second read
- **Agent-new regime:** foreground reactive flows and background proactive flows coexist as long-lived stateful LLM flows rather than isolated one-shot inference.
- **Control points:** heterogeneous execution graph, stage-elastic NPU/iGPU mapping, bandwidth-aware dispatch, fine-grained preemption and slack-aware proactive piggybacking.
- **Reported value:** 91–97% lower reactive latency in mixed workloads, 1.2–4.9× proactive throughput in evaluated comparisons, and lower energy/iGPU usage.
- **Boundary:** Intel Core Ultra commodity hetero-SoC, not a smartphone; same research lineage as HeRo.
- **Project impact:** strong Agent-aware C / CG-06 baseline; does not by itself establish target-phone differentiated residual.

See [deep.md](deep.md) for full Paper Insight 10Q.
