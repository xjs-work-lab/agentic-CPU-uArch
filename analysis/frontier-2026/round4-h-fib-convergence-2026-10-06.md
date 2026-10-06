# Frontier Round 4 — H-FIB Falsification and Convergence — 2026-10-06

## Decision question
Does Agent Foreground-Impact Budget survive strongest adjacent prior art as a distinct second differentiated Bet?

## Full 10Q Sources
- PAPER-066 — Murakkab — OSDI 2026;
- PAPER-067 — HUSH / Smartphone Background Activities in the Wild — MobiCom 2015;
- PAPER-068 — ReUA / Energy-Efficient Utility Accrual Scheduling — EMSOFT 2004 / TECS lineage.

## Three-way prior-art pressure

### Murakkab
Kills/narrows the broad claim that Agent workflows need a novel resource manager simply because workflow structure and SLOs should affect model/hardware/resource allocation.

Already demonstrated:
- Agent workflow DAG;
- quality / latency / cost SLOs;
- workflow/model profiles;
- model/tool/hardware selection;
- provisioning/routing/multiplexing;
- energy/cost/resource optimization.

### HUSH
Kills/narrows the broad claim that mobile systems have not used 'background-work usefulness' to decide whether to spend resources.

Already demonstrated on smartphones:
- personalized usefulness proxy;
- background allow/suppress decisions;
- energy vs staleness tradeoff;
- OS/framework enforcement.

### ReUA / TUF
Kills broad novelty for:
- graded completion value;
- delay tolerance represented as a utility curve;
- utility-aware energy/resource scheduling;
- aborting infeasible / low-value work.

## H-FIB decision
**DO NOT PROMOTE TO A SEPARATE DIRECTION.**

H-FIB becomes an **A→C bridge question**:

> Can Agent semantic execution state automatically derive a dynamic RequiredProgress/value signal that is not reconstructible from ordinary SLOs, time/utility functions, app/user history, deadlines/slack, topology, verification/legality or reuse proxies—and if so, does that signal improve target-phone foreground-QoE/resource decisions?

This splits cleanly:
- **A owns information value / semantic residual**;
- **C owns target-phone system-control transfer**.

No distinct H-FIB architecture/control substrate remains.

## Portfolio changes
- A — PRIMARY_BET / 82.5 — unchanged, baseline stronger.
- PT-A — PLATFORM_TRACK / 80 — unchanged.
- C — STRATEGIC_ENABLER / 72 — **second-Bet watch closed**.
- CG-06 — INVEST / 86.5 — unchanged.
- second differentiated Primary Bet — still unfilled.
- uArch Primary Bet — none.

## Kill discipline
Killed as independent novelty/opportunity formulations:
- Agent-aware resource orchestration in general;
- background-task usefulness budget in general;
- task utility/tolerance curves in general;
- utility-aware low-value abort in general;
- H-FIB as a standalone Direction.

Not killed:
- A's RequiredProgress semantic-information hypothesis;
- target-phone A→C transfer test;
- product value of generic QoS/utility mechanisms.

## Next search strategy
Stop second-Bet search in generic system-control/utility scheduling until new contradictory evidence appears.

Return to the field map and inspect **other structural workload changes** not reducible to scheduling/QoS:
1. persistent Agent memory/state substrate;
2. always-on/event-driven Agent execution only where it is not already CG-07;
3. memory hierarchy / retrieval/update behavior under long-lived on-device Agents;
4. other CPU-visible new-regime mechanisms revealed by 2025–2026 mobile/architecture evidence.

Any new candidate must first survive strong software/runtime baselines before hardware discussion.