# PAPER-039 — HybridCUA — EDP v1 FULL_10Q

Re-reviewed: 2026-10-07

## Q1 — Problem + target mapping
A unified computer-use Agent can access GUI and CLI, but current models often fail to decide when CLI helps and how to execute it reliably.

PT-A mapping: strongest software baseline for dynamic modality routing.

## Q2 — Novelty / new-regime relevance
HybridCUA constructs GUI-only, CLI-only and interleaved trajectories, then trains a unified model with SFT + CLI-aware RL.

Classification: generic CUA routing baseline; not mobile-specific.

## Q3 — Falsifiable hypothesis
If action-surface access alone is sufficient, adding CLI should improve the base model.

It does the opposite. Learned routing/execution supervision is required.

## Q4 — Research lineage / competing route
Dataset:
- 5,023 SFT trajectories;
- 3,000 verified RLVR tasks.

Important correction:
“HybridCUA-8K” is not 8,000 equivalent demonstrations.

Competes with:
- GUI-only CUA;
- tool/API-augmented CUA;
- deterministic routing systems such as PhoneHarness.

## Q5 — Mechanism / control point
SFT teaches a unified action grammar.

RL uses:
- task-level CLI-preference reward, based on whether a successful rollout matches the task's CLI-use label;
- step-level execution penalty for failed shell commands.

Thus the model learns both **when** to delegate to CLI and **how reliably** to execute commands.

## Q6 — Experiment + ablations
OSWorld:
- base GUI-only: 38.8%, 31.6 avg steps;
- base GUI+CLI: 18.4%, 22.1 steps — shorter due to early failure, not efficiency;
- after SFT GUI: 44.2%, 26.3;
- after SFT GUI+CLI: 46.0%, 19.8;
- after SFT+RL GUI: 50.4%, 22.1;
- after SFT+RL GUI+CLI: 53.6%, 14.0.

Hence the fair incremental hybrid accuracy gain after matched training is about +3.2 percentage points, not the headline +14.8 pp against raw base.

OOD:
- OSWorld-MCP: 47.1%;
- WindowsAgentArena: 36.0%.

Reward ablations:
- remove task CLI reward: accuracy changes little but efficiency gain shrinks; CLI share 58.9% vs 64.0%;
- remove execution penalty: execution errors rise to 16.5% vs 11.5%.

## Q7 — Reproducibility / metric boundary
Public project/data page exists.

The 53.6 “Acc.” can include partial evaluator credit; it should not automatically be read as full-task success rate.

Training is large-scale GPU work; deployment is desktop/computer-use, not smartphone.

## Q8 — Evidence vs alternatives
Demonstrated:
- added affordance increases policy complexity;
- trained selective routing improves efficiency and accuracy.

Not demonstrated:
- the same learned policy transfers to Android permissions/runtime constraints;
- a platform runtime should expose unrestricted shell access.

## Q9 — Decision contribution
Strongly supports CLM-PTA-003:
hybrid routing is an active/crowded software mechanism space.

It also changes PT-A wording:
> “expose more action surfaces” is not itself a platform value proposition.

The runtime must express capabilities, authority, expected effects and execution feedback so routing can be selective.

## Q10 — Next action
KEEP P0 strongest baseline.
Use trained selective routing, not naive “all tools available,” as PT-A baseline.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for computer-use routing; phone transfer unproven
- Decision impact: strengthen Platform-Track classification and narrow PT-A control point
- Open questions: phone privilege, safety-aware routing, latency/energy
- Primary source: https://arxiv.org/abs/2609.38008
