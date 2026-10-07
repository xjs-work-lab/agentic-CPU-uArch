# PAPER-083 — PORTAL: Fast and Secure Device Access with Arm CCA for Modern Arm Mobile SoCs

## Source
- IEEE Symposium on Security and Privacy 2025
- full author-hosted paper reviewed
- Prototype: Arm FVP + Orange Pi 5 Plus with Mali-G610 GPU
- Priority: P0 baseline

## Q1 — Problem + target mapping
Modern mobile SoCs integrate GPUs/NPUs/peripherals that need high-bandwidth shared-memory access.
Confidential Realm VMs need secure device I/O without turning every transfer into expensive encryption/decryption.

For confidential Agents, this directly pressure-tests the claim that protected heterogeneous execution requires a new Agent-specific hardware path.

## Q2 — Novelty / new-regime relevance
PORTAL exploits the integrated mobile-SoC threat model and CCA isolation:
- designated Realm VM + designated device share a protected plaintext region;
- GPC protects physical address-space ownership;
- SMMU stage-2 isolates device DMA;
- specialized Realm protects sensitive translation/control structures;
- memory encryption is avoided for the protected on-SoC path.

Classification:
**generic mobile confidential device-I/O mechanism**.

## Q3 — Falsifiable hypothesis
On integrated mobile SoCs, strict CCA/SMMU isolation can provide secure Realm-device I/O with lower cost than encrypting shared buffers.

Reported GPU experiments support this for selected workloads.

## Q4 — Research lineage / competing route
Alternatives/baselines:
- encrypted secure I/O;
- CCA CPU-only realms;
- accelerator TEEs;
- ACAI secure accelerator assignment.

PORTAL is particularly relevant because it explicitly targets modern Arm mobile SoCs.

## Q5 — Key mechanism / control point
### PORTAL region
Plaintext protected memory shared only by authorized Realm VM and device.

### GPC + SMMU
CPU-world access and device DMA are both constrained.

### Dynamic device management
Runtime device assignment/configuration is supported with protected control state.

## Q6 — Experiment design
Platforms:
- Arm Fixed Virtual Platform for CCA behavior;
- Orange Pi 5 Plus with Mali-G610 GPU.

Reported:
- ~9.8% one-time overhead for runtime device management;
- 1.07×–9.07× speedup over encryption-based secure I/O on selected Rodinia/data-intensive GPU workloads;
- average reported improvement around 3.71× across six selected GPU tasks.

## Q7 — Data / artifact / reproducibility
Strengths:
- IEEE S&P 2025;
- mobile-SoC-specific threat/model argument;
- integrated GPU prototype;
- explicit performance and security analysis.

Limitations:
- not actual CCA production silicon;
- Orange Pi is smartphone-adjacent, not commercial handset;
- GPU not NPU;
- no Agent workload;
- assumes integrated-package physical-attack properties for plaintext design.

## Q8 — Evidence vs hypothesis
### [FACT]
CCA/GPC/SMMU can be composed into a secure low-overhead Realm-device I/O path on the evaluated mobile-style platform.

### [OBSERVATION]
Protected accelerator/device access is generic confidential-computing territory.

### Not established
- dynamic Agent tool trust graph;
- NPU-specific smartphone measurements;
- Agent-specific secure data-flow policy.

## Q9 — Real contribution to project decision
**Strong baseline pressure.**

Removes broad novelty for:
- protected GPU/NPU/device access;
- secure shared buffers between realm and accelerator;
- avoiding encryption through mobile-SoC isolation.

An Agent security candidate must identify a control variable beyond ordinary Realm/device identity and access policy.

## Q10 — Next action
Use PORTAL with Aster/CAEC as strongest baseline before any confidential-Agent Direction.
Search only for task-dependent trust/resource graphs that create measurable phone value or overhead.

## Decision footer
- **Evidence maturity:** mobile-SoC SYSTEM_VALUE on prototype platform
- **Agent novelty impact:** negative baseline pressure
- **hardware impact:** existing CCA/GPC/SMMU mechanisms, not a new uArch Bet
- **Primary source:** https://doi.org/10.1109/SP61157.2025.00236