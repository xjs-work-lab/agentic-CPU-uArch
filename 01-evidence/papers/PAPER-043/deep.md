# PAPER-043 — Proactive Agent — EDP v1 FULL_10Q

Re-reviewed: 2026-10-07

## Q1 — Problem + target mapping
Can an Agent infer from human activity when assistance is appropriate before an explicit request?

For A this is the most direct early competing baseline:
Demand can be partially inferred from observable history.

## Q2 — Novelty / new-regime relevance
The paper builds a data-driven proactive Agent and benchmark with human judgments of whether proposed help is needed/acceptable.

Peer-reviewed at ICLR 2025.

## Q3 — Falsifiable hypothesis
Activity history should contain enough signal to predict useful proactive interventions, and fine-tuning on proactive examples should improve precision/F1 relative to base models.

## Q4 — Research lineage / competing route
Tsinghua / Renmin / Huawei Noah's Ark / Peng Cheng Laboratory.

Independent from PARE and ProAgentBench.

This work is an early baseline for later long-history real-world proactive datasets.

## Q5 — Mechanism / control point
Data pipeline:
- collect real human activity;
- generate candidate proactive predictions;
- human annotators accept/reject/reject-all;
- train a reward model as evaluator;
- synthesize/generate larger proactive training set;
- SFT proactive models.

Hindsight categories include need/no-need and correct/false intervention states.

Control point remains Agent-side prediction.

## Q6 — Experiment design + quantitative results
ProactiveBench:
- Agent training set: 6,790 events over 136 scenarios;
- real-world test set: 233 events across 12 scenarios;
- categories: coding, writing, daily life.

Reward-model labels:
- 1,760 human-annotated entries;
- random split 1,640 train / 120 test;
- three annotators per prediction, majority vote;
- human agreement reported >91.67% on test;
- trained reward model F1 91.80%.

Agent table:
Qwen2-7B-Proactive:
- Recall 100.00%
- Precision 49.78%
- Accuracy 50.66%
- False-Alarm 50.22%
- F1 66.47%

LLaMA-3.1-8B-Proactive:
- F1 66.25%

GPT-4o:
- F1 64.60%.

The paper itself notes a tendency to over-assist.

## Q7 — Artifact / reproducibility
Peer-reviewed paper and public repository exist.

Important provenance:
the large 6,790 Agent training set is generated through the gym/synthesis process; the 233-event test set is real-world.

The reward-model split is random at annotated-entry level.
Earlier repository audit found repeated candidate rows per observation history; any new classifier replay must group by observation history to avoid leakage.

## Q8 — Evidence vs alternatives
Demonstrated:
- assistance demand is learnable from ordinary behavior;
- false alarm is a major failure mode;
- proactive fine-tuning changes prediction behavior.

Not demonstrated:
- these labels equal online phone RequiredProgress;
- false-alarm row fractions equal wasted phone compute;
- lower layers need Agent-private semantics.

## Q9 — Decision contribution
Strengthens CLM-AGENT-002 and B4-TX.

This is **negative pressure on A differentiation**:
a history-based model can recover part of what A might otherwise call privileged demand knowledge.

But it does not kill A because RequiredProgress may encode active branch/task value not inferable from external behavior.

## Q10 — Next action
KEEP P0.

EXP-A-001 must:
- use grouped/user-aware splits;
- include a long-history learned demand predictor;
- measure cost-weighted false positives/false negatives;
- compare against internal DemandState only after matching observable history.

## Decision footer
- Evidence maturity: STRUCTURAL_SIGNAL
- Decision impact: HARDEN B4-TX; A remains open
- Open questions: phone transfer; intrinsic-state residual; cost-weighted utility
- Primary source: https://arxiv.org/abs/2410.12361
- Artifact: https://github.com/thunlp/ProactiveAgent
