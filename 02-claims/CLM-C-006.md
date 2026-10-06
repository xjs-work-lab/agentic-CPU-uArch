+++
id = "CLM-C-006"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "portable application-defined cross-layer scheduling in evaluated server systems"
supersedes = []
+++

# CLM-C-006

## Proposition
Application-specific scheduling policies can be expressed through a compact portable matching abstraction, deployed across multiple system layers, and coordinated through shared control state to outperform generic or single-layer scheduling in evaluated systems.

## Evidence
PAPER-061 / Syrup demonstrates this across:
- thread→core scheduling via ghOSt;
- packet/request→socket scheduling via eBPF;
- software/NIC hooks;
- cross-layer Map state.

## Boundary
This is server/KVS evidence.
It does not establish smartphone or Agent-specific value, automatic semantic extraction, or CPU/uArch necessity.
