# PAPER-084 — IsolateGPT: An Execution Isolation Architecture for LLM-Based Agentic Systems

## Source
- NDSS 2025
- DOI: https://doi.org/10.14722/ndss.2025.241131
- arXiv:2403.04960
- scope: third-party apps/tools in LLM-based Agent systems
- Priority: P0

## Q1 — Problem + target mapping
Tool-using Agents mix natural-language instructions, app descriptions, private user data and outputs from mutually untrusted third-party apps inside an execution workflow.

That creates two linked problems:
- one malicious app can influence another app or the system through natural-language messages;
- useful tasks still require legitimate app-to-app collaboration and data sharing.

Target mapping:
> can an Agent runtime represent and enforce a dynamic app/tool trust graph in software before claiming a hardware isolation/control gap?

## Q2 — Novelty / new-regime relevance
IsolateGPT adapts classic execution isolation to natural-language Agent ecosystems.

Architecture:
- **Hub** — trusted routing/planning/control point;
- **Spokes** — isolated app-specific execution environments with separate LLM/context/memory;
- **ISC protocol** — all cross-spoke collaboration mediated by the hub;
- **permission model** — user can allow once/session/always/deny cross-app sharing.

Classification:
**DIRECT_AGENTIC security/runtime evidence**.

## Q3 — Falsifiable hypothesis
If third-party apps are isolated and collaboration is restricted to well-defined hub-mediated channels with explicit permission, the system should reduce cross-app prompt-injection/data-exfiltration risk without destroying Agent functionality.

Falsifiers:
- isolation breaks legitimate multi-app workflows;
- routing/permission cost is too large;
- malicious natural-language data still crosses boundaries unchecked;
- one shared LLM/context is necessary for useful task performance;
- dynamic app installation/use cannot be managed through the hub.

Reported evaluation supports feasibility but not complete automatic security.

## Q4 — Research lineage / competing route
Lineage:
- process/container/VM isolation;
- browser site isolation / same-origin-style principles;
- OS permission systems;
- capability systems;
- prompt-injection defenses;
- later CaMeL control/data-flow separation.

Important baseline:
Agent-specific trust relationships can already be modeled as:
> app identity + isolated context + mediated communication + explicit permission.

## Q5 — Key mechanism / control point
### Hub
Hub receives user requests, plans which apps/resources are needed, maintains global context and mediates all collaboration.

### Spoke isolation
Each app has its own:
- operator;
- LLM/planner;
- persistent app-specific memory/context;
- isolated execution environment.

### Inter-Spoke Communication (ISC)
Spokes cannot communicate directly.
Hub exposes available functionality, requires structured request/response formats and validates/routs messages.

### Permissions
Cross-app data sharing can require user approval at different persistence levels.
Hub also surfaces whether a collaboration is expected by its trusted plan.

### Project interpretation
Dynamic tool/app composition is already representable in software.
A lower layer does not need to infer the trust graph from CPU behavior; the runtime already owns app identity, requested functionality and sharing policy.

## Q6 — Experiment design
Evaluation asks:
- security against malicious apps / prompt-injection-like cross-app behavior;
- functionality equivalence with an unisolated baseline;
- query-resolution overhead.

Reported high-level findings:
- many evaluated attacks are prevented or sharply reduced;
- task outcomes remain comparable in tested benchmark flows;
- for over roughly 75% of use cases, overhead is below 30%;
- overhead rises as more apps participate because planning/memory extraction/collaboration work grows.

## Q7 — Data / artifact / reproducibility
Strengths:
- NDSS 2025 peer review;
- explicit threat model;
- real multi-app Agent workflows;
- isolation and permission semantics are concrete;
- performance/security/functionality all evaluated.

Limitations:
- prototype isolation is software/process-centric rather than hardware-confidential;
- user involvement remains necessary for some ambiguous cross-spoke transfers;
- permission UX/policy automation is explicitly incomplete;
- not a mobile smartphone experiment;
- no CPU/NPU/energy/thermal evidence.

## Q8 — Evidence vs hypothesis
### [FACT]
Agent third-party app collaboration can be isolated and mediated in an Agent runtime while retaining tested functionality.

### [FACT]
App identity, collaboration request and cross-app data-sharing permission are explicit runtime facts.

### [OBSERVATION]
A dynamic app/tool trust graph does not inherently require a hardware-visible semantic ABI.

### [INFERENCE — project]
Any confidential-Agent Bet must beat a strong runtime that already knows exactly which app/tool is participating and what sharing is requested.

### Not established
- smartphone SYSTEM_VALUE;
- hardware-backed confidentiality;
- whether process/VM isolation cost becomes prohibitive on phones;
- secure NPU/device execution.

## Q9 — Real contribution to project decision
### Security frontier
**Strong software-baseline pressure.**

Kills broad novelty for:
- dynamic third-party app selection as a new low-level control variable;
- hub-mediated app collaboration;
- app/tool permission graph;
- isolated app contexts;
- ordinary app-to-app information-flow gating.

### PT-A
Permission/effect authorization can inform PT-A policy, but IsolateGPT does not create a new actuation lane.

### Hardware
No promotion.

## Q10 — Next action
1. KEEP as P0 baseline.
2. Compare with CaMeL/multi-CaMeL for finer data provenance/capability enforcement.
3. A hardware/security candidate must show value beyond explicit runtime trust/permission metadata.

## Decision footer
- **New-regime relevance:** DIRECT_AGENTIC
- **Evidence maturity:** SYSTEM_VALUE for evaluated Agent runtime security; not mobile SYSTEM_VALUE
- **security-frontier impact:** strong software capture
- **hardware impact:** none
- **Primary source:** https://doi.org/10.14722/ndss.2025.241131