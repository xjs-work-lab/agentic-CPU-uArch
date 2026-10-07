# Frontier Round 12 — H-CAL Final Residual Challenge — 2026-10-07

## Decision question
After direct phone training evidence and strongest software baselines, does Contiguous Agent Learning retain a distinct smartphone CPU/system control variable?

## FULL_10Q additions
- PAPER-094 — K-Merge — ACL 2026
- PAPER-095 — MobiLoRA — ACL 2025
- PAPER-096 — ZeroLock — 2026 preprint

## Residual challenge

### Adapter lifecycle
K-Merge shows that continually evolving on-device adapter collections can be represented by software state:
adapter slots, similarity, merge history and task routing.

This removes adapter-population growth as standalone differentiation.

### LoRA / KV state
MobiLoRA shows that LoRA identity and mobile application lifecycle can already be attached to KV-cache metadata and used for cross-adapter compression, retention and eviction.

It reports 18.1%–81.3% TTFT improvement in its evaluated mobile setting.

This removes ordinary adapter identity, app-state-aware cache policy and cross-adapter reuse as H-CAL-owned mechanisms.

### Training dependency
ZeroLock demonstrates that some BP update locking and activation lifetime can be changed at the algorithm level, with an Android prototype.

This further weakens generic training concurrency as a hardware-specific residual.

## What still remains unique?
The narrowest Agent-specific fact remains:
**a live adapter publication changes the validity of inference state produced under the previous adapter version.**

But:
- LOCAL already represents adapter version and KV validity explicitly in runtime software;
- correctness/semantic-to-physical validity naturally belongs to B-residual;
- scheduling/thermal/update windows belong to C;
- cache locality belongs to R2 / CG-01 conditionally.

No distinct H-CAL-owned reusable control abstraction remains.

## Evidence gap
The reviewed public set does not include a commercial-smartphone experiment that simultaneously measures live Agent serving + repeated local adaptation + version churn.

This prevents promotion. It does not justify creating a new lane in the absence of a distinct control variable.

## Decision
**H-CAL — KILL AS STANDALONE SECOND-BET / DIRECTION CANDIDATE.**

Retain Contiguous Agent Learning as a workload/evaluation scenario.

## Portfolio impact
- no Direction added;
- no score changes;
- second differentiated Primary Bet remains unfilled;
- no uArch candidate.

## Next
Return to frontier reset. H-CAL reopens only on direct target-phone evidence of a material residual beyond LOCAL + MobiLoRA + strongest mobile-training/scheduling baselines that cannot be absorbed by C/B/R2.
