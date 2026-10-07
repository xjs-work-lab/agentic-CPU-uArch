# Frontier Round 10 — Proactive Mobile Agent Gating / CG-07 Residual — 2026-10-07

## Decision question
Does proactive mobile Agent execution expose a new differentiated second-Bet direction, or does it primarily refine the CG-07 always-on-domain question?

## FULL_10Q sources
- PAPER-087 — ProactiveMobile — CVPR 2026
- PAPER-088 — PRPF / Perceive Before Reasoning — 2026 preprint

## Structural signal
PAPER-087 makes proactive assistance a structural mobile Agent workload:
`ongoing context → decide whether to intervene → infer latent intent → emit executable function(s)`.

The critical new property is selective intervention under continuous/recurring context.

## Strongest software/model baseline
PAPER-088 directly attacks the naïve premise that each context update must invoke a heavy reasoner.

PRPF separates lightweight perception, intervene/no-intervene gating, candidate-function compression and heavy reasoning only for accepted observations.

Reported on ProactiveMobile versus its 7B baseline:
- Success Rate 20.82% → 41.15%;
- False Trigger Rate 13.76% → 7.21%;
- expected inference compute −69.3%;
- end-to-end latency −60.1%.

Boundary: benchmark/GPU results, not phone battery/rail/thermal measurements.

## Residual mechanism
The architecture residual becomes:
`context observation → lightweight gate → accepted subset → heavy-domain handoff/wake → heavy reasoning`.

A dedicated always-on domain can only add value through residual variables such as dedicated idle power, gate energy/latency, context-arrival rate, acceptance rate, handoff/wake cost, batching/residency, gate quality and product QoE/thermal effects.

## Decision
**NO NEW DIRECTION.**

Proactive intervention gating is both a strong workload premise for CG-07 and a stronger software/model baseline against CG-07.

### CG-07 impact
**NARROW / RAISE BASELINE / NO SCORE CHANGE.**

CG-07 remains **EXPLORE / 75.0**.

## Experiment consequence
EXP-CG07-001 is upgraded from a direct-event break-even model to a post-gating residual model.

Required measured inputs now include context observations/hour, acceptance rate, baseline gate energy/latency, dedicated idle + gate active power, accepted-event handoff/wake cost, and battery/thermal/foreground QoE.

## Portfolio impact
- A / PT-A / C / CG-06 — unchanged;
- CG-07 — workload definition strengthened, strongest baseline raised, 75.0 unchanged;
- second differentiated Primary Bet — still unfilled;
- uArch Primary Bet — none.

## Next
Continue frontier reset outside generic scheduling/system control, persistent Agent memory, confidential execution/isolation, proactive/always-on intervention gating, and already-owned lanes.
