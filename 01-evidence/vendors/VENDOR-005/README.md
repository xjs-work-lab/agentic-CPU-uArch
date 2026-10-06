+++
id = "VENDOR-005"
type = "SOURCE"
source_type = "vendor"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Huawei Function Flow Runtime Kit (FFRT)"
primary_url = "https://developer.huawei.com/consumer/cn/sdk/function-flow-runtime-kit"
priority = "P1"
evidence_role = "existing Huawei dependency/QoS/task scheduling/delay actuator baseline"
origin_paths = ["references/vendor-cards/huawei/VENDOR-005.md"]
origin_blobs = ["baafc322e9b6b1c72401d28161c652dc4d803137"]
venue = "Huawei developer documentation"
publisher_actor_ids = ["ACT-HUAWEI"]
+++

# VENDOR-005 — Huawei FFRT

Public FFRT exposes task/data dependencies, QoS-related execution, task/queue scheduling and delayed/event-driven execution.

For R1 this is a **strong existing actuator baseline**, not a new opportunity.

**Boundary:** public evidence does not establish Agent-native LatestUsefulResume / ReleasePermission end-to-end semantics.
