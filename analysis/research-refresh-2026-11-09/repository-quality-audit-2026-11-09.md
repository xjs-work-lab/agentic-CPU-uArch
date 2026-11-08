# Agentic CPU µArch Research Refresh — Phase 1 Repository Audit

**Audit date:** 2026-11-09  
**Repository:** `xjs-work-lab/agentic-CPU-uArch`, default branch `main`  
**Research mode:** PUBLIC_ONLY. No owned phone tests, experiments, simulation, PoC, or proprietary evidence.  
**Scope exclusion:** No PPT/PPTX edits or re-generation in this refresh.

## 1. Repository snapshot

GitHub recursive tree was read without truncation:
- 1,179 files; 247 directories.
- 192 files under `01-evidence/papers/` (paper folders contain README/deep cards and selected review/screen files; this is not 192 distinct papers).
- 31 files under `01-evidence/patents/`.
- 42 files under `01-evidence/vendors/`.
- 168 files under `02-claims/`.
- 229 files under `03-evidence-cases/`.
- 193 files under `09-roadmap/`.
- 62 files under `analysis/`; 44 decision-event files under `08-decisions/events/`.
- Graph authority in `00-project/STATUS.md` records 632 canonical nodes and 1,202 semantic edges (historical graph QA references are dated October 2026).

The repository is structurally substantial and has canonical layers for sources, claims, evidence cases, actors/capabilities, trends/opportunities/directions, validation, decisions, roadmap, analysis, and history.

## 2. Authority and state reconciliation

Current decision authority is `09-roadmap/current.md` (updated 2026-10-08), with `DEC-PORTFOLIO-002` and `DEC-A-008` as formal decision events. It states:
- Three priority engineering/platform investments: CG-06, PT-A, C.
- Three conditional reserves: A, B-residual, R2.
- R1 WATCH; CG-07 FOLLOW/EXPLORE; CG-01 BENCHMARK/FOLLOW; R3 BLOCKED.
- Zero independently supported Agent-only CPU-uArch/ISA hardware Primary Bets.
- Public-source-only; no new local experiment or test.

The root README has a 2026-10-27 PPT delivery banner but still links to a research closure snapshot dated 2026-10-09. This is not inherently contradictory: the research was closed with boundaries, then presentation production continued. However, a new evidence-driven refresh now needs a new dated currentness layer rather than rewriting the October 8/9 decisions.

Historical drift risk:
- `00-project/STATUS.md` contains long historical sections with obsolete A=PRIMARY_BET/82.5 language. The top authority banner warns not to use these sections as current.
- `09-roadmap/final-2027-2029.md` is explicitly archived and must not be treated as the current portfolio.
- `CONTINUE-HERE.md` correctly says broad research is closed by default and should reopen only on decision-relevant new evidence.
- The refresh therefore must add a new dated evidence review and, only if warranted, a new Decision Event. It must not edit historical decisions in place.

## 3. Quality assessment — first pass

| Dimension | Current assessment | Reason / limitation |
|---|---|---|
| Repository architecture | Strong | Clear separation of source, claim, evidence case, direction, decision and history; canonical SSOT concept is explicit |
| Historical traceability | Strong | Stable IDs, decision events, migration/transaction records, source identity policies |
| Research method | Strong | Public-only boundary, 10Q paper/patent cards, negative evidence, comparison normalization, evidence maturity gates |
| Source-depth consistency | Mixed-to-strong | Many decision-critical papers have deep cards; source folders are heterogeneous and not every item is a full 10Q |
| Currentness | Needs refresh | Most canonical status/audit files date 2026-10-08/09; latest listed paper is PAPER-121 (2026-10-08 screen/deep); vendor records VENDOR-029 were reviewed 2026-10-08 |
| Industry/platform coverage | Needs refresh | Android NPU Manager and current vendor baseline captured, but new OEM silicon/platform disclosures and shipping implementation evidence require re-check |
| Evidence independence | Strong practice, must re-apply | Existing audit explicitly recognizes shared author lineages (e.g., llm.npu/ShadowNPU and Agent.xpu/HeRo); new work also needs lineage mapping |
| Claim-to-decision chain | Strong design, targeted audit needed | Round15G checked decision-critical sources, not every claim/every external URL |
| Quantitative comparability | Strong rules, recurring risk | The repo distinguishes kernel/operator/model-stage/E2E/Agent/device QoE; refresh must enforce it for new results |
| Repository automation | Good foundation | Graph, source identity, link/archive audit workflows exist; refresh outputs should be validated against them |
| Scientific completeness | Not established | Prior audit explicitly did not re-read every source or check every external URL; this refresh must target changed decision areas, not claim exhaustive literature coverage |

