# Evidence Depth Audit — Current Portfolio

Date: 2026-10-07
Audit mode: EDP v1 rescue
Scope: paper sources directly grounding A / PT-A / C / CG-06 / CG-07
Closed-lane Kill audit: pending later phase

## Executive result
The current active five-lane portfolio is grounded by **33 unique paper Sources**.

At audit start:
- **19 / 33** already carried FULL_10Q-class review metadata;
- **14 / 33** had no `review_depth` metadata;
- **13 of those 14** are P0 sources.

This is material historical evidence debt.

The gap is concentrated in research created before the Round-2/3 FULL_10Q discipline became routine.

## Risk tiers

| Tier | Sources | Why |
|---|---|---|
| Rescue-0 | PAPER-009, PAPER-051, PAPER-052 | direct C / CG-06 CPU↔NPU / heterogeneous-execution / CPU-matrix boundary |
| Rescue-0 | PAPER-041 | affects both A and PT-A Effect/Commit strongest-baseline semantics |
| Rescue-1 | PAPER-037, 038, 039, 040, 042 | core PT-A mobile action-modality / execution-substrate evidence |
| Rescue-1 | PAPER-013, 015, 043, 044, 050 | early A workload/proactive/speculation evidence |

PAPER-009 / 041 / 051 / 052 are handled in Evidence Rescue Round 1.

## Direction-level audit

| Lane | Depth risk | Current assessment |
|---|---|---|
| A | MEDIUM-HIGH | early workload / transaction / speculation sources need rescue; later strongest-baseline sources 056/058/063–068/100 are FULL_10Q |
| PT-A | HIGH | several direct mobile/hybrid execution sources 037–042 are not yet EDP v1 deep-read |
| C | MEDIUM | PAPER-009/051 historical gaps; later 060–068 and direct-phone HeRo 098 reduce conclusion fragility |
| CG-06 | HIGH | PAPER-009/052 are origin evidence for crossover/SME thesis; later 057/059/097/098 provide strong baseline pressure |
| CG-07 | LOW for papers | PAPER-087/088 are FULL_10Q; vendor/source-type audit remains pending |

## Important interpretation
A missing `review_depth` field does not prove the source was unread. Several Sources have migrated V1 `deep.md` files.

However, the Round-1 sample shows those older deep files often lack today's required:
- causal/ablation reconstruction;
- alternative explanation analysis;
- explicit external-validity boundary;
- exact distinction between generic software value and Agent/uArch residual.

Therefore migration-era `deep.md` is not automatically accepted as EDP v1 FULL_10Q.

## Rescue-0 status
- PAPER-009 — reread complete / wording narrowed
- PAPER-041 — reread complete / runtime-legality boundary narrowed
- PAPER-051 — reread complete / Agent-aware gain decomposition clarified
- PAPER-052 — reread complete / CPU-vs-NPU inference boundary strengthened

After Round 1, active-lane paper debt will be **10 papers**, all scheduled for Rescue-1.

## Next audit wave
Rescue-1 should deep-read the PT-A cluster first, then the remaining A early evidence.

Only after active-lane paper debt is zero should the historical Kill decisions H-FIB / H-PAM / H-CAL / security closure be backtraced under EDP v1.
