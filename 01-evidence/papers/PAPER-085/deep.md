# PAPER-085 — Defeating Prompt Injections by Design (CaMeL)

## Source
- IEEE Conference on Secure and Trustworthy Machine Learning (SaTML) 2026
- arXiv:2503.18813 v2
- Artifact: https://github.com/google-research/camel-prompt-injection
- benchmark: AgentDojo
- Priority: P0

## Q1 — Problem + target mapping
Agent tool outputs are untrusted data, but a normal LLM context mixes them with trusted user instructions.
This lets untrusted data alter control flow or exfiltrate private values through later tool calls.

Target mapping:
> can Agent-specific trust/data-flow facts be represented and deterministically enforced in software, or is a new lower-level trust primitive required?

## Q2 — Novelty / new-regime relevance
CaMeL explicitly separates:
- **trusted control flow** from user intent;
- **untrusted data flow** from tools/environment.

It uses:
- a Privileged LLM to produce the trusted program;
- a Quarantined LLM to interpret untrusted values;
- a custom interpreter and dependency graph;
- **capabilities** attached to values;
- deterministic security policies at tool-call boundaries.

Classification:
**DIRECT_AGENTIC information-flow security mechanism**, software-level.

## Q3 — Falsifiable hypothesis
If the trusted plan is fixed before untrusted data is observed, and provenance/capabilities are tracked through execution, prompt injection cannot introduce unauthorized control flow or data exfiltration within the defined threat model.

Falsifiers:
- untrusted data legitimately needs to determine new control flow;
- the privileged planner encodes an unsafe plan;
- provenance is lost across APIs/agents;
- security policy lacks application semantics;
- interpreter or capability implementation is buggy;
- utility loss becomes unacceptable.

## Q4 — Research lineage / competing route
Competing routes:
- prompt delimiting/sandwiching;
- prompt-injection detectors;
- tool filtering;
- IsolateGPT app isolation;
- information-flow control and capability systems;
- later multi-CaMeL provenance-preserving agent-to-agent communication.

CaMeL's strategic significance is that **Agent semantic security becomes explicit structured program/data metadata**, not a hidden natural-language property.

## Q5 — Key mechanism / control point
### Trusted plan
P-LLM sees trusted user instruction and tool descriptions and emits a Python-like program.

### Untrusted-data quarantine
Q-LLM processes tool/environment data without authority to rewrite the trusted control-flow program.

### Dependency graph
Interpreter tracks which values depend on which sources/operations.

### Capabilities
Values carry metadata describing provenance/allowed readers or uses.

### Tool-call security policy
Before side-effecting tool calls, deterministic policy checks capabilities/dependencies and can block or require confirmation.

### Project interpretation
This is a strong counterexample to assuming CPU/OS must discover Agent trust semantics.
The Agent runtime can expose:
- data provenance;
- control-flow origin;
- tool authority;
- permitted recipients/uses.

## Q6 — Experiment design
AgentDojo covers Workspace, Banking, Travel and Slack-style tool tasks plus prompt-injection attacks.

Version note:
- original/v1 public summaries reported ~67% provably secure task completion;
- v2 with newer models reports about **77.3%** utility for o3-high vs **84.5%** native tool calling.

Security:
- CaMeL sharply reduces successful prompt injections;
- updated evaluations report zero successful attacks for some models/configurations under the defined threat model;
- security-policy layer additionally constrains unauthorized data flows.

Do not merge v1/v2 utility numbers; use 77.3/84.5 only for current v2 scope.

## Q7 — Data / artifact / reproducibility
Strengths:
- SaTML 2026;
- public code;
- AgentDojo benchmark;
- deterministic interpreter/policy rather than prompt-only defense;
- explicit security/utility tradeoff.

Limitations:
- artifact itself warns it is research code and may contain implementation bugs;
- control flow derived solely from trusted input cannot naturally solve all data-dependent tasks;
- security policies require application semantics;
- no mobile/phone system cost;
- side channels and broader system compromise are outside core guarantee.

## Q8 — Evidence vs hypothesis
### [FACT]
Agent control flow, data provenance and tool permissions can be represented as explicit runtime objects and checked deterministically.

### [FACT]
Strong security can be obtained with a measurable but non-zero utility cost on AgentDojo.

### [OBSERVATION]
Trust/data-flow semantics are software reconstructible at Agent execution boundaries.

### [INFERENCE — project]
A hardware trust-graph candidate needs evidence that software provenance/capability enforcement is too slow, too coarse or unavailable on realistic phone pipelines.

### Not established
- smartphone SYSTEM_VALUE;
- hardware insufficiency;
- cross-agent composability (addressed by later multi-CaMeL);
- secure accelerator integration.

## Q9 — Real contribution to project decision
### Security frontier
**Strong software-baseline pressure.**

Removes broad white space for:
- trusted vs untrusted Agent data classification;
- provenance/dependency tracking;
- capability-based authorization;
- deterministic tool-call security checks;
- separating planning/control from untrusted environment data.

### PT-A
Capability/effect authorization can strengthen verified actuation policy, but no lane change.

## Q10 — Next action
1. KEEP P0.
2. Use multi-CaMeL to test whether provenance/capability survives agent-to-agent boundaries.
3. Do not open a security Direction unless target-phone evidence shows this software layer is insufficient.

## Decision footer
- **New-regime relevance:** DIRECT_AGENTIC security
- **Evidence maturity:** Agent SYSTEM_VALUE / no mobile SYSTEM_VALUE
- **security-frontier impact:** strong software capture
- **hardware impact:** none
- **Primary source:** https://arxiv.org/abs/2503.18813