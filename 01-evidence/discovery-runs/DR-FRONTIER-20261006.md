+++
id = "DR-FRONTIER-20261006"
type = "DISCOVERY_RUN"
lifecycle = "OPEN"
as_of = "2026-10-06"
coverage_quality = "AUTHORITY_SEED_FULL_10Q"
scope = "2024-2026 frontier re-open for second differentiated Bet search across smartphone Agent workloads, runtime/OS control, heterogeneous execution, compiler and CPU/uArch"
limitations = "Rounds 1-6 have completed decision-level 10Q review for their selected Sources. H-PAM passes lifecycle-operation recurrence but remains unpromoted because lower-level mobile CPU/NPU/memory-system residual evidence is still missing."
+++

# DR-FRONTIER-20261006

## Question
Does the current V2.2 portfolio miss a structural 2027–2029 smartphone Agentic CPU/system/uArch opportunity that could become a second differentiated Primary Bet?

## Search strategy
Authority-guided seed search before broad expansion.

Primary conference communities:
- ISCA / MICRO / HPCA
- ASPLOS
- OSDI / SOSP
- MobiSys
- CGO / PLDI / LCTES
- DAC as secondary HW-SW co-design coverage

Primary journals:
- IEEE Transactions on Computers
- IEEE Transactions on Mobile Computing
- IEEE Micro
- ACM TACO
- ACM TOCS
- ACM TECS

## Canonical seed set

### Newly added Sources
- PAPER-053 — Agent-X
- PAPER-054 — TimelyLLM
- PAPER-056 — AgentProg
- PAPER-057 — ShadowNPU

### Existing Source re-opened
- PAPER-003 — Sereno

Sereno was initially rediscovered during the frontier scan and mistakenly staged as a new PAPER-055 Source.
Full identity review showed PAPER-055 duplicated canonical PAPER-003.
The duplicate was removed; PAPER-003 remains the sole canonical Source identity.

## 10Q status
- PAPER-053 — **FULL_10Q COMPLETE**
- PAPER-054 — **FULL_10Q COMPLETE**
- PAPER-003 — **FULL_10Q REFRESH COMPLETE**
- PAPER-056 — **FULL_10Q COMPLETE**
- PAPER-057 — **FULL_10Q COMPLETE**

All five canonical seeds are now decision-grade within explicit scope boundaries. Cross-paper synthesis is recorded in `analysis/frontier-2026/cross-seed-synthesis-2026-10-06.md`.

## Current decision-grade observations

### PAPER-053 Agent-X
Agent-specific prompt/output structure can yield material software-only execution value.
Impact:
- raises A/C software baseline;
- no Direction promotion.

### PAPER-054 TimelyLLM
Time-indexed usefulness of Agent outputs is a real scheduling signal, but substantial value is already captured at the serving-runtime layer.
Impact:
- broad timing novelty narrowed;
- R1 remains strictly post-ready;
- no new Execution-Time Utility Bet.

### PAPER-003 Sereno
Direct commercial-smartphone evidence establishes severe foreground/background mobile-AI QoE conflict and large software-only recovery.
Impact:
- Foreground-Protected Persistent Agent anchor strengthened;
- C problem relevance strengthened;
- C G1 baseline strengthened;
- no software-insufficiency or uArch promotion.

### PAPER-056 AgentProg
Long-horizon mobile GUI Agent success depends materially on explicit control-flow context, persistent variables and belief state in the evaluated system.
Impact:
- CLM-AGENT-004 added;
- A's B4-TX baseline strengthened;
- no A/R3 promotion.

### PAPER-057 ShadowNPU
Optimized NPU-centric sub-operator placement can reclaim substantial CPU/GPU fallback work on evaluated Snapdragon phones.
Impact:
- CLM-CPU-004 added;
- CG-06 strongest baseline strengthened to NPU-OPT/HETERO-OPT;
- CG-06 remains INVEST / 86.5.

## Candidate blind spots for next pass
- Agent-specific residual beyond upper-layer time-utility scheduling;
- foreground-protected persistent Agent control beyond generic SERENO-like QoS;
- Agent-aware heterogeneous stage graph placement beyond generic heterogeneous inference;
- long-horizon semantic state and context cost;
- smartphone CPU/NPU/DRAM/thermal interaction under realistic persistent Agent duty cycles.

## Current portfolio boundary
- A remains the only differentiated Primary Bet.
- C remains Strategic Enabler; its second-Bet watch was closed in Round 4.
- CG-06 remains INVEST.
- R1 remains Conditional Reserve.
- R3 remains BLOCKED.
- second differentiated Primary Bet remains unfilled.

## Stop condition for this run
Close only after:
- remaining seed papers receive decision-level review;
- snowball covers recurring groups and competing routes;
- architecture/systems/mobile/compiler venue coverage is checked;
- at least one negative/strong-baseline route is included for each second-Bet candidate;
- portfolio impact is classified KEEP / UPGRADE / DOWNGRADE / NARROW / KILL.