## 4. Main quality risks to investigate

1. **Freshness gap:** A decision made October 8 can be outdated by November 9 if new work directly measures smartphone Agent workload, not merely generic edge inference.
2. **Publication status ambiguity:** arXiv preprints, accepted conference papers, official docs and shipping OEM implementations must remain separate evidence classes.
3. **External validity:** A result on one Snapdragon phone, one model and one GUI trace does not establish all Android devices, other NPU backends or whole-day battery outcomes.
4. **Baseline strength:** Compare against the strongest existing runtime/backend/OS configuration, not default/unmanaged execution only.
5. **Shared research lineages:** Multiple papers from the same group/platform are not independent replications.
6. **Software-vs-hardware attribution:** A useful CPU counter, state cache, scheduler or NPU power-vote control is not itself evidence for a new CPU structure.
7. **Portfolio drift:** New evidence must be mapped to the exact decision it can change; do not automatically promote A/B/R2 or create a new hardware bet.
8. **Decision date semantics:** Current docs use dates in October 2026; each new source must have original public timestamp and access/review timestamp.

## 5. First new decision-relevant evidence found

Two newly indexed primary preprints published after the October 8 decision are sufficiently close to the target to warrant full 10Q review:

- **PAPER-122 — EdgePace: Deadline- and Freshness-Aware LLM Scheduling on Unified-Memory Platforms**, arXiv:2610.37307, 2026-10-27. Original: https://arxiv.org/abs/2610.37307 and HTML: https://arxiv.org/html/2610.37307. Reports evaluation on OnePlus 13 plus Jetson platforms; foreground deadline misses reduced 24.1–96.1% vs unmanaged inference while retaining 64.9–98.5% LLM throughput. OnePlus example: camera deadline misses -91.3%, throughput retained 90.4%. Direct relevance: C and CG-06; also sharpens the DRAM/shared-resource part of B-residual. It is a preprint, not independent replication or OEM shipping evidence.
- **PAPER-123 — Tandem: Serving Hybrid Linear-Attention GUI Agents on Mobile NPUs**, arXiv:2610.26660, 2026-10-19. Original: https://arxiv.org/abs/2610.26660 and HTML: https://arxiv.org/html/2610.26660. Reports Snapdragon 8 Elite GUI-agent trace evaluation; relative to llama.cpp's fastest NPU configuration, text-step latency -30%, screenshot-step latency -16%, text-step energy -33%, and loaded-model standby power 0.76 W→0.22 W. Direct relevance: C, CG-06, B-residual; A only as software-observability counterpressure. It is a preprint and its workloads/model/phone are bounded.

These two sources are described in separate evidence cards in this directory. Their results must not be combined into one speedup or generalized to all phones.

## 6. Refresh plan

### Workstream A — workload / Agent runtime / state
- Re-evaluate GUI-agent repeated prompt rewriting, recurrent-state reuse, rollback, model-resident idle power, freshness and task-level deadlines.
- Search independent mobile Agent workloads and systems beyond the same author groups already represented in PAPER-098/Agent.xpu and PAPER-003/SERENO.
- Update A, B-residual and C only to the extent supported.

### Workstream B — mobile CPU/NPU/DRAM and power
- Compare new scheduling and memory-pressure mechanisms against SERENO, Agent.xpu, HeRo, Android NPU Manager, QNN shared-buffer and current device APIs.
- Separate OnePlus/Qualcomm phone results from Jetson and server results.
- Look for public counter availability, safe suspension granularity, accelerator preemption limits and power-vote behavior.

### Workstream C — compiler / ISA / microarchitecture
- Search Arm/LLVM release notes, AArch64 SME2/SME ABI, mobile CPU kernels and official silicon disclosures since October 8.
- Require target-phone results and strong CPU/NPU baselines before changing CG-06 or creating hardware hypotheses.
- Search negative results and evidence of generic software absorption.

### Workstream D — vendor / standards / patents
- Refresh Android/AOSP, Qualcomm, MediaTek, Apple, Arm, Samsung, LLVM and relevant patent-family disclosures.
- Distinguish announcement, specification, SDK support, implementation and shipping-device evidence.

## 7. Current preliminary status

