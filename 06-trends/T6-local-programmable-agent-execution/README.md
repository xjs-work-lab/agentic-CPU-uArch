+++
id = "T6"
type = "TREND"
record_state = "CURRENT"
title = "Local programmable Agent execution & sandboxed skills"
time_horizon = "2027-2029"
scope = "SMARTPHONE_AGENTIC_CPU_SYSTEM_UARCH"
trend_maturity = "FRONTIER_SIGNAL"
product_posture = "WATCH"
coverage_state = "SEED_TRIAGE_COMPLETE"
related_claims = []
related_capabilities = []
direction_links = []
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
