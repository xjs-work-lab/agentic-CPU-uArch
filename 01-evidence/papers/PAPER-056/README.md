+++
id = "PAPER-056"
type = "SOURCE"
source_type = "paper"
record_state = "ALIAS"
canonical_source_id = "PAPER-030"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "UNKNOWN"
title = "AgentProg: Empowering Long-Horizon GUI Agents with Program-Guided Context Management"
primary_url = "https://doi.org/10.1145/3745756.3809245"
priority = "P0"
evidence_role = "long-horizon mobile GUI Agent semantic execution-state/context-management evidence; strong software semantic-state baseline for A/R3"
authors = ["Shizuo Tian", "Hao Wen", "Yuxuan Chen", "Jiacheng Liu", "Shanhui Zhao", "Guohong Liu", "Ju Ren", "Yunxin Liu", "Yuanchun Li"]
venue = "ACM MobiSys 2026"
+++

# PAPER-056 — AgentProg

## 30-second read
- **Why it matters:** Directly studies long-horizon mobile GUI Agents, where control-flow, task-critical variables and hidden environment state become first-class execution state.
- **What it establishes:** Explicit program/control/data-flow structure plus a global belief state materially improves task completion and prevents history interference on AndroidWorld/AW-Extend.
- **Reported anchors:** 78.0% AndroidWorld; 68.4% AW-Extend; removing execution tree drops AW-Extend to 39.5%; removing explicit variables drops it to 50.0%.
- **Critical cost:** the evaluated AgentProg configuration is cloud-model/prompt-engineering heavy and substantially slower/more token-expensive than UI-TARS and Mobile-Agent-v3.
- **Portfolio meaning:** supports semantic-state information value, but simultaneously strengthens the application/runtime software baseline. It does not establish DemandState residual or CPU/uArch need.
- **Primary source:** https://doi.org/10.1145/3745756.3809245

## Decision-use gate
**FULL 10Q COMPLETE — decision-grade only within the evaluated functional scope.**

Use as:
- direct evidence that long-horizon mobile GUI Agents benefit from explicit control/data-flow, persistent variables and belief state;
- strong software/runtime baseline for any claim that Agent semantics must be pushed lower in the stack;
- workload evidence for long-horizon context correctness.

Do **not** use as:
- on-device LLM performance/energy evidence (the evaluated implementation uses cloud/API models);
- proof of DemandState / RequiredProgress incremental value;
- proof of CPU/uArch insufficiency;
- proof that semantic state should be exposed directly to hardware.

See [deep.md](deep.md) for the full Paper Insight 10Q.


## Canonical identity
PAPER-056 is a historical DOI-entry alias for canonical PAPER-030.
Both represent the same AgentProg work.
Active Evidence Cases and Experiments must reference PAPER-030.
