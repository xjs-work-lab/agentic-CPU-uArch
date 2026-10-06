+++
id = "EXP-R1-001"
type = "EXPERIMENT"
record_state = "CURRENT"
status = "SIMULATION_SUPPORT"
execution_state = "READY_FOR_PHONE_INPUTS"
title = "R1 strong-baseline post-ready timing break-even / kill test"
direction_ids = ["R1"]
tests_claim_ids = ["CLM-R1-EXP-001"]
input_source_ids = ["PAPER-047", "PAPER-048", "PATENT-005", "PATENT-017", "PATENT-018", "PATENT-019", "VENDOR-005", "TOOL-005", "TOOL-010", "TOOL-011"]
evidence_target = "SYSTEM_VALUE"
+++

# EXP-R1-001 — Strong-baseline post-ready timing kill test

- **B4-release:** strong generic workflow/mobile release scheduler.
- **B5:** perfect LatestUsefulResume/legal-window oracle.
- **B6-semantic:** B4 plus explicit Agent ReleasePermission / LatestUsefulResume / confidence.
- B6 gets no credit for timing already inferable by B4.

Reference 5% gate requires ~16.51% usable post-ready opportunity at GenericReleaseCapture 50%, ~33.02% at 75%, and ~82.54% at 90%; only 4/63 coarse cells pass at 90%.

Required phone inputs: UsablePostReadyOpportunityShare, GenericReleaseCapture vs B5, B6 incremental value, timing-window scale, late-release violation, and real energy/QoE/useful-progress conversion.

**Boundary:** no phone result is fabricated; no uArch promotion.

Exact frozen V1 experiment and pass-1 result are in [deep.md](deep.md).
