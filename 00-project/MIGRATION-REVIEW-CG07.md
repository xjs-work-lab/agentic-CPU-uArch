# CG-07 V2.2 Migration — Independent Review

Updated: 2026-10-06  
Authority: review record only

## Review question

Does the CG-07 slice preserve the difference between:
- public product architecture;
- vendor quantitative claims;
- synthetic break-even analysis;
- independent SYSTEM_VALUE?

## Verdict

**GO**

No authority cutover.

## Product architecture

PASS.

VENDOR-019 correctly supports the narrow statement that MediaTek publicly exposes:
- dual NPU;
- Super Efficient NPU 2.0;
- dedicated always-on background Agent/AI domain.

A MediaTek Actor and reusable Capability are created.

## Vendor power claim

PASS.

The 40% lower always-on AI power number is represented as:
`SOURCE_CLAIM`.

It is not:
- FACT;
- independent measurement;
- SYSTEM_VALUE;
- a measured Stage16A model parameter.

## Synthetic model

PASS.

The Stage16A model is preserved as an Experiment with:
- status SIMULATION_SUPPORT;
- exact model script;
- explicit synthetic parameters;
- explicit real-measurement promotion gate.

The corresponding Claim is only:
"these parameters control the synthetic break-even surface."

It does not say:
"CG-07 saves battery on a real phone."

## Independent-validation boundary

PASS.

The lack of public idle/wake/duty-cycle/battery-thermal data is encoded through:
Discovery Run → BOUNDARY Claim.

Missing graph edges are not used as absence evidence.

## Huawei gap

PASS.

Huawei comparison remains:
"equivalent public smartphone architecture not established in the reviewed source set."

No internal-absence Capability or Claim is created.

## Strategic state

PASS.

CG-07 remains:
- 75.0
- EXPLORE
- architecture benchmark / co-design study

It is not promoted to:
- INVEST;
- Primary Bet;
- silicon commitment.

## Strong baseline

PASS.

Direction/Experiment text retains:
- shared NPU DVFS/power gating;
- batching;
- CPU/small-model path;
- A semantic progress control;
- existing background scheduling.

Thus dedicated hardware must beat a serious alternative baseline.

## Graph QA

PASS.

Run:
`37459438555`

Result:
- 103 canonical nodes
- 162 canonical semantic edges
- 162 generated reverse edges
- 0 hard errors
- 20 accepted independence-UNKNOWN warnings

## Remaining evidence gap

Real decision still requires:
- event rate/duty cycle;
- wake energy/latency;
- dedicated idle/active power;
- shared-domain power/residency;
- batching sensitivity;
- battery/thermal/foreground QoE.

This missing data is accurately visible.

## Decision

**GO — merge CG-07.**

Next recommended slice:
**CG-01 — Flex Cache / heterogeneous shared-cache handoff**, before R2 so locality evidence can be reused without conflating strategic state.
