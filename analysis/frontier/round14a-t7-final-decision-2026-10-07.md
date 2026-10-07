# Round 14-A — T7 Final Ownership Decision

Date: 2026-10-07
Trend: T7 — Local multi-Agent concurrency & shared model/state
Decision: COMPLETE

## Final answer

### Product Evolution
**KEEP T7 — FRONTIER_SIGNAL / WATCH**

The architecture trend is credible:
- specialized Agents;
- local/device roles;
- shared model/state;
- cross-Agent reuse;
- verified feedback loops.

But direct representative smartphone SoC evidence for several concurrent local Agents sharing CPU/NPU/model state remains insufficient.

### Differentiation Portfolio
**NO NEW DIRECTION.**
**KILL_DIFFERENTIATED_BET for standalone T7.**

This does not kill product relevance.

> Prior art constrains novelty, not product relevance.

## Ownership map

| T7 mechanism | Existing owner | Why |
|---|---|---|
| foreground/background queues, dependency, future consumer | C | explicit runtime scheduling/control state |
| shared context/KV, adapter/version validity, reuse/residency | T5 + B-residual | state lifecycle/coherence |
| step expectation, verification, failure/recovery | T3 + PT-A | verified actuation contract |
| local cache locality only if phone residual survives | R2 / CG-01 | already conditional measurement route |

## Three independent pressure tests

### PAPER-103 — MobiMem
- mobile multi-role architecture;
- experience/action reuse;
- workflow DAG scheduling;
- no Agent-identity-specific physical control point.

### PAPER-104 — LOCAL
- strongest shared-model seed;
- one model/KV/adapters/memory budget;
- Agent identity can disappear from hard KV key;
- useful signal = context/adapter/version + pending consumer + memory pressure.

### PAPER-105 — EcoAgent
- AAAI 2026 independent mobile architecture;
- gains from role placement, closed-loop verification and communication compression;
- “device-side” models actually run on RTX 3090 simulation;
- no phone-local shared-resource contention result.

## Hardware gate

```text
STRUCTURAL_SIGNAL       = partial
target-phone SYSTEM_VALUE = not established for local multi-Agent concurrency
SOFTWARE_INSUFFICIENCY  = not established; evidence favors software capture
hardware-specific cause = absent
UARCH_CANDIDATE         = no
```

## Reopen condition
A future T7-specific Direction requires a target-phone experiment where multiple local Agents materially benefit from a control variable that remains unavailable after conditioning on:
- workflow topology / pending consumer;
- priority/SLO;
- context namespace;
- model/adapter/version;
- KV hotness/residency;
- memory pressure;
- actuation verification/recovery.

A simple increase in concurrency or memory footprint is not enough.

## Next frontier
Proceed to **T6 — Local programmable Agent execution & sandboxed skills**.

Reason:
T6 is more likely than T8 to expose a CPU-visible structural regime through interpreter/JIT/code-cache/sandbox/executable-lifetime behavior, while T8 currently has a high risk of collapsing into generic distributed orchestration.
