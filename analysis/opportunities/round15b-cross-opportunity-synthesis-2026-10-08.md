# Round 15B — AO1..AO5 Cross-Opportunity Bridge and Differentiation Audit

Date: 2026-10-08
Stage: **CROSS_AO_BRIDGE_MAPPED / PROVISIONAL SYNTHESIS**, not portfolio cutover.
Purpose: turn five opportunity problem spaces into a small **architecture theme map** with nonduplicated source evidence, strong software-pressure and current Gate-A versus future Gate-B boundaries.

## Source delta — ProgRouter first-hand FULL_10Q
- [PAPER-121 ProgRouter original](../../01-evidence/papers/PAPER-121/deep.md): arXiv 2608.25992v2, authors report Findings EMNLP 2026 acceptance; original paper sections 2–5, Appendix D (NVML energy) and Appendix E (ablations).
- ProgRouter ledger gives goals, subtask state, outputs; hierarchical progress scoring combines coarse validity regime, completion ratio, trend and semantic state-quality; meta-learned structured and coordinator-summary embedding predict marginal model gain; routing uses remaining-progress value and budget/virtual energy queue.
- GPU benchmark: HumanEval+ 93.0% pass/4796 J full vs 90.9%/4400 J structured-only; 87.2%/4784J semantic-only; no predictor 89%/4785J. On MBPP full 79.4%/3376J/10.3 s; on MATH-500 84.3%/6112J vs CASCADIA 87.8%/6875J, so no blanket claim of best pass rate.
- **Important negative result:** naïve progress-per-cost policy 17.7% pass/7797J on HumanEval+ vs full 93%/4796J — the value comes from predicting progress **and** maintaining cost/quality policy, not from a naked semantic label.
- **Energy boundary:** NVML board power 100 ms, GPU model load/prefill/decode/coordinator counted, CPU/host/RAM/storage/network omitted. No phone SoC/NPU/thermal/jank data.
- **Information boundary:** semantic embedding is computed from coordinator-maintained state description; not proven new non-reconstructible Agent DemandState. B4-TX now includes ledger progress, multi-view outcome and model-specific gain predictor. This tightens A/AO-5 but does not close matched-observability residual.
- Review depth: PAPER-121 **FULL_10Q**; earlier screen.md is superseded triage history, not contradictory source authority.

## Five AO roles — overlap without false equivalence

| AO | Owns (unique engineering question) | Shared interface / nearest AO | Strongest non-novel software baseline | Remaining mobile architecture gap |
|---|---|---|---|---|
| **AO-1** Execution Fabric | CPU↔GPU/NPU dispatch, queue/sync latency and mixed-criticality progression | AO2 cancellation; AO3 residency; AO5 priority info | Agent.xpu/MARS/software placement, fine-grained preemption, affinity and CPU orchestration | Whether cross-engine critical-path cost remains after best software, which hardware fabric primitive (if any) could reduce it |
| **AO-2** Revisable/Transactional | authority/commit/abort and *physical* speculative-work reclaim after semantic revision | AO1 queue retirement; AO3 state invalidation | Cordon/Atomix/TomasuLLM/Versioned Execution; patent CN120704926A generic transaction prior art | Whether phone local xPU work/state is left expensive to revoke below trusted runtime |
| **AO-3** Persistent State | KV/derived state version, validity, reuse, tier residency, rehydration | AO1 engine handoff; AO2 version epoch | MobiMem replay, PBKV/CacheScout/PLACEMEM/LOCAL and runtime invalidation | Do real mixed-model Agent flows force expensive repeated CPU↔NPU/GPU state rebuilds after software replay? |
| **AO-4** Proactive Front-End | trusted 24/7 event intake, intervention/no-action, wake threshold/foreground interference | AO5 opportunity value; AO1 escalation | CHRE/AOP + PRPF-class gating + shared-NPU DVFS/batching | Is dedicated Agent gating hardware incrementally efficient at real event/no-action rates and matched helpfulness? |
| **AO-5** Semantic Progress/QoE | value-of-information for Agent *genuinely private* goal/branch necessity beyond baseline | AO4 admission and AO1 execution policy, AO2 effect legality | B4-TX now includes LAS/SMetric/ProgRouter ledger progress and TUF/utility, runtime transaction legality | Does extra hidden RequiredProgress alter safe optimal control with all reconstructible state matched? |

## Three provisional architecture themes — NOT three investment bets

