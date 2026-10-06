+++
id = "TOOL-011"
type = "SOURCE"
source_type = "tool"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Android AlarmManager"
primary_url = "https://developer.android.com/reference/android/app/AlarmManager"
priority = "UNSPECIFIED"
evidence_role = "generic mobile wakeup shifting / batching baseline"
origin_paths = ["references/evidence-index.md"]
origin_blobs = ["025f8297559be8d13fdc1f7418647c71aefd033c"]
+++

# TOOL-011 — Android AlarmManager

Official Android alarm surface where inexact alarms may be shifted/batched to reduce wakeups.

**Boundary:** generic coalescing; not proof of explicit Agent ReleasePermission value.
