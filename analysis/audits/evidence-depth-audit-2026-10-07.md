# Evidence Depth Audit — Current Portfolio

Date: 2026-10-07
Audit mode: EDP v1 rescue
Primary scope: paper sources directly grounding A / PT-A / C / CG-06 / CG-07
Full current-ROADMAP warning scope: also includes B-residual / R1 / R2 / R3
Historical closed-lane Kill audit: pending later phase

## Executive result
The five active/differentiated/platform lanes A / PT-A / C / CG-06 / CG-07 are grounded by **33 unique paper Sources**.

At audit start:
- **19 / 33** already carried FULL_10Q-class review metadata;
- **14 / 33** had no `review_depth` metadata;
- **13 of those 14** are P0 sources.

This is material historical evidence debt.

After Rescue Round 1 re-reads PAPER-009 / 041 / 051 / 052, the five-lane debt falls to **10 papers**.

## Full current-ROADMAP QA result
The new warning-only EDP graph check follows every Direction scheduled by the current ROADMAP, not only the five primary lanes.

After Round 1, Graph QA reports **22 decision-critical paper warnings**:
- **10** in A / PT-A;
- **12 additional** in current conditional-reserve lanes B-residual / R1 / R2;
- **0 paper-depth warnings** in C / CG-06 / CG-07 after Rescue-0;
- R3 currently relies on patents rather than paper Sources, so it is outside this paper-only warning count.

Additional current-roadmap paper debt:
- PAPER-008 — R2
- PAPER-028 / 029 / 030 / 031 / 032 / 033 / 034 / 035 — B-residual
- PAPER-047 / 048 — R1
- PAPER-049 — R2

This distinction matters:
> **10 is the remaining debt in the five primary active lanes; 22 is the remaining paper-depth warning backlog across the whole current ROADMAP.**

## Risk tiers

| Tier | Sources | Why |
|---|---|---|
| Rescue-0 | PAPER-009, PAPER-051, PAPER-052 | direct C / CG-06 CPU↔NPU / heterogeneous-execution / CPU-matrix boundary |
| Rescue-0 | PAPER-041 | affects both A and PT-A Effect/Commit strongest-baseline semantics |
| Rescue-1A | PAPER-037, 038, 039, 040, 042 | core PT-A mobile action-modality / execution-substrate evidence |
| Rescue-1B | PAPER-013, 015, 043, 044, 050 | early A workload/proactive/speculation evidence |
| Rescue-2 | PAPER-008, 028–035, 047–049 | current conditional-reserve decision evidence |

PAPER-009 / 041 / 051 / 052 are handled in Evidence Rescue Round 1.

## Direction-level audit

| Lane | Depth risk | Current assessment |
|---|---|---|
| A | MEDIUM-HIGH | early workload / transaction / speculation sources need rescue; later strongest-baseline sources 056/058/063–068/100 are FULL_10Q |
| PT-A | HIGH | several direct mobile/hybrid execution sources 037–042 are not yet EDP v1 deep-read |
| C | LOW-MEDIUM after Round 1 | PAPER-009/051 rescued; later 060–068 and direct-phone HeRo 098 provide strong depth |
| CG-06 | MEDIUM after Round 1 | PAPER-009/052 rescued; later 057/059/097/098 provide strong baseline pressure |
| CG-07 | LOW for papers | PAPER-087/088 are FULL_10Q; vendor/source-type audit remains pending |
| B-residual | HIGH | eight paper Sources currently trigger EDP warnings |
| R1 | MEDIUM-HIGH | PAPER-047/048 trigger EDP warnings |
| R2 | MEDIUM-HIGH | PAPER-008/049 trigger EDP warnings |
| R3 | N/A for paper gate | current evidence is patent-heavy; patent deep-review gate must be audited separately |

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

## Next audit waves
1. **Rescue-1A:** PT-A PAPER-037/038/039/040/042.
2. **Rescue-1B:** A PAPER-013/015/043/044/050.
3. Re-run active-lane decision backtrace.
4. **Rescue-2:** B-residual / R1 / R2 paper debt.
5. Audit R3 and other decision-critical patents using direct claim review.
6. Only then audit historical closed/Kill lanes H-FIB / H-PAM / H-CAL / security under EDP v1.

Frontier Round 14 remains paused until the primary active lanes are evidence-depth clean; final portfolio convergence should wait until the full current-roadmap audit is also complete.
