# Round 14-B — SkillDroid FULL_10Q result

Date: 2026-10-07
Source: PAPER-106
State: COMPLETE

## Product-trend impact
**T6 strengthened; no maturity change.**

SkillDroid directly shows a mobile-Agent trajectory becoming a persistent executable procedural artifact rather than only textual memory. Repeated tasks can shift from full reasoning every step to skill lookup, verified replay and repair/recompile.

## Critical correction to "compile"
PAPER-106 does not compile Agent behavior into native machine code, WASM or a demonstrated bytecode/JIT target. It builds typed parameter slots, weighted Android UI locators, state descriptors, a structured action skeleton and versioned SQLite skill templates.

Replay executes through DroidRun/ADB. The evidence supports **procedural skill materialization**, not a new CPU instruction/code-cache regime.

## Measured value
Controlled same-stack baseline:
- success: 85.3% vs 62.0%;
- mean LLM calls: 5.8 vs 11.3;
- mean latency: 69.0 s vs 84.1 s;
- pure 0-LLM replay: 35/150 rounds;
- all non-full-fallback Layer-2 variants: 79 rounds, 100% reported success.

## Deployment boundary
Windows 11 host + Pixel 9a/API 35 Android emulator + ADB + remote OpenAI API for reasoning paths.

The paper reports ~100 ms ADB action latency versus ~4 ms cited for native AccessibilityService performAction(). There is no direct target-phone CPU/system-value result for executable lifecycle.

## Ownership pressure
- skill/version/reuse → **T5**
- verify/fallback/repair/provenance → **PT-A**
- execution/warm-cold policy → **C**

## Decision
- T6 = FRONTIER_SIGNAL / WATCH unchanged
- new Direction = none
- second differentiated Primary Bet = UNFILLED
- score/lane changes = none
- uArch candidate = none

## Next
Deep-read Android AppFunctions as the strongest current native Android baseline, then ask whether dynamic skill creation/validation/loading/sandboxing leaves a material phone-local residual beyond state/version/authority/resource-control software.
