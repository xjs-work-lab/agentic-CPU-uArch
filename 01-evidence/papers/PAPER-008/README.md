+++
id = "PAPER-008"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "R2_AGENTIC_CPU_LOCALITY_SIGNAL_AND_AGORA_SOFTWARE_BASELINE"
independence_assessment = "ACADEMIC_PLUS_HYPERSCALER_PRODUCTION_AND_CONTROLLED_SERVER_STUDY"
title = "Architectural Implications of Agentic AI Workflows"
primary_url = "https://arxiv.org/abs/2608.04458"
priority = "P0"
evidence_role = "Agentic server CPU locality/context-switch structural signal; indirect mobile transfer"
authors = ["Jirong Yang", "Peizhe Liu", "Chaojie Zhang", "Jovan Stojkovic"]
venue = "arXiv preprint · 2026"
+++

# PAPER-008 — Architectural Implications of Agentic AI Workflows

## 30-second read
- Production Microsoft Azure study plus controlled open-source Agent-framework characterization.
- Agent execution is fragmented, bursty and heterogeneous; orchestration/tools put CPU on the critical path.
- Controlled study reports low IPC, high backend stalls and increasing context-switch/locality pressure with concurrency.
- Agora demonstrates strong software recovery on commodity servers.
- Role-aware pooling reduces tool CPU demand up to 46%, worst-case tool latency 13%, while retaining 99% serving throughput.
- Strong R2 structural signal, but also strong software-sufficiency evidence.
- No smartphone PMU/energy/thermal experiment.

See [deep.md](deep.md).
