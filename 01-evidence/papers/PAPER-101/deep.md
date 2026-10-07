# PAPER-101 — Mind the Gap — EDP v1 FULL_10Q

Re-reviewed: 2026-10-07

## Q1 — Problem + target mapping
GUI Agents assume that the UI they observed remains the UI that receives the eventual input.

Android does not guarantee that invariant.

PT-A mapping: negative evidence against “observe → reason → inject → verify later” as a sufficient execution contract.

## Q2 — Novelty / new-regime relevance
The work frames mobile GUI-agent execution as a TOCTOU problem:
`state at observation != state at actuation`.

It targets the Agent/OS boundary, not model jailbreaks or traditional clickjacking alone.

## Q3 — Falsifiable hypothesis
If visual/context atomicity holds, an unprivileged app should not be able to redirect an Agent's already-decided action by changing foreground state during reasoning.

The attack repeatedly falsifies that assumption.

## Q4 — Lineage / competing route
Accepted ACM CCS 2026.
Independent security group: Nanjing University with Honor/other collaborators.

It is high-value negative evidence because it challenges verification/recovery-centric PT-A assumptions from outside the mobile-Agent systems lineage.

## Q5 — Mechanism / control point
Root chain:
`observe UI at T_o → model/network reasoning delay → foreground changes → coordinate/input injection at T_a → Android delivers to current component`.

Key missing invariant identified by the paper:
GUI agents do not bind the intended action to a process/component identity.

Attack extensions:
- foreground transition through normal Intent behavior;
- UI state preservation;
- recovery-loop weaponization;
- Intent Alignment Strategy (IAS) to make a malicious verification gate semantically plausible.

## Q6 — Experiment design + results
- six open-source Android GUI agents;
- 15 tasks across five security domains;
- measured observation→action windows: 4.18–15.43 s;
- atomic action rebinding: 100% success in reported evaluation;
- attacks include unauthorized SMS, app actions/deletion/uninstallation and multi-step chains;
- generic confirmation context: agents rejected 59/60 trials;
- IAS carrier raises confirmation/verification-gate pass rate to 30–100% depending on agent.

The malicious app requires no dangerous permissions.

## Q7 — Artifact / reproducibility
Primary paper and logs/demo availability statement exist; full experimental artifact is not an ordinary open benchmark in the current source set.

Strength: real Android architectural behavior and multiple agents.
Boundary: adversarially constructed attack tasks, not production attack prevalence.

## Q8 — Evidence vs alternative explanations
Demonstrated:
current GUI-agent pipelines can decouple intent from actual input recipient.

Also demonstrated:
recovery and semantic confirmation can become attack surfaces.

Not demonstrated:
- every future Agent runtime remains vulnerable;
- a particular proposed defense is sufficient;
- CPU/uArch is required.

## Q9 — Decision contribution
This is a **scope-limit** on CLM-PTA-002.

PT-A must distinguish:
1. outcome verification after action;
2. target/context integrity before/during action delivery.

Analyst inference, not paper-proven solution:
a robust contract should bind action to a fresh app/window/component/state epoch and abort/re-observe on mismatch.

This is currently an OS/runtime/platform requirement, not a uArch Bet.

## Q10 — Next action
Add CLM-PTA-006 and EXP-PTA-002.
Test post-action-only verification against fresh-state identity checks and stronger target-bound execution.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for security failure mode
- Decision impact: REFRAME PT-A contract; no lane/score/uArch promotion
- Open questions: cheapest deployable binding primitive, non-GUI tools, latency/energy overhead
- Primary source: https://arxiv.org/abs/2601.12349
