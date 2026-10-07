+++
id = "CLM-SEC-001"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "tool-using and multi-component Agent systems with third-party apps/models/providers"
supersedes = []
+++

# CLM-SEC-001

## Proposition
Agent systems create a real security/isolation workload in which third-party apps/tools, model providers, Agent runtimes and user data may belong to distinct or mutually distrustful trust domains while still needing controlled collaboration.

## Evidence basis
- PAPER-080 / AgenTEE — separate Agent runtime, inference engine and third-party application realms/stakeholders;
- PAPER-084 / IsolateGPT — isolated third-party app spokes with controlled cross-app collaboration;
- PAPER-085 / CaMeL — untrusted tool/environment data must be separated from trusted Agent control flow;
- PAPER-086 / multi-CaMeL — trust/provenance boundaries recur when Agents invoke other Agents as tools.

## Boundary
This establishes a **workload/security requirement**, not a differentiated CPU mechanism or target-phone SYSTEM_VALUE.