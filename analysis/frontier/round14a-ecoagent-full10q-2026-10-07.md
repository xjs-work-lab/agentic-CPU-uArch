# Round 14-A — EcoAgent FULL_10Q result

Date: 2026-10-07
Source: PAPER-105
State: COMPLETE

## Core result
EcoAgent strengthens **T3/PT-A product relevance** more than T7 differentiation.

Its causal ablation shows value from:
1. adding cloud planning;
2. adding local observation/verification;
3. transmitting compact semantic state for replanning.

The “device-side” models are hosted on RTX 3090 to simulate mobile inference, so the paper does not provide phone-SoC multi-Agent contention evidence.

## Important correction
EcoAgent should not be summarized as “matching the best cloud agents.”

Reported SR:
- EcoAgent: 25.6–27.6%;
- M3A: 28.4%;
- Agent S2: 54.3%;
- V-Droid: 59.5%.

Its differentiator is operational efficiency and closed-loop placement, not best task success.

## T3
Strengthened, no maturity/posture change.

## T7
Final negative discriminator for standalone differentiation.

No new local CPU/NPU control point is isolated.

See `round14a-t7-final-decision-2026-10-07.md`.
