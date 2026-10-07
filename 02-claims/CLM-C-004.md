+++
id = "CLM-C-004"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "Agent-aware incremental system-control signal"
supersedes = []
+++

# CLM-C-004

## Proposition
Agent-workload-visible scheduling state can add incremental value beyond a stronger generic execution layer on an end-user multi-Agent edge platform.

## Current interpretation
PAPER-051 separates:
- UMA-aware SME + zero-copy execution;
- HAL-based draft-budget scheduling, adding about 1.05–1.17× over the corresponding UMA-aware configuration;
- suspend-and-yield under synthetic tool stalls, contributing to the larger full-system gain in extreme stall settings.

## Boundary
Apple M4/M4 Pro-class CPU-GPU UMA evidence. Tool stalls are synthetically injected in the reported experiment; smartphone/NPU transfer and handset energy/thermal value remain unestablished. HAL and blocked state are software-visible proxies, not proof of irreducible Agent semantics.

## Migration
- V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- Transform: `STRUCTURAL_REPACK`

## Evidence-depth audit
EDP v1 revalidated 2026-10-07; gain decomposition clarified, decision unchanged.
