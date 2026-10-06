# PAPER-061 — Syrup: User-Defined Scheduling Across the Stack

## Source
- ACM SOSP 2021
- DOI: https://doi.org/10.1145/3477132.3483548
- Open paper: https://web.stanford.edu/~kkaffes/papers/syrup.pdf
- Authors: Stanford MAST Lab
- Main workloads: RocksDB + MICA
- Backends: Linux/eBPF software, programmable NIC/eBPF hardware, ghOSt userspace thread scheduling
- Priority: P0

## Q1 — Problem + target mapping

### Paper problem
Scheduling happens independently at multiple layers—application/runtime, kernel thread scheduler, network stack and NIC—and each layer often lacks application/request semantics and coordination with other layers.

Syrup asks:
> Can an application specify its scheduling intent once and safely deploy coordinated policies across multiple low-level scheduling mechanisms without rebuilding a custom OS/runtime?

### Project mapping
This is strong conceptual prior art for H-SCL/C because it already separates:
- high-level application policy/intent;
- a portable matching abstraction;
- low-level executors/hooks;
- shared cross-layer state.

The target is datacenter/server networking, not smartphone Agents.

## Q2 — Novelty / new-regime relevance

Syrup's novelty is not application-aware scheduling itself.
The core contribution is a general **policy portability and deployment substrate**:
- applications express policies as matching functions between inputs and executors;
- framework compiles/deploys them to eBPF software, programmable NIC or ghOSt;
- Map abstraction communicates information across layers;
- multiple tenants can safely use different policies.

Classification: **generic cross-layer control substrate**, not Agent-native.

## Q3 — Falsifiable hypothesis

Core hypothesis:
> If application-specific scheduling intent can be expressed in a portable matching abstraction and deployed safely at the right system hooks, coordinated cross-layer policies can achieve a significant fraction of custom-system performance without per-application kernel/hardware rewrites.

Falsifiers:
- abstraction cannot express useful policies;
- cross-layer communication overhead dominates;
- safe deployment prevents required control;
- policies are not portable across hooks;
- multi-layer policy provides no benefit over best single layer.

The evaluated KVS/networking experiments support the hypothesis in that scope.

## Q4 — Research lineage / competing route

Direct lineage:
- ghOSt (SOSP 2021) provides userspace CPU scheduling delegation and is a Syrup backend;
- prior application-specific dataplanes such as IX, Shinjuku and Shenango motivate the performance value of bespoke scheduling;
- eBPF/P4 provide safe programmable hooks;
- informed request/NIC scheduling work motivates moving application knowledge closer to low-level queues.

Competing route:
- build specialized per-workload runtime/OS/network dataplane;
- hard-code policies in each subsystem;
- use a generic fixed scheduler;
- user-space policy delegation without a shared cross-layer abstraction.

## Q5 — Key mechanism / control point

### Matching abstraction
Scheduling is represented as:
> input/work item → executor/resource

Examples:
- threads → cores;
- packets/connections → sockets;
- packets → NIC queues.

### Cross-layer deployment
The same high-level policy style can be compiled/deployed to:
- kernel/network eBPF hooks;
- programmable NIC;
- ghOSt userspace thread scheduler.

### Map abstraction
Application code and policy components at different layers can exchange state such as:
- load;
- latency;
- expected completion time;
- request/thread type.

### Isolation
Policies are scoped to application-owned inputs and run through safe backends.

### Project interpretation
Syrup already occupies the broad idea:
> portable application-specific cross-resource policy + low-level deployment + shared control state.

H-SCL cannot claim novelty for that architecture alone.

## Q6 — Experiment design

Hardware:
- Intel Xeon server sets;
- Intel 82599ES or programmable Netronome 10GbE NIC;
- Linux 5.9 generally; Linux 4.19 for ghOSt-compatible cross-layer experiment.

Applications:
- RocksDB with heterogeneous GET/SCAN service times;
- MICA KVS for policy portability across software/NIC hooks.

Questions evaluated:
1. expressiveness of multiple policies;
2. cross-layer coordination;
3. portability across hooks;
4. policy/Map overhead.

