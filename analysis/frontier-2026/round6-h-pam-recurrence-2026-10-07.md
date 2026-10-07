# Frontier Round 6 — H-PAM Recurrence and Mobile-Execution Test — 2026-10-07

## Decision question
Does persistent Agent memory survive beyond a cross-paper workload inference and show recurring operation semantics that matter in mobile Agent execution?

## Full 10Q Sources
- PAPER-073 — MobiMem — arXiv 2025 preprint / P0
- PAPER-074 — AgeMem — ACL 2026 Long Paper / P0

## Pending source
- Benchmarking Memory Architectures for Mobile Agents in Short-Term and Long-Term Applications — MobiSys Workshop 2026 — **PENDING_FULLTEXT / not decision-grade**

## Result 1 — operation semantics are real
MobiMem directly distinguishes:
- Profile Memory;
- Experience Memory;
- Action Memory.

These classes drive different operations and execution services:
- graph/vector retrieval;
- template abstraction;
- step-DAG scheduling;
- action replay;
- stale validation;
- fallback/recovery;
- interruption handling.

Therefore Agent memory is not merely a passive vector store.

## Result 2 — lifecycle operations recur independently
AgeMem independently exposes learned:
- ADD;
- UPDATE;
- DELETE;
- RETRIEVE;
- SUMMARY;
- FILTER.

RL changes operation frequency and improves task/memory quality.

Therefore H-PAM's **cross-framework operation recurrence gate passes**.

## Result 3 — upper-layer capture is already strong
This is the most important negative result.

MobiMem obtains major value through:
- specialized data structures;
- template reuse;
- AgentRR;
- step-level DAG scheduling;
- exception recovery.

AgeMem consumes memory operations directly in the Agent policy.

So the operation semantics are often already explicit and actionable above the OS/hardware layer.

## H-PAM decision
**KEEP / NARROW. DO NOT PROMOTE TO DIRECTION.**

Passed:
- Agent-native workload premise;
- recurring lifecycle operation classes;
- mobile Agent execution relevance.

Still missing:
- direct evidence that lifecycle semantics change CPU/NPU/data placement beyond upper-layer software;
- mobile memory-bandwidth/energy/thermal measurement tied to Agent operation classes;
- proof that ordinary API operation identity is insufficient;
- target-phone SYSTEM_VALUE for a distinct memory data-plane control point.

## Refined residual
> Does a recurring Agent-memory fact beyond ordinary operation identity—such as consolidation urgency, semantic replacement dependency, memory salience/confidence/age, cross-representation coupling or rebuild cost—change phone resource/data-placement decisions enough to survive strong generic baselines?

## Existing-lane boundary
- B-residual owns semantic validity / dependency / stale derived-state correctness.
- PT-A owns verified action reuse / replay / effect recovery.
- C owns generic resource control.
- R2 owns CPU continuation microstate.
- CG-01 owns generic cache/shared-handoff mechanisms.
- CG-07 owns always-on hardware-domain economics.

H-PAM only survives if it exposes an **operational memory data-plane residual not already owned above**.

## Portfolio impact
No score/lane changes.

- A — PRIMARY_BET / 82.5
- PT-A — PLATFORM_TRACK / 80
- C — STRATEGIC_ENABLER / 72
- CG-06 — INVEST / 86.5
- second differentiated Primary Bet — unfilled
- H-PAM — KEEP/NARROW analysis hypothesis
- uArch Primary Bet — none

## Next gate
Do **not** read more generic Agent-memory algorithm papers unless they provide a distinct operation class.

Next evidence must be systems-facing:
1. obtain the MobiSys Workshop full text;
2. find direct phone traces/profiling for Agent memory update/retrieve/consolidate/replay;
3. search mobile/edge memory engines for operation-class-specific CPU/NPU/data movement;
4. test whether operation type alone is enough or whether a richer lifecycle fact changes placement/maintenance policy;
5. if no lower-level residual appears, merge/kill H-PAM rather than extend it indefinitely.