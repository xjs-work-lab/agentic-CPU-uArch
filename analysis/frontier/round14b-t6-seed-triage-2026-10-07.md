# Round 14-B — T6 Local Programmable Agent Execution Seed Triage

Date: 2026-10-07
State: SEED_TRIAGE_COMPLETE / NOT DECISION-COMPLETE

Question:
> Do local programmable Agent skills create a repeated smartphone execution regime with a control point beyond ordinary tool invocation, workflow scheduling, state lifecycle and authority/verification?

## Seed 1 — SkillDroid
Primary: https://arxiv.org/abs/2604.14872

Why it matters:
- direct mobile GUI Agent setting;
- converts successful LLM-guided trajectories into persistent parameterized skill templates;
- replays the resulting interaction program with zero per-step LLM calls on the normal replay path;
- includes state verification, bounded step fallback and failure-triggered recompilation.

Reported signals:
- 150-round longitudinal evaluation over 15 Android task types;
- 85.3% overall success, reported as 23 percentage points above a stateless LLM baseline;
- 49% fewer LLM calls;
- paper body reports 100% success across 79 replay rounds and 2.4× replay speed versus full LLM execution.

Source-quality note:
the arXiv abstract contains an apparent “1000%” typo; the paper body reports **100%**. Use the body value.

T6 interpretation:
- strong evidence that repeated Agent behavior can become an **executable procedural artifact**, not merely natural-language memory;
- however the artifact is a typed GUI action program interpreted/replayed through DroidRun/ADB/accessibility mechanisms;
- no demonstrated native/JIT machine-code generation, CPU code-cache churn, battery/thermal effect or phone-specific sandbox-transition bottleneck.

Ownership pressure:
- reusable/versioned skill artifact → T5;
- state verification/fallback/recovery → PT-A;
- execution timing/resource policy → C.

Pressure:
**SkillDroid strengthens T6 product relevance but does not yet establish a standalone T6 Direction.**

## Seed 2 — Android AppFunctions
Official:
- https://developer.android.com/ai/appfunctions
- https://developer.android.com/reference/android/app/appfunctions/package-summary
- https://developer.android.com/jetpack/androidx/releases/appfunctions
- https://developer.android.com/blog/posts/build-intelligent-android-apps-integrate-into-android-s-intelligence-system-using-app-functions

Why it matters:
- Android 16+ platform/Jetpack feature for Agents to discover and execute app functionality locally;
- Android acts as a registry; trusted/system-privileged callers invoke exposed functions;
- current Android documentation describes type-safe, sandboxed tool definitions and explicit permission/authority boundaries;
- September 23, 2026 Jetpack alpha12 adds runtime registration APIs among other changes.

Critical distinction:
AppFunctions makes **local Agent-callable tools a product/platform reality**, but normal functions are app/developer-defined. Build-time generated bindings/tool definitions are not evidence that the Agent repeatedly generates new CPU executable code at runtime.

T6 interpretation:
- raises the strongest platform baseline substantially;
- likely product path for many “local skills” without a novel CPU execution substrate;
- pushes any differentiated T6 thesis toward dynamic artifacts that cannot be represented as ordinary registered functions.

Pressure:
**AppFunctions is negative pressure on broad T6 novelty while positive evidence for product relevance.**

## Seed 3 — MCP-SandboxScan
Primary: https://arxiv.org/abs/2601.01241

Why it matters:
- executes untrusted Agent/MCP tools inside a WebAssembly/WASI sandbox;
- targets runtime-only security/provenance behavior that static scanning can miss;
- demonstrates that tool execution introduces genuine capability and exposure boundaries.

T6 interpretation:
- strong baseline for sandbox/capability semantics;
- no smartphone or phone-SoC system-value evidence;
- currently more relevant to PT-A/platform security than to a new CPU/uArch Direction.

Pressure:
**Keep as strongest isolation baseline, not as phone residual evidence.**

## Seed 4 — SpecBox
Primary: https://arxiv.org/abs/2607.23933

Why it matters:
- exposes a real Agent sandbox lifecycle tension: persistent reservation wastes memory, lazy creation causes cold-start/tail latency;
- uses speculative prewarming/prefetch, semantic result caching and a shared-memory transport path;
- reports up to 2.9× lower P99 end-to-end latency than on-demand sandboxing and 45.9% lower peak memory than persistent reservation in its evaluated high-concurrency setting.

Critical boundary:
- multi-tenant server/disaggregated sandbox regime;
- not smartphone evidence;
- mechanisms map naturally to scheduling/prediction and reusable-state ownership.

Pressure:
**SpecBox raises the strongest generic runtime baseline that a phone-specific T6 claim must beat.**

## Cross-seed synthesis

### Product trend
**KEEP T6 as FRONTIER_SIGNAL / WATCH.**

There is now credible evidence that Agent execution is moving toward:
- persistent executable/procedural skills;
- typed local tool registries;
- explicit capability/sandbox boundaries;
- managed executable/sandbox lifecycle.

That is enough to keep the product trend under active audit.

### New Direction
**NOT YET.**

The current evidence largely decomposes into existing ownership:
- skill/tool state, versions, reuse and residency → T5;
- execution scheduling and warm/cold lifecycle policy → C;
- capability, authority, verification and recovery → PT-A;
- ordinary app function execution → Android/platform baseline.

### Surviving T6 residual question
A standalone T6 Direction requires evidence that:
1. Agent-executable artifacts are generated/updated/executed locally on representative phones at meaningful frequency.
2. Their compile/validate/load/instantiate/interpreter/JIT/code-cache/sandbox-transition costs materially affect end-to-end latency, energy, thermal behavior or foreground QoE.
3. A useful control variable remains after ordinary AppFunctions, C scheduling, T5 state/version lifecycle and PT-A authority/verification are included.
4. The residual can be isolated with a smallest discriminating experiment.

Potential residual variables to test, not yet claims:
- executable-artifact trust/validity state;
- hot-skill/code residency and eviction;
- interpreter/JIT tier or compile timing;
- capability-bound executable reuse;
- cross-version invalidation of executable Agent artifacts.

## Next
Deep-read in this order:
1. **SkillDroid FULL_10Q** — strongest direct mobile evidence.
2. **Android AppFunctions deep vendor card** — strongest product baseline.
3. **MCP-SandboxScan FULL_10Q if needed** — isolation baseline.
4. **SpecBox FULL_10Q if needed** — lifecycle/scheduling baseline.

Then issue the ownership/residual decision:
- NEW DIRECTION;
- MERGE INTO C/T5/PT-A;
- WATCH;
- KILL_DIFFERENTIATED_BET.

No trend maturity, portfolio lane, score or uArch change at seed-triage stage.
