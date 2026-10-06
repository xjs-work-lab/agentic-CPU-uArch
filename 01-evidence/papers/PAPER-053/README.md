+++
id = "PAPER-053"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
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
**FULL 10Q COMPLETE — decision-grade only within the evaluated scope.**

Decision use:
- valid as a strong **software-baseline / workload-characterization** input;
- valid evidence that Agent-specific prompt/output structure can yield material software-only latency value on the evaluated M4 Pro + TinyAgent system;
- **not** valid as smartphone SYSTEM_VALUE;
- **not** evidence of DemandState value;
- **not** evidence of CPU/uArch necessity.

See [deep.md](deep.md) for the full Paper Insight 10Q.
