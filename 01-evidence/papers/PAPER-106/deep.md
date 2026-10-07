# PAPER-106 — SkillDroid: Compile Once, Reuse Forever

## Source
- Primary: https://arxiv.org/abs/2604.14872
- HTML: https://arxiv.org/html/2604.14872v1
- Authors: Qijia Chen, Andrea Bellucci, Zhida Sun, Giulio Jacucci
- Institutions: University of Helsinki; Universidad Carlos III de Madrid; Shenzhen University
- Date: arXiv v1, 2026-04-16
- Review: FULL_10Q / EDP v1
- Priority: P0
- Dependency framework: https://github.com/droidrun/droidrun
- SkillDroid-specific code status at v1: paper says code/evaluation scripts will be released upon acceptance; no project-specific artifact is treated as verified here.

## Q1 — Problem + target mapping
SkillDroid asks whether repeated mobile GUI tasks must invoke an LLM at every action step or whether a successful trajectory can become a reusable executable procedural skill.

Project mapping:
1. **T6:** product relevance of local programmable Agent execution.
2. **T5:** reusable procedural skills as versioned persistent Agent state.
3. **PT-A:** verification, fallback and repair.
4. **C:** warm/cold execution and resource policy.
5. **CPU/uArch:** whether interpreter/JIT/code-cache/sandbox cost survives strong native software baselines.

## Q2 — Novelty / new-regime relevance
The useful novelty is **trajectory → parameterized executable interaction program**.

A successful Layer-1 run yields typed argument slots, a generalized intent pattern, weighted element locators, state descriptors, an action skeleton and a persistent versioned skill. Later invocations can match and replay it without full per-step LLM reasoning.

This is a credible product/workload signal, but not evidence for a new CPU execution substrate.

## Q3 — Falsifiable hypothesis
Paper hypothesis:
> compiling successful mobile-GUI trajectories into parameterized executable skills improves repeated-task reliability and reduces repeated LLM calls/latency versus an otherwise identical stateless executor.

The controlled emulator/ADB evaluation supports that hypothesis.

T6 differentiation hypothesis:
> if programmable Agent skills create a distinct smartphone CPU/system regime, target-phone execution should expose material compile/validate/load/instantiate/interpreter/JIT/code-cache/sandbox-transition cost that survives native function/action execution plus ordinary state/scheduling/verification baselines.

PAPER-106 does not test that second hypothesis.

## Q4 — Research lineage / strongest competing routes
Source-local alternatives include:
- mobile GUI agents reasoning each step: DroidBot-GPT, AutoDroid, AppAgent, Mobile-Agent;
- natural-language workflow/experience memories;
- generated Python/REST tools;
- MobileGPT, which caches procedures but still uses a lighter LLM during replay;
- simulated executable skill libraries such as Voyager.

For this project the stronger product baseline is:
1. native Android accessibility/action execution;
2. Android AppFunctions-style typed local functions;
3. versioned procedural-state reuse;
4. verified fallback/recovery.

That baseline must be beaten before T6 can become a differentiated Direction.

## Q5 — Mechanism / actual execution object
### Layer 1
TaskOrchestrator executes up to 20 GUI steps. After verified success, SkillCompiler extracts typed slots, generalizes the intent, builds weighted element locators, derives replay state and stores the template in synchronous SQLite.

### Layer 2
Matching uses regex, all-MiniLM-L6-v2 embedding similarity and app filtering. The action skeleton replays through DroidRun/ADB with state verification, step skipping, bounded step-level LLM fallback or full Layer-1 fallback.

### Layer 3
Failure state is tracked. Failure rate above 0.5 triggers later recompilation. Recovered trajectories create new versions, capped at 3.

### T6 interpretation
The executable object is a **typed, versioned procedural state artifact**. It is not native machine code, WASM, demonstrated bytecode/JIT, or a measured executable-page/code-cache workload.

## Q6 — Experiment design + results
Main experiment:
- 150 rounds / 15 Android task types;
- four instruction-variation levels;
- controlled perturbations;
- 5 phases from initial compilation to steady-state reuse;
- gpt-4o-mini main; 75-round gpt-4o supplementary;
- programmatic ADB/device-state ground truth.

Controlled baseline keeps the same tasks, LLM, prompts, action execution, reset and checker but removes skill matching/replay/compilation.

