# Decision Backtrace Audit — Rescue state

Date: 2026-10-07
Method: roadmap → direction → claim → evidence case → source → mechanism/experiment

## A — Agent Semantic Progress Control
Current decision: PRIMARY_BET / 82.5 / SIMULATION_SUPPORT.

Outstanding depth risk:
PAPER-013 / 015 / 043 / 044 / 050 remain pre-EDP-depth sources.

Therefore A is **not yet depth-clean**.

## PT-A — Heterogeneous Verified Agent Actuation Runtime
Current decision: PLATFORM_TRACK / 80.0 / SYSTEM_VALUE.

### Rescue-1A backtrace result
PT-A survives, but its control contract is reframed.

Previous shorthand:
> heterogeneous GUI/API/CLI/tool routing + verification/recovery

Current evidence-supported formulation:
> **capability/authority-aware routing → bounded actuation → fresh target/context binding → OutcomeReceipt → action-effect verification → bounded recovery**

### Why this changed
- PAPER-038: structured surfaces matter, but ADB/benchmark privileges make authority/entitlement part of the real control point.
- PAPER-039: naive GUI+CLI access can materially worsen accuracy; selective routing is a learned/software baseline.
- PAPER-040: mixed-action value is real but not attributable solely to verification.
- PAPER-042: complete UIAnchor system is strong; component attribution remains bounded.
- PAPER-102: verification/recovery has causal software value.
- PAPER-101: observation→action TOCTOU shows post-action verification alone does not prove intended-target delivery.

### PT-A decision
KEEP:
- PLATFORM_TRACK
- 80.0
- SYSTEM_VALUE

No promotion:
- SOFTWARE_INSUFFICIENCY not passed.
- context-bound actuation is first an OS/runtime hypothesis.
- no CPU/uArch candidate.

New discriminating test:
- `EXP-PTA-002` compares post-action-only verification with fresh-context and stronger target-bound execution.

## C — Efficient System-Control Substrate
STRATEGIC_ENABLER / 72.0 / SYSTEM_VALUE.
Round-1 revalidation unchanged.

## CG-06 — CPU-Resident Latency-Critical Agent AI Fast Path
INVEST / 86.5 / STRUCTURAL_SIGNAL.
Round-1 revalidation unchanged; strongest NPU/HETERO baseline remains mandatory.

## CG-07 — Always-On Agent AI
EXPLORE / 75.0.
Paper-depth clean for PAPER-087/088; vendor/source-type audit later.

## Current portfolio result
No lane or score changes from Rescue-1A.

The meaningful change is **PT-A REFRAME**, recorded by `DEC-PTA-RESCUE-001`.

## Whole-roadmap caveat
Five primary-lane paper warnings remain, all in A.
Twelve reserve-lane paper warnings remain.

Do not claim the entire portfolio is evidence-depth clean yet.

## Next
Rescue-1B A, then rerun this backtrace before Frontier Round 14.