1. **Theme F — Execution–State Lifecycle** (AO1+AO2+AO3): execution/dispatch, cancel/invalidate and preserve/rebuild share timing/state resources; distinct semantics and correctness owners. Core graph bridge **CLM-XAO-001**, supported by **EC-XAO-001-A**, limited by **EC-XAO-001-B**.
2. **Theme P — Proactive Low-Power Admission** (AO4): always-on observation, calibrated no-action gating, consent/permission-constrained context escalation. It supplies workload to Theme F, but LP sensing/dual NPU/AP wakes are established product/prior art. **CLM-XAO-002**, **EC-XAO-002-A/B**.
3. **Theme V — Progress/QoE Policy and Information Contract** (AO5): task usefulness/legality and conditional progress-value, deciding **which** stages remain worth executing. Inputs may feed F/P but are primarily software-derived; **CLM-XAO-003**, **EC-XAO-003-A/B**, and **EC-AO5-006-D UNDERCUT**. Not an independent CPU-uArch block.

### Dependency, double-counting and contradiction audit
- **Shared source ≠ independent confirmation:** MediaTek VENDOR-019 informs AO1/AO4; Qualcomm VENDOR-001 CPU-only Flex Cache and VENDOR-023 NPU-local SRAM inform AO1/AO3; neither may count as multiple corroborating hardware wins. PAPER-121 informs AO5 and one cross-AO policy bridge, not an independent second Agent silicon result.
- **Semantic authority ≠ physical lifetime:** AO2 software effect/commit authority cannot itself tell the on-chip memory/engine whether arbitrary derived state is physically ready to reuse. Conversely AO3 validity/residency cannot authorize external state-changing actions.
- **Admission ≠ scheduling:** AO4 gates context observations before heavy Agent decisions; AO5 values work once a workflow exists. PRPF and ProgRouter cannot be summed or assumed colocated.
- **Software already implements much:** AO1 runtime binding/preemption, AO2 transactions and abort, AO3 replay/version-aware caching, AO4 pre-reasoning gating, AO5 ledger-derived progress and budget routing. Therefore novelty and hardware necessity cannot be declared merely because there are five AOs.
- **Source comparability:** server GPU/Joule, benchmark success, vendor product claims, CPU-only phone results and desktop/gpu local Agent KV studies are distinct evidence scopes; do not aggregate across them.

## Differentiation hypothesis test / cross-AO control points
| Control point | Current verdict | Candidate evidence that changes it |
|---|---|---|
| Generic Agent scheduler / semantic hint / dynamic utility curve | CROWDED, software baseline | Only non-reconstructible conditional-information benefit over complete B4-TX could reopen |
| Agent transaction/commit/rollback | CROWDED software + patent | Repeated local xPU speculative queue/state reclaim physically dominating UX/energy |
| Larger cache or special KV memory | CROWDED generic; product trend | Agent-specific mobile reuse/version/coherence handoff beyond best software+generic shared memory |
| Separate always-on efficient NPU | FOLLOW competitor productization (CG-07), not novelty | Comparable *post-gating* useful-events/day and joules/day including missed-need/foreground |
| Persistent execution/state/handoff descriptors, cheap cancel | OPEN architecture hypothesis, not silicon | Public instruction/API/SoC measurements demonstrating substantial mobile cross-xPU residual |

## Current decisions and no premature promotion
- No new Direction; no fabricated uArch/ISA/queue/cache hardware feature or second Primary Bet.
- Existing A Primary Bet / 82.5 / SIMULATION_SUPPORT, PT-A and C platform, CG-06 INVEST, CG-07 EXPLORE, CG-01 BENCHMARK, reserves B/R1/R2 and R3 blocked are **unchanged**.
- **Gate A (public foresight)**: three conceptual architecture themes survive bounded research. **Gate B (silicon)**: none proved.
- Current Round15B state: initial bridge + new source deep read complete; **portfolio/rank/roadmap 2027–2029 not reconverged**.

## Next smallest research round (Round15C)
1. Challenge Theme F with most relevant official CPU↔NPU queue/preemption/coherence and smartphone cross-engine measurements, and revisit patent independent claims only where a *new* proposed control point faces material prior art.
2. Challenge Themes P/V with product/system event rates, privacy/false-trigger metrics and **software-observable vs truly hidden** Need/Value; prioritize negative evidence over new concepts.
3. Construct explicit 2027–29 year/layer technology roadmap for 3 provisional themes and rank candidates against current A/PT-A/C/CG07/B/R1/R2 without filling investment quota.
4. Complete user-goal audit in `00-project/final-questions-status.md` before claiming final management recommendation.
