+++
id = "VENDOR-021"
type = "SOURCE"
source_type = "vendor"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
independence_assessment = "OFFICIAL_MICROSOFT_DOCUMENTATION"
title = "Windows Resume / Continuity SDK for Android-to-Windows task continuation"
primary_url = "https://learn.microsoft.com/en-us/windows/apps/develop/windows-integration/cross-device-resume"
priority = "P0"
evidence_role = "direct platform product baseline for Android-to-Windows activity-context continuation"
+++

# VENDOR-021 — Microsoft Windows Resume / Continuity SDK

## 30-second read
- Official Android→Windows continuity API.
- Android apps send/update/delete AppContext through Link to Windows.
- Windows resumes activity using that context.
- Resume is currently a Limited Access Feature.
- Confirms cross-device continuation as platform infrastructure.
- Transfers application activity context, not live Agent inference state.

See [deep.md](deep.md).
