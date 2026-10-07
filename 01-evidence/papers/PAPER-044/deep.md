# PAPER-044 — ProAgentBench — EDP v1 FULL_10Q

Re-reviewed: 2026-10-07

## Q1 — Problem + target mapping
Proactive systems need to decide when to assist from real continuous behavior rather than isolated synthetic prompts.

For A, this is a strong generic-history competitor to explicit DemandState.

## Q2 — Novelty / new-regime relevance
The benchmark contributes:
- long continuous real-user sessions;
- pre-assistance context;
- When-to-Assist + How-to-Assist decomposition;
- time-aware evaluation.

This is not an A mechanism; it is a strong B4 source.

## Q3 — Falsifiable hypothesis
Real and longer behavioral history should improve proactive timing/content prediction relative to synthetic/short-context baselines.

## Q4 — Research lineage / competing route
Independent group from P043.
It extends the proactive-prediction line from generated/human-labeled examples to real longitudinal sessions.

## Q5 — Mechanism / control point
Inputs:
- screenshots/activity;
- timestamps;
- app/window metadata;
- user history.

Task:
- binary When-to-Assist;
- conditional How-to-Assist.

This is a learned Agent-side predictor from observable user context.

## Q6 — Experiment design + quantitative results
Dataset:
- 17 participants in released dataset;
- 28,528 events;
- 7,222 LLM-related events (~25.3%);
- 500+ hours;
- 167,423 screenshots in released artifact;
- student-heavy participant population.

Protocol:
- isolate each user's history;
- use time-based splits;
- choose contextually similar negative moments rather than trivial inactivity.

Fine-tuning comparison uses 741 real instances and an equal-size synthetic set.

LLaMA-3.1-8B-Instruct:
- zero-shot When accuracy 57.3%, F1 66.7%;
- synthetic SFT ~62.1% accuracy / 70.2% F1;
- real-world SFT 74.0% accuracy / 78.5% F1;
- How-to-Assist intention accuracy 34.8% synthetic vs 42.1% real.

Qwen3-VL-8B-Instruct:
- zero-shot 51.7% accuracy / 66.1% F1;
- synthetic SFT 54.8% / 67.8%;
- real-world SFT 63.5% / 72.4%.

Context ablation tests ~10 s through 10 min.
Longer history improves timing and intent metrics; the paper reports diminishing returns for intention accuracy beyond ~5 minutes.

## Q7 — Artifact / reproducibility
Public dataset is organized by participant and time.

Important boundary:
the protocol is time-based within isolated user histories; it is not equivalent to leave-one-user-out generalization.
Personal history can therefore be part of the strong baseline.

Released text annotations may be model-generated and can contain noise.

## Q8 — Evidence vs alternatives
Demonstrated:
- real long-history behavior materially improves assistance timing prediction;
- synthetic data misses behavioral structure.

Critical interpretation boundary:
the benchmark's positive assistance triggers are anchored to observed user help-seeking / LLM-use events.
That is a strong proxy for when the user sought AI help, but not direct ground truth for:
- counterfactual optimal intervention time;
- Agent internal RequiredProgress;
- optional/speculative branch value.

## Q9 — Decision contribution
This materially hardens CLM-AGENT-002 and B4-TX.

A cannot claim:
“history cannot infer demand.”

A can only claim residual value if explicit internal DemandState separates states that remain observationally similar under this kind of long-history/personalized baseline.

## Q10 — Next action
KEEP P0.

EXP-A-001 should use:
- user-personalized/time-based B4;
- matched-observability pairs;
- calibration and cost-weighted error;
- real phone system outcome before SYSTEM_VALUE promotion.

## Decision footer
- Evidence maturity: STRUCTURAL_SIGNAL
- Decision impact: HARDEN B4-TX; A residual becomes conditional-information test
- Open questions: cross-user transfer; phone mapping; optimal-intervention vs observed-help trigger
- Primary source: https://arxiv.org/abs/2602.04482
- Dataset: https://huggingface.co/datasets/qv9n2xk7m1z8pt4/ProAgentBench
