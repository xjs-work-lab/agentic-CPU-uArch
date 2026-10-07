# VENDOR-023 — Qualcomm Hexagon NPU Agentic Architecture — deep vendor card

## Q1 — What is officially disclosed?
Qualcomm describes its next-generation Hexagon NPU as designed for Agentic AI and discloses:
- transformer-focused Element Accelerator;
- scalar, vector and matrix execution capability;
- a 50% larger shared-memory subsystem;
- support across INT2 through FP16;
- MoE-oriented model execution and flash-to-memory expert management concepts.

## Q2 — Real technical mechanism
The relevant AO-1 mechanisms are:
- keep more model state, activations and intermediate tensors close to the NPU;
- combine specialized and programmable execution forms;
- reduce external-memory trips;
- coordinate with CPU orchestration as tasks move across the system.

## Q3 — Workload/product problem
The official framing is persistent, multimodal, low-latency Agentic execution with:
- long context;
- multiple tools;
- concurrent tasks;
- routing/orchestration.

## Q4 — Quantitative claims
Qualcomm reports:
- 50% larger NPU shared memory;
- up to 50% higher INT4 prefill performance;
plus other product claims.

These are vendor-reported and not independent measurements.

## Q5 — Capability vs claim
PUBLIC PRODUCT SIGNAL:
- specialized transformer acceleration;
- larger on-NPU shared memory;
- mixed scalar/vector/matrix path;
- explicit CPU-NPU complementary role.

VENDOR CLAIM:
- the stated performance improvements and Agent experience benefits.

## Q6 — Independent corroboration
Agent.xpu and mobile CPU/NPU crossover literature independently support the importance of:
- local memory;
- operator/backend affinity;
- orchestration;
- data movement.

They do not validate Qualcomm's exact percentages.

## Q7 — Prior-art boundary
Specialized tensor acceleration and larger local memory are not globally novel.
The AO-1 opportunity is system-level execution/state handoff and control, not merely a bigger NPU SRAM.

## Q8 — AO-1 relevance
Strong PRODUCT_SIGNAL that product architecture is moving beyond "one NPU runs one model" toward an execution fabric with specialized models, local state and CPU orchestration.

## Q9 — Decision impact
Strengthens AO-1 product relevance and AO-3 state-fabric relevance.
Does not prove that a new cross-xPU hardware interface is required.

## Q10 — Next
Track how CPU, NPU memory and system interconnect expose state/priority/continuation information in future public architecture documentation.

## Footer
- Source confidence: high for disclosed product direction; value claims vendor-origin
- Decision impact: strengthen product signal, not independent SYSTEM_VALUE
- Primary source: https://www.qualcomm.com/news/onq/2026/09/hexagon-npu-agentic-ai-architecture
