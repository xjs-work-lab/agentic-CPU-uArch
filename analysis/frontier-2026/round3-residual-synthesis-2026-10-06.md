# Frontier Round 3 Residual Audit — 2026-10-06

## Decision question
After broad semantic-control patterns were folded into A/C, which genuinely Agent-specific residuals still survive strong prior art and deserve second-Bet research?

## Residuals tested
1. cancel / discard / commit legality;
2. RequiredProgress / task-value progress;
3. state-reuse identity / future usefulness;
4. foreground-impact budget for persistent/background Agents.

## Decision-grade Sources added
- PAPER-063 — Speculative Actions — ICLR 2026 — FULL_10Q / P0;
- PAPER-064 — Sherlock — arXiv 2025 preprint — FULL_10Q / P1;
- PAPER-065 — KVFlow — NeurIPS 2025 — FULL_10Q / P0.

## 1. Cancel / discard / commit legality
### Result: **NARROW — Agent-native but upper-layer capturable**

Evidence:
- Speculative Actions treats idempotence, reversibility, sandboxability and semantic commit guards as execution-critical metadata.
- Sherlock uses verifier-pending state, dependency lineage, rollback and downstream discard/re-execution.

Conclusion:
> Effect/Commit legality is real Agent-specific information, but strong Agent/workflow runtimes already exploit it directly.

Portfolio mapping:
- **PT-A** owns the common platform contract for effect metadata, commit, verification and bounded recovery;
- **A B4-TX** assumes legality/rollback facts are reconstructible where the runtime exposes lineage/transactions;
- no independent second Bet;
- no hardware promotion.

Open residual:
Only lower-layer incremental value **beyond** Agent-runtime speculation/rollback remains interesting.

## 2. State-reuse identity / future usefulness
### Result: **NARROW — workflow topology is already a strong proxy**

KVFlow demonstrates that:
- Agent workflow structure can be represented as an Agent Step Graph;
- steps-to-execution predicts future activation;
- this signal can drive KV retention/eviction and prefetch;
- generic recency is not the strongest software baseline.

Conclusion:
> 'This state will be useful again soon' is often reconstructible from workflow topology rather than requiring a new semantic hardware hint.

Portfolio mapping:
- add STE/future-activation/reuse-distance to **A B4-TX**;
- state-reuse identity alone is not a new Direction;
- mobile CPU/NPU/DRAM reuse remains an external-validity gap, not proof of novelty.

## 3. RequiredProgress
### Result: **KEEP — but definition narrowed sharply**

No reviewed authority-grade system paper in this pass establishes the exact A hypothesis:
> a semantic measure of how much execution still contributes to the user's required final outcome that remains informative beyond program/workflow topology, critical-path/slack, verifier vulnerability, legality and future reuse.

This is important, but absence of a matching paper is **not proof of novelty**.

A's residual is now explicitly:
> Does DemandState / RequiredProgress contain information that cannot be reproduced by strong topology-, history-, legality-, verification- and reuse-derived proxies, and does that residual preserve >=~5% end-outcome value on target-relevant workloads?

RequiredProgress therefore remains inside A, not a new Direction.

## 4. Foreground-impact budget
### Result: **KEEP AS HIGHEST-PRIORITY OPEN RESIDUAL — not yet a Direction**

Current strong mobile baselines:
- PAPER-003 Sereno: generic foreground QoE protection against background mobile LLM interference;
- PAPER-060 MUSched: generic interaction-critical semantic CPU scheduling.

Current Agent-side evidence:
- recent mobile-Agent work discusses foreground/background execution and user interaction modes, but the reviewed strong source set does not yet establish a reusable **Agent-aware resource-impact budget** that couples task progress/urgency/discardability to CPU/NPU/memory/thermal interference control.

Important wording:
> **not publicly established in the reviewed decision-grade source set**

Do not convert this into 'does not exist'.

## Candidate hypothesis H-FIB
Working hypothesis:
> A persistent/background Agent can expose or derive a compact foreground-impact budget from its task state—how much delay, degradation, suspension or discarded progress is acceptable—and a smartphone control plane can use that budget to allocate CPU/NPU/memory/thermal resources with better end outcome than generic foreground-protection policies.

Why it is interesting:
- mobile interference is directly established;
- Agent tasks have heterogeneous urgency/progress/recoverability;
- generic QoS protects the foreground but does not necessarily know the marginal value of continuing background Agent work;
- the signal could connect A semantic state to C system control without inventing a new semantic-control substrate.

Why it may die:
- Sereno/MUSched-style generic control may already approximate the optimal decision;
- task deadlines/slack may reconstruct the useful portion;
- Agent runtime may simply pause itself without needing a system contract;
- resource-impact modeling may be too device/workload specific;
- end-outcome gain may be <~5%.

## Round-3 competition table
| Residual | Evidence result | Ownership | Second-Bet state |
|---|---|---|---|
| cancel/discard/commit legality | strong Agent-runtime capture | PT-A + A baseline | NARROW / not separate |
| state-reuse identity | strong workflow-aware cache capture | A baseline | NARROW / not separate |
| RequiredProgress | exact residual not yet explained by strongest proxies | A | KEEP inside Primary Bet A |
| foreground-impact budget | generic mobile QoE baseline strong; Agent-specific resource budget unestablished | A↔C seam | **OPEN HYPOTHESIS / highest-priority second-Bet probe** |

## Portfolio impact
- A remains PRIMARY_BET / 82.5 / SIMULATION_SUPPORT.
- PT-A remains PLATFORM_TRACK / 80.0 / SYSTEM_VALUE.
- C remains STRATEGIC_ENABLER / second-Bet watch / 72.0.
- CG-06 remains INVEST / 86.5.
- R3 remains BLOCKED.
- second differentiated Primary Bet remains intentionally unfilled.

## Next research gate
Do not search more broad semantic-scheduler papers.

Next round should directly falsify **H-FIB**:
1. find persistent/background mobile-Agent workloads with measurable CPU/NPU/memory/thermal footprint;
2. identify whether the Agent runtime knows delay/degrade/cancel/restart tolerance that generic QoS cannot infer;
3. compare against Sereno/MUSched/deadline-slack strongest baselines;
4. search MobiSys/OSDI/ASPLOS/EuroSys/ATC and mobile-agent systems for equivalent contracts;
5. define a device-free trace/simulation test only if evidence shows a distinct information variable.

## Current conclusion
Round 3 does **not** discover a second Bet.

It does something more useful: it reduces the candidate search to one concrete seam:
> **Agent marginal-value / tolerance state → foreground-impact budget → mobile cross-resource control.**

That seam must now survive prior art and strongest-baseline falsification before becoming a Direction.