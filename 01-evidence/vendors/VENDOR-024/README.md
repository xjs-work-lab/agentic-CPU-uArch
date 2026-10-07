+++
id = "VENDOR-024"
type = "SOURCE"
source_type = "vendor"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-08"
independence_assessment = "OFFICIAL_AOSP_PLATFORM_DOCUMENTATION"
title = "Android Context Hub Runtime Environment (CHRE) — always-on low-power nanoapp platform"
primary_url = "https://source.android.com/docs/core/interaction/contexthub"
priority = "P0"
evidence_role = "STRONG_ESTABLISHED_BASELINE / low-power context processing independent of application processor"
+++

# VENDOR-024 — Android Context Hub Runtime Environment (CHRE) — always-on low-power nanoapp platform

## Evidence summary
Android documents that the main applications processor (AP) is inefficient for frequent, short context events while screen-off; CHRE is a portable runtime for small trusted nanoapps on a lower-power processor.

Source identity preflight: canonical URL checked against VENDOR-001/005/006/017–023; no match. Independent evidence weight depends on underlying source, not Source ID.

See [deep.md](deep.md) for direct-reading 10Q and boundaries.
