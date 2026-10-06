+++
id = "CLM-AGENT-007"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "workflow-aware Agent KV-cache management in evaluated server systems"
supersedes = []
+++

# CLM-AGENT-007

## Proposition
Agent workflow topology and predicted future activation distance can provide a software-visible state-reuse signal that guides cache retention, eviction and prefetch more effectively than generic recency in evaluated multi-Agent serving systems.

## Evidence
PAPER-065 / KVFlow uses an Agent Step Graph and steps-to-execution (STE) to drive KV-cache priority and prefetch.

## Current interpretation
Generic 'state-reuse identity' is not automatically hidden from software: workflow topology can reconstruct a strong future-use proxy.

## Boundary
This is server-GPU KV-cache evidence.
It does not establish:
- smartphone transfer;
- CPU cache/uArch state identity;
- CPU/NPU/DRAM cross-resource benefit;
- equivalence to DemandState/RequiredProgress;
- hardware insufficiency.