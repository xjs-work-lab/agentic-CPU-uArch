+++
id = "CG-01"
type = "DIRECTION"
record_state = "CURRENT"
title = "Flex Cache / heterogeneous shared-cache handoff"
direction_class = "COMPETITIVE_GAP"
competitive_action = "BENCHMARK"
score_context = 71.0
evidence_maturity = "PRODUCT_SIGNAL"
maturity_scope = "Qualcomm product architecture is public; Agent-specific phone locality residual beyond strong software and generic hardware baselines is not established."
strongest_baseline = "STRONG_SOFTWARE_LOCALITY_PLUS_GENERIC_SHARED_COHERENT_CACHE"
related_claims = ["CLM-CG01-001", "CLM-CG01-002", "CLM-CG01-003", "CLM-CG01-004", "CLM-CG01-EXP-001"]
related_capabilities = ["CAP-QUALCOMM-ORYON-FLEX-CACHE"]
+++

# CG-01 — Flex Cache / heterogeneous shared-cache handoff

## 30-second decision
**BENCHMARK / targeted adaptation study / 71.0**

Qualcomm Flex Cache is a real productized competitor architecture and a meaningful generic hardware locality baseline.

It is **not** a standalone shared-cache novelty Bet.

## Strategic question
Does representative Huawei smartphone Agent execution leave a material continuation-locality residual after:
- strong affinity/pooling/warm-core software;
- generic coherent/system cache;
- existing cache-aware migration/resource controls?

If yes, study adaptation/differentiation.

If not, use Flex Cache only as a benchmark/baseline.

## Why retained
- competitor productization increases confidence that cross-core working-set residency matters;
- Huawei equivalent productized mechanism is not publicly established in the reviewed set;
- team can measure CPU/cache/system locality.

## Why not a hardware program
- generic shared cache is mature/crowded;
- software locality can capture substantial value;
- direct phone Agent PMU residual is missing;
- copying Flex Cache is not assumed optimal.

## Next gate
`EXP-CG01-001`

No Agent-specific cache/uArch feature before generic capture is measured.
