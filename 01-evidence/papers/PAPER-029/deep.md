# PAPER-029 — An Efficient Context Management System for On-Device LLMaaS

## Source
- Peer-reviewed: SenSys 2026
- DOI: https://doi.org/10.1145/3774906.3800479
- Authors: Wangsong Yin, Mengwei Xu, Yuanchun Li, Xuanzhe Liu
- Review: FULL_10Q / EDP v1
- Priority: P1

## Q1 — Problem + target mapping
If an on-device LLM becomes an OS service, many apps may keep persistent contexts whose KV caches cannot all remain in RAM.

B-residual question: does Agent semantic lineage provide material additional physical-state validity/preservation value beyond a strong mobile context manager?

## Q2 — Novelty / relevance
Libra is not Agent-semantic. It is a direct mobile systems baseline for persistent context/KV lifecycle under tight RAM and storage constraints.

## Q3 — Falsifiable hypothesis
Fine-grained chunk management, adaptive compression and overlapped swap/recompute should reduce context-switch cost under constrained memory.

## Q4 — Strongest baselines
Conventional low-memory-killer/app memory management; vanilla disk swapping; vLLM-style chunking + swapping; statically quantized chunk management.

## Q5 — Mechanism / control point
Libra splits KV into flexible token chunks and applies tolerance-aware per-chunk compression, LCTRU-style lifecycle/eviction, ahead-of-time swapping and multithreaded swap/recompute overlap.

The physical control variables are runtime-visible context recency, chunk importance, memory budget and I/O/computation overlap.

## Q6 — Experiment design
COTS devices include Jetson Orin NX, Jetson TX2 and an MI14 smartphone with 8 GB RAM, UFS 4.0, 8-core X4/A720/A520 CPU, Adreno GPU and Hexagon NPU.

Models include Llama2-7B and OPT-6.7B. The paper evaluates synthesized 72-hour context-switch traces.

Reported:
- up to 20× and 9.7× average switching-latency reduction versus strong chunk-based baselines;
- gains persist across devices/models/access patterns;
- under tight switching-latency constraints, substantially more active contexts can be supported.

## Q7 — Artifact / limitations
Strengths: peer reviewed, real COTS phone, real mobile storage/memory constraints, multiple devices and baselines.

Limitations:
- LLMaaS context switching, not Agent semantic revision;
- no S0/S1 semantic lineage experiment;
- no CPU-cache/TLB/predictor claim;
- no proof that physical artifact validity requires cross-tier metadata.

## Q8 — Evidence vs hypothesis
FACT: persistent KV/context lifecycle is a real mobile-system problem.
FACT: generic runtime/memory/storage mechanisms capture large context-switch value on a COTS phone.
INFERENCE: B4-safe-generic must include sophisticated context lifecycle management.
NOT ESTABLISHED: Agent semantic state adds physical-artifact preservation beyond this baseline.

## Q9 — Project decision
Negative pressure on B-residual promotion. It raises the strongest generic mobile baseline and narrows the surviving cross-tier residual.

B-residual remains CONDITIONAL_RESERVE / 63.0 / SIMULATION_SUPPORT.

## Q10 — Next
EXP-BR-001 must compare semantic lineage against a baseline that already includes Libra-class context lifecycle plus version/hash/provenance correctness.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for generic mobile context lifecycle
- Decision impact: strengthen B4-safe-generic; no B-residual promotion
- Primary source: https://doi.org/10.1145/3774906.3800479
