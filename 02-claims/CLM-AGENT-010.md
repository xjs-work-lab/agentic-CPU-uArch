+++
id = "CLM-AGENT-010"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "specialized memory lifecycle semantics and execution services in evaluated mobile GUI-Agent system"
supersedes = []
+++

# CLM-AGENT-010

## Proposition
In an evaluated mobile GUI-Agent system, different persistent memory classes and lifecycle states directly affect execution behavior, including profile retrieval, task-template instantiation, action replay/validation, fine-grained dependency scheduling and interruption/error recovery.

## Evidence
PAPER-073 / MobiMem.

## Interpretation
MobiMem shows that Agent memory semantics are operational, not merely archival:
- Experience Memory exposes step dependencies;
- Action Memory exposes replayability/staleness;
- exception context affects suspension/recovery and later template evolution.

## Boundary
Most demonstrated value is captured by application/runtime/OS software mechanisms.
This Claim does **not** establish:
- a distinct CPU/NPU/data-placement residual;
- lower-layer visibility insufficiency;
- phone memory-bandwidth/thermal value;
- hardware/uArch necessity.