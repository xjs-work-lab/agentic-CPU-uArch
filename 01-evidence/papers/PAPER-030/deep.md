# PAPER-030 — AgentProg — FULL_10Q

## Source
- MobiSys 2026
- Primary: https://arxiv.org/abs/2512.10371
- Official conference page: https://www.sigmobile.org/mobisys/2026/accepted_papers/
- Code: https://github.com/MobileLLM/AgentProg
- Review: FULL_10Q / EDP v1
- Priority: P0

## Q1 — Problem
Long-horizon mobile GUI Agents lose task-critical information as interaction history grows.

## Q2 — New-regime relevance
AgentProg introduces Semantic Task Program, explicit variables/control flow, execution-tree pruning, a program counter and Global Belief State.

This is Agent-native at S0/S1, not a lower physical-memory mechanism.

## Q3 — Hypothesis
Program structure should retain task-critical information better than sliding windows, summarization and hierarchical planning.

## Q4 — Baselines
M3A-style summarization, UI-TARS windowing and Mobile-Agent-v3 hierarchical planning/history.

## Q5 — Mechanism
Retain variables needed downstream, prune inactive/completed history, retrieve active-path context, and detect belief–reality mismatch for correction/replanning.

No physical KV/memory/storage validity contract is introduced.

## Q6 — Experiment
Official MobiSys materials report:
- AndroidWorld success 78.0%;
- AW-Extend success 68.4%;
- AW-Extend tasks average over 30 steps.

The public review also flags significant latency/inference-cost concerns.

## Q7 — Limitations
Peer-reviewed and open-source, but:
- evaluates Agent correctness/context, not cross-tier coherence;
- semantic planning/belief maintenance adds inference cost;
- no experiment tests whether S0/S1 revision should preserve/invalidate S2/S3 artifacts;
- no phone CPU/uArch attribution.

## Q8 — Evidence
FACT: semantic/program state improves long-horizon mobile Agent robustness.
FACT: large benefit is realized entirely in Agent runtime/context management.
INFERENCE: semantic state value does not by itself justify a cross-tier state fabric.
NOT ESTABLISHED: incremental S0/S1→S2/S3 validity information.

## Q9 — Project decision
Two-sided result: strengthens semantic-state product relevance while strengthening S0/S1 software sufficiency.

Net: narrow B-residual, no promotion.

## Q10 — Next
EXP-BR-001 must show incremental target-phone value after AgentProg-class context management is already present.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for mobile semantic/context management
- Cross-tier maturity: STRUCTURAL_SIGNAL only
- Primary source: https://arxiv.org/abs/2512.10371
