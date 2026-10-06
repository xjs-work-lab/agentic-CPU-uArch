+++
id = "CLM-C-007"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "automatic runtime criticality inference and asymmetric CPU placement in evaluated managed-language systems"
supersedes = []
+++

# CLM-C-007

## Proposition
Rich runtime state such as synchronization, thread progress, priorities and core sensitivity can be analyzed automatically to infer bottleneck/critical work and drive heterogeneous big/small CPU placement without programmer hints or new hardware in evaluated managed-runtime systems.

## Evidence
PAPER-062 / WASH.

## Boundary
Server/managed-runtime AMP scope only.
No smartphone Agent SYSTEM_VALUE, CPU↔NPU placement or hardware/uArch need is established.
