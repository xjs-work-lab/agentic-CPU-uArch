# VENDOR-021 — Windows Resume / Continuity SDK — FULL_10Q

## Q1 — Capability
Microsoft provides Windows Resume / Continuity SDK for Android-to-Windows activity continuation.

## Q2 — Mechanism
Android initializes the SDK and sends, updates or deletes AppContext through Link to Windows.

## Q3 — State
AppContext carries metadata needed to identify and resume the activity on the target.

## Q4 — Lifecycle
Connection, disconnection, re-publication and access approval are explicit platform states.

## Q5 — T8 relevance
Direct product evidence that cross-device continuation is becoming OS/platform infrastructure.

## Q6 — Boundary
The transferred object is activity context, not CPU registers, KV cache, model runtime or live Agent execution state.

## Q7 — Product maturity
Official current documentation; Android SDK 24+ and Windows 11 prerequisites; feature is Limited Access.

## Q8 — Evidence
PUBLIC_CAPABILITY: Android→Windows AppContext continuity.
INFERENCE: T8 product trend is credible.
NOT ESTABLISHED: new phone CPU continuation mechanism.

## Q9 — Decision impact
Promote T8 product maturity while raising the platform baseline.

## Q10 — Next
Benchmark richer Agent continuation only where AppContext/task/checkpoint/KV baselines fail.

Primary: https://learn.microsoft.com/en-us/windows/apps/develop/windows-integration/cross-device-resume
