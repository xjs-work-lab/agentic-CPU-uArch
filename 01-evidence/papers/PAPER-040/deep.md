# PAPER-040 — PhoneHarness — EDP v1 FULL_10Q

Re-reviewed: 2026-10-07

## Q1 — Problem + target mapping
Phone tasks may require GUI navigation, deterministic local commands or external tools. Pure GUI benchmarks hide this heterogeneity and often grade final app state without an auditable mixed-action trace.

PT-A mapping: heterogeneous actuation substrate + outcome evidence.

## Q2 — Novelty / new-regime relevance
PhoneHarness separates:
- outer orchestration;
- deterministic CLI/device actions;
- bounded GUI delegation;
- host-side MCP-style tools;
- trace-backed benchmark verification.

It is a harness + benchmark, not only an Agent model.

## Q3 — Falsifiable hypothesis
A mixed-action harness with deterministic-first routing and verifiable side effects should outperform GUI-only / less-structured phone-agent settings especially on tasks with deterministic or tool-assisted routes.

Reported task breakdown supports this pattern.

## Q4 — Competing route
Comparators:
- AutoGLM-Phone;
- Seed2.0-Pro;
- MobileClaw.

Independent Tencent-led line relative to ClawMobile, Beyond-GUI and HybridCUA.

## Q5 — Mechanism / control point
Host-device architecture:
- device-side server/loop/tool registry;
- model proxy;
- GUI proxy using ADB interactions;
- MCP proxy for host tools.

Routing principle:
structured/CLI path when reliable, bounded GUI subtask otherwise.

Trace records outer tool calls plus nested GUI traces; task-specific verifiers inspect observable side effects.

## Q6 — Evaluation + results
Benchmark:
- 14 mock-app tasks;
- 45 real-app tasks;
- 30 exploratory safety tasks;
- scored 124-task split from a 181-task candidate pool, 30 app scenarios.

Main table:
- PhoneHarness 75.0%;
- Seed2.0-Pro 62.1%;
- MobileClaw 62.1%;
- AutoGLM-Phone 37.1%.

PhoneHarness by task:
- device/system 96.7%;
- single-app GUI 63.3% (Seed2.0-Pro 76.7%);
- tool-assisted 74.3%;
- cross-app 65.5% (tie Seed2.0-Pro).

Affordance slices:
- GUI-or-CLI alternative: 97.0%;
- GUI-primary + optional CLI: 67.6%.

Mean steps:
- PhoneHarness 23;
- Seed2 24;
- MobileClaw 28;
- AutoGLM 37.

Auxiliary runtime split:
- PhoneHarness 155 s/task, 131 s/success;
- GUI-only 202/146 s;
- MobileClaw 172/146 s.

Same-harness model combinations show large controller-model sensitivity, so the headline difference is not attributable to routing alone.

## Q7 — Artifact / deployment boundary
Public artifact reference setup:
- Pixel 6 / API 33 Android emulator;
- Termux/Termux:API/ADBKeyboard;
- remote OpenAI-compatible model endpoint;
- host GUI/MCP proxies.

The paper explicitly notes some capabilities are not purely on-device.

Therefore this is strong evaluation-platform evidence, but weaker evidence for a deployable retail-phone privilege model.

## Q8 — Evidence vs alternative explanations
Demonstrated:
- mixed action spaces can materially improve verifiable task pass rate in the harness;
- gains concentrate where structured/tool routes exist.

Not isolated:
- exact contribution of routing vs model choice vs extra capabilities vs verifier design;
- runtime verification/recovery as a causal component.

Many verifiers are benchmark-side/task-side evidence checks.

## Q9 — Decision contribution
Supports PT-A platform importance and benchmark design.

Narrows CLM-PTA-002:
PhoneHarness should not be cited as isolated causal proof that runtime verification alone improves reliability.

It is stronger evidence for:
> common action contract + traceable side effects + task-level OutcomeReceipt.

## Q10 — Next action
KEEP P0.
Use its 124-task mixed-action design as a PT-A benchmark seed.
Require product-capability/authority labels and adversarial context-switch cases.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for mixed-action evaluation/runtime
- Decision impact: KEEP/NARROW causal attribution
- Open questions: real retail phone, local inference, authority model, verifier completeness
- Primary source: https://arxiv.org/abs/2606.14832
