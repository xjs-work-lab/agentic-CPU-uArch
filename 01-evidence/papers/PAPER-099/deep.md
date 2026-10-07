# PAPER-099 — MobileExplorer

## Source
- arXiv:2605.26546, 2026 preprint
- Samsung Galaxy S24 + Jetson AGX Orin + MacBook Air M4 inference platforms
- AndroidWorld + added complex/dynamic tasks
- Priority: P1

## Q1 — Problem + target mapping
Vision-based GUI Agents repeatedly execute:
`screenshot → VLM reasoning → action → new screenshot`.

On phones, VLM reasoning dominates latency while UI actions are comparatively cheap.

Target mapping:
> can the Agent safely use long reasoning stalls to explore the environment and reduce later reasoning?

## Q2 — Novelty / new-regime relevance
MobileExplorer overlaps:
- expensive VLM reasoning on the current state;
- lightweight speculative UI probes of likely-relevant controls.

Exploration must then rollback to the state used by the VLM before the official action is committed.

Classification:
**NATIVE to interactive Agent execution**, but its control semantics strongly overlap PT-A speculation/rollback.

## Q3 — Falsifiable hypothesis
If reasoning latency creates usable slack, safe parallel exploration should reduce future uncertainty/steps without extending the critical path.

Falsifiers:
- rollback is unreliable or expensive;
- exploration changes state irreversibly;
- exploration competes materially with VLM inference for power/memory;
- hints do not reduce future reasoning;
- strong hierarchical planning achieves the same benefit without speculative actions.

## Q4 — Research lineage / competing route
Competing routes:
- AutoDroid / AutoDroid-V2 prebuilt UI graphs/scripts;
- verifier/candidate-selection pipelines;
- GUI history/context pruning;
- hierarchical local executors;
- PT-A-style speculative action safety and rollback.

## Q5 — Key mechanism / control point
1. rank clickable elements by task relevance;
2. probe selected UI branches during VLM inference;
3. use fast backtracking first;
4. if needed, use home-and-replay recovery;
5. summarize exploration into compact hints for subsequent reasoning.

The critical control variable is **whether an exploratory action is safely reversible within the reasoning window**.

## Q6 — Experiment design
Motivation:
- Samsung Galaxy S24, 12 GB RAM;
- 2B/4B-class VLMs via llama.cpp Q8;
- measured on-device reasoning latency is tens of seconds in representative tasks.

Main benchmark:
- AndroidWorld;
- emulator executes GUI environment while model inference runs on target hardware via HTTP for stable latency measurement;
- three inference platforms: Galaxy S24, Jetson AGX Orin, MacBook Air M4.

Reported:
- headline reduction in average reasoning steps/end-to-end latency around 23% in reported settings;
- success maintained or improved by up to ~5%;
- AndroidWorld success reported around 50.9% in one table;
- system controller adds little memory/power overhead relative to model inference.

## Q7 — Data / artifact / reproducibility
Strengths:
- direct mobile inference measurements;
- explicit rollback mechanism;
- end-to-end Agent metric, not only kernel latency;
- multiple hardware classes;
- dynamic UI tasks.

Limitations:
- preprint;
- benchmark GUI execution is separated from inference device in the main setup;
- rollback safety depends on app/UI semantics;
- no strong transaction/effect-class baseline;
- code release stated as pending acceptance in the manuscript.

## Q8 — Evidence vs hypothesis
### [FACT]
VLM reasoning dominates per-step latency in the tested on-device setup.

### [FACT]
Parallel UI exploration with rollback can reduce task steps/end-to-end latency in the reported evaluation.

### [OBSERVATION]
Agent reasoning latency creates an exploitable environment-interaction slack window.

### [INFERENCE — project]
This is a strong PT-A workload for speculative-effect classes and rollback, not an independent CPU/uArch control point.

## Q9 — Real contribution to project decision
MobileExplorer strengthens PT-A because it turns speculative action/rollback from an abstract safety mechanism into a latency-reduction technique for mobile GUI Agents.

It does not justify a new Direction:
- speculation legality is already PT-A-owned;
- high-level task relevance can be software-derived;
- no lower-layer hardware residual is shown.

## Q10 — Next action
1. KEEP as PT-A baseline/workload evidence.
2. Add “reasoning-window speculative exploration” to PT-A evaluation scenarios.
3. Compare against effect-class-aware bounded speculation.
4. No score/lane change.

## Decision footer
- **Evidence maturity:** partial mobile SYSTEM_VALUE
- **Decision impact:** strengthens PT-A workload; no new Direction
- **Open questions:** same-device interference, rollback correctness, irreversible actions
- **Primary source:** https://arxiv.org/abs/2605.26546
