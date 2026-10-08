> **HISTORICAL / INOPERATIVE — HARD USER CONSTRAINT 2026-10-08:** This entire experiment/instrumentation program is *not* part of the study, regardless of capability or future availability. **DO NOT execute, schedule or treat EXP tasks as prerequisite to the 2027–29 strategic conclusion.** The active plan is [Round15E public-only roadmap](round15e-integrated-public-roadmap-2027-2029.md). Other headings below preserve historical rationale only.

> **Status correction — 2026-10-08**
>
> This document is retained as a **future validation reference only**.
> The project currently has no owned target-phone experimental environment and therefore should not treat this plan as the immediate next phase.
> Current next phase: public-evidence Architecture Opportunity Discovery / Round 15.
>
> The experiment definitions remain useful as future falsifiers if measurement capability becomes available.

# 2027 Execution Plan — Target-Phone Discriminating Program

Updated: 2026-10-07  
State: DEFERRED_FUTURE_VALIDATION_REFERENCE  
Parent roadmap: final-2027-2029.md

## Objective

Under an experiment-capable program, 2027 would be a measurement year. Under the current project premise, this plan is not executable now.

The objective is to convert the remaining high-value uncertainties into measured target-phone decisions while reusing one instrumentation stack across multiple Directions.

Primary outputs:
1. decide whether A survives as a differentiated Primary Bet;
2. map the real CPU/NPU/HETERO fast-path region for CG-06;
3. productize PT-A/C software-platform foundations;
4. promote or close CG-07 / CG-01;
5. kill or retain B-residual / R1 / R2;
6. keep R3 blocked unless a parent path proves software insufficiency plus a hardware-specific cause.

## Shared phone instrumentation — build once

The common harness should collect, where platform access permits:

### Workflow / semantic state
- workload / Agent role / task identity;
- workflow DAG / current node / dependency state;
- RequiredProgress / DemandState labels for A experiments;
- revision / cancellation / commit / verification state;
- DependencyReady and actual release/resume timestamps;
- action target/context epoch and OutcomeReceipt;
- cross-device/tool/backend identity where relevant.

### CPU / accelerator execution
- CPU cluster/core and affinity;
- GPU/NPU stage assignment;
- operator/sub-operator shape;
- precision / quantization path;
- dispatch / synchronization / fallback;
- state/cache reuse;
- context switches / migrations;
- CPU burst duration.

### Locality / PMU
Where exposed:
- L1I/L1D/L2/LLC miss proxies;
- TLB miss proxies;
- branch mispredict / frontend-stall proxies;
- memory bandwidth;
- reuse distance / suspension duration;
- warm-core/cache-domain identity.

### Product outcomes
- end-to-end task success;
- RequiredProgress completed;
- TTFT / per-step / end-to-end latency;
- foreground jank / QoE;
- energy and battery impact;
- thermal state / throttling;
- controller/metadata overhead.

One trace schema should feed A, C, CG-06, CG-01, B-residual, R1 and R2.

PT-A adds actuation/context-integrity events.
CG-07 adds always-on observation/gating/wake telemetry.

## Wave 0 — Baseline + instrumentation freeze

Deliver before interpreting residuals:
- representative smartphone Agent workload suite;
- strong software baselines enabled, not default-only baselines;
- common trace schema;
- repeatability/noise controls;
- matched-outcome comparison method;
- workload/session/time-aware train/test split where learning is involved;
- power/thermal/foreground-QoE accounting.

Do not promote any Direction from kernel-only microbenchmarks.

## Wave 1 — Highest information gain

### 1A — EXP-A-001
Question:
does explicit Agent-internal DemandState / RequiredProgress add >=~5% meaningful outcome value over B4-TX at matched QoE with zero illegal cancellation?

Priority reason:
A is the sole differentiated Primary Bet; it deserves an early falsifier.

Decision:
- PASS → A reaches target-phone SYSTEM_VALUE and may feed an A→C integration test;
- FAIL → downgrade/kill A as differentiated research.

### 1B — EXP-CG06-001
Question:
where does CPU-MATRIX / CPU-VECTOR / HETERO-OPT beat a strong NPU-OPT path on the full Agent critical path?

Priority reason:
CG-06 is the highest-priority competitive INVEST lane and can use the same stage/operator/power trace infrastructure.

Decision:
- persistent meaningful region → productize CPU/HETERO fast path with existing ISA/compiler/runtime;
- no durable region → narrow CG-06 investment to fallback/coverage/tooling rather than CPU-resident performance strategy.

### 1C — EXP-C-001
Question:
after G2 Agent-aware heterogeneous orchestration, is there still >=~5% reusable Agent-specific system-control residual?

