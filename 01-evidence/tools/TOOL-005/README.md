+++
id = "TOOL-005"
type = "SOURCE"
source_type = "tool"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "OpenHarmony FFRT C API guideline"
primary_url = "https://gitcode.com/openharmony/docs/blob/master/en/application-dev/ffrt/ffrt-api-guideline-c.md"
priority = "UNSPECIFIED"
evidence_role = "FFRT delayed-task/dependency semantic caveat used to bound R1 actuator equivalence"
origin_paths = ["references/evidence-index.md", "07-experiments/l0-implementation-plan.md"]
origin_blobs = ["025f8297559be8d13fdc1f7418647c71aefd033c"]
+++

# TOOL-005 — OpenHarmony FFRT C API guideline

Frozen V1 preserves the caveat that a generic delay attribute cannot simply be treated as an equivalent dynamic DependencyReady-relative semantic release bound when dependencies are involved.

**Boundary:** implementation-equivalence constraint only; not R1 SYSTEM_VALUE.
