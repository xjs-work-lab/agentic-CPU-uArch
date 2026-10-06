+++
id = "CLM-AGENT-005"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "evaluated on-device mobile GUI-Agent task-level program lowering"
supersedes = []
+++

# CLM-AGENT-005

## Proposition
On evaluated mobile GUI-Agent workloads, stable app/task semantics can be compiled into a task-level executable script plus reusable static app knowledge/prefix state, materially reducing repeated on-device model inference and token cost while preserving or improving task success relative to a step-wise Agent baseline.

## Current interpretation
PAPER-058 / AutoDroid-V2 provides direct smartphone evidence that a large part of step-wise Agent reasoning overhead can be moved into:
- offline app documentation / dependency structure;
- one task-level generated program;
- deterministic local interpretation;
- reusable static prompt / KV-prefix state;
- exception-triggered replanning rather than mandatory per-step replanning.

This establishes a strong **upper-layer semantic-lowering baseline**.

## Boundary
It does not establish:
- that all mobile GUI tasks admit stable scripting;
- cross-framework portable resource-control semantics;
- Agent-specific OS/runtime residual;
- CPU/NPU placement value;
- CPU/uArch necessity.

Highly dynamic or insufficiently documented UI states can force regeneration and reduce the efficiency advantage.
