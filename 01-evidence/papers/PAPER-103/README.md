+++
id = "PAPER-103"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "T5_PRODUCT_TREND_AND_T7_MULTI_AGENT_RESIDUAL_PRESSURE"
independence_assessment = "SAME_IPADS_SJTU_LINEAGE_AS_MOBIAGENT_AGENTRR"
title = "Beyond Training: Enabling Self-Evolution of Agents with MOBIMEM"
primary_url = "https://arxiv.org/abs/2512.15784"
priority = "P0"
evidence_role = "direct Android/mobile evidence for memory-centric Agent evolution, verified action replay and fine-grained workflow scheduling; negative pressure on standalone multi-Agent novelty"
authors = ["Zibin Liu", "Cheng Zhang", "Xi Zhao", "Yunfei Feng", "Bingyu Bai", "Dahu Feng", "Erhu Feng", "Yubin Xia", "Haibo Chen"]
venue = "arXiv preprint, submitted 2025-12-15"
artifact_urls = ["https://github.com/IPADS-SAI/MobiAgent"]
+++

# PAPER-103 — MobiMem

## 30-second read
- **Strongest product signal:** reusable Experience/Action Memory can replace repeated model reasoning in recurring mobile workflows.
- **Direct phone evidence:** MobiMind-4B on Snapdragon 8 Elite via llama.cpp, CPU-only in the reported cross-hardware Action Memory experiment.
- **Action reuse:** ActTree 37.5% average reuse; ActChain 59.7% with LLM-generated templates and 77.3% with human-crafted templates.
- **Phone latency effect:** reported 1.6×–9× speedup across tasks on the Snapdragon setup.
- **Workflow scheduling:** fine-grained step-DAG scheduling reaches up to 1.98× over serial in evaluated multi-app scenarios.
- **Correctness path:** cached actions are checked against current UI hierarchy; failure discards reuse and falls back to Operator/LLM execution.
- **T5 impact:** materially strengthens the product trend for Agent state/experience/action lifecycle and reuse.
- **T7 impact:** does not isolate multi-Agent identity as the causal control point; most gains map to software-visible DAG/state/replay mechanisms.
- **Boundary:** paper is an arXiv preprint; the “flagship smartphone” deployment claim names Experience Memory + AgentRR only and does not disclose product/device/vendor or independently validate full-system deployment.

See [deep.md](deep.md) for the FULL_10Q decision card.
