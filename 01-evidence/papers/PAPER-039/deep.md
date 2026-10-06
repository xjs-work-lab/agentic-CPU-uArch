> V1 semantic source copied from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.
> The compact README owns the V2.2 Source metadata.

# PAPER-039 — HybridCUA: Learning to Orchestrate GUI and CLI for Computer-Use Agents

## Source
- Paper: https://arxiv.org/abs/2609.38008
- Authors: Tongbo Chen, Junbo Niu, Zhengxi Lu, Niu Lian, Fei Tang
- Venue/status: arXiv preprint, 2026-09-29
- Target: computer-use Agents / OSWorld, WindowsAgentArena
- Project relevance: learned actuation-modality scheduler
- Priority: P0

## Q1 — Problem
Agents with GUI and CLI access still need to decide when and how to use each interface.

## Q2 — Novelty
HybridCUA trains the policy itself to orchestrate GUI/CLI actions using hybrid trajectories and CLI-aware RL rewards.

## Q3 — Hypothesis
Learned hybrid orchestration can improve success over the base model by choosing CLI selectively rather than relying on one modality.

## Q4 — Competing route
This is direct negative evidence against treating “learned GUI/CLI modality selection” as open whitespace.

## Q5 — Mechanism
- GUI-only, CLI-only and interleaved trajectory data;
- supervised fine-tuning;
- reinforcement learning with CLI-aware rewards;
- one policy chooses modality and action.

## Q6 — Experiment
Reported:
- 53.6% OSWorld accuracy for HybridCUA-9B;
- +14.8 percentage points over base model;
- +4.0 points on WindowsAgentArena.

## Q7 — Artifact
Artifact status not yet verified.

## Q8 — Evidence vs hypothesis
**[FACT]** learned cross-modality orchestration is already a concrete 2026 research direction.

**Boundary:** desktop/computer-use, not smartphone CPU/system measurement.

## Q9 — Project contribution
This sharply narrows a potential second Bet:
> dynamic GUI/CLI scheduler

is not itself differentiated.

A remaining phone-specific residual would need system-side information that model-only routing cannot observe or exploit.

## Q10 — Next action
- KEEP as P0 second-Bet negative evidence.
- Do not propose generic learned modality routing as project novelty.
- Use as B4 for any future mobile action-modality policy.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for evaluated computer-use setting; STRUCTURAL_SIGNAL for phone transfer
- Decision impact: narrows/blocks generic actuation-modality scheduler Bet
- Open questions: smartphone transfer; energy/device telemetry inputs
- Primary source: https://arxiv.org/abs/2609.38008
