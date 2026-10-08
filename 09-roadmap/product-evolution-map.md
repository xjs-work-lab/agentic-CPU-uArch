+++
id = "ROADMAP-PRODUCT-2027-2029"
type = "ROADMAP"
record_state = "CURRENT"
roadmap_kind = "PRODUCT_EVOLUTION"
trend_ids = ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"]
scope = "2027_2029_SMARTPHONE_AGENTIC_PRODUCT_EVOLUTION"
+++

# 2027–2029 Agentic Smartphone Product Evolution Map

Date: 2026-10-07
State: Round 14 trend reset v1
Purpose: separate likely product evolution from originality/whitespace.

## Executive view

The current evidence supports **seven product-relevant trend families**. T7 remains a frontier product signal under WATCH; Round 14 frontier differentiation coverage is complete.

A trend can remain important even when its broad novelty is crowded.

| Trend | Product maturity | Product posture | Linked Direction posture(s) | Canonical Direction links |
|---|---|---|---|---|
| T1 Semantic-aware progress & resource control | EMERGING_PRODUCT_TREND | ADAPT_AND_DIFFERENTIATE | A=RESIDUAL_RESEARCH; C/R1=RESIDUAL_RESEARCH; R3=FRONTIER_UNPROVEN | A, C, R1, R3 |
| T2 Heterogeneous Agent AI execution continuum | ESTABLISHED_PRODUCT_TREND | PRODUCTIZE | C/CG-06=RESIDUAL_RESEARCH | C, CG-06 |
| T3 Verified / transactional Agent actuation | EMERGING_PRODUCT_TREND | PRODUCTIZE | PT-A=RESIDUAL_RESEARCH | PT-A |
| T4 Always-on proactive Agent front-end | EMERGING_PRODUCT_TREND | BENCHMARK_AND_PREPARE | CG-07=RESIDUAL_RESEARCH | CG-07 |
| T5 Agent state lifecycle, reuse & locality | EMERGING_PRODUCT_TREND | ADAPT_AND_DIFFERENTIATE | B-residual/CG-01/R2=RESIDUAL_RESEARCH; R3=FRONTIER_UNPROVEN | B-residual, CG-01, R2, R3 |
| T6 Local programmable Agent execution & sandboxed skills | EMERGING_PRODUCT_TREND | BENCHMARK_AND_PREPARE | C/B-residual/PT-A=RESIDUAL_RESEARCH; standalone T6-specific Bet closed | C, B-residual, PT-A |
| T7 Local multi-Agent concurrency & shared model/state | FRONTIER_SIGNAL | WATCH | C/B-residual/PT-A=RESIDUAL_RESEARCH | C, B-residual, PT-A |
| T8 Cross-device Agent fabric & continuation | EMERGING_PRODUCT_TREND | BENCHMARK_AND_PREPARE | C/B-residual/PT-A=RESIDUAL_RESEARCH; standalone T8-specific Bet closed | C, B-residual, PT-A |

---

## T1 — Semantic-aware progress & resource control

### Product thesis
Future Agent systems increasingly expose work whose value depends on goal survival, user demand, confirmation, utility and progress state rather than simple runnable/not-runnable status.

### Product posture
**ADAPT_AND_DIFFERENTIATE**

Prepare runtime/OS contracts and measurement infrastructure even before any hardware conclusion.

### Research boundary
A is now a **conditional research reserve**, not an active differentiated Bet. Its only surviving hypothesis is **non-reconstructible DemandState / RequiredProgress**, not yet shown beyond best software.
C owns the software/system-control substrate.

### What prior art changes
Prior work kills broad claims like “semantic scheduling is new.”
It does not remove the product need for semantic-aware control.

---

## T2 — Heterogeneous Agent AI execution continuum

### Product thesis
Agent workloads will not map cleanly to one engine.
CPU, GPU and NPU roles vary by phase, operator, precision role, shape, responsiveness target and implementation quality.

### Product posture
**PRODUCTIZE**

Target-specific adaptation and differentiation remain valuable implementation/research activities, but they do not create a second Product posture token.

Product roadmap should explicitly include:
- CPU-resident latency-critical AI path;
- matrix/vector fast path;
- optimized NPU path;
- operator/sub-operator partition;
- dynamic CPU/GPU/NPU placement;
- persistent sessions and dispatch reduction;
- layout/state reuse;
- memory-bandwidth-aware orchestration.

