+++
id = "PAPER-088"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "STRONG_SOFTWARE_BASELINE_WITH_PREPRINT_BOUNDARY"
independence_assessment = "PREPRINT_PROACTIVE_MOBILE_AGENT"
title = "Perceive Before Reasoning: A Pre-Reasoning Perception Framework for Efficient and Reliable Proactive Mobile Agents"
primary_url = "https://arxiv.org/abs/2606.03236"
priority = "P0"
evidence_role = "strong software baseline for lightweight intervention gating and candidate-function compression before expensive proactive-Agent reasoning"
authors = ["Zhijie Ding", "Weinan Hong", "Zicheng Zhu", "Lei Li", "Dezhi Kong"]
venue = "arXiv preprint 2026"
+++

# PAPER-088 — PRPF

## 30-second read
- **Why it matters:** Directly pressure-tests the assumption that proactive/always-on Agent context must repeatedly invoke a heavy reasoner.
- **Mechanism:** lightweight Multimodal Proactive Perceptor first decides whether to intervene and compresses the candidate function pool; heavy Proactive Agent Reasoner runs only after the gate.
- **Reported result:** Success Rate 20.82% → 41.15%, False Trigger Rate 13.76% → 7.21%, expected inference compute −69.3%, end-to-end latency −60.1% vs ProactiveMobile 7B baseline.
- **Crucial boundary:** efficiency experiments are GPU benchmark measurements/training on NVIDIA H20, not commercial smartphone power or battery measurements.
- **Portfolio meaning:** PRPF-class gating becomes a mandatory strongest baseline for CG-07; 'always-on Agent' alone cannot justify a dedicated hardware domain.
- **Primary source:** https://arxiv.org/abs/2606.03236

See [deep.md](deep.md) for full Paper Insight 10Q.