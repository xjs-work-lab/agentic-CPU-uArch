> V1 semantic source copied from frozen baseline `960abb4ef50a8f5b0bd357c067f08346025d`.
> The compact README owns the V2.2 Source metadata.

# PAPER-040 — PhoneHarness: Harnessing Phone-Use Agents through Mixed GUI, CLI, and Tool Actions

## Source
- Paper: https://arxiv.org/abs/2606.14832
- Authors: Chenxin Li, Zhengyao Fang, Zhengyang Tang, Pengyuan Lyu, Xingran Zhou
- Venue/status: arXiv preprint, 2026
- Target: mobile/phone Agent mixed-action workflows
- Project relevance: hybrid actuation + verifiable side effects
- Priority: P0

## Q1 — Problem
Phone-use tasks often require a mixture of GUI, CLI and structured tools, and success should be verified by actual side effects rather than a plausible textual completion.

## Q2 — New-regime relevance
Directly Agentic + mobile. It makes action-surface selection and execution verification first-class.

## Q3 — Hypothesis
A mixed-action harness with deterministic-first routing and execution-based verification improves reliable phone task completion over narrower action spaces.

## Q4 — Competing route
Strong direct pressure against a broad project Bet around:
- mixed GUI/CLI/tool action space;
- deterministic-first routing;
- execution verification.

## Q5 — Mechanism
- GUI proxy;
- device CLI actions;
- host-side tools;
- deterministic-first routing;
- rule/state-based verification of actual effects.

## Q6 — Experiment
Reported:
- 75.0% overall pass rate;
- +12.9 percentage points over strongest non-PhoneHarness setting;
- 96.7% for device/system operations;
- 74.3% tool-assisted workflows;
- 63.3% single-app GUI;
- ~23 average steps and ~131 s average successful-task time.

## Q7 — Artifact
Public artifact status should be verified before reproduction.

## Q8 — Evidence vs hypothesis
**[FACT]** mixed action surfaces materially improve some phone task classes.

**Boundary:** deterministic-first routing is a policy choice; the paper does not prove it is globally optimal.

## Q9 — Project contribution
Hybrid phone actuation is a **must-have platform direction**, but broad novelty is already crowded.

## Q10 — Next action
- KEEP as P0 platform-direction evidence.
- Use mixed-action + execution verification as B4.
- Do not count this broad mechanism as a Primary Bet.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for evaluated mobile tasks
- Decision impact: Platform Track, not differentiated Primary Bet
- Open questions: system telemetry-aware routing; on-device cost/energy
- Primary source: https://arxiv.org/abs/2606.14832
