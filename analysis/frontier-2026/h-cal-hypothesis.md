# H-CAL — Contiguous Agent Learning

Status: **CLOSED / KILLED AS STANDALONE CANDIDATE**

Updated: 2026-10-07

## Question
Does a smartphone Agent that continuously learns from private interaction traces create a distinct CPU/system control problem beyond generic on-device fine-tuning and existing C / B-residual / R2 mechanisms?

## Structural signal
PAPER-089 LOCAL establishes an Agent-native regime in which foreground inference remains live while feedback/judge tasks, adapter updates, publication and KV-cache maintenance share one device and evolving model state.

This breaks the stable-weight assumption of ordinary inference.

## Direct smartphone reality check
PAPER-091 establishes that sustained 3B-model fine-tuning on a modern phone is physically feasible but can impose material battery, thermal-throttling and backward-pass cost.

Therefore the workload is real enough to investigate.

## Strongest generic baselines
Before claiming an Agent-specific residual, H-CAL must beat:
- PAPER-090 FBLayout: mobile-GPU forward/backward layout and data-movement optimization;
- PAPER-092 MobileFineTuner: mobile-native memory/energy-aware training runtime;
- PAPER-093 MeSP: structured recomputation / exact-gradient memory reduction;
- generic foreground/background scheduling and thermal control;
- server/federated/offline adaptation where product constraints allow.

## Residual map
| Residual | Current owner / pressure | Status |
|---|---|---|
| foreground inference vs background training admission | C + generic scheduling | crowded |
| training thermal/energy control | C + generic mobile training | crowded |
| backward kernels / tensor layout | generic training compiler/runtime | crowded |
| activation memory | MeSP / checkpointing / layout | crowded |
| adapter-version → KV validity | B-residual + LOCAL software baseline | still interesting but not independent |
| KV/cache locality after updates | R2 / CG-01 + LOCAL cache manager | conditional |
| Agent feedback determines when/what to update | application/runtime semantic policy | not lower-layer proof yet |

## Current decision
**KEEP ONLY AS A NARROW ANALYSIS HYPOTHESIS.**

The broad thesis “Agent continual learning needs a new mobile training substrate” is already heavily captured by generic training/runtime techniques.

The surviving question is:

> Does real smartphone **live Agent serving + repeated local adaptation** create a measurable residual from version churn / cache invalidation / mixed foreground-background execution that existing C/B/R2 software cannot reconstruct or control well enough?

## Promotion gate
H-CAL can become a Direction only after representative smartphone Agent traces show repeated local update cadence, concurrent serving/adaptation creates material product cost, strongest generic baselines are applied, existing lanes cannot absorb the control variable, and a reusable smartphone CPU/system control point remains.

## Kill / merge condition
Kill H-CAL as standalone if adaptation can be deferred/offloaded, generic training runtime + C handles interference, versioned cache invalidation is fully captured by B-residual/runtime software, or no meaningful reusable target-phone residual remains.

## Next
Run one targeted residual search for direct mobile evidence of concurrent inference + local adaptation / online Agent learning / adapter-version churn. Do not broaden back into generic training literature unless it challenges the strongest baseline.


## Round 12 final decision

**H-CAL is closed as a standalone second-Bet / Direction candidate.**

The final challenge adds:
- PAPER-094 K-Merge: evolving adapter collections are explicitly software-managed under storage constraints;
- PAPER-095 MobiLoRA: LoRA identity, shared semantic context and mobile application lifecycle are already software-visible KV management inputs;
- PAPER-096 ZeroLock: training dependency and activation lifetime are partly algorithm choices rather than fixed hardware constraints.

### Merge map
- foreground/background learning admission, energy and thermal budget → C;
- adapter-version publication / stale KV correctness → B-residual;
- cache residency/locality → R2 / CG-01 only after direct target-phone residual;
- training kernels/layout/backward optimization → generic platform/compiler work;
- continual personalization → workload/evaluation scenario.

### Reopen rule
Only direct target-phone evidence of live Agent serving + repeated local adaptation may reopen H-CAL, and only if a material residual survives LOCAL + MobiLoRA + strongest mobile-training/scheduling baselines and cannot be represented by C/B/R2.

This closure does not claim contiguous learning is unimportant. It says the reviewed evidence does not justify a distinct H-CAL-owned CPU/system/uArch lane.
