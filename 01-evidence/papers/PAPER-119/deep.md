# PAPER-119 — Full Paper Insight 10Q

**Primary source:** https://aclanthology.org/2026.acl-long.581/
**Depth:** FULL_10Q / original 2026 paper
**Identity:** DOI 10.18653/v1/2026.acl-long.581
**Evidence status:** PEER_REVIEWED_ACL_2026

## Q1 — Problem and mobile mapping
Static multi-Agent scripts run verification/refinement/testing for every request regardless of task difficulty. AO-5 asks whether lower-layer explicit semantic RequiredProgress adds value after the runtime already observes artifacts and validation state.

## Q2 — New-regime relevance
Agent workflow-specific adaptive execution/verification. Core mechanism is software orchestration, not an OS/CPU or NPU scheduling policy.

## Q3 — Falsifiable hypothesis
A two-stage controller using cheap artifact checks plus conditional expensive routing reduces full workflow compute/latency while preserving outcome quality against a fixed heavy workflow. A failure is inaccurate early-exit or excessive controller overhead.

## Q4 — Research lineage and baselines
ACL 2026 long paper; compared IO, CoT, Self-Refine, Reflexion, ADAS and AFlow. Authors: University of Connecticut, MBZUAI and Roblox. Builds atop an existing AFlow workflow and changes per-query routing.

## Q5 — Detailed mechanism and information source
Per-agent structured artifact envelope; gate features: programmatic spec adherence, DistilBERT-like small judge, candidate agreement, historical agent reliability. Risk-tier threshold classifies cheap no-go/likely-good. When forwarded, LLM controller inspects gate summary, intermediate artifact and DAG, selecting early exit, verification, test or refinement. This information is runtime/artifact-visible; no opaque private Agent DemandState required.

## Q6 — Controlled experiment and results
HumanEval/MBPP code generation plus GSM8K mathematical reasoning. Official ACL camera-ready PDF Table 2 reports output-token decrease relative to AFlow between 37.4% and 63.4%, latency decrease 36.8–41.9%, accuracy decrease up to 1.4 percentage points. Overall reported average token decrease 50.5%, latency >36%; website abstract's 43% number is not the camera-ready abstract/table average. On MBPP baseline AFlow 94.2%/6643.2 output tokens/134.28s vs full 93.7%/2430.2/77.99s.

## Q7 — Ablation and overhead
On MBPP: Gate-only 86.7%/2516.4 tokens/65.24s; LAS-only 93.9%/3678.1/90.25s; combined 93.7%/2430.2/77.99s. Measured gate overhead 0 tokens/0.15s per step vs LAS controller 725 tokens/19.44s. Gate precision 66.29% recall 98.60%, so naive cheap gating can terminate erroneously; trained, calibrated control matters.

## Q8 — Reproducibility and external validity
Official ACL final 12-page PDF Section 4–8 plus Tables 1–6 and Limitations directly inspected. Code URL announced (https://github.com/YoshuaDavy/LLM-as-Scheduler), release/completeness not independently verified. Three datasets and benchmark-tuned gate; cloud LLM APIs, not a real phone. Results use quality-cost tradeoffs, not matched smartphone foreground QoE/battery.

## Q9 — AO-5 contribution and counterpressure
Counterexample to vague novelty of 'semantic-progress scheduling': intermediate artifact quality and DAG state can already drive valuable software policy. Not a falsifier of an *unobservable* goal-necessity/RequiredProgress residual because it does not run a matched-observability B4-TX vs privileged-state information-value test.

## Q10 — Next action
Add LAS gate+reliability/verification branch selection to AO-5 strongest observable baseline. Separate runtime verification state from truly privileged future-goal/required-work information. Keep A score unchanged pending cross-AO synthesis.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for the evaluated *software/server/benchmark* system, not target-phone SYSTEM_VALUE
- AO-5: AO-5 direct software strongest baseline: validator-conditioned dynamic workflow routing and early exit
- Direct mobile CPU-uArch evidence: none
- Open gate: conditional information value of internal RequiredProgress over matched B4-TX, plus mobile transfer
- Primary source: https://aclanthology.org/2026.acl-long.581/
