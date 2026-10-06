# VENDOR-005 — Huawei Function Flow Runtime Kit (FFRT)

## Metadata

| Field | Value |
|---|---|
| Vendor | Huawei / OpenHarmony |
| Date | Current public documentation; exact page publication date not verified |
| Source type | developer_doc |
| Priority | P1 |
| Primary URL | https://developer.huawei.com/consumer/cn/sdk/function-flow-runtime-kit |
| Related candidates | A/C1; C; R1 |
| Huawei public equivalent | Established |

## 1. Officially documented capability

**[PUBLIC_CAPABILITY]**
FFRT is Huawei's task-concurrency scheduling/runtime layer.

Current project evidence maps public FFRT capabilities to:
- task/data dependencies;
- QoS-related execution;
- task/queue scheduling;
- delayed/event-driven execution;
- external event integration.

## 2. Technical mechanism / interface

FFRT provides the generic task-graph/runtime substrate below higher-level application/Agent logic.

For this project it is a **strong existing actuator baseline**, not a new opportunity.

## 3. Project relevance

FFRT is central to:
- C1 D0→D1 lowering;
- Candidate A actuator sufficiency;
- R1 dependency-ready vs semantic-release distinction;
- C system-control instrumentation.

Any new Agent semantic mechanism must show what cannot already be translated into existing FFRT controls.

## 4. Important claims / boundaries

Do not infer that FFRT already carries:
- DemandState;
- LatestUsefulResume;
- Agent StateAffinity;
- Agent effect/commit meaning.

Those end-to-end semantics are not publicly established.

Also preserve the documented delayed-task/dependency semantic caveat already captured in the project's experiment layer.

## 5. Independent corroboration

- Huawei Agent Framework sources establish the layer above.
- Huawei Kernel Enhance/Gewu establishes adjacent/lower system controls.
- OpenHarmony FFRT C API documentation is used in Stage 12/15 experiments.

## 6. Huawei public comparison

This is the Huawei baseline itself.

The public gap question is:
> does Agent-native information add measurable value beyond translating into FFRT's existing task/dependency/QoS/event mechanisms?

## 7. Decision use / next action

**Decision impact:** strong generic baseline / existing Huawei control point.

Next:
- instrument Agent Framework→FFRT lowering;
- measure D0 software capture before proposing new D1 or hardware interfaces.

## Footer
- **Strategic disposition:** Existing Huawei baseline
- **Decision impact:** Raises software-sufficiency bar for A/C1/R1
- **Open questions:** semantic propagation and phone trace behavior
- **Primary URL:** https://developer.huawei.com/consumer/cn/sdk/function-flow-runtime-kit
