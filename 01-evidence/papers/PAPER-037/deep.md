> V1 semantic source copied from frozen baseline `960abb4ef50a8f5b0bd357c067f08346025d`.
> The compact README owns the V2.2 Source metadata.

# PAPER-037 — ClawMobile: Rethinking Smartphone-Native Agentic Systems

## Source
- Paper: https://arxiv.org/abs/2602.22942
- Authors: Hongchao Du, Shangyu Wu, Qiao Li, Riwei Pan, Jinheng Li, Youcheng Sun, et al.
- Venue/status: arXiv preprint, 2026
- Target: Google Pixel 9 / Android 16
- Project relevance: second-Bet structural-gap audit; hybrid actuation; verification/recovery
- Priority: P0

## Q1 — Problem + target mapping
Real smartphone Agents fail not only because of planning quality, but because device execution is heterogeneous and unstable:
- API/command paths are deterministic but incomplete;
- GUI/UI-Agent paths are flexible but uncertain;
- asynchronous launches, permissions and transient UI changes create silent/partial failures.

## Q2 — Novelty / new-regime relevance
ClawMobile makes multiple smartphone action backends explicit and dynamically selects among them, with a deterministic-first policy and explicit verification/recovery.

Classification: **Agentic-native mobile runtime problem**, but the broad hybrid-backend idea is not unique after 2026.

## Q3 — Falsifiable hypothesis
A smartphone Agent runtime that prefers deterministic backends when possible and verifies outcomes after execution can improve real-task reliability versus a single GUI-centric backend.

## Q4 — Competing routes
- pure GUI Agents;
- CLI/ADB Agents;
- typed/lightweight executors;
- mixed GUI/CLI/tool harnesses;
- learned hybrid orchestration.

## Q5 — Mechanism / control point
Inputs:
- task intent;
- available backend/capability;
- current device state;
- execution result.

Decision:
- structured API/command first;
- semantic UI Agent when needed;
- direct UI fallback.

Feedback:
- re-observe device state;
- verify progress;
- retry/replan/reselect backend on failure.

Layer:
Agent runtime / mobile control framework.

## Q6 — Experiment
Pixel 9 / Android 16, six real-life tasks, same GPT-5.2 model.

Reported table:
- ClawMobile reaches 100% completion on all six listed tasks;
- DroidRun varies from 33–100%;
- ClawMobile is, on average, 57.5 s slower than DroidRun.

This is evidence of a reliability/latency tradeoff, not a blanket efficiency win.

## Q7 — Artifact
Official repository:
https://github.com/clawmobile/clawmobile

## Q8 — Evidence vs hypothesis
**[FACT]** Hybrid control + explicit verification improves robustness on the small evaluated task set.

**Boundary:** six tasks are insufficient to prove an optimal general scheduling policy.

## Q9 — Project contribution
This is strong evidence that hybrid actuation and verification are **good platform directions**.

It also weakens novelty of a broad second Bet based on:
> API/UI backend selection + verify/recover.

ClawMobile itself states that formal hybrid scheduling under cost/reliability remains open.

## Q10 — Next action
- KEEP as P0 industry-direction evidence.
- Treat hybrid actuation as Platform Track candidate, not automatically a Primary Bet.
- Any differentiated project proposal must beat deterministic-first + explicit verification.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for evaluated mobile tasks; broader policy remains STRUCTURAL_SIGNAL
- Decision impact: supports Platform Track; narrows second-Bet whitespace
- Open questions: scale, backend-selection policy, energy/system cost
- Primary source: https://arxiv.org/abs/2602.22942
- Artifact: https://github.com/clawmobile/clawmobile
