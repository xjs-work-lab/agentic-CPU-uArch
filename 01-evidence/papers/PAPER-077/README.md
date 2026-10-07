+++
id = "PAPER-077"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_EDGE_BOUNDARY"
independence_assessment = "PREPRINT_EDGE_AGENT_MEMORY_BENCHMARK"
title = "MemArena: An Ego-Centric Benchmark for On-Device Agentic Personal Memory Assistants at Scale"
primary_url = "https://arxiv.org/abs/2608.02613"
priority = "P0"
evidence_role = "systems-facing benchmark separating memory-backend accuracy, query latency and structured-ingest energy on an edge AI platform under dense long-horizon personal-memory workload"
authors = ["Jiadong Zhang", "Xiaosong Ma"]
venue = "arXiv preprint 2026"
+++

# PAPER-077 — MemArena

## 30-second read
- **Why it matters:** Separates memory-backend cost from reader-model inference under an activity-dense personal-memory workload.
- **Scale:** 50 agents × 15 simulated days, 10.3M dialog tokens, ~24.1K ego-observed tokens/agent/day.
- **Query-time result:** on one NVIDIA Spark GB10 edge node, BM25/Memobase/MemSearch add about 87/7/48 ms search latency; for most reader sizes this is a small share of TTFT.
- **Important asymmetry:** structured Memobase ingestion uses extractor-LLM calls; a 15-day cache is reported to cost ~52–1,222 kJ depending on extractor/model scale.
- **Portfolio meaning:** foreground retrieval is often relatively light; background ingest/structure building can be far more expensive.
- **Boundary:** edge AI node, not smartphone SoC; synthetic world; preprint.
- **Primary source:** https://arxiv.org/abs/2608.02613

See [deep.md](deep.md) for full Paper Insight 10Q.