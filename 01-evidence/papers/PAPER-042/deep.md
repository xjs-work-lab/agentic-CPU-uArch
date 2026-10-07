# PAPER-042 — UIAnchor — EDP v1 FULL_10Q

Re-reviewed: 2026-10-07

## Q1 — Problem + target mapping
Service-composed mobile workflows are long, cross-app and dynamic. The authors' failure analysis identifies two recurrent bottlenecks:
1. missing/misreading actionable UI elements;
2. acting without verifying target correctness or outcome.

PT-A mapping: mobile actuation verification/recovery.

## Q2 — Novelty / new-regime relevance
UIAnchor “anchors” both perception and execution:
- two-stage high-recall/context-aware UI parser;
- meta-controller for pre-action verification;
- post-action outcome perception;
- step-state tracking;
- targeted recovery.

Classification: Agent-native mobile GUI reliability system.

## Q3 — Falsifiable hypothesis
Improving both UI perception and execution anchoring should improve long-horizon mobile task success relative to strong GUI-agent baselines.

The reported full-system results support this.

## Q4 — Lineage / competing route
Peer-reviewed PACM IMWUT / UbiComp 2026.
Independent author group relative to ClawMobile / PhoneHarness / VeriGUI.

Strong neighboring route: model-internal action-effect verification such as VeriGUI.

## Q5 — Mechanism / control point
Observed/parsed UI → candidate target → pre-action validation → execute → post-action outcome perception → state update → targeted recovery if mismatch.

This is still a software/meta-controller mechanism.

## Q6 — Experiment + quantitative anchors
The paper defines L1–L5 task complexity by horizon, cross-app scope and UI granularity.

On L4:
- 20–30 steps;
- multi-app;
- targets <100×100 px;
- whole UIAnchor system improves success by 31.5% over GPT-4o and 16.6% over Mobile-Agent-v3.

With edge/cloud assistance:
- ~2 s per step;
- reported per-step latency reduction up to 75.5%;
- energy reduction 52.4%.

## Q7 — Reproducibility / evidence-access boundary
Peer-reviewed primary ACM page and UbiComp program metadata are verified.

EDP v1 limitation:
the accessible primary evidence in this audit does not expose enough component-level ablation detail to attribute the headline success/latency/energy numbers specifically to verification/recovery rather than the combined parser + controller + edge/cloud system.

Those component contributions remain **Unknown / Not yet verified**.

## Q8 — Evidence vs alternative explanations
Demonstrated:
the complete system containing explicit verification/recovery is strong on evaluated mobile GUI tasks.

Not established by currently verified evidence:
- isolated causal gain of pre/post verification;
- isolated energy cost/benefit of verification;
- retail-phone-only execution without edge/cloud assistance.

## Q9 — Decision contribution
KEEP as direct mobile system evidence, but narrow EC-PTA-002-A:
> UIAnchor establishes that execution anchoring is part of a high-performing mobile system, not that verification alone caused all reported gains.

Causal verification evidence should instead be supplemented by PAPER-102 / VeriGUI.

## Q10 — Next action
KEEP P0.
Do not reuse 75.5% latency or 52.4% energy as “verification savings.”
Seek the full ablation/artifact before final quantitative report.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for full mobile system
- Decision impact: KEEP; narrow causal attribution
- Open questions: component ablation, device/edge breakdown, verifier overhead
- Primary source: https://doi.org/10.1145/3832008
