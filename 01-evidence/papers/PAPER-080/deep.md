# PAPER-080 — AgenTEE: Confidential LLM Agent Execution on Edge Devices

## Source
- EuroMLSys 2026
- DOI: https://doi.org/10.1145/3805621.3807660
- arXiv:2604.18231
- Platform: OpenCCA on Radxa Rock 5B
- Models: GPT2-Medium-q8_0 and Llama-3.2-1B-Instruct-Q4_0
- Agent workloads: chatbot and itinerary planner
- Priority: P0

## Q1 — Problem + target mapping
On-device Agents combine several assets and trust domains:
- Agent runtime / system prompt / orchestration logic;
- model weights and inference state such as KV cache;
- third-party applications and credentials;
- user/device data.

Unlike one conventional application, these components may be owned by mutually distrustful stakeholders.

Target mapping:
> future smartphone Agents may need hardware-backed composition of mutually distrustful Agent/model/tool providers while retaining low-latency local execution.

## Q2 — Novelty / new-regime relevance
AgenTEE decomposes the pipeline into separately attested confidential VMs (realms):
- Agent realm;
- model/inference realm;
- third-party application realms.

Communication uses CAEC Confidential Shared Memory rather than exposing plaintext to the normal-world OS/hypervisor.

Agent-specific workload novelty:
**multi-stakeholder Agent composition** and protection of runtime state/tool credentials.

Mechanism novelty is much narrower because CCA and CAEC are generic confidential-computing primitives.

## Q3 — Falsifiable hypothesis
If Agent components are isolated into mutually attested CCA realms and communicate through protected shared memory, the platform can protect assets from the host and from mutually distrustful providers at modest runtime cost.

Falsifiers:
- VM/realm switching or attestation dominates latency;
- shared-memory protection prevents efficient data movement;
- model memory duplication is prohibitive;
- secure accelerator access is unavailable;
- dynamic tool invocation requires realm lifecycle operations too frequently;
- ordinary Android pVM/process isolation is sufficient for the actual threat model.

Evaluated simple Agent pipelines support feasibility, not smartphone-scale completeness.

## Q4 — Research lineage / competing route
Strong baseline chain:
- Android AVF / protected VMs;
- Arm TrustZone;
- Arm CCA realms;
- Aster for Android pVM lifecycle/security;
- CAEC for mutually attested inter-realm shared memory;
- PORTAL / ACAI for protected device/accelerator access.

Thus AgenTEE should be read primarily as an Agent workload instantiation over an emerging confidential-computing stack.

## Q5 — Key mechanism / control point
### Trust-domain decomposition
Agent runtime, model and third-party services run in separate realms.

### Remote attestation + provisioning
Each owner validates its realm and only then provisions model/code/credentials.

### Confidential inter-realm communication
AgenTEE applies CAEC CSM and adds a lightweight user-space channel abstraction.

### Project interpretation
The possible new control object is not 'TEE for Agents'.
It would have to be:
> a **task-dependent Agent trust-domain graph** whose composition, communication and protected resource assignment change with tool/workflow execution.

The paper itself does not prove this needs a new lower-layer mechanism.

## Q6 — Experiment design
Three isolation modes:
- normal-world processes;
- normal-world VMs;
- AgenTEE realms.

Two agents × two models.

Representative end-to-end overhead:
- chatbot / GPT2-Medium: ~5.14% vs process, ~2.04% vs VM;
- chatbot / Llama-1B: ~4.23% vs process, ~1.63% vs VM;
- itinerary / GPT2-Medium: ~4.24% vs process, ~1.05% vs VM;
- itinerary / Llama-1B: ~4.08% vs process, ~2.52% vs VM.

## Q7 — Data / artifact / reproducibility
Strengths:
- peer-reviewed EuroMLSys 2026;
- public artifact/site;
- actual Arm CCA prototype stack;
- Agent-specific trust model;
- explicit latency comparison.

Limitations:
- no commercial Arm CCA hardware;
- Radxa Rock 5B prototype is not target smartphone;
- inference is CPU-bound and extremely slow relative to modern phone NPU paths;
- only two simple Agent workloads;
- normal-world user interface is trusted in the paper's model;
- microarchitectural side channels and physical attacks out of scope.

## Q8 — Evidence vs hypothesis
### [FACT]
Mutually distrustful Agent/model/application providers can be compartmentalized with CCA realms and protected shared memory on the evaluated prototype.

### [FACT]
Measured overhead is modest relative to process/VM baselines for the evaluated CPU-only Agent workloads.

### [OBSERVATION]
Agent pipelines create a richer trust-domain composition than a monolithic local inference service.

### [INFERENCE — project]
Confidential composition is a legitimate 2027–2029 smartphone workload dimension.

### Not established
- smartphone SYSTEM_VALUE;
- dynamic trust-graph churn;
- secure NPU/GPU path;
- incremental value over Aster/CAEC/PORTAL;
- differentiated CPU/uArch mechanism.

## Q9 — Real contribution to project decision
**KEEP as frontier seed / do not open Direction yet.**

It fills a coverage blind spot: security/isolation was absent from the current SSOT.

But it cannot become a second Bet merely because Agents need CCA:
- generic CCA provides realms;
- Aster provides Android pVM lifecycle;
- CAEC provides mutual attestation + confidential sharing;
- PORTAL/ACAI cover protected device access.

Only an Agent-specific residual such as highly dynamic trust-domain composition/resource assignment could remain.

## Q10 — Next action
1. KEEP as P0 frontier seed.
2. Pressure-test against Aster, CAEC and PORTAL.
3. Search for dynamic tool/app trust-domain switching and secure accelerator assignment in real Agent pipelines.
4. Do not create hardware work until smartphone SYSTEM_VALUE and generic CCA insufficiency are shown.

## Decision footer
- **New-regime relevance:** DIRECT_AGENTIC trust-domain composition
- **Evidence maturity:** prototype SYSTEM_VALUE / not smartphone SYSTEM_VALUE
- **Portfolio impact:** coverage seed only
- **Hardware impact:** none
- **Primary source:** https://arxiv.org/abs/2604.18231