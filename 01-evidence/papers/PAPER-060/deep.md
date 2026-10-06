# PAPER-060 — Surviving the Impossible Trinity: Revisiting CPU Scheduling Problem on Modern COTS Mobile Devices (MUSched)

## Source
- USENIX OSDI 2026 Operational Systems Paper
- Paper page: https://www.usenix.org/conference/osdi26/presentation/xiao
- PDF: https://www.usenix.org/system/files/osdi26-xiao.pdf
- Authors: Honor Device Co., Ltd. + Nanjing University + Southeast University
- Laboratory phone: Honor Magic 7, Snapdragon 8 Elite, MagicOS 9 / Android 15, Linux 6.6
- Production claim: >20 million Honor devices since January 2024 across multiple tiers and MediaTek/Qualcomm platforms
- Priority: P0

## Q1 — Problem + target mapping

### Paper problem
Android CPU scheduling has a semantic gap:
- scheduler sees threads/timeslices;
- user experience depends on interaction-critical execution paths;
- critical paths cross processes through Binder IPC and locks;
- prime/high-performance cores are scarce;
- 120 Hz interactions impose ~8.3 ms frame deadlines.

Native CFS/EAS/nice/cgroup heuristics cannot reliably infer which short-lived threads belong to the current user interaction.

### Project mapping
This is directly relevant to A, C and H-SCL because it demonstrates the exact general pattern we are testing:
> high-level user/application context → compact low-level control fact → OS scheduler action.

However the semantic source is generic mobile interaction context, not Agent-specific DemandState/RequiredProgress.

## Q2 — Novelty / new-regime relevance

MUSched is not novel because 'application-aware scheduling' is new. Its novelty is the deployable mobile combination of:
- scenario-aware annotation;
- a bounded VIP class between RT and CFS;
- lock/Binder priority propagation across processes;
- eBPF/sched_ext-style user-space policy updates on COTS phones.

Classification: **generic mobile-system semantic control**, not Agent-native.

This is crucial prior-art pressure: the broad concept of lowering semantic context into scheduler-visible priority/control is already demonstrated at commercial scale.

## Q3 — Falsifiable hypothesis

Core hypothesis:
> If the system identifies the true interaction critical path and propagates urgency through cross-process dependencies, bounded priority elevation can improve mobile QoE more reliably than semantics-blind generic scheduling without unacceptable stability/energy overhead.

Falsifiers:
- critical-thread annotation is inaccurate or too app-specific;
- priority propagation simply moves contention elsewhere;
- overhead erases latency gain;
- thermal/energy cost dominates;
- gains disappear in production;
- generic mobile workloads are already sufficiently optimized.

The paper supports the hypothesis for launch/animation/swipe-type interaction scenarios, while its gaming result exposes a clear negative regime.

## Q4 — Research lineage / competing route

MUSched explicitly sits on mature prior art:
- ghOSt (SOSP 2021): flexible user-space delegation of Linux CPU scheduling;
- Syrup (SOSP 2021): user-defined scheduling across stack components;
- SmartOS (APSys 2021): mobile task importance / user-adaptive resource allocation;
- Orthrus (IEEE TMC 2024): mobile process scheduling + CPU frequency-governor co-optimization;
- TIHMM / Rethinking Process Management for Interactive Mobile Systems (MobiCom 2024): richer Android process-state modeling;
- CFS/EAS/nice/cgroups: strong generic Android baseline.

Therefore H-SCL cannot claim broad novelty around application semantics, user-space policy or semantic priority propagation.

## Q5 — Key mechanism / control point

### Scenario-aware annotation
MUSched combines:
1. generalized Android thread roles (UI, Render, Binder etc.);
2. offline systrace profiling to recover application-specific critical-path threads;
3. beta-user jank traces to fill rare/missed cases.

Framework hooks tag the relevant threads when a user-interactive scenario begins.

### VIP scheduling class
- sits between RT and CFS;
- RT runs first, then VIP, then CFS;
- local per-core VIP queue;
- 3 ms slice;
- bounded scenario-specific VIP time budgets to prevent starvation.

### Dependency propagation
When a VIP thread waits on locks/futex/rwsem or Binder-related dependencies, urgency can be propagated to the holder/servicer so the dependency chain is accelerated, rather than only the blocked foreground thread.

### User-space policy plug-and-play
eBPF/sched_ext-style control keeps low-level enforcement close to the kernel while allowing user-space scenario policies to be updated without kernel recompilation/reboot.

### Project interpretation
MUSched already demonstrates a reusable pattern:
> semantic classification + dependency relation → compact scheduler-visible tag/class → generic CPU resource action.

That pattern is very close to H-SCL's broad idea.

## Q6 — Experiment design

### Laboratory
- Honor Magic 7 / Snapdragon 8 Elite;
- Android 15 / Linux 6.6;
- 10 representative apps (short video, social, shopping, video, navigation, news);
- native Android scheduling baseline;
- 100 cold-start runs per app;
- controlled display mode, thermal state, battery mode, governor and cache clearing;
- realistic background activities plus synthetic stress-ng/rt-app pressure.

