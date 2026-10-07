# PAPER-037 — ClawMobile — EDP v1 FULL_10Q

Re-reviewed: 2026-10-07

## Q1 — Problem + target mapping
Smartphone Agents must execute across fragmented interfaces whose reliability differs: structured device/system APIs are deterministic but incomplete, while GUI automation is broad but brittle to timing, UI drift, prompts and app state.

ClawMobile makes this an explicit runtime problem: a high-level orchestrator selects among deterministic backends and semantic UI control, then checks progress and recovers.

Project mapping: direct PT-A smartphone runtime evidence.

## Q2 — Novelty / new-regime relevance
The architecture separates probabilistic planning from bounded control backends and makes backend selection iterative rather than one-shot.

Classification: **Agent-native mobile runtime integration**, but the individual mechanisms—tool routing, ADB/Termux APIs, GUI agents, verification—are not globally novel.

## Q3 — Falsifiable hypothesis
A hierarchical phone runtime that preferentially uses structured backends and explicitly verifies progress should complete heterogeneous mobile tasks more reliably than a single GUI backend or a naive hybrid runtime.

## Q4 — Research lineage / competing route
Relevant routes:
- pure GUI/mobile agents such as DroidRun;
- tool/API-first mobile control;
- later mixed-action systems such as PhoneHarness;
- learned routing such as HybridCUA.

ClawMobile is an independent MBZUAI-led line relative to the other PT-A core sources.

## Q5 — Mechanism / control point
`task → orchestrator → capability lookup/backend choice → bounded backend result → device-state re-observation → completion test → retry/replan/reselect`

Backends include:
- ADB/system commands;
- Termux API;
- DroidRun semantic UI backend.

The maintained implementation exposes progressive capabilities, so availability/authority is part of the effective action surface.

## Q6 — Experiment design + quantitative results
Device: Google Pixel 9, Android 16.

Agents:
- DR = DroidRun;
- CM-w/o-DR = ClawMobile without advanced UI backend;
- CM = full ClawMobile.

All use GPT-5.2 as the underlying model.

Six tasks:
1. Settings dark theme: completion 100/100/100%; 26/22/21 s.
2. Chrome gold price: 73/100/100%; 26/67/67 s.
3. Install RedNote: 33/100/100%; 29/232/117 s.
4. YouTube play video / skip ad: 100/80/100%; 66/600/88 s.
5. YouTube comment: 85/50/100%; 121/600/235 s.
6. Cross-app Premier League summary: 73/100/100%; 60/219/145 s.

Full ClawMobile reaches 100% reported completion on this small set but is on average slower than DroidRun.

## Q7 — Artifact / reproducibility
Strengths:
- real retail-class Android device;
- open-source implementation;
- explicit phone-side runtime;
- action backend outputs are machine-readable.

Important deployment correction:
the paper states: **ClawMobile runs locally, while model inference is performed remotely**.
The runtime asks for model-provider/API credentials. Therefore “on-device runtime” must not be interpreted as “on-device GPT-5.2 inference.”

Comparator asymmetry:
DroidRun runs on a host machine connected over USB, while ClawMobile runs on the phone.

## Q8 — Evidence vs alternative explanations
Demonstrated:
- heterogeneous backend coordination is practical on a real phone;
- explicit state re-observation/recovery is part of a successful runtime.

Not isolated:
- exact causal contribution of verification vs backend capability vs orchestration;
- energy/power benefit;
- local-model benefit.

The six-task set is too small to establish a universal reliability gain.

## Q9 — Decision contribution
Supports PT-A as a **platform/runtime track**.

It does not support:
- a CPU/uArch mechanism;
- on-device model execution;
- universal deterministic-first optimality.

The strongest reusable lesson is a capability-aware actuation contract with bounded results and explicit progress checks.

## Q10 — Next action
KEEP P0.
Use in PT-A as real-phone feasibility evidence.
Compare future PT-A against learned routing and adversarial context mutation, not only GUI-only.

## Decision footer
- Evidence maturity: **SYSTEM_VALUE for phone runtime integration**
- Decision impact: KEEP PT-A; narrow deployment interpretation
- Open questions: larger task set, local-model overhead, permission/authority semantics, security under state mutation
- Primary source: https://arxiv.org/abs/2602.22942
