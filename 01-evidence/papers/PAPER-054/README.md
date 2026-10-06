+++
id = "PAPER-054"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "SEED_SCREENING_ONLY"
decision_use = "PENDING_10Q"
independence_assessment = "UNKNOWN"
title = "TimelyLLM: Time-sensitive LLM Serving System for Physical-I/O Limited Agents"
primary_url = "https://doi.org/10.1145/3745756.3809203"
priority = "P0"
evidence_role = "execution-aware generation scheduling and time-utility evidence; direct challenge/bridge for A, R1 and C"
authors = ["Neiwen Ling", "Guojun Chen", "Anurag Khandelwal", "Lin Zhong"]
venue = "ACM MobiSys 2026"
+++

# PAPER-054 — TimelyLLM

## 30-second read
- **Why it matters:** Treats Agent generation as execution-timed work rather than an always-run-to-completion LLM request.
- **What it establishes:** Segmented generation plus slack-aware scheduling can exploit the gap between plan generation and physical execution in evaluated agents.
- **Reported anchors:** up to 1.52x higher time utility and up to 84% lower agent waiting time in evaluated multi-agent workloads.
- **Portfolio pressure:** Strongly reinforces the need to distinguish ready work from useful-now work, but also raises the baseline for A/R1 because substantial value can be obtained from execution-aware software scheduling without new semantic-to-hardware mechanisms.
- **Boundary:** Evaluated on physical-I/O-limited agents, not yet smartphone persistent-agent SYSTEM_VALUE.
- **Primary source:** https://doi.org/10.1145/3745756.3809203


## Decision-use gate
This Source is currently **SEED SCREENING ONLY**.

Do not use it to change Direction lane/score, promote/demote a Bet, or assert a new project conclusion until a full Paper Insight 10Q review is completed.

The existing 30-second read / portfolio-pressure notes are retrieval and triage hypotheses only, not decision-grade conclusions.
