# Frontier Round 5 — Persistent Agent Memory Seed Synthesis — 2026-10-06

## Decision question
After system-control/H-FIB convergence, does persistent Agent memory expose a structural smartphone CPU/system opportunity that merits second-Bet investigation?

## Full 10Q Sources
- PAPER-069 — MUSE — ACM Multimedia 2026
- PAPER-070 — LEANN — MLSys 2026 Best Paper
- PAPER-071 — M3-Agent — ICLR 2026
- PAPER-072 — CD-ANN — Journal of Systems Architecture 2026

## Provenance correction
AME (2025 v1) and MUSE (2026 v2) share arXiv:2511.19192 and a clear mechanism/result lineage.

**Canonical handling: one Source, PAPER-069 MUSE.**
AME remains provenance/history only and is not counted as independent evidence.

## Cross-paper synthesis

### 1. Persistent memory is a real Agent workload
M3-Agent establishes that episodic memory, semantic memory, continuous multimodal acquisition, memory update and iterative task-time retrieval can materially improve long-horizon Agent capability.

This is DIRECT_AGENTIC workload evidence.

### 2. Dynamic semantic memory/search creates real phone systems pressure
MUSE establishes on commercial Snapdragon SoCs that high-dimensional retrieval, continuous background ingestion, index construction/maintenance, data-layout conversion, DDR↔accelerator-local movement and CPU/GPU/NPU operation mapping can materially alter performance, energy and thermal behavior.

This is direct phone SYSTEM_VALUE for a **generic semantic-retrieval workload**, not yet for an Agent memory implementation.

### 3. Capacity is strongly software-capturable
LEANN shows that full embedding/index residency is not a fixed requirement:
- selectively recompute embeddings;
- prune/compress graph structure;
- trade compute for storage.

Therefore:
> "Agent memory grows large" is not a differentiated Bet.

### 4. Dynamic insertion/update is also generic
CD-ANN shows that growing vector sets, insertion cost and limited resident index memory can be attacked using segmented HNSW and on-demand residency.

Therefore:
> "Agent memory updates frequently" is also not sufficient differentiation.

## Core tension
The promising bridge is:
> M3-Agent proves a richer **memory lifecycle** than ordinary RAG, while MUSE proves a dynamic mobile retrieval substrate has real SoC cost.

But the missing evidence is:
> whether Agent-specific memory operations produce a systems-level operation mix or control variable that generic vector/index systems cannot already exploit.

## Candidate H-PAM
Opened as **analysis hypothesis only**:
`analysis/frontier-2026/h-pam-hypothesis.md`

Surviving candidate:
> persistent Agent memory operation-class semantics and temporal coupling may create a reusable mobile data-plane control point beyond generic vector-search software.

No Direction is created.

## Overlap audit
| Existing lane | Potential overlap | Current boundary |
|---|---|---|
| B-residual | semantic revision / stale derived state | B owns correctness/coherence; H-PAM only execution/data plane |
| R2 | CPU-local warm continuation state | no direct overlap unless evidence becomes CPU microstate-specific |
| CG-01 | cache/shared-memory handoff | generic cache mechanisms remain baseline, not H-PAM novelty |
| CG-07 | always-on AI domain | memory background duty cycle does not imply dedicated silicon |
| C | generic resource scheduling | ordinary QoS/placement remains C baseline |

## Portfolio impact
**No lane/score changes.**

- A — PRIMARY_BET / 82.5
- PT-A — PLATFORM_TRACK / 80
- C — STRATEGIC_ENABLER / 72
- CG-06 — INVEST / 86.5
- second differentiated Primary Bet — still unfilled
- uArch Primary Bet — none

## What changed
The second-Bet search now has a credible **new structural frontier**, but not yet a candidate Bet:
> persistent Agent memory lifecycle / on-device memory data plane.

## Next falsification round
Priority order:
1. full review of MobiSys 2026 mobile-Agent memory-architecture benchmark;
2. review Agent-native memory systems that expose store/update/consolidate/forget/retrieve actions;
3. identify actual operation mix and duty cycle;
4. compare against MUSE/LEANN/CD-ANN strongest baselines;
5. only then decide KEEP / NARROW / KILL / promote-to-candidate.

## Current conclusion
Persistent Agent memory is **worth continuing to research**.

It is not yet differentiated enough to become a Direction, second Primary Bet, or CPU/uArch proposal.