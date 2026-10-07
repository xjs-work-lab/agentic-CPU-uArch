+++
id = "PAPER-115"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-08"
decision_critical = true
decision_use = "AO1_CPU_TOOL_CRITICAL_PATH_AND_SOFTWARE_SCHEDULING_BASELINE"
independence_assessment = "ACADEMIC_PREPRINT_TWO_SERVER_CPU_GPU_PLATFORMS_NO_MOBILE"
title = "Towards Understanding, Analyzing, and Optimizing Agentic AI Execution: A CPU-Centric Perspective"
primary_url = "https://arxiv.org/abs/2511.00739"
priority = "P0"
evidence_role = "CPU/tool critical-path characterization plus CPU-GPU scheduling baseline"
authors = ["Ritik Raj","Souvik Kundu","Ishita Vohra","Hong Wang","Tushar Krishna"]
venue = "arXiv preprint · v3 2026-04-16"
+++

# PAPER-115 — CPU-Centric Agentic AI Execution

## 30-second read
- Full-text reviewed.
- Characterizes Agent workloads by orchestrator location, static/dynamic execution path and single/multi-step flow.
- Profiles Toolformer, SWE-Agent, Haystack RAG, ChemCrow and a LangChain web Agent on two CPU-GPU systems.
- Tool execution can dominate E2E latency; faster GPU inference can shift the bottleneck toward CPU tools.
- CPU throughput can saturate due to LLC/I/O pressure, Python multiprocessing, oversubscription and context switching before the GPU becomes the limiting resource.
- COMB and MAS demonstrate substantial recovery through software CPU-GPU co-scheduling.
- Strong structural evidence for AO-1, but server tools and large CPU/GPU systems are not direct smartphone evidence.

See deep.md.
