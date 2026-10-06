> V1 semantic source copied from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.
> The compact README owns the V2.2 Source metadata.

# VENDOR-006 — Huawei Kernel Enhance Kit / Gewu

## Metadata

| Field | Value |
|---|---|
| Vendor | Huawei |
| Date | Current public documentation; exact page publication date not verified |
| Source type | developer_doc |
| Priority | P1 |
| Primary URL | https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/kernel-enhance-overview |
| Related candidates | A/C1; C; M4; CPU-NPU control |
| Huawei public equivalent | Established |

## 1. Officially documented capability

**[PUBLIC_CAPABILITY]**
The Huawei public stack exposes Kernel Enhance capabilities used in this project as evidence for:
- thread/task QoS control;
- system resource management;
- on-device inference/resource integration through Gewu-related mechanisms.

## 2. Technical mechanism / interface

This layer is the lower system-control/AI-runtime baseline beneath Agent/runtime semantics.

Conceptually:
> task/runtime intent → kernel/resource/inference control → CPU/NPU/memory behavior.

## 3. Project relevance

VENDOR-006 is a critical baseline for:
- D1 actuator sufficiency;
- foreground/background resource control;
- inference request/resource control;
- C Efficient System-Control Substrate.

It means the project should not invent generic QoS/resource primitives that Huawei already exposes.

## 4. Important claims / boundaries

Public documentation does **not by itself establish**:
- automatic DemandState propagation;
- Agent commit/effect propagation;
- semantic ReleasePermission;
- Agent-specific CPU/NPU cache/locality policy.

The capability is a control surface, not proof of Agent-native semantics.

## 5. Independent corroboration

Related public Huawei evidence:
- VENDOR-005 FFRT;
- VENDOR-013 Agent Framework 2.0;
- Huawei tooling/trace sources.

## 6. Huawei public comparison

This is an existing Huawei actuator baseline.

The research residual is:
> what new information changes lower resource decisions beyond existing QoS/inference controls?

## 7. Decision use / next action

**Decision impact:** Kill generic missing-control-surface claims; keep semantic-information residual.

Next:
- map actual phone Agent control path;
- quantify host/control/inference overhead before promoting C/D1.

## Footer
- **Strategic disposition:** Existing Huawei baseline
- **Decision impact:** Strong software/system sufficiency baseline
- **Open questions:** exact Agent→Gewu/kernel semantic path; target-device residual
- **Primary URL:** https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/kernel-enhance-overview
