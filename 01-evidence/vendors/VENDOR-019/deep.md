> Exact V1 vendor card copied from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.

# VENDOR-019 — MediaTek Dimensity 9600 Pro / Dedicated Always-On Agent AI Domain

## Metadata

| Field | Value |
|---|---|
| Vendor | MediaTek |
| Date | 2026-09-15 |
| Source type | product_page / press_release |
| Priority | P0 |
| Evidence role | COMPETITIVE_GAP / DIRECT_PRODUCT |
| Primary URL | https://www.mediatek.com/products/smartphones/mediatek-dimensity-9600-pro |
| Related official URLs | https://www.mediatek.com/press-room/mediatek-dimensity-9600-pro-sets-new-standard-for-flagship-smartphone-chips |
| Related candidates | CG-07; M4; A baseline; C |
| Strategic disposition | Adaptation / Differentiation candidate |
| Huawei public equivalent | Not established |

## Q1 — What exactly was officially released / documented?

**[PUBLIC_CAPABILITY]**
MediaTek Dimensity 9600 Pro publicly exposes:
- **dual-NPU architecture**;
- high-performance **NPU 1090**;
- **Super Efficient NPU 2.0**;
- Agentic AI Engine;
- AI Compute Fusion Architecture;
- Scheduling Engine 3.0;
- CPU/NPU/GPU/ISP system integration.

The low-power NPU is explicitly described as a dedicated always-on domain for background AI/Agent work.

## Q2 — What is the real technical mechanism?

The key mechanism is **compute-domain specialization by duty cycle**:

- NPU 1090 → heavy generative/Agentic workloads;
- Super Efficient NPU 2.0 → continuous/background/always-on Agent activity;
- system scheduling/fusion → coordinate CPU/NPU/power/memory behavior.

This is structurally different from using one high-performance accelerator for both bursty foreground and persistent low-duty work.

## Q3 — What problem / workload does MediaTek say it solves?

The source explicitly targets a smartphone where a personal AI assistant:
- stays active 24/7;
- observes/contextualizes;
- reasons;
- assists in real time;
- coexists with normal foreground mobile workloads.

The stated design problem is balancing responsiveness with power consumption.

## Q4 — What quantitative claims are made?

| Claim | Number / statement | Condition / comparison | Classification |
|---|---|---|---|
| Always-on AI power | 40% lower | Super Efficient NPU 2.0 vs predecessor | VENDOR_CLAIM |
| LLM prefill | +51% | NPU 1090 vs prior generation | VENDOR_CLAIM |
| Token generation per watt | +55% | vs prior generation | VENDOR_CLAIM |
| INT4 compute | 2× | vs prior generation | VENDOR_CLAIM |
| Model launch | +27% | AI Compute Fusion / scheduling statement | VENDOR_CLAIM |
| LLM token generation | +40% | scheduling/fusion statement | VENDOR_CLAIM |

These figures are vendor-reported.

## Q5 — Capability vs claim vs positioning

### PUBLIC_CAPABILITY
- dual NPU;
- dedicated Super Efficient NPU 2.0;
- NPU 1090;
- Agentic AI Engine;
- integrated scheduling/fusion architecture.

### VENDOR_CLAIM
- all performance/power percentages above.

### POSITIONING
- “agentic phone”;
- always-on proactive digital companion;
- multi-Agent concurrent experience.

## Q6 — Huawei public comparison

Equivalent Huawei smartphone architecture is **not publicly evidenced in the current source set** for:
- explicit high-performance + dedicated always-on Agent NPU split;
- dedicated background Agent AI domain.

Huawei public sources do show:
- on-device inference;
- Agent Framework;
- system QoS/resource control.

Those do not establish equivalence to this dual-domain NPU architecture.

## Q7 — Strategic disposition for Huawei

**Adaptation / Differentiation candidate — CG-07.**

This mechanism is important even if globally non-novel because it attacks the exact user problem:
> keep useful persistent Agent progress without visible battery/thermal/foreground penalty.

Potential Huawei routes:
- equivalent efficient AI domain;
- stronger shared-NPU power-gating/DVFS instead;
- CPU-resident small-model path;
- semantic progress control A + efficient execution-domain co-design.

## Q8 — Independent corroboration / contradiction

### Academic
Current project literature supports:
- persistent/background Agent workloads;
- heterogeneous mobile Agent orchestration;
- mobile accelerator efficiency constraints.

It does not independently validate Dimensity 9600 Pro's exact 40%/51%/55% figures.

### Patent / prior art
Always-on accelerators, heterogeneous scheduling and low-power AI are broadly crowded.

### Real-device / engineering
No independent 9600 Pro Agent-system benchmark is currently canonical.

## Q9 — Project decision impact

**Decision impact: New competitive-gap candidate / stronger A baseline.**

This source:
- creates CG-07;
- forces A/M4 to compare against a dedicated efficient execution-domain baseline;
- strengthens multi-domain Agent architecture thesis.

It does not:
- kill A;
- prove dual-NPU is the only solution;
- justify new Huawei silicon before workload economics are measured.

## Q10 — Next discriminating evidence

Measure:
1. persistent-Agent duty cycle;
2. accelerator wake/start cost;
3. residency/idle power;
4. foreground interference;
5. battery/thermal impact;
6. shared-NPU DVFS/power-gating baseline;
7. CPU-small-model baseline;
8. combined A semantic-progress + low-power-domain value.

## Evidence Triangle

| Dimension | Status |
|---|---|
| Official vendor evidence | Yes |
| Independent academic evidence | Partial |
| Patent / prior-art evidence | Yes |
| Real-device evidence | No |
| Huawei public comparison | Not established |

## Decision footer

- **Evidence role:** COMPETITIVE_GAP / DIRECT_PRODUCT
- **Source confidence:** High for product architecture disclosure; quantitative value remains vendor-reported
- **Independent corroboration:** Partial
- **Huawei public-equivalent status:** Not established
- **Strategic disposition:** Adaptation / Differentiation
- **Decision impact:** Create CG-07; strengthen persistent-Agent baseline
- **Open questions:** workload duty cycle; independent device data; Huawei equivalent; economics/IP
- **Primary URL:** https://www.mediatek.com/products/smartphones/mediatek-dimensity-9600-pro
