# PAPER-082 — CAEC: Confidential, Attestable, and Efficient Inter-CVM Communication with Arm CCA

## Source
- EuroS&P 2026
- arXiv:2512.01594
- Project: https://caec-paper.github.io/
- Scope: generic Arm CCA inter-realm communication/data sharing
- Priority: P0 baseline

## Q1 — Problem + target mapping
Standard confidential VMs isolate memory from both hypervisor and peer VMs, forcing confidential inter-CVM communication through hypervisor-visible buffers plus encryption.

For Agent pipelines, this appears directly relevant because model/runtime/tool components may occupy different trust domains.

## Q2 — Novelty / new-regime relevance
CAEC adds Confidential Shared Memory (CSM) to CCA:
- protected from hypervisor and non-participants;
- shareable among mutually attested realms;
- dynamically creatable/attachable/revocable;
- per-participant permissions;
- compatible with existing CCA hardware.

Classification:
**generic confidential multi-component composition**, not Agent-native.

## Q3 — Falsifiable hypothesis
Protected shared pages and attested realm identity can eliminate expensive per-message encryption while preserving CCA isolation.

The evaluation strongly supports this in the tested environment.

## Q4 — Research lineage / competing route
Alternatives:
- encrypt every message in hypervisor-visible shared memory;
- ordinary CCA private realms;
- network/TLS channels;
- duplicate large objects such as models per realm.

CAEC attacks the generic substrate directly.

## Q5 — Key mechanism / control point
### Attestable realm identity
RMM creates system-wide identifiers cryptographically bound into attestation tokens.

### CSM lifecycle
- create;
- mutually consented share/attach;
- permissions;
- revoke;
- detach;
- destroy.

### Protected sharing
RMM maps the same protected physical pages into participating realm address spaces while excluding the hypervisor and other realms.

## Q6 — Experiment design
Communication compares:
- plaintext normal-world shared memory;
- OpenSSL-encrypted shared memory;
- MbedTLS-encrypted shared memory;
- CSM.

Reported ranges vs OpenSSL:
- ~24–212× lower latency;
- ~25–209× fewer CPU cycles;
- ~26–204× higher throughput.

Large-object sharing:
- GPT-2 / GPT-2 Medium across 2–3 realms;
- overall memory reduction ~16.6–28.3%;
- tested inference latency is effectively unchanged when model pages live in CSM.

## Q7 — Data / artifact / reproducibility
Strengths:
- EuroS&P 2026;
- explicit security model;
- open project/artifact;
- communication + large-model-sharing evaluation;
- no hardware change required beyond CCA.

Limitations:
- prototype CCA platforms;
- not Android smartphone;
- not an Agent workload;
- side-channel/physical assumptions bounded by CCA threat model.

## Q8 — Evidence vs hypothesis
### [FACT]
Mutually attested realms can dynamically share protected memory with very low communication overhead and explicit lifecycle control.

### [FACT]
Large read-only objects such as LLM weights can be shared across realms without duplicate physical copies in the tested system.

### [OBSERVATION]
Multi-party confidential communication and resource sharing are not Agent-specific substrate gaps.

## Q9 — Real contribution to project decision
**Strongest baseline against an AgenTEE-derived second Bet.**

CAEC removes broad white space for:
- realm-to-realm confidential channels;
- mutual attestation;
- dynamic protected sharing/revocation;
- shared model-memory efficiency.

Any Agent residual must be about the **policy/dynamics of trust-domain composition**, not the mechanism of protected communication itself.

## Q10 — Next action
Use CAEC as mandatory baseline.
Search whether real Agent workflows cause frequent, task-dependent trust graph changes whose costs/security requirements are not served by generic CSM + pVM lifecycle.

## Decision footer
- **Evidence maturity:** SYSTEM_VALUE in generic CCA prototype scope
- **Agent novelty impact:** strong negative baseline pressure
- **Hardware impact:** none beyond existing CCA substrate
- **Primary source:** https://arxiv.org/abs/2512.01594