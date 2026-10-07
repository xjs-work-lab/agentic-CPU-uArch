# VENDOR-022 — Qualcomm Oryon CPU / Flex Cache — deep vendor card

## Q1 — What is officially disclosed?
Qualcomm states that its next-generation premium Oryon CPU introduces Flex Cache, a cache pool accessible by heterogeneous CPU cores and dynamically allocated according to workload demand.

The official page explicitly connects the design to multi-step Agentic AI.

## Q2 — Real technical mechanism
The mechanism is shared/dynamic CPU cache capacity across heterogeneous cores, intended to reduce working-set spill and cold handoff as work migrates between cores.

## Q3 — Workload/product problem
Qualcomm describes Agent tasks as multi-step work that plans, calls tools and moves between CPU cores.

The product thesis is that a shared pool lets handed-off work continue from resident data instead of restarting cold or reaching system memory.

## Q4 — Quantitative claims
The page makes product-performance positioning claims, but this card does not use vendor headline performance as independent evidence.

The decision-critical fact is the disclosed cache architecture and the explicit Agentic workload rationale.

## Q5 — Capability vs claim
PUBLIC PRODUCT SIGNAL:
- Flex Cache;
- heterogeneous cores can access the same dynamically allocated cache pool.

VENDOR INTERPRETATION:
- improves Agentic task handoff and working-set residency.

## Q6 — Independent corroboration
PAPER-008, PAPER-049 and AO-1 locality evidence support the general value of preserving locality.
They do not independently validate Qualcomm's Agent-specific benefit.

## Q7 — Prior-art boundary
Generic shared cache, task migration and cache-aware scheduling are heavily crowded, including PATENT-024.

The opportunity cannot be "shared cache for Agent" as a broad novelty claim.

## Q8 — AO-1 relevance
Strong PRODUCT_SIGNAL that a leading mobile vendor is changing CPU-subsystem organization and explaining the change with multi-step Agent workloads.

## Q9 — Decision impact
Strengthens AO-1 and AO-3 product relevance.
Does not establish hardware necessity for our own design.

## Q10 — Next
Compare Qualcomm's core-to-core working-set problem with the broader CPU↔NPU/GPU state-handoff problem.

## Footer
- Source confidence: high for disclosed product architecture; vendor-origin for value claims
- Decision impact: strengthen product signal, not independent SYSTEM_VALUE
- Primary source: https://www.qualcomm.com/news/onq/2026/08/oryon-cpu-5ghz-flexcache