Reported aggregate:
- SkillDroid: 128/150 = 85.3%; 5.8 LLM calls/round; 69.0 s/round.
- Baseline: 93/150 = 62.0%; 11.3 calls/round; 84.1 s/round.

Replay paths:
- Pure replay: 35 rounds, 100%, 0 LLM calls, 36.0 s.
- Semantic-match replay: 32 rounds, 100%, 1.0 call, 54.7 s.
- Step-level fallback: 12 rounds, 100%, 5.0 calls, 50.9 s.
- All non-full-fallback Layer 2: 79 rounds, 100%, 1.2 calls, 45.1 s.
- Layer2→Layer1 full fallback: 29 rounds, 75.9%, 10.1 calls, 113.2 s.
- Fresh Layer1: 42 rounds, 64.3%, 11.6 calls, 84.0 s.

Important correction: only **35/150 pure-replay rounds** are zero-LLM; not every Layer-2 variant is.

## Q7 — Deployment / reproducibility / limitations
Implementation:
- Python 3.12;
- DroidRun v0.5;
- synchronous SQLite;
- all-MiniLM-L6-v2, 22M / ~80 MB;
- Windows 11 host;
- Pixel 9a / API 35 Android emulator;
- ADB action execution;
- remote OpenAI API for reasoning paths.

This is **not a physical-phone experiment**.

The paper reports ~100 ms per ADB action and ~4 ms for native Android AccessibilityService performAction(), making the evaluated action path roughly 25× slower than the cited native path.

Other limits:
- text-only accessibility-tree perception;
- English only;
- one main LLM family;
- 15 task types;
- one task/one app per skill;
- physical-device breadth is future work;
- limited perturbation set;
- SkillDroid-specific code not yet treated as a verified public artifact at v1.

## Q8 — Evidence vs hypothesis
### [FACT]
Same-stack comparison reports higher success and lower LLM-call demand with skills.

### [FACT]
Pure replay can execute a stored action skeleton without an LLM call; 35/150 rounds use this path.

### [FACT]
The compiled artifact is parameterized GUI actions + locators/state descriptors + versions, replayed via DroidRun/ADB.

### [FACT]
All experiments use a Windows host + Android emulator.

### [INFERENCE — project]
SkillDroid strengthens T6 as a product trend signal for persistent executable/procedural Agent skills.

### [INFERENCE — project]
It does not establish a standalone T6 CPU/uArch Direction because current value is explained by avoiding repeated LLM reasoning, procedural-state reuse, verification/fallback and GUI automation.

## Q9 — Project decision
### T6
PAPER-106 materially strengthens product relevance but narrows the differentiated mechanism:
- no native codegen;
- no WASM/JIT;
- no phone code-cache evidence;
- no target-phone sandbox cost;
- no energy/thermal/QoE result.

Therefore:
- Trend maturity: **FRONTIER_SIGNAL unchanged**
- Product posture: **WATCH unchanged**
- New Direction: **none**

### Ownership
- **T5:** persistent/versioned/reusable procedural state.
- **PT-A:** state verification, bounded fallback, repair and provenance.
- **C:** warm/cold execution/resource scheduling.

PAPER-106 does not cross STRUCTURAL_SIGNAL → SYSTEM_VALUE → SOFTWARE_INSUFFICIENCY for programmable-code execution on a target phone.

## Q10 — Next
1. Keep PAPER-106 as P0 / FULL_10Q.
2. Link CLM-T6-001 and CLM-T6-002 to T6.
3. Preserve T6 FRONTIER_SIGNAL / WATCH.
4. Do not create a Direction from "compiled skill" wording alone.
5. Deep-read Android AppFunctions as the strongest native Android product baseline.
6. Only then decide whether MCP-SandboxScan / SpecBox require FULL_10Q.
7. Reopen CPU/uArch consideration only with physical-phone evidence for material dynamic-executable lifecycle cost after native software baselines.

## Decision footer
- **Evidence maturity:** mobile/emulator structural signal; not target-phone SYSTEM_VALUE for executable lifecycle
- **Decision impact:** strengthen T6 product relevance; narrow differentiated CPU/uArch interpretation; no lane/score/maturity change
- **Open questions:** physical-phone frequency, native function/action baseline, executable-artifact creation/validation cost, sandbox transitions, energy/thermal/QoE, code residency/eviction
- **Primary source:** https://arxiv.org/abs/2604.14872
