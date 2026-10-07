# QA-EVIDENCE-RESCUE-R1A-PTA

Date: 2026-10-07
Scope: PT-A Evidence Rescue 1A deep audit.

## Revalidated decision-critical sources
- PAPER-037 ClawMobile
- PAPER-038 Beyond the GUI Paradigm
- PAPER-039 HybridCUA
- PAPER-040 PhoneHarness
- PAPER-042 UIAnchor

## New decision-critical evidence
- PAPER-101 — Mind the Gap / Action Rebinding / ACM CCS 2026
- PAPER-102 — VeriGUI / ACL 2026

## Canonical decision delta
PT-A remains:
- PLATFORM_TRACK
- 80.0
- SYSTEM_VALUE

PT-A is reframed around:
`capability/authority-aware routing → fresh context-bound actuation → OutcomeReceipt → verification → bounded recovery`.

Added:
- CLM-PTA-006
- CLM-PTA-EXP-002
- EXP-PTA-002
- DEC-PTA-RESCUE-001

No SOFTWARE_INSUFFICIENCY pass.
No hardware-specific cause.
No uArch candidate.

## QA
Initial run:
- `37611716486` — FAIL deterministic projection.
- Cause: projection omitted the newly added PAPER-102 premise edge from existing EC-PTA-003-B.
- Canonical source/evidence file was correct.

Final validation:
- run: `37611820867`
- job: `112760599058`
- validated head: `d091b6d142edfe1fbb6eb87ffefd08ccc9e951d7`
- result: PASS
- deterministic projection: PASS
- hard graph errors: 0
- graph: 383 nodes / 610 canonical semantic edges / 610 generated reverse edges
- whole-roadmap EDP warnings: 17
- squash merge: `e6a83b36494ec9bcc044b3aec6441152efd132f1`
- cleanup run: `37611888348`
- cleanup: PASS

## Next
Rescue-1B:
PAPER-013 / 015 / 043 / 044 / 050 for Candidate A.
