# Frontier Round 11 — Contiguous On-Device Agent Learning — 2026-10-07

## Decision question
Does continual/personalized on-device learning create the next differentiated smartphone CPU/system Bet for Agentic AI?

## FULL_10Q source set
- PAPER-089 — LOCAL — Agent-native contiguous learning runtime
- PAPER-090 — FBLayout — MobiSys 2026 mobile-GPU fine-tuning baseline
- PAPER-091 — sustained 3B smartphone fine-tuning measurement
- PAPER-092 — MobileFineTuner mobile-native training runtime
- PAPER-093 — MeSP exact-gradient memory baseline

## What is genuinely Agent-new
The strongest Agent-native signal is:
`interaction → feedback/judge → adapter update → publish new version → invalidate/refresh versioned KV state → continue serving`.

Unlike generic offline fine-tuning, the Agent remains interactive while local model state evolves.

## What is generic
Most expensive work remains recognizable mobile training:
- backward compute;
- tensor layout/data movement;
- activation memory;
- thermal/energy budget;
- training scheduling.

Strong software baselines already attack these:
- FBLayout: 2.2–5.7× mobile training speedup through layout co-design;
- MeSP: 49% average memory reduction with exact gradients;
- MobileFineTuner: mobile-native sharding/checkpointing/energy-aware runtime;
- PAPER-091 kernel repair: 1.47× faster and about one-third less energy in its tested phone training path.

## Direct phone system value
PAPER-091 closes a realism gap: sustained multi-billion-parameter fine-tuning is feasible on a current smartphone, but thermal throttling and battery cost are material.

This establishes SYSTEM_VALUE for the training workload, not differentiation.

## Residual after strongest baselines
Potential Agent-specific residual:
- update timing driven by interaction feedback;
- adapter-version / KV-cache validity coherence;
- live serving concurrent with background learning;
- multi-Agent/adapter-scoped cache identity.

But scheduling maps to C, version coherence maps to B-residual, locality maps to R2/CG-01, and LOCAL already demonstrates substantial software capture.

## Decision
**H-CAL OPENED AS A NARROW ANALYSIS HYPOTHESIS / NOT A DIRECTION.**

No portfolio score change. No second Primary Bet. No uArch candidate.

One targeted residual round remains before closure: direct smartphone evidence combining live Agent serving, repeated adaptation, version churn and measured product cost.

## Next
Search specifically for smartphone concurrent inference + local adaptation / online Agent learning. If the residual maps cleanly into C/B/R2 after that search, close H-CAL and continue frontier reset.