## Round 2 — Prior-art pressure test

Full 10Q completed:
- PAPER-058 — AutoDroid-V2 (MobiSys 2025)
- PAPER-059 — llm.npu (ASPLOS 2025)
- PAPER-060 — MUSched (OSDI 2026)
- PAPER-061 — Syrup (SOSP 2021)

Decision-grade effect:
- task-level semantic→code lowering is already a strong mobile-Agent software baseline;
- generic semantic→mobile-CPU scheduling is already demonstrated;
- portable application-defined cross-layer scheduling/policy is established prior art;
- optimized NPU software is a sustained moving frontier.

H-SCL is therefore narrowed to:
> automatic extraction of genuinely Agent-specific cross-framework facts with incremental smartphone cross-resource value beyond B4-TX/G1.

No portfolio lane/score changed.

See:
- `analysis/frontier-2026/round2-synthesis-2026-10-06.md`
- `analysis/frontier-2026/h-scl-hypothesis.md`

### Next P0 prior-art candidate — PENDING FULL 10Q
**Interactive Context for Mobile OS Resource Management (IEEE TMC 2020)**

Its abstract indicates application-transparent mobile semantic-context inference/propagation into CPU scheduling and power control.

It is **not decision-grade** until full-text review and 10Q are complete.

Secondary candidate:
WASH / Portable Performance on Asymmetric Multicore Processors (CGO 2016).


## Round 3 — Agent-specific residual audit

Full 10Q completed:
- PAPER-063 — Speculative Actions — ICLR 2026 / P0
- PAPER-064 — Sherlock — arXiv 2025 preprint / P1
- PAPER-065 — KVFlow — NeurIPS 2025 / P0

Residual decisions:
- **cancel/discard/commit legality — NARROW**: Agent-native, but strong Agent/workflow runtimes already use commit guards, reversible/idempotent/sandboxed effects, verification state, rollback and discard.
- **state-reuse identity — NARROW**: KVFlow reconstructs future reuse from Agent Step Graph / STE and uses it for KV retention/prefetch.
- **RequiredProgress — KEEP inside A**: exact residual remains open only beyond topology/criticality/verification/legality/reuse proxies.
- **foreground-impact budget — OPEN HYPOTHESIS / highest-priority next probe**: no equivalent decision-grade Agent-aware smartphone resource-budget contract is publicly established in the reviewed source set.

Canonical synthesis:
- `analysis/frontier-2026/round3-residual-synthesis-2026-10-06.md`
- `analysis/frontier-2026/h-fib-hypothesis.md`

Portfolio:
- no lane/score changes;
- no second Primary Bet;
- no uArch promotion.

### Next search gate
Pressure-test **H-FIB — Agent Foreground-Impact Budget** against:
- persistent/background mobile-Agent workloads;
- Sereno/MUSched generic foreground protection;
- TimelyLLM deadline/slack control;
- simple Agent self-throttling;
- mobile CPU/NPU/memory/thermal interference.

The target claim is not "foreground protection is valuable"; that is already established.
The target is whether **Agent-specific marginal value / tolerance state** changes the resource-control decision beyond generic QoS.


### Adjacent comparator discovered after Round 3 — PENDING FULL 10Q
- **Murakkab — Resource-Efficient Agentic Workflow Orchestration in Cloud Platforms — OSDI 2026**
- Role: strongest adjacent Agent-aware resource-orchestration comparator for H-FIB.
- Current use: screening only; no portfolio/Claim impact before full 10Q.
- Boundary: cloud Agent workflows, not smartphone foreground/background resource control.


## Round 4 — H-FIB falsification and convergence

Full 10Q completed:
- PAPER-066 — Murakkab — OSDI 2026
- PAPER-067 — HUSH / Smartphone Background Activities in the Wild — MobiCom 2015
- PAPER-068 — ReUA / Utility-Accrual Scheduling — EMSOFT 2004 / TECS lineage

Decision:
- Agent-aware workflow/SLO/resource orchestration is already strong software prior art (Murakkab).
- personalized smartphone background-work usefulness → suppress/allow is direct mobile prior art (HUSH).
- graded task utility / delay tolerance / low-value abort is foundational scheduling prior art (TUF/ReUA).

Therefore:
> **H-FIB is not promoted to a Direction.**

It is now an **A→C bridge question**:
- A must prove non-reconstructible Agent semantic RequiredProgress/value beyond SLO/TUF/history/topology/legality/reuse proxies.
- C may later test whether that proven information improves target-phone control.

Portfolio change:
- C remains STRATEGIC_ENABLER / 72.0.
- **C second-Bet watch is closed on current evidence.**
- A remains PRIMARY_BET / 82.5.
- second differentiated Primary Bet remains unfilled.

