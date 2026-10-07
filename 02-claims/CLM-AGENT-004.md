+++
id = "CLM-AGENT-004"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "long-horizon mobile GUI Agent semantic execution state"
supersedes = []
+++

# CLM-AGENT-004

## Proposition
On evaluated long-horizon mobile GUI Agent benchmarks, explicitly representing program/control-flow state, persistent task variables and global belief state materially improves task-completion robustness compared with sliding-window, summarization and hierarchical-planning context baselines.

## Current interpretation
PAPER-030 / AgentProg provides direct benchmark and ablation evidence that:
- execution-tree-guided context pruning;
- explicit variable persistence;
- global belief-state tracking
are all materially useful to long-horizon mobile GUI Agent task completion.

This establishes **semantic execution-state information value** at the application/runtime layer.

## Boundary
It does not establish:
- DemandState / RequiredProgress incremental value;
- on-device model efficiency;
- phone energy/thermal/QoE value;
- CPU/uArch necessity.
