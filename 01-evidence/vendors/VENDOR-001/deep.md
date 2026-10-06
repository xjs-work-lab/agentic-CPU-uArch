> Exact V1 vendor card copied from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.

# VENDOR-001 — Qualcomm Oryon CPU / Flex Cache

## Metadata

| Field | Value |
|---|---|
| Vendor | Qualcomm Technologies |
| Date | 2026-08-25 |
| Source type | technical_blog / product architecture disclosure |
| Priority | P0 |
| Evidence role | COMPETITIVE_GAP / BOUNDARY_BASELINE |
| Primary URL | https://www.qualcomm.com/news/onq/2026/08/oryon-cpu-5ghz-flexcache |
| Related candidates | CG-01; R2; M3 |
| Strategic disposition | Adaptation / Differentiation candidate |
| Huawei public equivalent | Not established |

## Q1 — What exactly was officially released / documented?

**[PUBLIC_CAPABILITY]**
Qualcomm disclosed a next-generation Oryon mobile CPU with:
- 5 GHz peak CPU frequency;
- a new **Flex Cache** architecture;
- heterogeneous CPU cores able to access one dynamically allocated cache pool.

The post explicitly presents this as part of the next premium Snapdragon mobile platform.

## Q2 — What is the real technical mechanism?

The important mechanism is not the 5 GHz headline.

Flex Cache changes the cache-sharing model:
- heterogeneous cores draw from a common cache pool;
- capacity is dynamically allocated by workload;
- larger working sets can remain resident;
- work can move across cores without forcing every handoff to start from a cold private-cache footprint.

For this project, the control point is:
> **cross-core continuation locality / shared working-set residency**.

## Q3 — What problem / workload does Qualcomm say it solves?

Qualcomm maps the mechanism to:
- multi-step Agentic AI;
- core handoff;
- gaming;
- multitasking;
- video editing;
- memory-pressure-sensitive large working sets.

**[POSITIONING]**
The Agentic framing is that a request becomes a multi-step plan that migrates across cores.

## Q4 — What quantitative claims are made?

| Claim | Number / statement | Condition / comparison | Classification |
|---|---|---|---|
| CPU frequency | first mobile CPU at 5 GHz | next-generation Oryon | VENDOR_CLAIM |
| Working-set behavior | larger working sets remain resident rather than spill | Flex Cache description | VENDOR_CLAIM / mechanism rationale |
| Agent handoff value | shared cache avoids cold handoff across cores | qualitative | POSITIONING |

No independent Flex-Cache Agent benchmark is supplied in this source.

## Q5 — Capability vs claim vs positioning

### PUBLIC_CAPABILITY
- Flex Cache exists in the disclosed product architecture.
- heterogeneous cores share a dynamically allocated cache pool.

### VENDOR_CLAIM
- performance/locality benefits described by Qualcomm;
- 5 GHz / fastest-mobile-CPU positioning.

### POSITIONING
- Agentic workloads are a key motivating use case.

## Q6 — Huawei public comparison

Huawei public evidence in this project includes:
- cache-aware task migration;
- heterogeneous resource scheduling;
- shared-resource-interference-aware migration patents/mechanisms.

However, an equivalent **productized flexible shared cache pool across heterogeneous mobile CPU cores** is **not publicly evidenced in the current Huawei source set**.

This is not proof of internal absence.

## Q7 — Strategic disposition for Huawei

**Adaptation / Differentiation candidate.**

Reason:
- generic shared cache is not globally novel;
- Qualcomm productization increases confidence that cross-core locality is a real design concern;
- Huawei may need either a similar mechanism or a different way to solve the same handoff/locality problem.

Do not assume that copying Flex Cache is the optimal Huawei answer.

## Q8 — Independent corroboration / contradiction

### Academic
- PAPER-008: Agentic workflows can create high context-switch/locality pressure.
- PAPER-049: strong software affinity/locality policies recover substantial value in production.

### Patent / prior art
- PATENT-023: Huawei cache-aware task migration.
- PATENT-024: Qualcomm cache-demand-aware heterogeneous scheduling.
- generic shared cache / locality mechanisms are heavily crowded.

### Real-device / engineering
No independent phone Agent benchmark of Flex Cache is currently in the project.

## Q9 — Project decision impact

**Decision impact:**
- **Kill broad shared-cache novelty claim.**
- **Keep CG-01 as competitive-gap / adaptation route.**
- strengthen R2 generic-hardware baseline.

This source does **not** prove:
- that Huawei lacks an equivalent internal mechanism;
- that Flex Cache gives ≥5% Agent-specific value;
- that an Agent-specific cache/uArch feature is needed.

## Q10 — Next discriminating evidence

1. target-phone PMU continuation-locality traces;
2. compare default vs strong affinity/pooling/warm-core policies;
3. determine whether generic coherent/system cache already removes most value;
4. inspect Huawei public CPU/cache topology when disclosed;
5. patent/IP review before proposing a similar architecture.

## Evidence Triangle

| Dimension | Status |
|---|---|
| Official vendor evidence | Yes |
| Independent academic evidence | Partial |
| Patent / prior-art evidence | Yes |
| Real-device evidence | No |
| Huawei public comparison | Partial / not established |

## Decision footer

- **Evidence role:** COMPETITIVE_GAP / BOUNDARY_BASELINE
- **Source confidence:** High for disclosed Qualcomm capability; medium/low for claimed Agent value
- **Independent corroboration:** Partial
- **Huawei public-equivalent status:** Not established
- **Strategic disposition:** Adaptation / Differentiation
- **Decision impact:** Retain CG-01; no Primary-Bet/uArch promotion
- **Open questions:** phone Agent locality magnitude; software capture; Huawei equivalent; IP path
- **Primary URL:** https://www.qualcomm.com/news/onq/2026/08/oryon-cpu-5ghz-flexcache
