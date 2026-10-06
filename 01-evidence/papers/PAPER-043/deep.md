> V1 semantic source copied/repacked from frozen baseline `960abb4ef50a8f5b0bd357c067f08346025d`.
> Do not reinterpret this page as V2.2 metadata authority; the compact README owns the Source object.

# PAPER-043 — Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance

## Source
- Paper: https://arxiv.org/abs/2410.12361
- Authors: Yaxi Lu, Shenzhi Yang, Cheng Qian, Guirong Chen, Qinyu Luo, Yesai Wu, Huadong Wang, Xin Cong, Zhong Zhang, Yankai Lin, Weiwen Liu, Yasheng Wang, Zhiyuan Liu, Fangming Liu, Maosong Sun
- Venue/status: arXiv preprint, 2024
- Artifact: https://github.com/thunlp/ProactiveAgent
- Project relevance: A / C1 semantic demand / B4 demand-prediction baseline
- Priority: P0

## Q1 — What problem is the paper solving, and how does it map to smartphones?
Most LLM Agents are reactive. This work asks whether an Agent can infer from ongoing human activity when assistance is appropriate before an explicit request.

For this project the relevance is direct at the **Agent semantic/control** layer:
- useful intervention vs false alarm;
- missed need vs correct rejection;
- pre-decision observation history.

The collected behavior is largely desktop/workstation activity, so it is not direct smartphone CPU evidence.

## Q2 — Is the problem/new mechanism actually new?
Proactive intervention timing is Agentic-native relative to request-response inference.

The broad idea of learned proactive prediction is now established prior work; our novelty cannot be “predict when the user needs help.”

## Q3 — What falsifiable hypothesis is being tested?
Author hypothesis:
real human activity plus human accept/reject annotation can train/evaluate an Agent to decide when to proactively assist.

Project hypothesis derived from it:
a strong generic learned predictor may infer a substantial fraction of demand from observable history, reducing the residual information advantage of privileged Agent DemandState.

## Q4 — What is the research lineage / competing route?
Competing routes:
- always-reactive assistant;
- heuristic proactive trigger;
- LLM-as-trigger;
- reward-model / classifier-based assistance prediction;
- later long-history real-world approaches such as ProAgentBench.

## Q5 — What is the key technical mechanism / control point?
Input:
- observed human activity history.

Prediction:
- candidate proactive task / whether it should be accepted.

Human annotation is converted into four hindsight categories:
- Missed-Need (MN);
- Correct-Rejection (CR);
- Correct-Detection (CD);
- False-Alarm (FA).

Control point:
Agent runtime / proactive trigger, not OS/uArch.

## Q6 — How is the experiment designed?
The paper builds ProactiveBench with **6,790 events**, combining collected real-world activity and generated data.

The public repository exposes:
- test traces;
- annotation pipeline;
- reward-model train/test data;
- evaluation scripts.

Reported fine-tuned proactive model F1 reaches **66.47%**.

The public evaluation table also shows high recall but substantial false-alarm pressure for multiple models, demonstrating that proactive triggering remains difficult.

## Q7 — What data/artifact/reproducibility support exists?
Strong.

Public repository:
https://github.com/thunlp/ProactiveAgent

Decision-critical public artifact:
- `dataset/reward_data/train_data.jsonl`
- `dataset/reward_data/test_data.jsonl`

Paper Table 1 reports the reward-model split as **1,640 train / 120 test labels**.

Stage 15 direct audit of the current public repository artifact finds:
- **1,629 rows** in the current train JSONL;
- 120 rows in the current test JSONL;

This 11-row train-count difference is treated as an artifact/version/filtering provenance difference, not silently normalized.

Current-artifact details:
- 1,629 rows;
- only 313 unique observation histories;
- 1,387 candidate-task rows;
- 474 valid candidates;
- 913 invalid candidates.

Important:
multiple candidate rows share one observation history, so row-level random splitting creates leakage.

## Q8 — Do the results actually support the hypothesis?
**[FACT]** Human activity contains learnable proactive-assistance signals.

**[FACT]** Public data includes explicit accepted/rejected-style candidate labels.

**[OBSERVATION]** In the public training artifact, invalid candidate rows outnumber valid candidate rows.

**Boundary:** that row ratio is **not** an online false-alarm prevalence because several candidate tasks are generated for the same observation history.

**[INFERENCE]** The artifact is strong hindsight semantic evidence for A, but simultaneously strengthens B4 because it makes generic demand prediction trainable.

## Q9 — What is the real contribution / technology control point for us?
This paper changes A in two ways.

### Positive for A
Non-useful/premature proactive assistance is a real semantic category, not an invented scheduler label.

### Negative pressure on A
Demand is partly inferable from ordinary history.

Therefore A's residual cannot be:
> semantic demand exists.

It must be:
> explicit Agent-native DemandState / EffectCommit still changes outcomes after the strongest generic history predictor.

## Q10 — What should we do next?
- KEEP as P0 A/B4 evidence.
- Group train/test by observation-history identity; never row-random split.
- Use CD/FA only as hindsight proxy labels.
- Build B4 from pre-decision features only.
- Do not map false-alarm row fraction to phone non-required compute share.
- Combine with ProAgentBench long-history evidence.
- Require target-device traces for cost, foreground overlap and cancellation legality.

## Decision footer
- **Evidence maturity:** STRUCTURAL_SIGNAL for Agent demand semantics / public B4 training source
- **Decision impact:** KEEP; hardens A baseline
- **Open questions:** phone transfer; cost weighting; real cancellation boundaries
- **Primary source:** https://arxiv.org/abs/2410.12361
- **Artifact:** https://github.com/thunlp/ProactiveAgent
