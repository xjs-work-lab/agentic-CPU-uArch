+++
id = "EXP-PTA-002"
type = "EXPERIMENT"
record_state = "CURRENT"
status = "READY"
title = "PT-A fresh-context action-binding experiment"
direction_ids = ["PT-A"]
tests_claim_ids = ["CLM-PTA-EXP-002"]
input_source_ids = ["PAPER-037", "PAPER-040", "PAPER-042", "PAPER-101", "PAPER-102"]
evidence_target = "PLATFORM_CONTEXT_INTEGRITY"
+++

# EXP-PTA-002 — Fresh-context action binding

## Decision question
Does PT-A need an explicit context-bound actuation contract beyond ordinary post-action verification/recovery?

## Baselines
- **B0 — post-action verification only:** observe → reason → inject → verify/recover.
- **B1 — fresh context check:** immediately before actuation re-check foreground app/window + target presence/state fingerprint; abort/re-observe on mismatch.
- **B2 — target-bound contract:** bind planned action to an explicit app/window/component/state-epoch token where the platform permits, reject delivery when binding is stale.
- **B3 — strongest software Agent:** B1 plus VeriGUI-class action-effect self-verification and Cordon-like effect/authority metadata where applicable.

## Perturbations
- benign foreground switches;
- permission dialogs / pop-ups;
- notification interruptions;
- app background/foreground;
- adversarial rebinding-style transitions;
- dynamic UI content;
- network/render delays.

## Outcomes
Primary:
- unsafe/misbound effect rate;
- false-success rate;
- task success;
- successful recovery without unintended side effects.

Budgets:
- pre-action added latency;
- extra observations/model calls;
- CPU/NPU work;
- energy;
- foreground QoE.

## Falsifiers
- If B1 reduces misbinding to negligible levels at low cost, do **not** open a heavier platform/hardware mechanism.
- If B3 closes the gap, classify the residual as software-sufficient.
- Only if a material residual survives strongest software/OS checks should PT-A revisit lower-layer support.

## Hardware boundary
This experiment is deliberately OS/runtime first.
It does not assume CPU/uArch differentiation.
