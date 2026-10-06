# H-FIB — Agent Foreground-Impact Budget

Status: **ANALYSIS HYPOTHESIS / NOT A DIRECTION**
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
