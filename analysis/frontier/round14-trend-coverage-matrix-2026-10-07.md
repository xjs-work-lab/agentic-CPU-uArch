# Round 14 — Product Trend Coverage Matrix

Date: 2026-10-07
Mode: authority-seed coverage reset before FULL_10Q
Decision question: which 2027–2029 Agentic smartphone workload trends are already owned, which are product-relevant but crowded, and which may represent genuinely uncovered structural breaks?

## Coverage result

| Trend | Current coverage | Product relevance | Novelty/whitespace | Round 14 state |
|---|---|---|---|---|
| T1 Semantic-aware progress/control | A + C | HIGH | A residual only | OWNED |
| T2 Heterogeneous CPU/GPU/NPU Agent AI | C + CG-06 | HIGH | target-specific residual | OWNED / PRODUCTIZE |
| T3 Verified/transactional actuation | PT-A | HIGH | platform residual | OWNED / PRODUCTIZE |
| T4 Always-on proactive front-end | CG-07 | MEDIUM-HIGH | architecture residual open | OWNED / BENCHMARK |
| T5 State lifecycle/reuse/locality | B-residual + CG-01 + R2 + H-CAL lineage | MEDIUM-HIGH | fragmented residuals | PARTIALLY OWNED |
| T6 Local programmable execution/sandbox | none | UNKNOWN-MEDIUM | potentially new | AUDIT |
| T7 Local multi-Agent concurrency/shared state | partial C/B overlap | UNKNOWN-HIGH | potentially new but may collapse into C/B | **AUDIT FIRST** |
| T8 Cross-device Agent fabric/continuation | partial PT-A/C overlap | UNKNOWN-MEDIUM | high generic-distributed-systems risk | AUDIT LATER |

## Why T7 moves to first priority
The initial authority/open-web seed scan found stronger direct mobile signals than expected:
- edge/cloud mobile multi-agent role decomposition;
- mobile memory/state systems with specialized agents and parallel sub-task execution;
- on-device multi-agent runtime signals;
- model/KV/adapter identity and cross-agent state sharing in on-device/edge runtimes.

This raises the probability that multi-Agent concurrency is a **product trend**.

But it does **not** yet establish a new Direction.
The first pressure question is:

> Does local multi-Agent execution create a control variable or physical bottleneck that is not already captured by C's Agent-aware orchestration or B/T5 state lifecycle?

If no, T7 becomes a product trend owned by C/T5 rather than a new Bet.

## T7 authority-seed audit plan

### Seed classes
1. Mobile multi-agent automation with explicit planning/execution/observation roles.
2. Mobile/edge memory/state systems with multi-agent execution and real device measurements.
3. On-device runtime papers that share model/KV/adapters among multiple agents.
4. Android-native open-source multi-agent runtimes as artifact evidence only.

### Required extraction
For each serious seed:
- what actually runs on phone vs cloud/server;
- number and kind of concurrent Agents;
- shared model instance or separate models;
- shared KV/context/adapter state;
- scheduling/control variable;
- synchronization/consistency mechanism;
- CPU/GPU/NPU placement;
- memory pressure;
- foreground QoE;
- latency/energy/thermal;
- whether gain is merely DAG parallelism;
- whether C already owns the mechanism;
- whether T5/B already owns the state problem.

### Kill/merge rules
- **MERGE INTO C** if the mechanism is ordinary workflow/DAG scheduling and xPU orchestration.
- **MERGE INTO T5/B** if the main issue is state/KV/adapter validity and reuse.
- **KEEP T7 FRONTIER** only if local multi-Agent concurrency introduces a distinct repeated physical/system control problem.
- **PROMOTE TO DIRECTION** only after a strongest-baseline residual exists.
- **No uArch discussion** before SYSTEM_VALUE + SOFTWARE_INSUFFICIENCY.

## T6 pressure question
Is local programmable execution an actual phone workload trend or mainly a portability/sandbox implementation detail?

Early seeds:
- embedded persistent Agent runtimes using WASM;
- browser-native Agent runtimes using WASM/action bundles;
- native mobile Agent runtimes with local tools/sandboxing.

Before FULL_10Q, require at least one strong mobile/phone seed showing:
- recurring dynamic executable generation or interpretation;
- measurable CPU/system cost;
- product-relevant frequency.

Otherwise classify T6 as platform implementation technique rather than CPU trend.

## T8 pressure question
Does cross-device continuation preserve Agent execution state in a way that changes phone-local resource control?

Early seeds show:
- dynamic distributed task DAGs;
- cross-device task assignment/replanning;
- persistent sessions;
- device-local vs global recovery scopes.

Before promotion, require evidence that the phone carries a continuation state whose migration/recovery cost is materially different from ordinary RPC/task offload.

Otherwise merge into distributed Agent platform architecture, not CPU roadmap.

## Round 14 stage gate
Do **not** add a new Direction merely because a frontier has papers.

A frontier advances only if:
1. it is a plausible 2027–2029 product trend;
2. it has representative smartphone or directly transferable mobile evidence;
3. existing Directions cannot naturally own its control point;
4. strongest software baseline is identified;
5. a discriminating residual can be written.

## Next smallest step
**Round 14-A: T7 Local Multi-Agent Concurrency pressure test.**

Deep-read the strongest mobile/system seeds first.
Only then decide:
- NEW DIRECTION;
- MERGE INTO C;
- MERGE INTO T5/B;
- WATCH;
- KILL differentiated novelty.
