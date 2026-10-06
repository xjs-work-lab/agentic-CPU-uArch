# H-FIB — Agent Foreground-Impact Budget

Status: **A→C BRIDGE QUESTION / DO NOT PROMOTE TO SEPARATE DIRECTION**
Opened: 2026-10-06

## Hypothesis
> A persistent/background Agent can expose or derive a compact foreground-impact budget from its task state—representing tolerable delay, slowdown, suspension, degradation or discarded progress—and a smartphone control plane can use that information to improve end outcome beyond strong generic foreground-QoE protection.

## Why now
Direct smartphone evidence already shows severe asymmetric interference between background AI inference and foreground applications.
However, generic protection answers mainly:
> 'How much should the background yield to preserve foreground QoE?'

H-FIB asks a different question:
> 'Given what the Agent is trying to accomplish, how much background progress is actually worth buying at this moment?'

## Candidate information variables
These are hypotheses, not a proposed ABI:
- task urgency / useful-by time;
- remaining RequiredProgress value;
- pause/resume tolerance;
- cancel/restart cost;
- reversible/discardable speculative work;
- state-reuse loss if suspended;
- minimum useful service rate;
- foreground-impact budget.

## Strongest baselines
H-FIB must beat:
- PAPER-003 Sereno-style generic foreground QoE protection;
- PAPER-060 MUSched-like semantic interaction scheduling;
- deadline/slack/useful-time controls such as PAPER-054 TimelyLLM;
- A B4-TX reconstructible topology/criticality/legality/reuse proxies;
- simple Agent self-pause / rate-limit policies;
- device-level thermal/power governors.

## Falsifiers / Kill criteria
Kill H-FIB as a separate candidate if:
1. generic foreground-QoE control reproduces the same decisions/outcomes;
2. deadline/slack or ordinary priority reconstructs the useful signal;
3. Agent self-throttling captures the benefit without a system-level contract;
4. the signal does not recur across at least two materially different Agent workload styles;
5. incremental end-outcome value is <~5% at matched foreground QoE;
6. device/workload dependence prevents a reusable control abstraction;
7. C already cleanly owns the useful mechanism with no distinct Agent-specific control point.

## Promotion gate
Do not create a Direction until all are true:
1. direct or high-quality target-relevant evidence shows persistent/background Agent resource conflict;
2. a compact Agent-specific tolerance/value variable is identified;
3. that variable is not reconstructible by G1/B4-TX;
4. the same variable matters across >1 Agent workload regime;
5. a software-first experiment can distinguish H-FIB from generic QoS;
6. likely 2027–2029 team control point exists in compiler/runtime/OS scope.

## Hardware boundary
H-FIB is **not** a hardware/uArch hypothesis.

Any hardware discussion requires:
`SYSTEM_VALUE → SOFTWARE_INSUFFICIENCY → hardware-specific visibility/timescale/control cause`.

## Next search terms
- persistent mobile Agent background execution;
- on-device Agent foreground/background QoE;
- Agent-aware admission / throttling / resource budget;
- task-value-aware mobile AI scheduling;
- interruptible / pausable Agent inference;
- progress-aware background AI;
- mobile Agent thermal / memory bandwidth interference;
- Agent utility under foreground QoE constraints.

## Newly discovered strongest adjacent comparator — PENDING FULL 10Q

### Murakkab — OSDI 2026
**Status:** PENDING_FULL_10Q / not decision-grade for H-FIB yet.

Why it matters:
- explicitly exposes Agent workflow structure to a resource optimizer;
- maps workflow components to models and hardware;
- optimizes accuracy / latency / energy / cost under user-defined SLOs;
- reports large cloud resource/energy/cost reductions.

Why it does not yet answer H-FIB:
- cloud GPU scope, not smartphone foreground/background QoE;
- SLO/resource optimization is not yet shown to encode Agent marginal-value / pause / discard tolerance;
- full paper must be reviewed before any decision impact.

Primary page:
https://www.usenix.org/conference/osdi26/presentation/chaudhry

### Search boundary
Murakkab is now a mandatory strongest-baseline review before H-FIB can be promoted.


## Round-4 conclusion after Murakkab + HUSH + ReUA

Three independent prior-art lines remove the broad H-FIB opportunity:

1. **Agent-aware cross-layer orchestration — PAPER-066 Murakkab**
   - workflow graph + quality/latency/cost SLO + profiles;
   - model/tool/hardware/provisioning/routing optimization;
   - therefore 'Agent-aware resource orchestration' is not white space.

2. **Personalized mobile background usefulness — PAPER-067 HUSH**
   - mobile OS estimates whether background work is useful to the user;
   - allow/suppress policy trades energy against staleness;
   - therefore 'background work has different value and should be throttled accordingly' is not white space.

3. **Explicit task utility/tolerance scheduling — PAPER-068 ReUA/TUF**
   - application-specific graded utility vs completion time;
   - utility/energy-aware scheduling and low-value/infeasible-task abort;
   - therefore 'task marginal value/tolerance should guide resource allocation' is foundational prior art.

### Decision
**Do not create H-FIB as a separate Direction.**

The only surviving question is an A→C transfer gate:

> Can Agent semantic execution state **automatically derive** a dynamic RequiredProgress/value signal that is not reconstructible from ordinary SLOs, time/utility functions, app/user history, deadlines/slack, topology, legality or reuse proxies—and if so, does that signal improve target-phone foreground-QoE/resource decisions?

This is not a distinct scheduler architecture.
It is:
- **A** owns the information-value hypothesis;
- **C** owns the target-phone control/usefulness test.

### Reopen condition
Only reopen H-FIB as a separate Direction if later evidence reveals a reusable Agent-specific control abstraction that:
1. is distinct from A's semantic information itself;
2. is not equivalent to SLO/TUF/history/utility functions;
3. is not cleanly owned by C's generic control substrate;
4. recurs across multiple Agent workloads;
5. produces target-phone SYSTEM_VALUE.

### Portfolio consequence
C remains a Strategic Enabler, but its **second-Bet watch is closed on current evidence**.
