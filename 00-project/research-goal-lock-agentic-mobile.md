# Research Goal Lock — Agentic / AGX Mobile CPU-uArch

Updated: 2026-10-08
State: CURRENT

## Research environment

This project operates under a **strict public-source-only, no-experiment constraint**:
- no new device tests, lab benchmarks, code execution/reproduction experiments, simulations, or PoC validation conducted by this research;
- no owned target-phone test platform and no privileged competitor/internal test data;
- findings use publicly accessible **primary** papers (deep-read Methods/Results/Limitations), published experimental findings **reported by their authors**, patents with direct claim review where material, standards, official vendor white papers, product technical documentation, public artifacts and independent public analyses;
- public third-party measurements may be analysed **as reported evidence**, with experiment setup and transportability bounds explicit; their replication or new local measurement is **not** assumed;
- if a claim would need new test data, give a bounded, transparent public-evidence judgment (**SUPPORTED / INFERENCE / HYPOTHESIS / NOT_PUBLICLY_ESTABLISHED**), not a promise to test it.

This is an **operating rule through the final 2027–2029 leadership report**, not a temporary resource shortage.

## Original decision goal

Answer:

> In the Agentic / AGX era, how will mobile user experience and workload structure change, and what does that imply for compiler, runtime, OS scheduling, CPU/GPU/NPU cooperation, SoC organization and CPU microarchitecture over 2027–2029?

The output is not a proof that a silicon feature will succeed.

The output is:
1. important trends the team should follow;
2. academic mechanisms that may move into products;
3. unresolved structural problems;
4. technically plausible cross-layer opportunities;
5. potential hardware/uArch support worth architectural study;
6. areas that are already crowded or mostly software-sufficient;
7. a prioritized research/product technology roadmap.

## User / experience change hypothesis

Agentic mobile computing differs from classic app/GenAI execution through combinations of:
- proactive rather than purely reactive assistance;
- persistent personal context;
- repeated model re-entry and long-lived state;
- tool/action loops rather than one-shot inference;
- revisions, interruptions and changing goals;
- speculative work and cancellation;
- continuous low-duty-cycle observation/gating;
- cross-app and cross-device action;
- several specialized models/agents instead of one monolithic model;
- stricter requirements on privacy, responsiveness, trust, battery and foreground QoE.

Research must ask which of these create **new operating regimes**, not simply rename generic optimization.

## Controllable layers

The project may recommend co-design across:
- Agent framework / planner;
- compiler / graph lowering / Agent IR;
- runtime;
- OS scheduler / memory / security;
- CPU / GPU / NPU orchestration;
- memory hierarchy / interconnect;
- CPU subsystem and microarchitecture;
- low-power always-on domains.

## Two different gates

### Gate A — Architecture Opportunity Discovery
Used by this project now.

A candidate may be kept when:
1. Agentic-era workload or UX creates a structural change;
2. public evidence shows a real or credible mechanism/tension;
3. existing software/product baselines do not obviously close the whole problem;
4. a cross-layer lever is technically plausible;
5. the opportunity has product relevance or strategic learning value.

Output states:
- FOLLOW / PRODUCT SIGNAL;
- CO-DESIGN OPPORTUNITY;
- ARCHITECTURE HYPOTHESIS;
- RESEARCH RESERVE;
- CLOSED / CROWDED.

**No new experiment is permitted within this research workflow.** A decision-ready Gate-A foresight recommendation may use convergent public materials and clearly labelled inference without calling for any local verification.

### Gate B — Product/Silicon Commitment
**Out of scope for this public-source-only project.** Preserve this as an explanatory boundary for eventual product/silicon commitment, not as a required next step or future task assigned to this research.

STRUCTURAL_SIGNAL → SYSTEM_VALUE → SOFTWARE_INSUFFICIENCY → hardware-specific cause → UARCH_CANDIDATE.

**Gate B is not performed here.** Its unresolved conditions cannot be used to declare that an evidence-supported Gate-A architecture hypothesis has no research value.

## Evidence interpretation

Prior art constrains novelty, not product relevance.

Lack of public phone measurements means:
**unvalidated transfer**, not **no opportunity**.

A server-system paper can support a mobile architecture hypothesis when:
- the workload mechanism is plausibly transferable;
- the platform differences are explicit;
- mobile power/thermal/QoE constraints are analyzed as an open boundary.

A vendor architecture can support a product-trend signal even when its performance claims are marketing claims.

## Required final deliverable

A leadership-grade 2027–2029 map containing:
- 3–5 structural Agentic mobile changes;
- 3–5 cross-layer architecture themes;
- academic-leading mechanisms to follow;
- competitor/product signals;
- open problems / white space;
- software vs hardware design levers;
- probable 3-year evolution;
- confidence and evidence boundaries;
- explicit public-evidence sufficiency/uncertainty and **external/publicly verifiable evidence still required** where relevant, but no proposed execution of experiments as part of this project.

## Anti-drift rule

If an attractive conclusion seems to depend on doing an experiment, **do not schedule, propose to execute or rely on that experiment**. Instead ask:
> What can primary public papers, patent claims, vendor technical documents, published third-party evaluations and comparative mechanism analysis establish, and what remains unknowable?

Answer the public-evidence strategic question to the strongest supported extent and state the ceiling of confidence. Do not turn future Gate-B verification into a blocking prerequisite for the final report.

## Evidence conclusion labels
- **PUBLICLY_DEMONSTRATED:** published experiment/standard/official source directly establishes a bounded fact; cite exact sections, experiment tables or claims.
- **CROSS_SOURCE_INFERENCE:** technically defensible comparative inference; state competing software explanations.
- **ARCHITECTURE_HYPOTHESIS:** plausible differentiated cross-layer opportunity, not publicly verified necessity.
- **NOT_PUBLICLY_ESTABLISHED:** insufficient or non-transferable evidence; do not invent a metric, causal claim or competitor architecture.

The final recommendation can still rank FOLLOW / PRIMARY_BET / RESERVE / KILL using these labels and its uncertainty profile. No local tests are required to complete it.
