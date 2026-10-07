+++
id = "PT-A"
type = "DIRECTION"
record_state = "CURRENT"
title = "Heterogeneous Verified Agent Actuation Runtime"
direction_class = "PLATFORM_TRACK"
investment_lane = "PLATFORM_TRACK"
score_context = 80.0
evidence_maturity = "SYSTEM_VALUE"
maturity_scope = "mobile action-surface and verification/recovery value are established for evaluated systems; capability entitlement and context-bound action delivery are unresolved platform requirements; no differentiated CPU/uArch control point is established"
related_claims = ["CLM-PTA-001", "CLM-PTA-002", "CLM-PTA-003", "CLM-PTA-004", "CLM-PTA-005", "CLM-PTA-006", "CLM-AGENT-006", "CLM-PTA-EXP-001", "CLM-PTA-EXP-002"]
related_capabilities = []
+++

# PT-A — Heterogeneous Verified Agent Actuation Runtime

## 30-second decision
**PLATFORM_TRACK / 80.0 / SYSTEM_VALUE — lane and score unchanged.**

Rescue-1A strengthens and narrows the core contract:

> **capability/authority-aware routing → bounded actuation → fresh target/context binding → observable OutcomeReceipt → verification → bounded recovery**

The key lesson is no longer “give the Agent GUI + CLI + tools.”
More action surfaces without routing discipline can make an Agent worse, and verification after an action is not enough if the action can be delivered to a different context than the one observed.

## Why keep
- PAPER-037 gives real-Pixel evidence that heterogeneous deterministic/UI backends plus explicit progress checks are practical.
- PAPER-038 shows GUI is not a universal action surface, while also exposing the importance of capability/privilege boundaries.
- PAPER-040 shows a mixed-action/trace-verifier harness can materially improve verifiable workflow completion where structured routes exist.
- PAPER-102 gives causal software evidence that explicit action-effect verification improves recovery.
- PAPER-101 supplies negative security evidence that observation→action context integrity is a distinct execution requirement.
- PAPER-099 remains direct evidence that rollback capability changes the economics of speculative GUI work.

## Why not a Primary Bet
The generic mechanism surface is increasingly crowded:
- deterministic structured-first routing;
- learned GUI↔CLI routing;
- MCP/tool routing;
- transactional effects;
- model-internal action-effect verification;
- runtime recovery.

The newly identified context-binding residual is important, but current evidence points first to an **Agent/OS execution contract**, not a CPU/uArch innovation.

## Strongest baseline
PT-A must now beat:
- trained selective routing, not naive “all tools exposed”;
- VeriGUI-class model self-verification/recovery;
- Cordon-style mediated effect/authority/lineage handling where applicable;
- task-specific outcome verifiers;
- a cheap fresh-app/window/target re-observation immediately before action.

A PT-A feature gets differentiated credit only for residual value beyond these.

## 2027 platform contract
A common backend/effect/outcome contract should make explicit, where applicable:
- action capability and required authority/entitlement;
- target app/window/component or equivalent execution recipient;
- observation/state epoch or freshness token;
- effect class;
- idempotent / reversible / sandboxed;
- provisional vs committed state;
- expected effect / verification guard;
- OutcomeReceipt / observed side effect;
- rollback / compensation capability and scope;
- dependency lineage needed to invalidate downstream speculative work.

## Validation
- EXP-PTA-001: heterogeneous action + outcome contract baseline.
- EXP-PTA-002: fresh-context / action-binding residual under benign and adversarial state mutation.

## Hardware boundary
No PT-A-specific CPU/uArch work unless EXP-PTA-002 leaves a material residual after strongest software/OS baselines and that residual has a hardware-timescale cause.

## Portfolio state
No lane/score/maturity change:
- PLATFORM_TRACK;
- 80.0;
- SYSTEM_VALUE.
