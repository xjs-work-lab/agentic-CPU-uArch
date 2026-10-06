# TXN-20261006-FRONTIER-ROUND2-01 — Prior-art pressure test

## Question
Does the first-round H-SCL / second-Bet white space survive stronger mobile-Agent software, NPU, semantic-scheduler and cross-layer systems prior art?

## Sources completed with full 10Q
- PAPER-058 AutoDroid-V2 — MobiSys 2025
- PAPER-059 llm.npu — ASPLOS 2025
- PAPER-060 MUSched — OSDI 2026
- PAPER-061 Syrup — SOSP 2021

## Canonical objects created
- CLM-AGENT-005
- EC-A-006-A
- EC-CG06-004-B
- CLM-MOBILE-002
- EC-C-006-A
- CLM-C-006
- EC-C-007-A

## Decision Events created
- DEC-A-003 — AutoDroid-V2 baseline strengthening
- DEC-CG06-003 — llm.npu NPU-OPT lineage strengthening
- DEC-A-004 — MUSched semantic-scheduler baseline strengthening
- DEC-C-003 — MUSched G1 strengthening
- DEC-C-004 — Syrup cross-layer prior-art strengthening

## Direction / experiment changes
- A remains PRIMARY_BET / 82.5 / SIMULATION_SUPPORT; B4-TX strengthened.
- C remains STRATEGIC_ENABLER / second-Bet watch / 72; G1 strengthened.
- CG-06 remains INVEST / 86.5; EXP-CG06-001 now explicitly includes PAPER-059 and stronger NPU-OPT reconstruction.
- R3 remains BLOCKED.
- no new Direction created.

## H-SCL decision
H-SCL remains **analysis hypothesis only** and is narrowed hard.

Broad formulations killed/narrowed:
- semantic-to-program lowering — crowded by AutoDroid-V2;
- generic semantic-to-CPU-scheduler lowering — crowded by MUSched;
- portable user-defined cross-layer policy/control interface — crowded by Syrup.

Surviving question:
> automatic extraction of genuinely Agent-specific, cross-framework facts that produce incremental smartphone cross-resource value beyond B4-TX/G1.

## Evidence independence notes
- PAPER-058 and PAPER-056 share research-group lineage; do not count as independent replication.
- PAPER-059 and PAPER-057 share author/group lineage; use as trajectory/mechanism evidence.
- PAPER-060 production deployment evidence is vendor-reported; laboratory phone evaluation is separately peer-reviewed.
- PAPER-061 is independent academic prior art but server/KVS, not phone/Agent SYSTEM_VALUE.

## Next smallest useful step
Obtain and fully review **Interactive Context for Mobile OS Resource Management** before deciding whether H-SCL should remain separate, merge into A/C, or be killed as a second-Bet candidate.

If needed next:
WASH / Portable Performance on Asymmetric Multicore Processors for automatic runtime criticality inference.

## Progress toward final roadmap
This round does not add a Bet; it improves the roadmap by removing false novelty and making the evidence gate more discriminating.
