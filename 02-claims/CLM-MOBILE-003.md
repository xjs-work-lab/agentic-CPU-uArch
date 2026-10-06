+++
id = "CLM-MOBILE-003"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "personalized smartphone background-activity usefulness and suppression"
supersedes = []
+++

# CLM-MOBILE-003

## Proposition
A smartphone OS can infer a personalized usefulness proxy for app background activity from user/app history and use it to suppress low-value background work, reducing energy while bounding user-visible staleness in evaluated mobile systems.

## Evidence
PAPER-067 / HUSH (MobiCom 2015).

## Boundary
Background app/screen-off scope on legacy Galaxy phones.
This does not establish:
- Agent-internal semantic progress value;
- active foreground CPU/NPU/memory contention;
- modern mobile-Agent transfer;
- hardware/uArch need.