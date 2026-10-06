+++
id = "DR-HUAWEI-CG06-BASELINE"
type = "DISCOVERY_RUN"
lifecycle = "CLOSED"
as_of = "2026-10-05"
coverage_quality = "PARTIAL_RECONSTRUCTION"
scope = "Huawei smartphone CPU matrix-AI / CPU-resident Agent/local-AI public evidence"
origin_paths = ["05-huawei-stack/competitive-gap-map.md", "09-research-log/2026-10-05-stage15c-frontier-contradiction-competitive-gap.md", "07-experiments/stage15c-frontier-contradiction-gates.md", "references/vendor-cards/arm/VENDOR-018.md"]
limitations = "The full historical query/corpus log is not preserved. This object records only the documented V1 scope and boundary; it cannot establish internal absence."
+++

# DR-HUAWEI-CG06-BASELINE

## Purpose
Reconstruct the bounded public-evidence audit already recorded in V1 for CG-06.

## Documented scope
Compare the publicly evidenced Arm C2/SME2 smartphone CPU-local AI path with Huawei public smartphone CPU/AI capability evidence available to the project at the Stage15C/15D baseline.

## Documented result
V1 states that Huawei publicly exposes Kirin/Ascend on-device compute and Agent/OS directions, but an equivalent **smartphone CPU matrix-AI fast path was not publicly established in the reviewed source set**.

## Limitation
The complete historical query list and full corpus enumeration were not retained. Therefore this Discovery Run is explicitly `PARTIAL_RECONSTRUCTION`.

It supports only a bounded public-evidence Claim.

It does **not** support:
- "Huawei does not have this capability";
- "Huawei internally lacks an equivalent path";
- any inference beyond the recorded public-source boundary.
