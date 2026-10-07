+++
id = "T6"
type = "TREND"
record_state = "CURRENT"
title = "Local programmable Agent execution & sandboxed skills"
time_horizon = "2027-2029"
scope = "SMARTPHONE_AGENTIC_CPU_SYSTEM_UARCH"
trend_maturity = "EMERGING_PRODUCT_TREND"
product_posture = "BENCHMARK_AND_PREPARE"
coverage_state = "OWNED_BY_EXISTING_DIRECTIONS_AND_PLATFORM"
related_claims = ["CLM-T6-001", "CLM-T6-002", "CLM-T6-003", "CLM-T6-004", "CLM-T6-005", "CLM-T6-006"]
related_capabilities = []
direction_links = [{ direction_id = "C", differentiation_posture = "RESIDUAL_RESEARCH" }, { direction_id = "B-residual", differentiation_posture = "RESIDUAL_RESEARCH" }, { direction_id = "PT-A", differentiation_posture = "RESIDUAL_RESEARCH" }]
+++

# T6 — Local programmable Agent execution & sandboxed skills

## Product thesis
T6 asks whether locally generated/interpreted code, scripts, WASM/DSL bundles or dynamically composed skills become a repeated smartphone workload that materially changes CPU/runtime behavior. It is a frontier signal, not yet a Direction.

## Interpretation invariant
A paper or product may strengthen this Trend while simultaneously narrowing the novelty of one or more linked Directions.

> **Prior art constrains novelty, not product relevance.**


## Round 14-B seed triage

### Strongest direct mobile seed — SkillDroid
SkillDroid compiles a successful LLM-guided Android GUI trajectory into a typed parameterized action program, persists it locally, and mechanically replays it through Android automation with verification/fallback.

Primary: https://arxiv.org/abs/2604.14872

Important boundary:
- this is genuinely executable Agent procedural state;
- it is **not** evidence of native/JIT-generated machine code or a new CPU frontend regime;
- the paper does not yet establish phone CPU energy/thermal/code-cache/sandbox-transition residuals.

### Strongest current Android product baseline — AppFunctions
Android AppFunctions exposes app-defined functions to trusted/system-privileged Agents through an OS registry and local discovery/execution path.

Official:
- https://developer.android.com/ai/appfunctions
- https://developer.android.com/reference/android/app/appfunctions/package-summary
- https://developer.android.com/jetpack/androidx/releases/appfunctions

Important boundary:
AppFunctions productizes local typed Agent tools and authority boundaries, but normal AppFunctions are developer/app-defined functionality. Build-time/generated tool definitions must not be confused with runtime Agent code generation.

### Generic runtime pressure baselines
- MCP-SandboxScan — https://arxiv.org/abs/2601.01241
- SpecBox — https://arxiv.org/abs/2607.23933

These establish that sandbox capability isolation and sandbox lifetime can matter in Agent systems, but neither is direct smartphone CPU/uArch evidence.

## Seed-stage decision
- Trend maturity: **FRONTIER_SIGNAL unchanged**
- Product posture: **WATCH unchanged**
- New Direction: **none**
- Second differentiated Primary Bet: **still unfilled**
- uArch candidate: **none**

## Surviving residual gate
T6 becomes a Direction only if target-phone evidence shows all of the following:
1. Agent-executable artifacts are created/updated/executed locally at meaningful frequency.
2. Compile/validate/load/instantiate/interpreter/JIT/code-cache/sandbox-transition costs are material to end-to-end phone outcomes.
3. The relevant control variable is not already ordinary function invocation, C-style workflow/resource scheduling, T5-style state/version lifecycle, or PT-A-style authority/verification.
4. A smallest discriminating experiment can isolate the residual against the strongest software/runtime baseline.

## Next
FULL_10Q SkillDroid first; then deep-read the Android AppFunctions product baseline and only the sandbox papers needed to pressure-test the residual.


## SkillDroid FULL_10Q — PAPER-106
SkillDroid converts successful LLM-guided mobile GUI trajectories into persistent **parameterized interaction programs** with typed slots, weighted UI locators, state descriptors, verification/fallback and versioned recompilation.

