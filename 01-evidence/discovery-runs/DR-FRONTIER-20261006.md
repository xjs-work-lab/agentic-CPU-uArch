+++
id = "DR-FRONTIER-20261006"
type = "DISCOVERY_RUN"
lifecycle = "OPEN"
as_of = "2026-10-06"
coverage_quality = "AUTHORITY_SEED_FULL_10Q"
scope = "2024-2026 frontier re-open for second differentiated Bet search across smartphone Agent workloads, runtime/OS control, heterogeneous execution, compiler and CPU/uArch"
limitations = "Seed, Round-2 prior art and Round-3 Agent-specific residual Sources have completed decision-level 10Q review. H-FIB foreground-impact-budget evidence and broader venue coverage remain incomplete; no second-Bet promotion is authorized yet."
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
- C remains Strategic Enabler / second-Bet watch.
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
