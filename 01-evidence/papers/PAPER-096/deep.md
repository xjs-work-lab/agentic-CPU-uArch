# PAPER-096 — ZeroLock: Concurrent Memory-Efficient LLM Training via Modular Update Decoupling

## Source
- arXiv:2608.07974, 2026 preprint
- Android and multi-GPU prototypes
- Priority: P1 generic training baseline

## Q1 — Problem + target mapping
Backpropagation couples forward/backward dependencies across model chunks, creating pipeline bubbles and requiring upstream activations to remain live until downstream backward work completes.

ZeroLock asks whether this “update locking” can be removed at the algorithm level.

For H-CAL this pressure-tests any assumption that training concurrency/memory coupling is an immutable architecture constraint.

## Q2 — Novelty / new-regime relevance
ZeroLock uses local objective construction:
- partition model into chunks;
- give each chunk an independent local loss/readout path;
- allow chunk updates without waiting for downstream global BP;
- combine with LoRA.

Classification:
**GENERIC ENABLING / training algorithm-system baseline**.

## Q3 — Falsifiable hypothesis
If chunk-local objectives approximate the global optimization sufficiently well, modular updates can reduce waiting and activation retention without unacceptable convergence loss.

The paper supplies convergence analysis plus prototypes.

## Q4 — Research lineage / competing route
Competing routes:
- GPipe / 1F1B / PipeDream;
- Confidant-class mobile pipeline training;
- gradient checkpointing;
- BP-free/local-objective learning;
- MeSP-style structured backprop;
- mobile runtime scheduling.

## Q5 — Key mechanism / control point
The key mechanism is **algorithmic update decoupling**.

Early forwarding lets downstream work begin before upstream local backward completes.
Each stage retains only local trainable state/optimizer/checkpoint and exchanges hidden state instead of full gradients/optimizer state across stages.

## Q6 — Experiment design
The paper evaluates multi-GPU and Android prototypes.

Reported:
- multi-GPU: 26.5% memory reduction and 4.9% throughput gain vs BP-based baseline;
- Android TinyLlama fine-tuning: peak PSS <4,000 MiB;
- battery temperature around 37°C;
- wall-clock time 1644.1 s in the reported Android setting.

## Q7 — Data / artifact / reproducibility
Strengths:
- real Android prototype;
- algorithm + system co-design;
- convergence analysis;
- memory and timing observations;
- code artifact linked.

Limitations:
- preprint;
- Android experiment is training-oriented, not live inference + training;
- server and phone results are not identical metrics;
- local objectives alter the learning algorithm and may have task-dependent quality trade-offs.

## Q8 — Evidence vs hypothesis
### [FACT]
Training dependency structure can itself be changed by the learning algorithm.

### [FACT]
The paper demonstrates Android feasibility for its training scheme.

### [OBSERVATION]
Some apparent execution/memory coupling is not fixed by hardware.

### [INFERENCE — project]
Generic training concurrency is even less suitable as a differentiated Agent hardware thesis after ZeroLock-class baselines.

## Q9 — Real contribution to project decision
ZeroLock narrows H-CAL's generic-training portion:
- update locking is not an immutable hardware property;
- activation lifetime can be altered algorithmically;
- phone training concurrency has additional software/algorithm options.

It does **not** resolve:
- live Agent serving latency during updates;
- adapter-publication/KV-version correctness;
- product-specific update cadence.

## Q10 — Next action
1. KEEP as generic strongest baseline.
2. Do not use training concurrency alone to justify H-CAL.
3. Combine with LOCAL/MobiLoRA when judging the remaining version/cache residual.
4. No portfolio score change.

## Decision footer
- **Evidence maturity:** preprint + Android prototype
- **H-CAL impact:** narrows generic training residual
- **Hardware impact:** none
- **Primary source:** https://arxiv.org/abs/2608.07974
