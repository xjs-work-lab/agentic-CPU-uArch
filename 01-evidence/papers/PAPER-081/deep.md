# PAPER-081 — Bringing Confidential Computing to Android (Aster)

## Source
- MobiSys 2026, 16 pages
- DOI: https://doi.org/10.1145/3745756.3809250
- Project: https://aster-cca.github.io/
- Scope: Android Virtualization Framework + Arm CCA
- Priority: P0 baseline

## Q1 — Problem + target mapping
Android AVF provides protected VMs but relies on a trusted hypervisor and MMU-based isolation.
Aster asks how AVF security requirements map onto Arm TEEs and how CCA can provide stronger hardware-backed pVM isolation.

For Agent research, Aster defines the strongest mobile baseline before claiming that an Agent needs a new protected execution primitive.

## Q2 — Novelty / new-regime relevance
Aster places Android in normal world and protected VMs in realm world and extends CCA integration with:
- stricter privilege separation;
- physical/in-memory protection;
- pVM launch policy;
- trusted boot / DICE attestation;
- rollback protection;
- lifecycle/failure management.

Classification:
**generic Android confidential-computing substrate**, not Agent-specific.

## Q3 — Falsifiable hypothesis
CCA can back Android pVMs while preserving AVF semantics and materially strengthening isolation at modest runtime cost.

The implementation/evaluation supports feasibility on available prototype platforms.

## Q4 — Research lineage / competing route
Baseline/related:
- Android AVF;
- trusted hypervisor pVMs;
- TrustZone;
- CCA realms;
- prior Aster design;
- confidential VM systems.

Important strongest-baseline implication:
Agent proposals get no novelty credit for ordinary pVM lifecycle, attestation, rollback or realm isolation.

## Q5 — Key mechanism / control point
### Realm-backed pVM lifecycle
Android can create/tear down pVMs on demand; Realm-Monitor mediates lifecycle and scheduling.

### Launch policy
Only signed/approved pVMs execute.

### Attestation
DICE chain binds firmware → Realm-Monitor → pVM measurements.

### Rollback / failure recovery
Persistent state/versioning and forced-shutdown recovery are handled explicitly.

### Memory isolation
CCA GPC/world separation and per-pVM protection strengthen isolation from Android/hypervisor.

## Q6 — Experiment design
Two prototypes:
- QEMU/Android functional environment;
- Arm board performance prototype capturing microarchitectural effects.

Tests include:
- boot / pVM lifecycle;
- RV8 CPU workloads;
- LMbench system/I/O;
- public-key generation, OTP, isolated compilation and AVF-related cases.

One reported board comparison shows ~2.70% average overall Aster overhead for realm-world execution; some pVM/boot setup steps incur larger one-time cryptographic/measurement cost.

## Q7 — Data / artifact / reproducibility
Strengths:
- MobiSys 2026;
- full Android/firmware/virtualization implementation;
- open project;
- lifecycle + attestation + rollback are implemented, not conceptual.

Limitations:
- no commercial CCA smartphone;
- performance board cannot run the exact Android configuration used in functional prototype;
- hardware encryption-context support is approximated where unavailable;
- no Agent workload.

## Q8 — Evidence vs hypothesis
### [FACT]
Generic Android pVM lifecycle/security can be mapped to CCA with low steady-state overhead in the evaluated prototype.

### [OBSERVATION]
Creation, teardown, attestation, rollback and failure recovery are not Agent-specific white space.

### Not established
- Agent trust graph;
- Agent-specific realm churn;
- confidential NPU execution;
- target commercial phone economics.

## Q9 — Real contribution to project decision
**Strong baseline pressure on any confidential-Agent candidate.**

Kills broad novelty for:
- 'Agent needs a protected VM';
- dynamic pVM launch/teardown;
- attestation;
- rollback;
- hardware-backed memory isolation.

## Q10 — Next action
Use Aster as required baseline for AgenTEE-class directions.
Only retain an Agent-specific residual if the trust-domain graph/resource sharing pattern is not adequately represented by generic pVM lifecycle.

## Decision footer
- **Evidence maturity:** mobile-system substrate SYSTEM_VALUE on prototype platforms
- **Agent novelty impact:** negative baseline pressure
- **Hardware impact:** CCA is existing architecture, not a new project Bet
- **Primary source:** https://doi.org/10.1145/3745756.3809250