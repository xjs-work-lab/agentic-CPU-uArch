# PAPER-066 — Murakkab: Resource-Efficient Agentic Workflow Orchestration in Cloud Platforms

## Source
- USENIX OSDI 2026
- Paper: https://www.usenix.org/system/files/osdi26-chaudhry.pdf
- Venue page: https://www.usenix.org/conference/osdi26/presentation/chaudhry
- Authors: MIT CSAIL + Microsoft Azure Research / Microsoft Azure
- Workflows: Video Q/A, Code Generation, Math Q/A
- Resource scope: A100/H100-class cloud GPU serving, multi-tenant workflows
- Priority: P0

## Q1 — Problem + target mapping
Today's Agent frameworks typically expose model/tool calls to resource managers as opaque serving requests.

Murakkab argues this loses optimization opportunities because:
- workflow structure;
- workflow-level knobs;
- model choices;
- hardware choices;
- accuracy/latency/cost objectives

are optimized separately.

Murakkab instead treats the entire Agent workflow as an optimizable graph.

For H-FIB this is the strongest adjacent challenge to any claim that 'Agent awareness should inform resource allocation'.

## Q2 — Novelty / new-regime relevance
Murakkab introduces a declarative workflow specification that separates logical task/dependency structure from:
- model selection;
- tool selection;
- hardware allocation;
- parallelism;
- resource provisioning.

The system then jointly optimizes these under per-request SLOs.

Classification: **Agent-native/amplified cloud systems orchestration**.

The Agent-specific part is exposing workflow structure and configurable Agent/tool stages to the optimizer rather than treating them as independent LLM calls.

## Q3 — Falsifiable hypothesis
If the serving system sees the whole Agent workflow and profiles quality/latency/resource tradeoffs across its configuration space, then it can allocate models/hardware/resources more efficiently than siloed Agent framework + generic autoscaling.

Falsifiers:
- profiles do not generalize;
- workflow structure is too dynamic;
- optimization/reconfiguration overhead dominates;
- per-stage model/hardware choices do not materially alter end outcome;
- ordinary per-model autoscaling reaches the same Pareto frontier.

The evaluated cloud workloads support the hypothesis within the paper's scope.

## Q4 — Research lineage / competing route
Relevant routes include:
- LangGraph / LlamaIndex orchestration;
- generic model-serving autoscaling;
- Parrot semantic-variable serving;
- Autellix Agent-program serving;
- Teola end-to-end LLM application optimization;
- declarative AI workload/query optimization;
- workflow/model-selection systems.

Murakkab's differentiator is the unified workflow→model/tool→hardware→resource optimization problem under SLOs.

## Q5 — Key mechanism / control point
### Declarative logical workflow
Tasks and dependencies are represented as a DAG without binding to a specific model/hardware configuration.

### Workflow profiles
Profiles capture response quality, end-to-end latency and resource demand under workflow/executor knobs.

### Model profiles
Profiles include throughput, TTFT/TPOT, energy and cost across model/hardware/parallelism configurations.

### MILP optimizer
At each optimization epoch it jointly chooses:
- workflow configuration;
- model/tool per executor;
- hardware/parallelism profile;
- instance count;
- routing/multiplexing.

Constraints include:
- quality/latency SLO feasibility;
- demand satisfaction;
- capacity;
- resource budgets/cost ceilings.

Objectives include minimizing energy/cost or maximizing accuracy under cost budget.

### Adaptive runtime
Optimization runs periodically while autoscaling handles shorter-timescale load variance.

## Q6 — Experiment design
Representative Agent workflows:
- Video Q/A;
- Code Generation/debate;
- Math Q/A.

Evaluation uses production-scale/request traces and multiple quality/latency tiers.

Reported headline:
- up to 2.8× lower GPU use;
- up to 3.7× lower energy;
- up to 4.3× lower cost.

One 24-hour multi-workflow comparison reports:
- LangGraph: 2568 GPUs / 82.1 MWh / $211.7k;
- LangGraph+Auto: 2472 / 80.6 MWh / $112.3k;
- Murakkab Opt: 1164 / 27.7 MWh / $57.2k;
- Murakkab Opt+Mult: 912 / 22.1 MWh / $47.2k.

The system also shows resource/energy tradeoffs as accuracy or latency SLOs are relaxed and adapts allocations under changing H100 availability/load.

## Q7 — Data / artifact / reproducibility
Strengths:
- OSDI peer review;
- detailed optimizer formulation and profiles;
- multiple workflows/model/hardware choices;
- production-scale traces;
- explicit sensitivity/generalization analysis.

Limitations:
- no smartphone evaluation;
- cloud GPU energy/cost economics differ materially from mobile SoCs;
- workflow profile quality depends on representative benchmark/profile data;
- reoptimization operates at relatively coarse epochs (60 minutes in the reported setup);
- this review did not identify a public standalone Murakkab artifact repository.

## Q8 — Evidence vs hypothesis
### [FACT]
Murakkab exposes Agent workflow structure and SLOs to an optimizer that jointly selects workflow, model/tool and hardware/resource configurations.

### [FACT]
The evaluated cloud workflows report large reductions in GPU use, energy and cost while meeting configured SLOs.

### [OBSERVATION]
Agent-aware resource orchestration does not require a new hardware semantic interface when the workflow, profiles and SLOs are visible in software.

### [INFERENCE — project]
Any H-FIB claim based only on 'Agent-specific resource allocation' or 'quality/latency/energy budget' is crowded.

### Not established
- smartphone foreground/background interference;
- pause/resume/cancel tolerance as an SLO;
- in-task marginal RequiredProgress value;
- mobile CPU/NPU/DRAM/thermal control;
- hardware/uArch necessity.

## Q9 — Real contribution to project decision
### H-FIB
**NARROW HARD.**

Kill the broad formulation:
> Agent workflows need a resource manager that sees workflow structure/SLOs and jointly maps models to hardware/resources.

Murakkab already demonstrates that architecture strongly.

A surviving H-FIB variable must add information beyond:
- workflow graph;
- quality SLO;
- latency SLO;
- cost/resource budget;
- profiled stage resource demand.

### C
Strong generic/Agent-aware software baseline. No lane/score promotion.

### A
Contextual pressure only: ordinary SLO/workflow structure must not be miscredited as RequiredProgress.

## Q10 — Next action
1. KEEP as P0 strongest comparator.
2. Add canonical Agent-aware orchestration Claim.
3. Add Murakkab-class orchestration to C/H-FIB strongest baseline.
4. Do not create a second Bet from generic Agent-aware SLO orchestration.
5. Compare H-FIB only on in-task marginal-value/tolerance information that Murakkab's request/workflow SLO does not encode.

## Decision footer
- **New-regime relevance:** Agent-native/amplified
- **Evidence maturity:** SYSTEM_VALUE in cloud Agent workflow scope
- **Decision impact:** broad H-FIB Agent-aware orchestration novelty killed/narrowed
- **C impact:** baseline strengthened, lane unchanged
- **Open questions:** phone transfer, in-task dynamic utility, foreground interference, pause/cancel tolerance
- **Primary source:** https://www.usenix.org/conference/osdi26/presentation/chaudhry