+++
id = "CLM-SEC-003"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "BOUNDARY"
status = "SUPPORTED"
scope = "Arm CCA / Android protected-VM / inter-realm communication / secure mobile-device I/O substrate"
supersedes = []
+++

# CLM-SEC-003

## Proposition
Protected VM lifecycle/attestation/rollback, mutually attested confidential inter-VM shared memory, and secure Realm-to-device I/O are established generic Arm CCA / mobile confidential-computing mechanisms and cannot by themselves establish Agent-specific CPU/uArch differentiation.

## Evidence basis
- PAPER-081 / Aster — Android pVM lifecycle, launch policy, attestation, rollback and CCA-backed memory isolation;
- PAPER-082 / CAEC — dynamic mutually attested CSM create/share/attach/revoke/destroy and large-object sharing;
- PAPER-083 / PORTAL — mobile-SoC Realm/device protected plaintext I/O via GPC + SMMU.

## Boundary
These works use prototype/emulated CCA-era platforms and do not establish commercial smartphone-Agent economics.
They constrain **mechanism novelty**, not future workload importance.