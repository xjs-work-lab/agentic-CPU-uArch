+++
id = "CLM-AGENT-008"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "evaluated cloud Agent workflow orchestration with per-request SLOs"
supersedes = []
+++

# CLM-AGENT-008

## Proposition
Exposing Agent workflow structure plus quality/latency/cost SLOs and profile-derived resource demand enables software to jointly optimize workflow configuration, model/tool selection, hardware mapping, provisioning and routing more efficiently than siloed orchestration in evaluated cloud Agent systems.

## Evidence
PAPER-066 / Murakkab (OSDI 2026).

## Boundary
Cloud GPU/multi-tenant scope only.
This Claim does not establish:
- smartphone foreground/background SYSTEM_VALUE;
- Agent-internal RequiredProgress;
- pause/cancel/restart tolerance as a distinct information variable;
- CPU/NPU/DRAM/thermal mobile control;
- hardware/uArch need.