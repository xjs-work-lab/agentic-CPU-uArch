> Evidence Rescue Round 1 re-read under EDP v1 on 2026-10-07.
> V1 provenance remains the frozen baseline; this page is the current mechanism-level interpretation.

# PAPER-051 — EdgeAgent

## Q1 — Problem + target mapping
Concurrent end-user Agent LLM inference on shared-memory CPU-GPU systems combines:
- memory-bound decode contention;
- varying speculative-drafting difficulty;
- tool-induced stalls.

Project mapping:
- C system-control baseline;
- proof that Agent-visible runtime state can add value above a stronger generic execution layer.

## Q2 — Novelty / new-regime relevance
EdgeAgent combines two layers:

### Generic / architecture-aware execution
- SME CPU kernels;
- asymmetric CPU/GPU layout;
- zero-copy UMA tensor parallelism.

### Agent-workload scheduling
- HAL-based draft-budget allocation;
- suspend-and-yield on tool stalls.

Classification: **Agent-amplified systems workload**, not a new CPU-uArch primitive.

## Q3 — Falsifiable hypothesis
If multi-Agent heterogeneity and stalls matter, then:
1. stronger UMA-aware execution should beat ordinary Batch-SD;
2. allocation based on live drafting productivity should add value;
3. reclaiming stalled slots should reduce head-of-line blocking.

The paper reports support for all three on Apple M4/M4 Pro-class systems.

## Q4 — Competing route
Important comparators/boundaries:
- Batch-SD;
- generic speculative decoding with uniform draft budget;
- ordinary CPU/GPU co-execution;
- later Murakkab / Agent.xpu / HeRo-class orchestration as stronger cross-system baselines.

HAL is a runtime proxy from observed acceptance behavior, not an irreducible Agent semantic signal.

## Q5 — Mechanism / control point
Mechanism chain:

`task drafting difficulty → accepted-token history (HAL) → draft-slot allocation → bandwidth efficiency`

and

`tool call stall → scheduler-visible blocked state → suspend/yield → slot backfill → makespan`

Execution chain:

`UMA + matrix/vector phase structure → SME/GPU asymmetric layout + zero-copy TP → reduced data movement / higher utilization`

## Q6 — Experiment design + results
The paper evaluates Apple M4 and M4 Pro-class UMA systems.

A pre-experiment uses DeepSeek-R1-Distill-Llama-8B and contrasts deliberate reasoning with predictable structured generation.

Key reported decomposition:
- optimized SME kernels + zero-copy TP: up to **1.29×** over Batch-SD;
- HAL scheduling: additional **1.05–1.17×** over the corresponding UMA-aware configuration;
- offline packing under 5% of makespan in the cited ablation;
- synthetic tool stalls are injected log-uniformly in [1,10] s and [1,100] s ranges;
- extreme [1,100] s, N=4 cited case: Batch-SD 213.1 s vs EdgeAgent 120.6 s, **1.77×**.

The 1.77× result is not equivalent to the isolated HAL increment.

## Q7 — Data / artifact / reproducibility
Strengths:
- accepted ASPLOS 2027 metadata on the primary paper page;
- mechanism-level ablation;
- two Apple SoC classes;
- explicit mixed Agent workload behavior.

Limits:
- no commercial smartphone;
- no NPU;
- synthetic stall distributions;
- speculative-decoding benefit depends on draft/target behavior and acceptance dynamics;
- energy/thermal transfer to handset not established.

## Q8 — Evidence vs alternative explanations
### Demonstrated
Agent-workload-visible states can improve scheduling above a stronger generic execution layer.

### Alternative explanation / boundary
Much of the value is explainable through generic scheduler-visible state:
- accepted-token history;
- blocked/tool-stall status;
- fixed hardware slot capacity.

This is valuable C baseline evidence but weak evidence for non-reconstructible Agent semantics.

## Q9 — Project decision contribution
KEEP CLM-C-002 and CLM-C-004 with stronger wording discipline.

Do not combine:
- 1.29× generic execution gain;
- 1.05–1.17× HAL increment;
- 1.77× extreme-stall full-system gain

into one “Agent-aware speedup” number.

C remains Strategic Enabler. Direct-phone SYSTEM_VALUE now comes primarily from PAPER-098 HeRo, not from transfer of EdgeAgent.

## Q10 — Next action
- KEEP as P0 baseline.
- Use HAL/blocked state as reconstructible G2 signals.
- Require A/C experiments to beat these proxies.
- Do not derive phone energy/thermal or uArch conclusions from EdgeAgent.

## Decision footer
- Evidence maturity: **SYSTEM_VALUE on Apple end-user UMA; smartphone transfer not established**
- Decision impact: **clarify decomposition; no lane/score change**
- Open questions: real phone stalls, NPU coexistence, energy/thermal
- Primary source: https://arxiv.org/abs/2610.03394
