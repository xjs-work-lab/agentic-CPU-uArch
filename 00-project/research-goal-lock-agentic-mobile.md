# Research Goal Lock — Agentic / AGX Mobile CPU-uArch

Updated: 2026-10-08
State: CURRENT

## Research environment

This project assumes:
- no owned target-phone experimental platform;
- no privileged internal competitor data;
- no ability to validate claims through new silicon or device experiments;
- conclusions must be built from public papers, patents, vendor/official material, artifacts, benchmarks and cross-source technical inference.

This is intentional.

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

No owned experiment is required.

### Gate B — Product/Silicon Commitment
Used only if experimental capability later exists.

STRUCTURAL_SIGNAL → SYSTEM_VALUE → SOFTWARE_INSUFFICIENCY → hardware-specific cause → UARCH_CANDIDATE.

Gate B must not be used to kill Gate-A exploration.

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
- future validation questions, not fabricated experiments.

## Anti-drift rule

If the research next step becomes impossible without owned hardware, stop and ask:
> Can this uncertainty instead be bounded through public evidence, mechanism comparison, simulation results from literature, patents or industry architecture signals?

Only unresolved commitment-level questions should remain experiment-gated.