Reported examples:
- policy variants can improve performance up to **8×** vs default policy in evaluated workloads;
- cross-layer thread + request scheduling achieves target tail latency up to **8000 RPS**, ~**60% higher load** than best single-layer scheduling in that experiment;
- same MICA steering policy is deployed in software and NIC hooks.

## Q7 — Data / artifact / reproducibility

Strengths:
- SOSP peer review;
- detailed design and code snippets;
- explicit workloads/hardware;
- multiple independent experimental questions;
- quantifies execution and Map overhead.

Overhead anchors:
- evaluated policy code: <2,000 CPU cycles per scheduling decision;
- host Map get/update: ~1 µs;
- NIC-offloaded Map operations: ~25 µs in the evaluated platform.

Limitations:
- no smartphone/mobile evaluation;
- ghOSt cross-layer experiment consumes a core for the spinning scheduling agent;
- hardware/backend constraints affect portability/performance;
- this review did not identify a maintained standalone Syrup artifact repository.

## Q8 — Evidence vs hypothesis

### [FACT — evaluated server scope]
Syrup demonstrates application-defined policies spanning thread and network scheduling with measurable gains over default/single-layer alternatives.

### [FACT — portability]
The paper deploys the same policy style to different software/hardware hooks and communicates state via Map.

### [OBSERVATION]
Application-specific information can be conveyed through a compact generic policy interface rather than exposing full application state to every subsystem.

### [INFERENCE — project]
Portable cross-layer scheduling/control is mature prior art at the architectural-pattern level.

### Not established
- Agent-specific semantic facts;
- automatic semantic extraction/lowering from Agent frameworks;
- mobile QoE/energy/thermal value;
- CPU/NPU/DRAM smartphone control;
- hardware/uArch need.

## Q9 — Real contribution to project decision

### H-SCL
**NARROW HARD / broad cross-resource abstraction killed.**

Do not claim novelty for:
- declarative workload-specific scheduling policy;
- mapping work items to resources;
- portable deployment across multiple stack layers;
- shared cross-layer state for scheduling.

Syrup already demonstrates all four.

The surviving H-SCL question becomes:
> Can a system **automatically derive** a small, recurring set of genuinely Agent-specific facts from heterogeneous Agent runtimes, and can those facts deliver smartphone SYSTEM_VALUE across CPU/NPU/memory/thermal beyond strong generic application-defined frameworks such as Syrup and mobile semantic schedulers such as MUSched?

### C
**G1 prior-art baseline strengthened; no promotion.**

C cannot claim generic cross-layer policy coordination as differentiated.
Its second-Bet case requires Agent-specific semantics + target-phone residual beyond a generic user-defined cross-layer control framework.

### A
No direct decision change because Syrup does not study Agent semantics or mobile execution; it remains conceptual baseline pressure only.

### R3
Remain BLOCKED. Syrup demonstrates flexible value on existing hardware/software mechanisms.

## Q10 — Next action

1. KEEP PAPER-061 as P0 prior art.
2. Create canonical Claim for portable cross-layer application-defined scheduling.
3. Add to C G1 / H-SCL strongest baseline.
4. Do not create a new Direction.
5. Continue H-SCL search specifically for **automatic semantic extraction** and **mobile Agent cross-resource value**, because policy deployment/portability itself is already crowded.
6. ghOSt does not need a separate full review unless CPU-policy delegation becomes a distinct unresolved mechanism; Syrup already uses it as a backend for the relevant cross-layer question.

## Decision footer
- **New-regime relevance:** generic cross-layer scheduling prior art
- **Evidence maturity:** SYSTEM_VALUE in evaluated server/KVS scope; STRUCTURAL_SIGNAL for smartphone transfer
- **Decision impact:** kills broad H-SCL cross-resource-interface novelty; strengthens C G1
- **C impact:** no lane/score change
- **A impact:** conceptual baseline only
- **R3 impact:** remain BLOCKED
- **Open questions:** automatic Agent semantic lowering, mobile cross-resource mapping, Agent-specific residual, phone overhead/energy
- **Primary source:** https://doi.org/10.1145/3477132.3483548