No formal decision has been changed in this Phase 1 audit. Preliminary interpretation:
- **C: likely strengthened**, because EdgePace adds a direct OnePlus 13 example for deadline/freshness-aware co-scheduling.
- **CG-06: likely strengthened as a software/measurement engineering track**, because CPU counter signals and NPU execution yielding affect heterogeneous QoE; not evidence of new ISA.
- **B-residual: narrowed, not promoted**, because state reuse/power management and cross-engine resource controls can be software-visible, but physical residual remains unmeasured.
- **A: not promoted**; new papers show more progress can be derived from workflow artifacts, but do not test privileged hidden RequiredProgress against complete matched observability.
- **PT-A: no direct change yet**; the new papers do not directly assess permission/target binding/real-world action verification.
- **R2: no direct change yet**; no new phone microstate/cache locality evidence found in the first targeted scan.

This is a preliminary Phase 1/early discovery assessment, not final November portfolio authority.

## 8. Non-goals

- Do not modify any PPT/PPTX, PNG, Speaker Notes or slide content.
- Do not overwrite October decision events or the October 8 current portfolio.
- Do not conduct local tests, experiments, simulations or PoCs.
- Do not claim exhaustive coverage of every paper, patent or OEM.


## 9. Second-pass discovery: high-value prior art missing from the October closure

The targeted independent search found four additional sources not present in the current paper inventory by arXiv ID/title search. Two predate the October 8 closure and therefore represent **coverage omissions**, not new post-closure publications. One cross-layer source has a manuscript DOI/venue metadata that needs publisher confirmation.

### Newly reviewed source additions

| Provisional refresh ID | Source | Date/status | Why it matters | Why it does not create a hardware bet |
|---|---|---|---|---|
| PAPER-124 | Is Your NPU Ready for LLMs? (arXiv:2607.05475) | arXiv v1 2026-07-06; manuscript lists POMACS 10(3), DOI 10.1145/3857370; publisher status pending | Four Qualcomm phones, five frameworks, CPU/GPU/NPU; CPU decode often leads NPU; host polling/sleep/affinity/DVFS change energy materially | Isolated inference only; no foreground Agent loop; no CPU ISA proposal |
| PAPER-125 | Mitigating Compiler Fusion-Induced Power Bursts (arXiv:2607.16555) | Preprint 2026-07-17 | Shows NPU compiler fusion can create transient current/voltage risk; graph-level PAPR barriers can mitigate selected cases | One Snapdragon 8 Gen 3, two vision backbones; no CPU uArch change; transfer law not calibrated |
| PAPER-126 | sd.npu (arXiv:2510.15312) | Full-text version 2025-12-17 | Three commercial phones and tasks including UI automation; progressive graph switching and NPU-tailored speculative decoding already address NPU-only mobile RAG | Runtime/graph/speculation techniques; not evidence of hidden hardware state |
| PAPER-127 | MemGUI-Bench (arXiv:2602.06075) | Preprint 2026-02 | Quantifies short/long-term GUI-agent memory deficits across 128 tasks/26 apps/11 agents | Benchmark and agent-memory result, not CPU/OS private-state evidence |

### Important correction to the research freshness narrative

PAPER-124 and PAPER-125 are not necessarily first published after October 8; their arXiv first-post dates are July 2026. They were missing from the previous evidence inventory, so their discovery is a repository coverage correction. EdgePace and Tandem are genuinely new after the October 8 portfolio decision (October 19 and October 27, respectively). PAPER-126 and PAPER-127 are older prior-art additions.

### Updated source-depth and independence cautions

- The Consensus research agent screened 20 papers at abstract level and produced a cited synthesis. It is a discovery/triage layer only; it is not treated as 20 full-text reviews.
- EdgePace and Tandem full texts were separately retrieved and reviewed. EdgePace's PMU read-overhead numbers are reported on Jetson Orin Nano Super, not OnePlus 13.
- Tandem is a separate research group and has a public llama.cpp fork. Its specific DMA cache-coherence bug is handled with OS cache clean/invalidate, not a new CPU hardware primitive.
- AOSP Android 17 NPU Manager and its CTS tests were checked directly. The CTS priority test is race-based and device-tuned; it is not an Agent freshness/QoE guarantee.
- Qualcomm QAIRT public docs expose manual/automatic HTP performance-control strategy and performance-vote release. This is software-visible runtime control, but not proof of generic per-sublayer inference preemption.

### Updated preliminary direction status

- C: STRENGTHEN.
- CG-06: STRENGTHEN, especially phase-aware CPU decode, CPU-side accelerator orchestration and compiler/backend quality.
- B-residual: NARROW to physical cross-engine validity/coherence gaps that software cannot cheaply reconstruct; ordinary recurrent-state reuse and selected DMA cache maintenance already have software solutions.
- A: KEEP CONDITIONAL / NARROW; GUI memory deficits do not prove private hardware RequiredProgress.
- PT-A and R2: no direct change in this batch.

No historical decision or PPT file was changed.