See:
- `analysis/frontier-2026/round4-h-fib-convergence-2026-10-06.md`
- `analysis/frontier-2026/h-fib-hypothesis.md`

### Search pivot
Stop generic semantic-control / utility-scheduling second-Bet search.
Next candidate families must come from other structural Agent workload changes, starting with persistent Agent memory/state and CPU-visible memory/retrieval/update behavior.


## Round 5 — Persistent Agent memory seed round

Full 10Q completed:
- PAPER-069 — MUSE — ACM Multimedia 2026 / P0
- PAPER-070 — LEANN — MLSys 2026 Best Paper / P0
- PAPER-071 — M3-Agent — ICLR 2026 / P0
- PAPER-072 — CD-ANN — Journal of Systems Architecture 2026 / P1

### Provenance correction
AME v1 and MUSE v2 share arXiv:2511.19192 and a direct mechanism/result lineage.

Canonical handling:
- **PAPER-069 = MUSE**
- AME is retained as source-evolution provenance only
- do not count AME and MUSE as independent corroboration

### Decision-grade result
- M3-Agent establishes persistent episodic + semantic + multimodal memory as a real Agent-native workload.
- MUSE establishes direct smartphone systems pressure from dynamic high-dimensional retrieval + continuous ingestion/index maintenance.
- LEANN establishes a strong compute-for-storage / compact-index software baseline.
- CD-ANN establishes a strong generic dynamic-index / segmented-residency baseline.

Therefore:
> persistent Agent memory is a credible new structural frontier, but **not yet a Direction or second Bet**.

Opened:
- `analysis/frontier-2026/h-pam-hypothesis.md`
- status: **ANALYSIS HYPOTHESIS / NOT A DIRECTION**

H-PAM asks only whether Agent-specific memory-lifecycle operations (acquire, consolidate, retrieve, revise, forget, replace) create a recurring smartphone systems control point that generic vector-search/index systems cannot already capture.

### Current authoritative portfolio status
This supersedes earlier intermediate snapshots in this Discovery Run:
- A — PRIMARY_BET / 82.5
- PT-A — PLATFORM_TRACK / 80.0
- C — STRATEGIC_ENABLER / 72.0; second-Bet watch closed
- CG-06 — INVEST / 86.5
- second differentiated Primary Bet — unfilled
- current second-Bet frontier — **H-PAM analysis hypothesis only**
- uArch Primary Bet — none

### Round-6 gate
Before H-PAM can become a Direction:
1. review direct mobile-Agent memory architecture evidence;
2. establish actual memory-operation mix and duty cycle rather than assume it;
3. review Agent-native memory systems with explicit store/update/consolidate/forget/retrieve actions;
4. pressure-test against MUSE/LEANN/CD-ANN and ordinary HNSW/IVF/PQ;
5. audit overlap with B-residual, C, R2, CG-01 and CG-07;
6. require a distinct target-phone SYSTEM_VALUE path before any hardware discussion.

## Round 6 — H-PAM recurrence and mobile-execution test

Full 10Q completed:
- PAPER-073 — MobiMem — arXiv 2025 preprint / P0
- PAPER-074 — AgeMem — ACL 2026 Long Paper / P0

Decision-grade result:
- MobiMem directly shows Profile/Experience/Action memory states affecting mobile Agent retrieval, template instantiation, fine-grained scheduling, action replay/stale validation and exception recovery.
- AgeMem independently exposes ADD / UPDATE / DELETE / RETRIEVE / SUMMARY / FILTER as learned Agent policy actions.
- therefore **Agent-memory lifecycle operation recurrence = PASS**.

Negative/strong-baseline result:
- MobiMem already captures major value through software templates, AgentRR, DAG scheduling and exception handling.
- AgeMem exposes operation identity explicitly at the tool/API boundary.

Therefore:
> H-PAM remains **KEEP / NARROW — ANALYSIS HYPOTHESIS / NOT A DIRECTION**.

Still missing:
- evidence that lifecycle semantics change CPU/NPU/data-placement or memory-maintenance decisions beyond upper-layer software;
- direct phone memory-bandwidth / energy / thermal profiling tied to Agent-memory operation classes;
- proof that ordinary API operation identity is insufficient.

MobiSys Workshop 2026 mobile-Agent memory benchmark:
- peer-reviewed publication metadata confirmed;
- full text not yet available through a stable accessible path in this review;
- remains **PENDING_FULLTEXT / NOT DECISION-GRADE**.

Canonical synthesis:
- analysis/frontier-2026/round6-h-pam-recurrence-2026-10-07.md
- analysis/frontier-2026/h-pam-hypothesis.md

Portfolio:
- no lane/score changes;
- no second Primary Bet;
- no uArch promotion.