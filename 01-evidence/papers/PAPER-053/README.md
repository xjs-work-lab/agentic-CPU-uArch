+++
id = "PAPER-053"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "SEED_SCREENING_ONLY"
decision_use = "PENDING_10Q"
independence_assessment = "UNKNOWN"
title = "Agent-X: Full Pipeline Acceleration of On-device AI Agents"
primary_url = "https://doi.org/10.1145/3745756.3809195"
priority = "P0"
evidence_role = "direct on-device Agent workload characterization and software-only full-pipeline acceleration; baseline pressure for A/C and workload evidence for second-Bet search"
authors = ["Jinha Chung", "Byeongjun Shin", "Jiin Kim", "Minsoo Rhu"]
venue = "ACM MobiSys 2026"
+++

# PAPER-053 — Agent-X: Full Pipeline Acceleration of On-device AI Agents

## 30-second read
- **Why it matters:** Directly characterizes on-device Agent workloads rather than generic mobile LLM inference.
- **What it establishes:** In the evaluated Agent workloads, both prefill and decode materially contribute to end-to-end latency; software-only prompt/prefix-cache restructuring plus lightweight speculative decoding can yield substantial end-to-end gain without accuracy loss.
- **Reported anchor:** 1.61x end-to-end speedup on representative evaluated Agent workloads.
- **Portfolio pressure:** Strengthens the strong-software baseline that A/C must beat and shows Agent-specific execution structure is exploitable without new hardware.
- **Boundary:** Does not establish DemandState value, Huawei-phone transfer, or CPU/uArch necessity.
- **Primary source:** https://doi.org/10.1145/3745756.3809195


## Decision-use gate
This Source is currently **SEED SCREENING ONLY**.

Do not use it to change Direction lane/score, promote/demote a Bet, or assert a new project conclusion until a full Paper Insight 10Q review is completed.

The existing 30-second read / portfolio-pressure notes are retrieval and triage hypotheses only, not decision-grade conclusions.
