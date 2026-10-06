+++
id = "PAPER-065"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "INDEPENDENT_ACADEMIC"
title = "KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows"
primary_url = "https://doi.org/10.52202/085713-4208"
priority = "P0"
evidence_role = "Agent-workflow topology and future-use distance as cache-retention/prefetch signal; A/C strongest software baseline for state-reuse identity"
authors = ["Zaifeng Pan", "Ajjkumar Patel", "Zhengding Hu", "Yipeng Shen", "Yue Guan", "Wanlu Li", "Lianhui Qin", "Yida Wang", "Yufei Ding"]
venue = "NeurIPS 2025"
+++

# PAPER-065 — KVFlow

## 30-second read
- **Why it matters:** Directly turns Agent workflow structure into a prediction of future state reuse.
- **What it establishes:** An Agent Step Graph and steps-to-execution (STE) can guide fine-grained KV-cache retention, eviction and prefetch for future Agent activations.
- **Reported anchors:** up to 1.83× over SGLang+HiCache for a large-prompt single-workflow setup and up to 2.19× in concurrent-workflow scenarios reported by the paper.
- **Portfolio meaning:** generic 'state-reuse identity / future-usefulness' is already software-capturable from workflow topology. A only gets credit for residual information beyond such reconstructible reuse-distance signals.
- **Boundary:** server GPU serving; not on-device phone evidence and not generic CPU cache/uArch evidence.
- **Primary source:** https://doi.org/10.52202/085713-4208

See [deep.md](deep.md) for full Paper Insight 10Q.