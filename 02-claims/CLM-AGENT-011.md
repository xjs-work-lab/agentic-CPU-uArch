+++
id = "CLM-AGENT-011"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "recurring explicit Agent memory lifecycle operations across independent long-horizon Agent systems"
supersedes = []
+++

# CLM-AGENT-011

## Proposition
Explicit memory lifecycle operations such as add, update, delete, retrieve, summarize/filter and replay/reuse recur across independent Agent-memory systems and can be adaptive decision variables rather than fixed background storage procedures.

## Evidence basis
- PAPER-074 / AgeMem: learned `ADD / UPDATE / DELETE / RETRIEVE / SUMMARY / FILTER` actions;
- PAPER-073 / MobiMem: profile update/retrieval, experience-template evolution, action replay/stale invalidation and exception-driven memory refinement.

## Current interpretation
The **operation-class recurrence gate is passed** for H-PAM.

However, the operation type is often already explicit at the Agent/runtime API boundary.
Therefore a lower layer cannot claim differentiation simply by identifying `retrieve` vs `update` vs `delete`.

## Boundary
This Claim does not establish:
- target-phone resource pressure for each operation;
- a recurring CPU/NPU/data-placement policy;
- that ordinary API/tool metadata is insufficient;
- a new system-control Direction;
- hardware/uArch need.