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
| T6 Local programmable execution/sandbox | SkillDroid + Android AppFunctions + generic sandbox baselines | MEDIUM-HIGH signal | residual unproven | **SEED TRIAGE COMPLETE** |
| T7 Local multi-Agent concurrency/shared state | C + T5/B-residual + PT-A | HIGH product signal | standalone residual closed | WATCH / KILL_DIFFERENTIATED_BET |
| T8 Cross-device Agent fabric/continuation | partial PT-A/C overlap | UNKNOWN-MEDIUM | high generic-distributed-systems risk | AUDIT LATER |

## Round 14-A closeout and T6 handoff
T7 pressure testing is complete:
- product trend retained as FRONTIER_SIGNAL / WATCH;
- standalone differentiated candidate closed with KILL_DIFFERENTIATED_BET;
- ownership merged into C + T5/B-residual + PT-A;
- no new Direction or uArch candidate.

Round 14-B therefore moves to **T6 Local programmable Agent execution & sandboxed skills**.

The key T6 distinction is not whether Agents can invoke tools. Android already provides a direct product baseline for local Agent-callable functions. The open question is whether **dynamic procedural artifacts themselves** create a repeated phone execution regime with a residual control point beyond existing platform owners.

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

Seed-triage result:
- **SkillDroid**: strongest direct mobile seed; executable typed GUI action programs are compiled from successful trajectories and replayed locally, but not as native/JIT code.
- **Android AppFunctions**: strongest official mobile product baseline; Agents can discover and execute type-safe, permission-controlled app functions locally, but these are app-defined capabilities rather than runtime Agent codegen.
- **MCP-SandboxScan**: strongest current WASM/WASI untrusted-tool isolation seed; non-mobile.
- **SpecBox**: strongest sandbox lifecycle latency/memory seed in this set; server/multi-tenant rather than phone.

Before promotion, require representative phone evidence showing:
- recurring dynamic executable/IR/bytecode/skill generation or interpretation;
- measurable compile/validate/load/instantiate/interpreter/JIT/code-cache/sandbox-transition cost;
- product-relevant frequency and end-to-end impact;
- residual value after C + T5 + PT-A + ordinary AppFunctions baselines.

Otherwise keep T6 as WATCH or merge it into existing platform ownership rather than creating a new CPU/uArch Direction.

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
**Round 14-B: FULL_10Q SkillDroid.**

Then build the official Android AppFunctions product baseline and pressure-test T6 against the minimum necessary sandbox/runtime evidence.

Only after that decide:
- NEW DIRECTION;
- MERGE INTO C/T5/PT-A;
- WATCH;
- KILL_DIFFERENTIATED_BET.
