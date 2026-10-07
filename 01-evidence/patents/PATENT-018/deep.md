# PATENT-018 — Task Allocation Method and Task Allocation Device — direct-claim audit

## Source
- JP2007140710A
- Primary: https://patents.google.com/patent/JP2007140710A/en

## Direct-claim result
Claim 1 directly recites:
- acquiring predecessor/dependency relationships;
- acquiring task time constraints;
- calculating earliest start time;
- calculating latest start time that still completes within the time constraint;
- calculating a task movable range from earliest/latest start difference;
- determining allocation destination in order from smaller movable range.

Dependent claims include communication-time effects and node-assignment details.

## Project decision
This is a clean direct-claim anchor for generic DAG/time-constraint earliest/latest-start/slack scheduling.

It does not claim:
- Agent semantic ReleasePermission;
- LatestUsefulResume derived from task meaning;
- post-ready phone energy/QoE value.

No FTO/legal conclusion.
