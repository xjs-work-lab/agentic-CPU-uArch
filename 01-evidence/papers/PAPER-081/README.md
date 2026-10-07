+++
id = "PAPER-081"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "PRIOR_ART_BASELINE"
independence_assessment = "PEER_REVIEWED_MOBILE_SYSTEMS"
title = "Bringing Confidential Computing to Android"
primary_url = "https://doi.org/10.1145/3745756.3809250"
priority = "P0"
evidence_role = "strong Android/Arm CCA baseline for protected-VM lifecycle, launch policy, attestation, rollback and hardware-backed memory isolation"
authors = ["Mark Kuhne", "Supraja Sridhara", "Andrin Bertschi", "Nicolas Dutly", "Fabio Aliberti", "Srdjan Capkun", "Shweta Shinde"]
venue = "MobiSys 2026"
+++

# PAPER-081 — Aster / Bringing Confidential Computing to Android

## 30-second read
- **Why it matters:** Establishes a current mobile baseline for Android protected VMs backed by Arm CCA rather than a trusted hypervisor.
- **Mechanisms:** realm-world pVMs, stronger memory protection, independent lifecycle management, launch policy, DICE attestation, rollback protection, failure recovery and privilege separation.
- **Reported result:** lift-and-shift AVF apps; minimal application/runtime impact; board microbenchmarks report ~2.7% average Aster overhead in one realm-world comparison, with some boot/crypto setup costs.
- **Portfolio meaning:** generic Android confidential lifecycle is already occupied; Agent novelty cannot be realm creation/teardown/attestation/rollback itself.
- **Boundary:** evaluation uses emulator + Arm board because native commercial CCA phone hardware was unavailable.
- **Primary source:** https://doi.org/10.1145/3745756.3809250

See [deep.md](deep.md) for full Paper Insight 10Q.