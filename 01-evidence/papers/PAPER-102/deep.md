# PAPER-102 — VeriGUI — EDP v1 FULL_10Q

Re-reviewed: 2026-10-07

## Q1 — Problem + target mapping
GUI agents often assume actions succeed. Rendering delay, network delay and system interruptions create silent failures and loops.

PT-A mapping: causal baseline for action-effect verification and recovery.

## Q2 — Novelty / new-regime relevance
TVAE explicitly links:
`Think → Verification of prior step → next Action → Expected effect`.

Training:
- Robust SFT with synthetic failure trajectories;
- GRPO with verification/efficiency rewards.

## Q3 — Falsifiable hypothesis
Explicit verification supervision should improve failure recognition and recovery beyond ordinary SFT/action accuracy training.

Ablations support that hypothesis.

## Q4 — Competing route
Baselines include Qwen2.5-VL, UI-R1, OS-Atlas, UI-TARS, UI-S1 and others.

Independent BJUT/Baidu line from UIAnchor and PT-A runtime systems.

## Q5 — Mechanism / control point
At step t+1, the model compares observed UI against the expected effect of action t.
Mismatch changes reasoning into diagnosis/recovery.

This is a model/software technique; no platform primitive required.

## Q6 — Experiment + causal results
Robustness benchmark:
- VeriGUI-3B: Loop Rate 24.3%, Recovery Success Rate 51.1%;
- VeriGUI-7B: LR 15.6%, RSR 52.5%.

3B training ablation:
- base: Sim-TSR 0, LR 30.0, RSR 35.0;
- Standard SFT: Sim-TSR 10.0, LR 30.4, RSR 29.7;
- Robust SFT: Sim-TSR 13.3, LR 26.5, RSR 45.5;
- +GRPO: Sim-TSR 16.7, LR 24.3, RSR 51.1, ASO 1.25.

Reward ablation:
- action reward only: RSR 44.9;
- + verification reward: RSR 48.1;
- + efficiency + verification: RSR 51.1.

Online AndroidWorld:
- VeriGUI-3B 12.6%;
- VeriGUI-7B 25.1%;
versus cited same-scale/open baselines including 6.1/10.9 at 3B and 14.9/22.7 at 7B.

## Q7 — Artifact / reproducibility boundary
Peer-reviewed ACL 2026 source.
Training uses substantial GPU resources.

AndroidWorld online environment uses Android emulators, not a retail-phone deployment.

The robustness benchmark's controlled failure model is simplified; online transfer partly addresses this.

## Q8 — Evidence vs alternatives
Demonstrated:
verification-aware training causally improves recovery metrics under the evaluated setup.

Not demonstrated:
- verification prevents action rebinding / context TOCTOU;
- verification requires a special runtime/hardware primitive;
- phone energy/latency value.

## Q9 — Decision contribution
Strengthens CLM-PTA-002 while raising the strongest software baseline.

This makes PT-A differentiation **less** about generic “verify and recover” and more about:
- common execution contract;
- capability/authority;
- target/context binding;
- external side-effect receipts.

## Q10 — Next action
KEEP P0.
Include VeriGUI-class model self-verification in EXP-PTA-001 / 002 baseline.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for software verification/recovery
- Decision impact: strengthen value, narrow differentiated residual
- Open questions: real-phone overhead, adversarial context integrity, non-GUI effects
- Primary source: https://aclanthology.org/2026.acl-long.1335/
