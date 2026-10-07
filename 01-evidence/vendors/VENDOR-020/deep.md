# VENDOR-020 — Android AppFunctions / Local Agent-callable App Functions

## Source
Primary official sources:
- https://developer.android.com/ai/appfunctions
- https://developer.android.com/reference/android/app/appfunctions/package-summary
- https://developer.android.com/jetpack/androidx/releases/appfunctions
- https://developer.android.com/reference/androidx/appfunctions/AppFunctionManager
- https://developer.android.com/blog/posts/build-intelligent-android-apps-integrate-into-android-s-intelligence-system-using-app-functions

Review: FULL_10Q / EDP v1
Date: 2026-10-07
Priority: P0

## Q1 — What is officially exposed?
Android AppFunctions is an Android 16+ platform/Jetpack mechanism for applications to expose callable functions to Agent-style callers.

The official model includes:
- app-declared functions;
- OS indexing/registry;
- metadata search/discovery;
- local execution;
- function enabled/disabled state;
- caller permission/access control;
- Jetpack developer tooling/bindings.

Google describes the app as analogous to a local MCP server and Android as the registry connecting Agent callers to app capabilities.

## Q2 — What is the actual mechanism?
Build-time path:
1. app declares/annotates an AppFunction;
2. Jetpack tooling generates metadata/schema/integration code;
3. Android indexes the function;
4. authorized callers discover metadata;
5. callers execute via AppFunctionManager / Jetpack APIs.

The important technical boundary is that generated tool definitions are **typed metadata and bindings**, not evidence of Agent-generated machine code.

## Q3 — What changed in 2026?
By AndroidX AppFunctions **1.0.0-alpha12 (2026-09-23)**, the library adds experimental runtime registration APIs:
- registerAppFunction;
- registerAppFunctions;
- RegisterAppFunctionRequest;
- CallbackAppFunction.

On supported API levels, an app can register callback-backed function implementations at runtime.

This increases T6 relevance because function lifecycle is not purely static build-time metadata.

## Q4 — What authority / access model exists?
AppFunctions is not unrestricted cross-app execution.

Official APIs expose:
- caller permission requirements;
- access levels such as SELF / SYSTEM / ANDROID_TRUSTED;
- function enabled state;
- privileged/system Agent discovery/execution paths.

This maps strongly to PT-A's authority/capability boundary.

## Q5 — What lifecycle state exists?
Runtime registration has explicit lifecycle semantics:
- callbacks are associated with the registering process/context;
- execution depends on the registering process remaining available;
- destroyed context/process state can remove/invalidate registration.

This is useful product/system state, but it remains software-visible lifecycle state.

## Q6 — What does execution actually mean?
AppFunctions invokes app-provided function implementations locally through Android's platform/Jetpack path.

It does **not** by itself mean:
- arbitrary runtime native code generation;
- WASM compilation;
- JVM/ART JIT changes caused by Agent identity;
- new executable pages or code-cache policy;
- a distinct CPU frontend mechanism.

Thus AppFunctions is a strong native baseline that any broader T6 CPU claim must beat.

## Q7 — Product maturity / deployment boundary
Strengths:
- official Android platform documentation;
- Android 16+ API family;
- Jetpack release train;
- discovery, execution, permissions and runtime registration are explicit APIs.

Boundaries:
- official docs still describe the feature as experimental/preview;
- full end-to-end Agent integration is limited to supported/privileged Agent paths and early-access scenarios;
- no canonical target-phone benchmark here measures frequency, latency, battery, thermal or foreground QoE of large-scale AppFunction use.

Therefore this supports **EMERGING_PRODUCT_TREND**, not ESTABLISHED_PRODUCT_TREND.

## Q8 — Evidence vs inference
### [PUBLIC_CAPABILITY]
Android exposes AppFunctions as a platform/Jetpack capability for Agent-callable app functions.

### [PUBLIC_CAPABILITY]
AndroidX alpha12 adds experimental runtime function registration.

### [PUBLIC_CAPABILITY]
Permissions, enabled state, metadata discovery and execution are platform-visible.

### [INFERENCE — project]
Local Agent tool execution is sufficiently product-real to promote T6 from frontier signal to emerging product trend.

### [INFERENCE — project]
Broad novelty is reduced: registry/schema/authority/lifecycle/function invocation are becoming platform capabilities.

### [NOT ESTABLISHED]
A phone CPU/uArch residual for arbitrary dynamic code generation/JIT/code-cache/sandbox transitions.

## Q9 — Project decision
Combined evidence:
- PAPER-106: procedural skill materialization/replay in mobile GUI automation;
- VENDOR-020: official Android typed function registry/execution with runtime registration.

Product decision:
- T6 trend maturity → **EMERGING_PRODUCT_TREND**
- product posture → **BENCHMARK_AND_PREPARE**

Differentiation:
- no new Direction;
- no second Primary Bet;
- no score/lane change;
- no uArch candidate.

Current ownership pressure:
- AppFunction registry/lifecycle + generic execution policy → C/platform;
- versioned reusable skill/function state → T5;
- permissions/authority/verification → PT-A.

## Q10 — Next discriminating evidence
Do not search broadly for more “tool calling”.

Test only the narrow residual:
1. dynamic Agent-generated WASM/DSL/bytecode or equivalent artifacts;
2. target-phone creation/validation/instantiation frequency;
3. interpreter/JIT/code-cache and sandbox transition cost;
4. energy/thermal/foreground-QoE effect;
5. strongest native AppFunctions + T5/PT-A/C baseline;
6. whether any control variable remains non-reconstructible from ordinary software-visible lifecycle/state.

MCP-SandboxScan and SpecBox are useful only if they sharpen this residual.

## Decision footer
- Evidence role: DIRECT_PLATFORM_PRODUCT / strongest Android baseline
- Source confidence: high for public platform capability
- Product maturity impact: promote T6 to EMERGING_PRODUCT_TREND
- Differentiation impact: narrow broad novelty; no Direction
- Hardware impact: none
- Primary URL: https://developer.android.com/ai/appfunctions