Headline laboratory result:
- average cold-start time: **14.8% reduction**;
- cold-start standard deviation: **24.25% reduction**;
- mixed foreground/background cases: reported response-latency reductions of **9.8%–22.8%**.

### Fast-path overhead
- context switch: 5 µs → 5 µs;
- pick-next-task: 2 µs → 3 µs;
- 120 FPS gaming average FPS essentially unchanged;
- normalized current 726.62 mA baseline vs 718.16 mA in the reported overhead test.

### Production
Source-reported deployment:
- >20M Honor devices;
- multiple product tiers;
- MediaTek + Qualcomm;
- startup / web browsing / touch-sliding scenarios.

Reported anomaly-frequency reductions:
- startup >2s: **30.7%**;
- animation drop >50ms: **25.0%**;
- swipe drop >50ms: **35.7%**.

## Q7 — Data / artifact / reproducibility

Strengths:
- peer-reviewed OSDI operational-systems paper;
- detailed implementation/evaluation;
- COTS flagship phone;
- 100 repeats/app in lab;
- large source-reported production deployment;
- mixed chipset/product tiers in deployment.

Limitations:
- no public MUSched source/artifact was identified in this review;
- production data are reported by a vendor-affiliated author team and are not independently audited in our source set;
- scenario annotation relies partly on offline profiling / predefined thread roles / field traces;
- the exact production policy stack is not fully reproducible from the paper alone.

Evidence confidence is therefore high for the laboratory design/result and peer-reviewed mechanism, but production generalization remains **vendor-reported operational evidence**.

## Q8 — Evidence vs hypothesis

### [FACT — paper evaluation]
On the evaluated Magic 7 setup, MUSched reports lower cold-start latency with small scheduler fast-path overhead.

### [SOURCE CLAIM — production]
The Honor-affiliated paper reports deployment on >20M devices since 2024 and lower anomaly rates across startup/animation/swipe scenarios.

### [OBSERVATION]
Mobile scheduler value can depend on semantic critical-path information that generic thread history/utilization does not represent well.

### [OBSERVATION]
A small low-level semantic contract (VIP tag/class + dependency propagation) can be enough to convey useful context without exposing rich application state to the kernel.

### [INFERENCE — project]
This substantially crowds H-SCL's broad semantic-control-lowering novelty and strengthens the generic baseline A/C must beat.

### Not established
- Agent-specific semantics;
- DemandState / RequiredProgress residual;
- persistent-Agent resource control;
- NPU/GPU/DRAM semantic control;
- Huawei internal/product equivalence;
- hardware/uArch insufficiency.

## Q9 — Real contribution to project decision

### H-SCL
**NARROW HARD.**

Kill the broad claim:
> 'A portable layer that lowers high-level semantic context into low-level CPU scheduling/resource control is a new opportunity.'

MUSched already demonstrates a highly relevant mobile version of that idea.

Surviving H-SCL must be explicitly Agent-specific and cross-resource:
> Is there a compact Agent control fact that is *not* already captured by generic interaction-criticality/dependency semantics, and that adds value across CPU/NPU/memory/thermal or persistent-Agent control beyond MUSched-like policies?

### A
**Baseline strengthening, no score change.**

B4-TX must include strong generic semantic-aware scheduling that knows:
- user-interaction scenario;
- critical path/thread roles;
- IPC/lock dependency propagation;
- bounded urgency/class.

DemandState/RequiredProgress only counts if it adds residual value beyond this.

### C
**Problem relevance + baseline strengthening, no promotion.**

MUSched is direct evidence that semantic-aware mobile system control can be commercially valuable.
But it also demonstrates that such value is already accessible through a generic interaction-aware software control plane.

C's second-Bet case must therefore prove an **Agent-specific residual beyond MUSched + Sereno + other G1 controls**.

### R3 / uArch
Remain BLOCKED.

The mechanism obtains material value through software/framework/kernel scheduling on existing hardware.

## Q10 — Next action

1. KEEP PAPER-060 as P0.
2. Create a canonical Claim for deployed semantic-aware mobile scheduling.
3. Add MUSched to A B4-TX and C G1.
4. Further narrow H-SCL to **Agent-specific cross-resource residual**, not generic semantic scheduling.
5. Snowball MUSched's closest prior art: ghOSt, Syrup, SmartOS, Orthrus, TIHMM.
6. Preserve the negative game result as evidence that semantic scheduling is workload-dependent and may worsen energy/thermal.
7. Do not create a new Direction or uArch candidate.

## Decision footer
- **New-regime relevance:** generic mobile semantic control, not Agent-native
- **Evidence maturity:** SYSTEM_VALUE on evaluated phone interaction workloads; production deployment is source-reported operational evidence
- **Decision impact:** strong A/C generic baseline; H-SCL broad novelty narrowed
- **A impact:** stronger B4-TX, no lane/score change
- **C impact:** stronger problem signal + stronger G1, no lane/score change
- **R3 impact:** remain BLOCKED
- **Open questions:** Agent-specific residual, cross-resource generality, independent production corroboration, Huawei transfer, persistent-Agent interaction
- **Primary source:** https://www.usenix.org/conference/osdi26/presentation/xiao
