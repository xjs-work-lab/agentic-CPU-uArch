+++
id = "DR-R2-STAGE15-GAP"
type = "DISCOVERY_RUN"
lifecycle = "CLOSED"
as_of = "2026-10-05"
coverage_quality = "PARTIAL_RECONSTRUCTION"
scope = "R2 software-locality baseline, generic mobile shared/coherent locality baseline, prior-art pressure, Stage15 residual sensitivity, and missing target-phone PMU causality"
origin_paths = ["06-opportunities/M3-state-locality.md", "07-experiments/stage15-r2-locality-kill-test.md", "09-research-log/2026-10-05-stage15-r2-locality-kill-test.md", "analysis/stage15_r2_locality/results/r2-locality-kill-pass1.md"]
limitations = "Full historical search corpus is not retained. The frozen V1 set establishes strong baseline pressure and a bounded phone-evidence gap, not proof that the R2 residual is zero."
+++

# DR-R2-STAGE15-GAP

## Purpose
Preserve the Stage15 R2 audit after strong software locality and generic shared/coherent mobile hardware are included in the baseline.

## Bounded result
The reviewed V1 set establishes:
- direct Agentic server locality/context-switch pressure;
- strong generic software locality recovery;
- generic mobile shared/coherent locality product baselines;
- crowded generic cache/TLB/predictor preservation and migration mechanisms.

The still-open residual is narrower:
**after strong software locality control and generic shared/coherent cache, do real smartphone Agent continuations still lose enough CPU-local cache/TLB/predictor state to create >=~5% meaningful end-outcome value for an Agent-specific mechanism?**

## Boundary
No reviewed source establishes that target-phone causal residual.
This is bounded absence in the frozen set, not real-world or internal absence.
