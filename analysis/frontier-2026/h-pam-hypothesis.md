# H-PAM — Persistent Agent Memory Execution Substrate

Status: **ANALYSIS HYPOTHESIS / NOT A DIRECTION**
Opened: 2026-10-06

## Working hypothesis
> Persistent smartphone Agents may create a recurring memory-operation lifecycle whose **operation semantics and phase mix**—acquire, embed, insert/update/delete, consolidate, retrieve, traverse, forget/replace—enable a reusable mobile runtime/compiler/system control point beyond generic vector-search/index software.

This is deliberately narrower than:
- "Agents need long-term memory";
- "vector databases are large";
- "ANN updates are expensive";
- "mobile NPU can accelerate vector search".

All four already have strong evidence or prior art.

## Evidence bridge

### Agent-native workload premise
PAPER-071 / M3-Agent:
- long-term episodic + semantic memory materially improves long-horizon Agent capability;
- memory is continuously built and later retrieved;
- memory is structured, multimodal and entity-centric.

### Direct phone systems premise
PAPER-069 / MUSE:
- dynamic high-dimensional retrieval + ingestion/index maintenance creates real mobile SoC execution/data-movement pressure;
- CPU/GPU/NPU placement and layout/index choices matter materially.

### Strong generic software baseline
PAPER-070 / LEANN:
- local vector-memory storage can be shifted toward recomputation and compact graph state.

PAPER-072 / CD-ANN:
- dynamic growth/insertion + limited client residency can be handled with segmented/on-demand ANN structures.

## What is NOT white space
Do not pursue H-PAM as:
- a generic vector database for phones;
- low-storage ANN;
- dynamic insertion/update support;
- generic CPU/GPU/NPU vector-search scheduling;
- generic cache/shared-memory acceleration;
- a semantic provenance/lineage system.

## Candidate residual
The only interesting residual is:
> Does a realistic persistent Agent expose **operation-class semantics and temporal coupling** that generic vector-search systems do not know, and can a mobile system exploit that information to improve meaningful end outcome?

Examples to test, not assume:
- memory acquisition vs task-time retrieval priority;
- consolidation/rewrite vs simple insertion;
- semantic invalidation / replacement vs generic delete;
- episodic→semantic promotion;
- multi-representation memory (graph + vector + raw media);
- state age / salience / confidence affecting placement or maintenance urgency;
- coordinated background ingestion with latency-critical foreground recall.

## Strongest baseline
Any H-PAM experiment must beat:
- MUSE-class heterogeneous mobile retrieval;
- LEANN-class compute-for-storage;
- CD-ANN-class segmented/on-demand dynamic indexing;
- optimized HNSW/IVF/PQ;
- generic batching, caching, prefetch, zero-copy and accelerator scheduling;
- existing C generic resource controls.

## Boundary against current portfolio

### B-residual
B-residual owns:
> semantic/workflow revision → lineage/invalidation/coherence of derived artifacts.

H-PAM owns only:
> operational execution/data-plane cost of the memory lifecycle.

If H-PAM's only residual is semantic invalidation/coherence, fold it into B-residual.

### R2
R2 owns CPU continuation microstate/locality.
H-PAM does not claim thread/cache warm-state novelty.

### CG-01
CG-01 owns generic shared-cache/handoff benchmarking.
H-PAM must not become a rebranded cache proposal.

### CG-07
CG-07 owns a potential dedicated always-on AI domain.
H-PAM does not imply a new always-on hardware island.

### C
C owns generic system/resource control.
If memory operation type merely selects an ordinary QoS/scheduling policy, fold it into C.

## Kill criteria
Kill H-PAM as a separate candidate if:
1. realistic Agent memory reduces to ordinary vector query/insert/delete at systems level;
2. MUSE + LEANN + CD-ANN-class baselines capture the meaningful value;
3. graph/consolidation semantics do not alter processor/data-placement decisions;
4. operation-class information can be reconstructed cheaply from ordinary API calls;
5. no direct phone workload shows sustained memory duty cycle;
6. incremental end-outcome / energy / latency value is <~5%;
7. the remaining issue is cleanly owned by B-residual, C, R2, CG-01 or CG-07.

## Promotion gate
Do not create a Direction until:
1. at least one direct/mobile Agent-memory workload trace exists;
2. operation frequencies and overlap are measured, not invented;
3. ≥2 materially different Agent-memory designs show a recurring systems pattern;
4. generic vector-index baselines are strong;
5. a distinct team-controllable software/runtime/compiler/CPU control point exists;
6. target-phone SYSTEM_VALUE is testable.

## Hardware boundary
H-PAM is **not a uArch hypothesis**.

Hardware discussion remains gated by:
STRUCTURAL_SIGNAL → SYSTEM_VALUE → SOFTWARE_INSUFFICIENCY → hardware-specific cause.

## Next evidence targets
1. MobiSys 2026 memory-architecture benchmark for mobile Agents.
2. Mobile long-term-memory acquisition / multimodal sensing work.
3. Agent memory systems with explicit update/consolidation/forget operations (AgeMem, MIRIX, LiCoMemory-class).
4. Dynamic ANN/vector systems to establish strongest non-Agent baseline.
5. Any real smartphone traces of memory ingestion/retrieval/index maintenance.