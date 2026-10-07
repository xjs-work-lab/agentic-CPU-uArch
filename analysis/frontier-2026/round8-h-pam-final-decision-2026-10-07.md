# Frontier Round 8 — H-PAM Final Systems-Residual Decision — 2026-10-07

## Decision question
After direct mobile acquisition evidence, edge phase-cost profiling, foundational adaptive sensing prior art and current multimodal pipeline systems, does H-PAM retain a distinct standalone control point?

## New FULL_10Q sources
- PAPER-076 — Modality-Aware Long-Term Memory Acquisition — MobiSys Companion 2026
- PAPER-077 — MemArena — arXiv 2026
- PAPER-078 — SeeMon — MobiSys 2008
- PAPER-079 — MMEdge — SenSys 2026

## Evidence result
### Direct workload signal
Mobile personal-memory acquisition is non-free and modality dependent.

### Phase asymmetry
Foreground search is often relatively light on the evaluated edge platform; structured ingest can be energy-heavy.

### Prior-art pressure
Adaptive semantic/value-vs-cost sensing and resource activation are longstanding mobile-systems mechanisms.

### Current systems pressure
Cross-modal sensing/encoding coupling, adaptive modality configuration and speculative skipping are already generic on-device systems mechanisms.

## Decision
**KILL H-PAM AS A STANDALONE SECOND-BET / DIRECTION CANDIDATE.**

Do not kill persistent Agent memory as a workload.

## Why
No distinct H-PAM-owned control abstraction remains after strongest baselines.
The remaining costs map cleanly into existing portfolio responsibilities or generic systems baselines.

## Merge map
| Residual observation | Canonical owner / treatment |
|---|---|
| background acquisition/maintenance may hurt QoE | C workload scenario / experiment input |
| verified action replay/staleness/recovery | PT-A |
| semantic invalidation/coherence | B-residual |
| progress/task-driving state | A / B4-TX baseline |
| CPU locality/cache residual | R2 / CG-01 only if measured |
| extractor/embedding heterogeneous execution | existing heterogeneous inference/control baseline |

## Portfolio impact
- A remains only differentiated Primary Bet.
- second differentiated Primary Bet remains unfilled.
- no score changes.
- no hardware/uArch promotion.

## Reopen condition
Direct target-phone evidence of a non-reconstructible Agent-memory fact with >~5% residual beyond all current baselines.

## Search consequence
Stop Agent-memory second-Bet expansion.
Next research round should perform a **frontier reset / coverage audit** and choose a different structural workload family rather than trying another memory-system variant.