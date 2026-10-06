> V1 semantic source copied from frozen baseline `960abb4ef50a8f5b0bd357c067f08346025d`.
> The compact README owns the V2.2 Source metadata.

# PAPER-038 — Beyond the GUI Paradigm: Do Mobile Agents Need the Phone Screen?

## Source
- Paper: https://arxiv.org/abs/2606.19388
- Authors: Unknown / Not yet verified
- Venue/status: arXiv preprint, 2026
- Target: AndroidWorld + MobileWorld
- Project relevance: hybrid action-modality control
- Priority: P0

## Q1 — Problem
Mobile Agents are commonly designed as GUI controllers, although Android also exposes CLI/structured state that can solve many tasks more efficiently.

## Q2 — New-regime relevance
This paper reframes action modality itself as a systems/design choice rather than assuming GUI-first execution.

## Q3 — Hypothesis
CLI control can match or exceed GUI Agents on many mobile tasks while using fewer steps, and some tasks expose information/actions unavailable through GUI.

## Q4 — Competing route
Directly pressures any project proposal that treats GUI Agent execution as the default universal substrate.

## Q5 — Mechanism
Coding-agent harnesses operate through ADB/CLI and optional structured tools rather than screenshots/UI actions.

## Q6 — Experiment
Reported:
- Claude Code reaches 71.8% AndroidWorld and 51.9% MobileWorld;
- reproducible GUI baselines are below it on the reported comparison;
- oracle CLI reaches 88.8% AndroidWorld and 86.3% MobileWorld;
- CLI agents use 10.7 mean steps vs 18.6 for GUI methods;
- on CLI-Advantage tasks, CLI agents substantially outperform GUI baselines.

## Q7 — Artifact
Authors state implementations/oracles/evaluation will be open sourced; exact artifact status not yet verified.

## Q8 — Evidence vs hypothesis
**[FACT]** Action modality changes success, step count and reachable state.

**[FACT]** GUI and CLI show different failure profiles.

## Q9 — Project contribution
This is positive evidence for heterogeneous actuation as a real mobile-Agent problem.

But it also means:
> “use CLI/API instead of GUI where possible”
is already an established direction, not project whitespace.

## Q10 — Next action
- KEEP as P0 action-modality evidence.
- Require any second Bet to define a control point beyond simply adding CLI/API.
- Use as strong baseline for a hybrid actuation Platform Track.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for benchmarked mobile action modalities
- Decision impact: supports hybrid actuation; kills GUI-only framing
- Open questions: dynamic per-step routing; on-device model cost
- Primary source: https://arxiv.org/abs/2606.19388
