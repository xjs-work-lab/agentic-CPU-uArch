# PAPER-074 — Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents (AgeMem)

## Source
- ACL 2026, Long Paper
- DOI: https://doi.org/10.18653/v1/2026.acl-long.981
- ACL Anthology: https://aclanthology.org/2026.acl-long.981/
- Artifact: https://github.com/y1y5/AgeMem
- Authors: Wuhan University + Alibaba Group
- Benchmarks: ALFWorld, SciWorld, PDDL, BabyAI, HotpotQA
- Backbones: Qwen2.5-7B-Instruct, Qwen3-4B-Instruct
- Priority: P0

## Q1 — Problem + target mapping
Long-horizon Agents have two coupled memory problems:
- persistent long-term memory must be written, corrected and cleaned over time;
- finite short-term context must be retrieved into, compressed and filtered.

Most systems manage those through heuristics or separate controllers.

AgeMem instead asks:
> Can memory management itself become part of the Agent policy, with explicit memory actions learned end-to-end?

Project mapping:
this is direct evidence for H-PAM's question about recurring Agent-memory lifecycle operations.

## Q2 — Novelty / new-regime relevance
AgeMem unifies LTM and STM operations in one action space.

LTM tools:
- `ADD` — insert new memory;
- `UPDATE` — modify an existing memory;
- `DELETE` — remove obsolete/incorrect memory.

STM/context tools:
- `RETRIEVE` — bring LTM into active context;
- `SUMMARY` — compress interaction history;
- `FILTER` — remove irrelevant/noisy context.

These are not static middleware calls; the model learns **when** to invoke them.

Classification:
**DIRECT_AGENTIC memory-lifecycle evidence**, but not a mobile systems paper.

## Q3 — Falsifiable hypothesis
Core hypothesis:
> An Agent policy that learns explicit LTM and STM memory actions jointly should outperform fixed/heuristic memory pipelines on long-horizon tasks.

Falsifiers:
- learned memory actions do not beat strong memory baselines;
- memory-action credit assignment is too sparse;
- tool use collapses into one dominant operation;
- LTM improvements come only from more retrieval;
- context-management tools reduce tokens but harm task success;
- behavior learned on HotpotQA does not transfer to other task families.

ACL evaluation supports the hypothesis across five benchmarks and two backbones.

## Q4 — Research lineage / competing route
Compared baselines include:
- LangMem;
- A-Mem;
- Mem0;
- Mem0g;
- no-memory;
- AgeMem-noRL;
- RAG variants for STM ablation.

Related system families:
- MobiMem specialized Profile/Experience/Action memory;
- M3-Agent episodic/semantic multimodal memory;
- MemGPT-style hierarchy;
- external heuristic memory controllers.

Strategically, AgeMem is independent of MobiMem and uses a different abstraction:
- MobiMem: specialized memory types coupled to GUI execution services;
- AgeMem: learned memory operations embedded in Agent policy.

That independence makes recurring lifecycle operations more credible.

## Q5 — Key mechanism / control point
### Unified tool interface
The Agent sees memory operations as structured actions alongside ordinary reasoning.

### Three-stage progressive training
Stage 1:
- construct LTM from contextual information;
- learn storage/update behavior.

Stage 2:
- reset active context while retaining LTM;
- inject distractors;
- learn filtering/summarization/context control.

Stage 3:
- integrated reasoning;
- retrieve and manage both STM and LTM during full tasks.

### Step-wise GRPO
Terminal/task rewards are propagated back across earlier memory decisions to address sparse/discontinuous memory-action credit assignment.

### Project interpretation
AgeMem shows that the memory lifecycle is not merely `query/insert`.
Agents may adaptively:
- add;
- revise;
- delete;
- retrieve;
- summarize;
- filter.

Those operation classes recur independently from MobiMem.

## Q6 — Experiment design
Training:
- RL fine-tuning only on HotpotQA training data;
- direct evaluation across five benchmark families.

Metrics:
- Success Rate for ALFWorld/SciWorld/BabyAI;
- Progress Rate for PDDL;
- LLM-as-a-Judge for HotpotQA;
- Memory Quality for LTM;
- prompt-token count;
- tool-use frequency.

Main results:
- Qwen2.5-7B AgeMem average: **41.96** vs no-memory **28.05**;
- Qwen3-4B AgeMem average: **54.31** vs no-memory **43.97**;
- gain over best compared memory baseline: **+4.82 pp** and **+8.57 pp** on the two backbones.

