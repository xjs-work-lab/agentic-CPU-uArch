+++
id = "CLM-MOBILE-002"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "semantic-aware CPU scheduling on evaluated commercial Android mobile systems"
supersedes = []
+++

# CLM-MOBILE-002

## Proposition
On evaluated commercial Android mobile systems, interaction-critical semantics and cross-process dependency information can be reduced to compact scheduler-visible control state and used by a software CPU scheduling framework to improve user-facing responsiveness with low scheduler-path overhead.

## Evidence
PAPER-060 / MUSched provides peer-reviewed phone evaluation using:
- scenario-aware annotation;
- bounded VIP scheduling class;
- lock/Binder dependency priority propagation;
- user-space/eBPF policy adaptation.

## Boundary
The production-scale deployment results are source-reported by a vendor-affiliated team.
This Claim does not establish:
- Agent-specific semantic residual;
- cross-resource CPU/NPU/memory value;
- Huawei equivalence;
- software insufficiency;
- hardware/uArch need.
