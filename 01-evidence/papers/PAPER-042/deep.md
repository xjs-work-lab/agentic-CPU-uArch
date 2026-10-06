> V1 semantic source copied from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.
> The compact README owns the V2.2 Source metadata.

# PAPER-042 — UIAnchor: Anchoring UI Perception and Action Execution for Reliable Service-Composed Mobile Task Automation with GUI Agents

## Source
- Paper: https://doi.org/10.1145/3832008
- Authors: Wentao Zhou, Sicong Liu, Zimu Zhou, Yimeng Duan, Yongyan Cai
- Venue/status: Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, 2026
- Target: mobile GUI Agents
- Project relevance: pre/post action verification, recovery
- Priority: P0

## Q1 — Problem
Mobile service-composed workflows fail because Agents miss/misread UI targets and execute actions without verifying target correctness or outcomes.

## Q2 — Novelty
UIAnchor adds both perception anchoring and execution anchoring:
- pre-action verification;
- post-action outcome perception;
- per-step state tracking;
- targeted recovery.

## Q3 — Hypothesis
Explicit verification around each action can improve long-horizon cross-app mobile automation reliability.

## Q4 — Competing route
Directly pressures a second Bet based on generic:
> post-action verification / recovery loop.

## Q5 — Mechanism
A modular meta-controller verifies target/state before action, observes outcome after action, tracks per-step state and invokes targeted recovery.

## Q6 — Experiment
Reported:
- on L4 tasks, +31.5% success over GPT-4o and +16.6% over Mobile-Agent-v3;
- edge/cloud assisted operation around ~2 s/step;
- up to 75.5% per-step latency reduction and 52.4% energy reduction.

## Q7 — Artifact
Artifact status not yet verified.

## Q8 — Evidence vs hypothesis
**[FACT]** execution verification and recovery are direct mobile-system value.

## Q9 — Project contribution
This establishes verification/recovery as a good mobile-Agent engineering direction but weakens novelty of a generic “verified actuation runtime” Bet.

## Q10 — Next action
- KEEP as P0 mobile reliability evidence.
- Put explicit verification/recovery into Platform Track baseline.
- Any differentiated proposal must expose a lower/system control point unavailable to runtime-only verification.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for evaluated mobile workflows
- Decision impact: supports Platform Track; narrows verified-actuation Bet
- Open questions: OS-level receipts vs runtime re-observation; phone energy accounting
- Primary source: https://doi.org/10.1145/3832008