### Research boundary
The broad heterogeneous-execution idea is crowded.
Whitespace is in target-specific crossover, low-overhead orchestration and CPU roles that remain after optimized NPU baselines.

---

## T3 — Verified / transactional Agent actuation

### Product thesis
Real agents need bounded execution, explicit authority/capability, target/context integrity, effect observability, verification and recovery.

### Product posture
**PRODUCTIZE**

This is a likely future platform capability even if broad academic novelty is already crowded.

### Research boundary
PT-A differentiation is now residual:
- target/context binding;
- common OutcomeReceipt contract;
- authority-aware actuation;
- low-overhead recovery under mobile conditions.

No CPU/uArch implication today.

---

## T4 — Always-on proactive Agent front-end

### Product thesis
Persistent/proactive agents create a recurring “observe → gate → intervene or remain silent” workload that may justify a low-power front end.

### Product posture
**BENCHMARK_AND_PREPARE**

Prepare:
- context-rate telemetry;
- gating-cost measurement;
- handoff/wake accounting;
- idle/residency measurements;
- CPU/shared-NPU/dedicated-domain comparisons.

### Research boundary
The trend is credible.
Dedicated hardware architecture remains unproven after strong lightweight gating.

---

## T5 — Agent state lifecycle, reuse & locality

### Product thesis
Agent execution creates persistent and reusable state across:
- context/KV;
- action/experience memory;
- adapter/version state;
- execution traces;
- CPU-local continuation state;
- cross-task shared prefixes;
- rollback/provisional artifacts.

### Product posture
**ADAPT_AND_DIFFERENTIATE**

Benchmarking remains an implementation activity for this Trend, not a second Product posture token.

Treat state lifecycle as a product trend even though several broad cache/state ideas are mature prior art.

### Research boundary
Keep distinct residuals:
- semantic→physical validity/coherence;
- phone CPU continuation locality;
- reusable state under memory pressure;
- version-aware state lifecycle.

Do not infer new cache/uArch structures before phone residual evidence.

---

# Frontier families for Round 14

## T6 — Local programmable Agent execution & sandboxed skills

### Structural question
Do mobile Agents increasingly generate, install, interpret or execute typed scripts, WASM/DSL/code bundles or dynamically composed skills locally enough to create a new CPU/runtime workload?

### Why it may matter
Potentially changes:
- executable/code-cache churn;
- JIT/interpreter cadence;
- instruction footprint;
- sandbox transitions;
- authority/capability boundaries;
- branch/frontend behavior;
- code/data lifetime.

### Current evidence state
Round 14-B now includes **PAPER-106 / SkillDroid FULL_10Q**.

SkillDroid establishes a concrete mobile-Agent product pattern:
- a successful LLM-guided GUI trajectory can become a persistent parameterized action program;
- replay can bypass per-step LLM reasoning;
- versioning/recompilation plus verification/fallback make the artifact operational rather than textual memory.

Critical boundary:
- the "compiled" object is a structured GUI-action template stored in SQLite, not native code/WASM/JIT output;
- experiments run on a Windows 11 host driving a Pixel 9a/API 35 emulator through ADB;
- no target-phone CPU/energy/thermal/code-cache/interpreter/JIT residual is measured.

Other baselines remain Android AppFunctions, MCP-SandboxScan and SpecBox.

The missing evidence is still decisive: no reviewed source yet shows a representative phone where dynamic executable artifacts create material interpreter/JIT/code-cache/sandbox-transition cost after native Android function/action execution and existing C/T5/PT-A controls.

### Android AppFunctions baseline + product decision
Official Android AppFunctions materially changes the product-side confidence:
- Android 16+ exposes an OS/Jetpack path for Agent discovery and local execution of app capabilities;
- the OS acts as a registry;
- declarations produce typed tool/function metadata;
- access is controlled by permissions, enabled state and access level;
- AndroidX 1.0.0-alpha12 (2026-09-23) adds experimental runtime function registration/callback APIs.

Together with SkillDroid, T6 now clears the **product-trend** threshold.

### Product posture
**BENCHMARK_AND_PREPARE**

T6 is promoted to **EMERGING_PRODUCT_TREND**, not ESTABLISHED_PRODUCT_TREND:
AppFunctions is still experimental/limited-access and target-phone workload economics are missing.