Decision:
- residual from ordinary blocked/ready/concurrency state → C-specific research survives;
- only DemandState adds value → classify as A→C transfer;
- no residual → keep C as platform enabler without differentiated research claim.

## Wave 2 — Platform correctness and shared locality measurements

### 2A — EXP-PTA-001 / EXP-PTA-002
Build and measure the verified actuation contract.

EXP-PTA-002 should run early enough to prevent unsafe platform assumptions:
- B0 post-action verification;
- B1 fresh-context re-check;
- B2 target-bound contract;
- B3 strongest software Agent.

If B1/B3 closes misbinding at acceptable cost, keep the solution software/OS-level.

### 2B — EXP-CG01-001 + EXP-R2-001
Run these on the same locality traces.

Common comparison:
- default scheduler;
- strong role/soft-affinity/warm-core baseline;
- generic coherent/shared-cache behavior;
- oracle headroom.

CG-01 asks a competitor/adaptation question.
R2 asks whether an Agent-specific CPU-local residual remains.

Do not let a positive CG-01 benchmark automatically promote R2.

## Wave 3 — State/timing reserves using the same traces

### 3A — EXP-BR-001
Measure:
- revision frequency;
- derived-state rebuild cost;
- generic safe-preservation capture;
- explicit lineage capture;
- retention survival;
- stale-reuse correctness.

Gate:
B6-cross-tier lineage must add >=~5% matched-outcome value over B4-safe-generic with stale reuse = 0.

### 3B — EXP-R1-001
Measure:
- post-ready opportunity share;
- generic release capture;
- semantic timing incremental value;
- timing-window scale;
- late-release violations;
- energy/QoE conversion.

Gate:
>=~5% incremental value beyond B4-release with acceptable hard-bound violations.

These reserve experiments should reuse the common workflow/revision/readiness instrumentation rather than create separate benchmark stacks.

## Wave 4 — Always-on economics

### EXP-CG07-001
Use real proactive/persistent smartphone traces.

Measure:
- observations/hour;
- post-gating acceptance rate;
- gate energy/latency;
- shared/CPU-front-end baseline;
- dedicated idle/active power where measurable;
- handoff/wake cost;
- batching/residency;
- battery/thermal/foreground QoE.

Decision:
promote only if a dedicated front end beats the strongest software-sparsified shared/CPU baseline.

Do not use vendor power claims or synthetic model parameters as measured inputs.

## R3 — remains blocked

Do not execute a D2/uArch PoC in 2027.

EXP-R3-001 may only activate if a parent path has already demonstrated:
1. target-phone SYSTEM_VALUE;
2. software insufficiency;
3. a causal hardware-timescale/state limitation.

Only then define a compact D2 mechanism and measure incremental value.

## Shared decision thresholds

Use approximately >=5% meaningful incremental end-outcome value as the default residual threshold where the existing experiment contract defines it.

A result does not count if:
- only a weak/default baseline loses;
- the gain disappears under strongest software/platform baseline;
- correctness/safety regresses;
- foreground QoE is traded away without accounting;
- energy/thermal cost erases the gain;
- the effect is kernel-only and negligible on end outcome.

## Portfolio review checkpoints

### Checkpoint A — after Wave 1
Decide:
- A keep/downgrade/kill;
- CG-06 product fast-path scope;
- C differentiated residual vs platform-only state.

### Checkpoint B — after Waves 2–3
Decide:
- PT-A contract level;
- CG-01 benchmark/adaptation;
- B-residual / R1 / R2 keep or close.

### Checkpoint C — after Wave 4
Decide:
- CG-07 remain EXPLORE, promote to architecture co-design, or close dedicated-domain residual.

### Hardware review
Only after all relevant checkpoints:
decide whether any path has crossed the formal hardware gate.

## Data reuse matrix

| Shared data | A | C | CG-06 | PT-A | CG-01 | B-residual | R1 | R2 | CG-07 |
|---|---|---|---|---|---|---|---|---|---|
| workflow/DAG/state | yes | yes | yes | yes | partial | yes | yes | yes | yes |
| CPU/NPU/GPU stage trace | partial | yes | yes | partial | yes | partial | partial | yes | partial |
| PMU/locality | no | partial | yes | no | yes | no | no | yes | no |
| revision/validity | yes | partial | partial | yes | partial | yes | partial | partial | partial |
| ready/release timing | yes | yes | partial | partial | partial | partial | yes | partial | partial |
| power/thermal/QoE | yes | yes | yes | yes | yes | yes | yes | yes | yes |

## Completion criterion

The 2027 program is complete when every active Direction is in one of four states:
- measured product/platform commitment;
- measured differentiated survivor;
- explicitly retained reserve with quantified residual;
- closed/killed with a recorded falsifier.

No Direction should remain alive solely because measurement was deferred.
