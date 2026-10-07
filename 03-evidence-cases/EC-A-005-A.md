+++
id = "EC-A-005-A"
type = "EVIDENCE_CASE"
record_state = "CURRENT"
relation = "SUPPORT"
target_kind = "CLAIM"
target_id = "CLM-AGENT-004"
warrant = "AgentProg benchmark and component-ablation results show that explicit control-flow context, persistent variables and belief state materially affect long-horizon mobile GUI Agent task success."
scope = "AndroidWorld and AW-Extend under the PAPER-030 evaluated AgentProg setup"
boundary = "Functional Agent/context evidence only; cloud/API-backed implementation and no CPU/uArch conclusion."
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-030"
locator = "AndroidWorld/AW-Extend results; Global Belief State, Execution Tree and Explicit Variables ablations"
+++

# EC-A-005-A

## Inference
`PAPER-030` → **SUPPORT** → `CLM-AGENT-004`

## Warrant
AgentProg's benchmark and ablation evidence independently exposes the contribution of control-flow pruning, persistent variables and belief state to long-horizon mobile GUI Agent success.

## Boundary
The evidence establishes semantic-state information value in the evaluated Agent software stack, not target-phone resource value or hardware necessity.