### Research boundary
No Direction is created.

AppFunctions is strong negative pressure on broad differentiation:
ordinary local Agent-tool discovery, schema, authority, enablement and function execution are becoming platform features.

The open residual is narrower:
genuinely dynamic executable artifacts whose compile/validate/instantiate/interpreter/JIT/code-cache/sandbox costs remain material on representative phones after native platform baselines.

### Round 14-B final
**PRODUCT TREND RETAINED — standalone differentiated Bet closed.**

PAPER-107 / SandScope and PAPER-108 / SpecBox close the current standalone residual:
- SandScope maps Agent-tool containment primarily to authority/provenance + platform security; WASI is not a unique CPU regime.
- SpecBox maps sandbox lifecycle to prediction, prewarm/prefetch, reuse and data-path orchestration.

### Differentiation action
**KILL_DIFFERENTIATED_BET for a standalone T6-specific Direction.**

Do not use KILL_PRODUCT_ROUTE.
T6 remains **EMERGING_PRODUCT_TREND / BENCHMARK_AND_PREPARE** and routes residual mechanisms to C + B-residual/T5 + PT-A.

Reopen only with physical-phone evidence for dynamic executable/JIT/code-cache/sandbox-transition costs that survive native Android/AppFunctions and existing software owners.

---

## T7 — Local multi-Agent concurrency & shared model/state

### Structural question
When several specialized local Agents share one phone/model/runtime, does the system create a distinct regime of:
- concurrent Agent queues;
- shared model/KV/adapters;
- agent identity/provenance;
- cross-agent prefetch/pre-prefill;
- synchronization/consistency;
- foreground/background Agent priority?

### Why it may matter
This could become a real product trend while still collapsing into C/B if all control variables are ordinary software-visible state.

### Current evidence state
Round 14-A deep-read MobiMem, LOCAL and EcoAgent.

The architecture trend is credible, but the reviewed evidence decomposes into existing software/platform owners:
- scheduling/future-consumer demand → C;
- versioned state/KV/adapter lifecycle → T5/B-residual;
- verification/recovery → PT-A.

Direct smartphone-SoC local multi-Agent shared-resource residual remains unestablished.

### Round 14 action
**WATCH — standalone differentiated Bet closed; reopen only on target-phone residual evidence**

---

## T8 — Cross-device Agent fabric & continuation

### Structural question
Does phone↔PC↔watch↔edge continuation require persistent execution-state handoff, consistency or recovery semantics that create a new phone CPU/system control point?

### Why it may matter
Cross-device agents are emerging, but the risk of rebranding ordinary distributed orchestration is high.

### Current evidence state
Round 14-C includes:
- DevicesWorld — executable mobile/desktop/IoT cross-device Agent benchmark;
- UFO³ — engineered distributed Agent DAG/protocol/recovery fabric;
- explicit Agent memory/config migration across edge servers;
- EdgeFlow + Windows Resume — strong generic state-transfer and product-continuity baselines.

The evidence confirms cross-device Agent continuation as a product trend but does not isolate a phone-specific CPU/uArch control point.

### Product posture
**BENCHMARK_AND_PREPARE**

T8 is promoted to **EMERGING_PRODUCT_TREND**.

### Differentiation action
**KILL_DIFFERENTIATED_BET for a standalone T8-specific Direction.**

Ownership:
- C — distributed placement/scheduling/retry/migration;
- B-residual/T5 — memory/context/KV/checkpoint state lifecycle;
- PT-A — authority/target/postcondition/recovery.

Reopen only if real phone experiments reveal in-flight Agent execution-state migration costs that remain after strongest generic state-transfer/platform baselines.

---

## Portfolio interpretation

Current portfolio should not be read as:
“only A is worth doing.”

It should be read as:
- **T1–T6 and T8 are meaningful product-evolution trends** with different maturity/originality levels.
- **A is currently the only differentiated Primary Bet.**
- C / PT-A / CG-06 / CG-07 / CG-01 can remain important product programs without being original Primary Bets.
- T6 and T8 are emerging Product Trends with standalone differentiation closed; T7 remains FRONTIER_SIGNAL / WATCH with existing-owner coverage.
- Round 14 frontier differentiation coverage is complete.

The final leadership roadmap should show both product importance and differentiation separately.
