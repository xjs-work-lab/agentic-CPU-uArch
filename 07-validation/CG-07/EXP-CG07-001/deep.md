> Verbatim CG-07 excerpts from frozen V1 baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.

## Gate CG-07 — Dedicated Always-On Agent AI Domain

Question:
> Does a dedicated low-power always-on AI domain materially improve persistent Agent progress/energy/foreground QoE versus sharing a high-performance NPU/CPU?

Strong external product signal:
- MediaTek Dimensity 9600 Pro Super Efficient NPU 2.0 + NPU 1090 + Agentic AI Engine.

Strong baseline:
- shared NPU with strong power gating/DVFS;
- CPU/SLM path;
- semantic progress controller A;
- periodic/batched sensing;
- existing background scheduling.

Promotion:
- always-on Agent workload duty cycle is high;
- wake/start/residency overhead is material;
- dedicated domain provides clear battery/thermal/QoE value;
- CPU/NPU orchestration remains a Huawei-controllable system route.

This can become a competitive-gap engineering track even if it is not a globally novel Primary Bet.


## 4. CG-07 always-on-domain break-even

Question:
> When is a dedicated low-power AI domain more energy-efficient than waking a shared high-performance NPU?

Per-window model:

```text
DedicatedEnergy =
T × P_dedicated_idle
+ N_events × active_time × (P_dedicated_active - P_dedicated_idle)

SharedEnergy =
N_events × (
  wake_energy
  + active_time × P_shared_active
)
```

Optional batching reduces effective wake count.

Tool:
`analysis/stage16a/cg07_always_on_break_even.py`

Primary outputs:
- break-even events/hour;
- break-even duty cycle;
- sensitivity to dedicated idle power, wake energy and event duration.

Synthetic values are only design-space examples.

---


## CG-07 — Dedicated Always-On Agent AI Domain

### Minimum workload measurements
- events/hour
- active duration/event
- batchability / effective wakes
- duty cycle
- model/stage type

### Shared-domain baseline
- wake energy
- wake latency
- active power
- idle/residency behavior
- batching policy

### Dedicated-domain candidate
- idle power
- active power
- wake behavior if applicable
- sustained thermal behavior

### Product outputs
- useful background progress
- foreground interference
- battery/energy
- thermal

### Derived outputs
- break-even events/hour
- break-even duty cycle
- energy delta
- sensitivity to batching/wake frequency

### Promotion gate
Dedicated domain beats strong shared-domain + batching/power-management baseline on representative persistent-Agent workloads.

---


## 5. CG-07 always-on-domain break-even

Synthetic reference:
- dedicated idle = 20 mW;
- dedicated active = 200 mW;
- shared active = 700 mW;
- shared wake energy = 8 mJ;
- one wake/event;
- one-hour observation window.

Break-even event rate:

| Active duration/event | Dedicated domain wins above ~ |
|---:|---:|
| 5 ms | 6792 events/hour ≈ 1.89/s |
| 20 ms | 3913 events/hour ≈ 1.09/s |
| 100 ms | 1200 events/hour ≈ 0.33/s |

Sensitivity already shows:
- dedicated idle power is first-order;
- shared-NPU wake energy is first-order;
- event duration/duty cycle is first-order.

For example, lowering dedicated idle from 20 mW to 5 mW reduces the 20 ms / 8 mJ break-even from ~1.09 events/s to ~0.28 events/s in the same synthetic model.

**Decision impact:** CG-07 should be decided from duty/wake/residency economics, not the existence of a dual-NPU product alone.

---


## 4. CG-07 — no independent public power dataset found

Targeted search found:
- MediaTek official dual-NPU / Super Efficient NPU 2.0 disclosure;
- vendor-reported 40% always-on AI power reduction;
- secondary articles repeating MediaTek claims.

No independent public measurement was found for:
- dedicated-domain idle power;
- wake energy;
- wake latency;
- real background-Agent event duty cycle;
- retail-phone always-on Agent battery/thermal behavior.

### Decision
**CG-07 remains EXPLORE / model-first.**

Do not turn the vendor 40% claim into a measured model parameter.

---



## V2.2 Frontier Round 10 update — proactive gating residual

PAPER-087 ProactiveMobile and PAPER-088 PRPF change the strongest-baseline model without changing the CG-07 score.

### New workload abstraction
`context observation → intervene/no-intervene gate → accepted subset → heavy reasoner`

Raw context-arrival rate is therefore not equivalent to heavy-reasoner duty cycle.

### Architecture residual
A dedicated low-power domain can only claim value on the residual after a strong lightweight gate. The key comparison is strongest CPU/shared-NPU/small-model front-end gate versus dedicated always-on front-end gate, with accepted-event handoff/wake cost and dedicated idle power included.

### Decision
**CG-07 remains EXPLORE / 75.0.**

Workload relevance is strengthened, but architecture necessity is narrowed. The original V1 direct-event model above remains as provenance; current `model.py` adds the V2.2 post-gating residual model while retaining the legacy function.
