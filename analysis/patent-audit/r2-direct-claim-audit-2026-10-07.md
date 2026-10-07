# Patent Direct-Claim Audit — R2

Date: 2026-10-07
State: COMPLETE

## Scope
PATENT-020 / 021 / 022 / 023 / 024

## Microstate restore family
### PATENT-020
Claim 1 directly covers context-specific branch predictor state loaded/restored for a newly swapped-in process context.

### PATENT-021
Claims directly cover cache-access footprint capture plus restoration of TLB/SLB/I-cache/D-cache state.

Result:
CLM-R2-004 remains SUPPORTED at direct claim level.

## Cache partition / migration family
### PATENT-022
Claim 1 directly covers per-process cache partition indicators and partition-aware refill.

### PATENT-023
Claim 1 directly covers source/destination load and per-task cache-miss-ratio-based task migration.

### PATENT-024
Claim 1 directly covers processor workload + task cache-demand-driven migration across heterogeneous processor clusters; claim 23 explicitly includes smartphones/tablets.

Result:
CLM-R2-005 remains SUPPORTED at direct claim level.

## Strategic boundary
These patents establish generic:
- predictor/cache/TLB warm-state restore;
- cache partitioning;
- PMU/cache-aware migration;
- mobile heterogeneous cache-demand-aware placement.

They do not establish that Agent future semantics have no additional predictive value.

## Portfolio
R2 remains:
- CONDITIONAL_RESERVE
- 54.5
- SIMULATION_SUPPORT
- no uArch promotion

## Evidence-integrity milestone
Patent audit: 13 / 13 COMPLETE.
Paper-depth warnings: 0.
Evidence Rescue: COMPLETE.

Next: final portfolio convergence.
