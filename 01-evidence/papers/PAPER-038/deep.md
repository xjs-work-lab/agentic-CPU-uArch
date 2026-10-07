# PAPER-038 — Beyond the GUI Paradigm — EDP v1 FULL_10Q

Re-reviewed: 2026-10-07

## Q1 — Problem + target mapping
The paper asks whether mobile Agents must interact through rendered UI, or whether text/CLI interfaces can directly expose phone services and state.

PT-A mapping: action-surface reachability and efficiency.

## Q2 — Novelty / new-regime relevance
It reframes mobile Agent interaction from “screen control” to “choose among OS/data/control surfaces.”

Classification: Agent-amplified systems/interface evidence.

## Q3 — Falsifiable hypothesis
If GUI is the universal substrate, CLI-only agents should be systematically weaker and oracle CLI coverage should be low.

The reported benchmark results reject that hypothesis for a large fraction of AndroidWorld/MobileWorld tasks.

## Q4 — Competing route
Compared with reproducible GUI agents:
- GUI-Owl-1.5-32B;
- MAI-UI-8B;
- Qwen3-VL-32B.

CLI harnesses:
- Claude Code;
- Terminus-2;
- mini-swe-agent;
with multiple model APIs and no mobile-specific post-training.

Independent group relative to ClawMobile / PhoneHarness / HybridCUA.

## Q5 — Mechanism / control point
CLI receives terminal stdout and emits shell/ADB operations instead of screenshots and coordinates.

The harness exposes:
- raw ADB shell;
- SQL/file tools;
- content providers / intents / system services;
- in MobileWorld, additional backend/service tools.

This gives CLI direct access to data/state operations the rendered UI may not expose efficiently.

## Q6 — Experiment design + results
Main:
- Claude Code + Opus 4.7: 71.8% AndroidWorld, 51.9% MobileWorld.
- Reproduced GUI baselines: AndroidWorld 69.3 / 68.1 / 57.8%; MobileWorld 43.2 / 26.3 / 13.3%.

Oracle CLI:
- AndroidWorld: 103/116 = 88.8% solvable;
- MobileWorld: 101/117 = 86.3% solvable.

Non-CLI-solvable tasks include visual-content interaction, drawing, camera/audio capture and some panel-only fields.

CLI-Advantage Suite:
- 45 templates across bulk operations, multi-condition filtering, aggregation/top-K, cross-app workflows and hidden device state;
- CLI agents 60.7–68.9% vs GUI agents 22.2–33.3%;
- mean steps 10.7 CLI vs 18.6 GUI;
- GUI agents <=11% on the cited cross-app slice.

## Q7 — Artifact / reproducibility
Strengths:
- multiple harness/model combinations;
- rule-based task verifiers;
- human-reviewed oracle solutions;
- explicit CLI-solvability ceiling.

Deployment boundary is substantial:
- all CLI agents use bash + ADB wrappers;
- MobileWorld uses a reproducible rooted AVD with direct backend observability;
- extra tools can include backend DB/container access.

These are valid benchmark/control surfaces but not equivalent to ordinary app-sandbox privileges on a retail handset.

## Q8 — Evidence vs alternative explanations
Demonstrated:
- GUI-only is not universally efficient/reachable under the benchmark action contract.
- Some operations are naturally structured/data-centric.

Not demonstrated:
- production mobile OS should expose raw ADB to an Agent;
- CLI is globally superior;
- benchmark privilege is deployable safely.

The result supports **capability heterogeneity**, not one preferred modality.

## Q9 — Decision contribution
CLM-PTA-001 survives but must be phrased as:
> action-surface capability changes reachable state, success and step count.

Do not translate the paper into “CLI should replace GUI.”

PT-A needs capability/authority-aware routing and must separate benchmark-accessible mechanisms from product-authorized mechanisms.

## Q10 — Next action
KEEP P0.
Use CLI as a structured-path baseline.
Add entitlement/authority to PT-A benchmark metadata.
Require retail-phone-equivalent capability constraints in product-facing tests.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for benchmarked action-surface heterogeneity
- Decision impact: KEEP/NARROW
- Open questions: retail privilege model, secure structured API surface, energy/latency under product constraints
- Primary source: https://arxiv.org/abs/2606.19388