In its controlled 150-round Android-emulator evaluation, SkillDroid reports 85.3% success versus 62.0% for the same Layer-1 stack without skills, while mean LLM calls fall from 11.3 to 5.8. Pure replay accounts for 35/150 rounds with zero LLM calls.

### Critical boundary
"Compile" means a structured GUI-action template persisted in SQLite and replayed through DroidRun/ADB. It does **not** establish native machine-code generation, WASM/bytecode, interpreter/JIT tiering, code-cache churn, executable-page management or phone sandbox-transition cost.

All experiments run on a Windows 11 host driving a Pixel 9a/API 35 Android emulator via ADB. The paper reports ~100 ms per ADB action and notes native Android AccessibilityService performAction() can be ~4 ms.

### Decision
- Trend maturity: **FRONTIER_SIGNAL unchanged**
- Product posture: **WATCH unchanged**
- New Direction: **none**
- Second differentiated Primary Bet: **unfilled**
- uArch candidate: **none**

Current ownership pressure:
- skill state/version/reuse → T5;
- verification/fallback/provenance → PT-A;
- execution/resource policy → C.

## Next
Deep-read Android AppFunctions as the strongest current native Android product baseline, then test whether any dynamic executable-artifact residual remains.


## Android AppFunctions deep vendor baseline — VENDOR-020

### Product signal
Android AppFunctions is a direct OS/platform signal that local Agent-callable functions are moving into the Android product stack.

Official documentation establishes:
- Android 16+ platform and Jetpack AppFunctions APIs;
- Android as a registry for app-defined functions;
- local discovery and execution by authorized/system-privileged Agent callers;
- type-safe function/tool metadata generated from app declarations;
- enabled-state and permission/access-level control;
- AndroidX 1.0.0-alpha12 runtime registration APIs for callback-backed functions.

This is stronger than a static “tool schema” seed because Android now exposes function lifecycle/discovery/execution as explicit platform state.

### Important boundary
AppFunctions does **not** establish arbitrary Agent-generated native code, JIT compilation or a new CPU instruction stream.

Build-time generated tool definitions are metadata/bindings.
Runtime registration registers callback implementations/signatures whose lifetime is tied to the registering app process/context.

### Product decision
T6 is promoted:
- **FRONTIER_SIGNAL → EMERGING_PRODUCT_TREND**
- **WATCH → BENCHMARK_AND_PREPARE**

Reason:
PAPER-106 supplies direct mobile procedural-skill evidence and VENDOR-020 supplies an official Android product/platform path.

Why no higher:
AppFunctions remains experimental/limited-access and representative target-phone cost/energy/QoE data are missing.

### Differentiation decision
- New Direction: **none**
- Direction links: **none**
- Second differentiated Primary Bet: **unfilled**
- uArch candidate: **none**

AppFunctions raises the strongest software baseline. A T6 Direction now requires evidence for **genuinely dynamic executable artifacts** whose phone-local compile/validate/instantiate/interpreter/JIT/code-cache/sandbox costs remain material after AppFunctions + T5 + PT-A + C baselines.

## Next
Pressure-test MCP-SandboxScan and SpecBox only to the depth needed to close or preserve that narrow residual.


## Round 14-B final pressure — PAPER-107 + PAPER-108

### SandScope
Current v2 expands the original MCP-SandboxScan seed to controlled cross-language subjects plus a 100-repository MCP corpus. WASI is useful for portable artifacts, but native protocol execution plus OS containment remain first-class paths. No target-phone executable-lifecycle cost is measured.

### SpecBox
SpecBox demonstrates large sandbox cold-start/lifecycle cost in server Agent serving and recovers value through prediction, prewarm/prefetch, result reuse and shared-memory transport. These are software-visible C/T5-class controls.

## Final T6 decision
- Product Trend: **KEEP EMERGING_PRODUCT_TREND**
- Product posture: **BENCHMARK_AND_PREPARE**
- standalone T6-specific candidate: **KILL_DIFFERENTIATED_BET**
- ownership: **C + B-residual/T5 + PT-A**
- no T6-specific Direction
- no second Primary Bet
- no uArch candidate

## Reopen condition
Require representative physical-phone evidence for residual dynamic executable generation/validation, interpreter/JIT cadence, code-cache/I-cache churn, sandbox transitions, or energy/thermal/QoE after AppFunctions + C/T5/PT-A.
