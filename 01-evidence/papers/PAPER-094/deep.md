# PAPER-094 — K-Merge: Online Continual Merging of Adapters for On-device Large Language Models

## Source
- ACL 2026 Long Papers, pp. 3013–3029
- Samsung R&D Institute UK / University of Pisa / University of Padova
- official ACL Anthology paper reviewed
- Priority: P1 software baseline

## Q1 — Problem + target mapping
On-device LLMs may support many tasks through LoRA adapters, but devices cannot indefinitely retain one adapter per task.

K-Merge studies **online continual adapter-set evolution**: adapters arrive incrementally and the device must incorporate new capabilities under a fixed storage budget while preserving earlier tasks.

For H-CAL this asks whether adapter evolution itself creates a special lower-layer control need.

## Q2 — Novelty / new-regime relevance
K-Merge formalizes on-device continual merging:
- incoming LoRA arrives;
- compare it with stored adapters;
- either allocate a free slot or merge into a similar stored adapter;
- preserve a small merge-history map for later task→adapter routing.

K-Merge++ adds a similarity threshold to avoid consuming slots on redundant early tasks.

Classification:
**GENERIC ENABLING / adapter-lifecycle software baseline**.

## Q3 — Falsifiable hypothesis
If adapter collections can be compressed online using only adapter weights and merge history, a lightweight data-free policy should preserve multi-task performance better than naïve merging under the same slot budget.

Falsifiers:
- repeated merges rapidly destroy old capabilities;
- selecting by adapter similarity provides little value;
- merge compute/storage is too expensive on-device;
- task identity/routing dominates the problem.

The paper reports strong aggregate task performance under its constrained evaluation.

## Q4 — Research lineage / competing route
Competing routes:
- retain all adapters;
- static offline clustering/merging;
- TIES / DARE-style model merging;
- task-specific adapter replacement;
- retrain a multitask adapter;
- server-side lifecycle management.

The important distinction is that K-Merge treats **adapter evolution as a software object with explicit history and bounded storage**.

## Q5 — Key mechanism / control point
### Similarity-based assignment
Compare incoming LoRA updates with current stored adapters and choose the closest candidate.

### History-aware merge
Maintain task membership history and use a running weighted merge so prior tasks are not forgotten simply due arrival order.

### Bounded adapter slots
The storage budget K is explicit; software decides allocate vs merge.

## Q6 — Experiment design
The paper evaluates sequential task arrival across real-world generative tasks/languages and compares online merging variants against alternative merging strategies under limited adapter slots.

The decision-relevant outcome is not a phone power number; it is that adapter population growth can be managed without retaining every historical LoRA or original training dataset.

## Q7 — Data / artifact / reproducibility
Strengths:
- peer reviewed ACL long paper;
- explicit online/continual setting;
- data-free runtime operation;
- fixed storage budget;
- project page released.

Limitations:
- no live local gradient updates;
- incoming LoRAs are trained before arrival;
- not a smartphone serving/training co-location study;
- no battery/thermal/foreground-QoE result.

## Q8 — Evidence vs hypothesis
### [FACT]
The paper supplies an online software policy for evolving an on-device LoRA collection under a fixed storage budget.

### [FACT]
Its state consists of adapter weights, task mapping/history and similarity/merge policy.

### [OBSERVATION]
A large part of “continual adapter lifecycle” is representable above the hardware interface.

### [INFERENCE — project]
Adapter population/version management alone is not a distinct H-CAL hardware residual.

## Q9 — Real contribution to project decision
K-Merge narrows H-CAL:
- evolving adapters do not automatically imply new system hardware;
- lifecycle/merge/storage state has a clear software representation;
- the surviving H-CAL question must involve **live training publication + inference-state validity/interference**, not adapter collection growth itself.

## Q10 — Next action
1. KEEP as an H-CAL strongest software baseline.
2. Do not count adapter lifecycle identity as standalone differentiation.
3. Combine with MobiLoRA for cache/runtime baseline.
4. No portfolio score change.

## Decision footer
- **Evidence maturity:** software algorithm/system baseline
- **H-CAL impact:** narrows
- **Hardware impact:** none
- **Primary source:** https://aclanthology.org/2026.acl-long.137/
