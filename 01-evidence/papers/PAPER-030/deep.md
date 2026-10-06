> V1 semantic source copied/repacked from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.

# PAPER-030 — AgentProg: Empowering Long-Horizon GUI Agents with Program-Guided Context Management

## Source
- Paper: https://arxiv.org/abs/2512.10371
- Venue: MobiSys 2026
- Authors: Shizuo Tian, Hao Wen, Yuxuan Chen, Jiacheng Liu, Shanhui Zhao, Guohong Liu, Ju Ren, Yunxin Liu, Yuanchun Li
- Target: long-horizon mobile GUI Agents / AndroidWorld + AW-Extend
- Project relevance: Candidate B semantic-state value; mobile S0/S1 baseline
- Priority: P0

## Q1 — What problem is being solved?
Long-horizon mobile GUI Agents accumulate large interaction histories and lose task-critical information when generic truncation/compression is used.

## Q2 — What is new vs generic?
AgentProg structures history as a Semantic Task Program with control flow, variables, execution-tree pruning and belief-state updates.

Classification: **Agentic-native at the semantic/context layer**, but not a lower-level memory-system mechanism.

## Q3 — Falsifiable hypothesis
Program semantics can identify what must persist and what can be discarded better than generic summarization/windowing/hierarchical planning.

## Q4 — Research lineage / competitors
- summarization;
- sliding-window history;
- hierarchical mobile-Agent planning;
- generic memory retrieval.

## Q5 — Mechanism / control point
Inputs:
- semantic task program;
- program counter;
- control-flow path;
- explicit variables;
- global belief state.

Actions:
- retain critical variables;
- prune inactive branches / stale loop history;
- retrieve step-specific history.

Layer: **Agent runtime/context construction (S0/S1)**.

## Q6 — Experiment
MobiSys 2026 reports:
- 78.0% success on AndroidWorld;
- 68.4% on AW-Extend;
- ~9k dynamic context tokens in the long-horizon analysis versus ~17k for Mobile-Agent-v3;
- practical latency/inference-cost concerns remain.

## Q7 — Artifact
Public code: https://github.com/MobileLLM/AgentProg

## Q8 — Evidence vs hypothesis
**[FACT]** Explicit semantic/program structure materially improves mobile Agent context selection and retention.

**Boundary:** it does not show that S0/S1 semantics must be propagated to S2/S3 system memory/KV placement. Much of the benefit is captured entirely at D0 Agent runtime.

## Q9 — Project contribution
This is a two-sided result for Candidate B:
- positive: semantic state has real mobile value;
- negative: large value can be captured before the memory-system boundary.

Therefore B cannot justify a cross-tier system fabric merely by showing that semantic state matters.

## Q10 — Next action
- KEEP as P0 Candidate-B evidence.
- Treat as strongest mobile D0 semantic-state baseline.
- Require any B system contract to beat/extend D0 program-guided state management.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for mobile Agent semantic/context management; STRUCTURAL_SIGNAL for cross-tier B
- Decision impact: NARROW Candidate B
- Open questions: whether semantic state changes S2/S3 physical-state decisions
- Primary source: https://arxiv.org/abs/2512.10371
