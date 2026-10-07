+++
id = "VENDOR-020"
type = "SOURCE"
source_type = "vendor"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
independence_assessment = "OFFICIAL_ANDROID_PLATFORM_DOCUMENTATION"
title = "Android AppFunctions / Local Agent-callable App Functions"
primary_url = "https://developer.android.com/ai/appfunctions"
priority = "P0"
evidence_role = "DIRECT_PLATFORM_PRODUCT / T6 strongest native Android baseline"
+++

# VENDOR-020 — Android AppFunctions

## 30-second read
- Android 16+ provides platform + Jetpack AppFunctions APIs for exposing app functionality to Agent callers.
- Android acts as a function registry; authorized/system-privileged callers can discover metadata and execute functions locally.
- App declarations are turned into typed function/tool metadata and generated integration code.
- Function availability is governed by enabled state plus caller permissions/access level.
- AndroidX 1.0.0-alpha12, released 2026-09-23, adds experimental runtime registration APIs including registerAppFunction(s).
- Runtime registration binds callback implementations to platform-visible functions and has app-process/context lifecycle semantics.
- This strongly confirms **T6 product relevance**.
- It simultaneously raises the software/platform baseline: ordinary local Agent-tool registry, schema, permissions and execution are not differentiated CPU research.
- It does not establish arbitrary Agent-generated native/JIT code or a phone CPU code-cache/sandbox residual.
- Decision: T6 → EMERGING_PRODUCT_TREND / BENCHMARK_AND_PREPARE; no Direction/uArch candidate.

See [deep.md](deep.md).
