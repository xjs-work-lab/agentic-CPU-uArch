+++
id = "DR-CG07-STAGE16A-GAP"
type = "DISCOVERY_RUN"
lifecycle = "CLOSED"
as_of = "2026-10-05"
coverage_quality = "PARTIAL_RECONSTRUCTION"
scope = "CG-07 independent Dimensity 9600 Pro always-on power/wake validation + Huawei public-equivalent smartphone architecture"
origin_paths = ["analysis/stage16a/results/pass2-public-evidence-summary.md", "05-huawei-stack/competitive-gap-map.md", "references/vendor-cards/mediatek/VENDOR-019.md"]
limitations = "The complete historical query/corpus log is not retained. This object preserves only the documented V1 search result and public-evidence boundary."
+++

# DR-CG07-STAGE16A-GAP

## Purpose
Preserve the bounded public-evidence audit used to keep CG-07 at **EXPLORE / model-first**.

## Documented findings
The V1 audit found:
- official MediaTek dual-NPU / Super Efficient NPU 2.0 disclosure;
- MediaTek's vendor-reported 40% always-on AI power reduction;
- secondary reporting repeating vendor claims.

It did **not** locate independent public measurements for:
- dedicated-domain idle power;
- wake energy;
- wake latency;
- real background-Agent duty cycle;
- retail-phone always-on Agent battery/thermal behavior.

The reviewed Huawei public set also did not establish an equivalent smartphone high-performance + dedicated always-on Agent NPU split.

## Boundary
This run is `PARTIAL_RECONSTRUCTION`.

It does not prove:
- MediaTek's 40% claim is false;
- Huawei internally lacks an equivalent capability;
- a dedicated domain cannot win after real measurement.
