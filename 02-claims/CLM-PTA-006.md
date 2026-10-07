+++
id = "CLM-PTA-006"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "mobile actuation context integrity / observation-to-action TOCTOU"
supersedes = []
+++

# CLM-PTA-006

## Proposition
For GUI actuation, the environment that receives an action can differ from the environment the Agent observed during reasoning; post-action verification alone therefore does not guarantee that the action was delivered to the intended app/component context.

## Current interpretation
PAPER-101 demonstrates Action Rebinding on Android:
- model/reasoning latency creates an observation→action window;
- Android can change foreground application during that window;
- coordinate/input delivery is not bound to the originally observed process/component;
- recovery and semantic confirmation can be exploited rather than reliably closing the gap.

## Boundary
This is security/system evidence across the evaluated Android agents and attack scenarios, not proof that every future runtime is vulnerable.

The source establishes the **problem**, not a specific optimal solution.

A fresh-state/app-window-component binding contract is an analyst hypothesis to test in EXP-PTA-002.

No CPU/uArch requirement is established.