Memory Quality:
- Qwen2.5-7B: **0.533**;
- Qwen3-4B: **0.605**;
both highest among compared systems in the reported HotpotQA evaluation.

STM efficiency:
- Qwen2.5: ~2117 tokens vs 2186 with AgeMem-RAG, ~3.1% reduction;
- Qwen3: ~2191 vs 2310, ~5.1% reduction.

## Q7 — Data / artifact / reproducibility
Strengths:
- ACL 2026 peer review;
- official ACL Anthology paper;
- open-source official repository;
- explicit training/evaluation configs;
- two LLM backbones;
- five benchmark families;
- ablations for LTM, STM and RL;
- direct tool-call frequency analysis.

Tool-use behavior after GRPO is especially relevant:
- Qwen2.5 ADD: **0.92 → 1.64** calls/episode;
- Qwen2.5 UPDATE: ~0 → **0.13**;
- Qwen2.5 DELETE: ~0 → **0.08**;
- Qwen2.5 RETRIEVE: **2.31 → 1.95**;
- Qwen2.5 FILTER: **0.02 → 0.31**.

Qwen3 shows the same broad pattern, including non-zero UPDATE/DELETE.

Limitations:
- no phone hardware;
- no latency/energy/thermal measurement for the memory operations;
- vector-store/system implementation cost is not the research target;
- reward/training overhead is separate from deployment-time memory operation cost;
- benchmark memory actions may not match mobile GUI Agent duty cycles.

## Q8 — Evidence vs hypothesis
### [FACT]
Explicit memory lifecycle operations recur as learned Agent actions across a peer-reviewed independent system.

### [FACT]
RL changes the mix/frequency of ADD/UPDATE/DELETE/RETRIEVE/SUMMARY/FILTER and improves task/memory quality.

### [OBSERVATION]
Memory operation class and timing are semantically meaningful to Agent behavior.

### [INFERENCE — project]
H-PAM's operation-class recurrence gate is now passed by independent evidence.

### Not established
- that those operations create distinct smartphone CPU/NPU/DDR pressure;
- that lower layers need to know the semantic operation class;
- that API-level operation identity cannot already reconstruct the useful information;
- SYSTEM_VALUE on target phones;
- hardware/uArch insufficiency.

## Q9 — Real contribution to project decision
### H-PAM
**KEEP / NARROW; recurrence strengthened, system residual still missing.**

After MobiMem + AgeMem:
- `update/delete/retrieve` are clearly recurring Agent-memory operations;
- memory policy is adaptive rather than fixed;
- different memory operations affect task outcome.

But AgeMem also weakens a broad systems claim:
> the Agent/runtime already explicitly knows the operation type.

Therefore H-PAM cannot claim differentiation merely because lower layers need to identify whether an operation is `update`, `delete` or `retrieve`—the API/tool boundary may expose that cheaply.

Surviving question:
> Is there a recurring memory lifecycle fact **beyond ordinary memory API identity**—for example consolidation urgency, semantic replacement dependency, salience/age/confidence or foreground-recall criticality—that materially changes phone data placement/execution?

### A / B-residual
- AgeMem adds strong evidence that memory state can be revised/deleted;
- semantic validity/coherence still belongs to B-residual if the issue is stale derived state;
- no A score/lane change.

### C / hardware
No new differentiated system-control or hardware evidence.

## Q10 — Next action
1. KEEP PAPER-074 as P0 independent recurrence evidence.
2. Add canonical Claim that Agent-memory lifecycle actions recur across independent systems.
3. Update H-PAM: recurrence gate PASS; mobile-system-residual gate OPEN.
4. Do not promote H-PAM.
5. Next search must look for direct phone/system measurement of memory lifecycle operations, not another general Agent-memory algorithm paper.
6. Keep the MobiSys 2026 benchmark pending until full text is available.

## Decision footer
- **New-regime relevance:** DIRECT_AGENTIC
- **Evidence maturity:** SYSTEM_VALUE for Agent task/memory management; no mobile systems maturity
- **H-PAM impact:** KEEP / NARROW
- **recurrence gate:** PASS
- **mobile-system-residual gate:** OPEN
- **hardware impact:** none
- **Primary source:** https://aclanthology.org/2026.acl-long.981/
- **Artifact:** https://github.com/y1y5/AgeMem