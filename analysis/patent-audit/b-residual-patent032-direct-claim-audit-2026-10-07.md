# Patent Direct-Claim Audit — B-residual / PATENT-032

Date: 2026-10-07
State: COMPLETE

## Question
Does PATENT-032 actually support CLM-BR-004:
semantic/version-aware Agent result/reasoning-cache validity and version-sensitive invalidation are already claimed?

## Current public claim text
Claim 1 directly recites:
- semantic retrieval from historical-result and reasoning-process caches;
- multi-factor validity arbitration including identity, time window and service-version consistency;
- valid-cache demand-satisfaction grading;
- fresh LLM reasoning with historical-logic reuse/correction when necessary;
- memory/cache update with current business version.

## Decision
CLM-BR-004 remains SUPPORTED.

The supported novelty boundary is application/runtime memory:
semantic + version-aware Agent cache validity.

The patent does not directly establish:
- smartphone physical-artifact lineage;
- S0/S1 revision → S2/S3 invalidation/preservation;
- NPU/DRAM/UFS coherence;
- hardware/uArch mechanisms.

## Portfolio impact
B-residual remains:
- CONDITIONAL_RESERVE
- 63.0
- SIMULATION_SUPPORT
- no uArch promotion

## Patent audit progress
4 / 13 complete.
9 remain:
- R1: 4
- R2: 5
