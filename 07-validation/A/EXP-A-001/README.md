+++
id = "EXP-A-001"
type = "EXPERIMENT"
record_state = "CURRENT"
status = "READY"
title = "A matched-observability DemandState residual test"
direction_ids = ["A"]
tests_claim_ids = ["CLM-A-001"]
input_source_ids = ["PAPER-013", "PAPER-015", "PAPER-117", "PAPER-043", "PAPER-044", "PAPER-050", "PAPER-056", "PAPER-058", "PAPER-060", "PAPER-063", "PAPER-064", "PAPER-065", "PAPER-066", "PAPER-067", "PAPER-068"]
evidence_target = "SYSTEM_VALUE"
+++

# EXP-A-001 — Matched-observability DemandState residual

## Decision question
Does explicit Agent-internal DemandState / RequiredProgress retain >=~5% end-outcome value over B4-TX at matched foreground QoE with zero illegal cancellation?

## Why the test changed
Rescue-1B shows that naive comparisons are insufficient:
- history predicts proactive need;
- runtime exposes speculative/commit state;
- transaction systems derive substantial effect legality.

The experiment must therefore test **conditional information value**, not merely show semantic-aware scheduling beats semantic-blind scheduling.

## Baseline B4-TX
Include, where available:
- per-user long behavioral history and learned When-to-Assist prediction;
- ordinary SLO/TUF/utility/deadline/slack;
- program/control/data-flow and belief state;
- script lowering and local typed execution;
- interaction criticality and dependency propagation;
- speculative active/cancelled/verified state;
- runtime commit/authorization state;
- Cordon/TomasuLLM-class effect/dependency legality;
- rollback/discard scope;
- workflow topology / STE / reuse state;
- resource profiles and device state.

## Core design — matched observability
Construct paired or grouped execution points where B4-TX observables are deliberately similar but the Agent-internal continuation value differs.

Examples:
- same tool/model stage, one branch still required and one branch invalidated by a new goal update;
- same slack/SLO/topology, one result lies on the surviving goal path and one does not;
- same cache/reuse distance, one state belongs to a required continuation and one to an optional/speculative branch.

B4-TX sees only permitted observable/runtime proxies.
B6-Demand additionally receives the canonical internal DemandState/RequiredProgress label.

## Evaluation
Primary:
- RequiredProgress completed before deadline / interaction boundary;
- end-to-end task success;
- foreground QoE/jank/latency;
- energy and thermal budget;
- illegal cancellation = 0.

Secondary:
- calibration;
- cost-weighted false progress;
- cancelled compute;
- saved compute;
- controller overhead;
- extra metadata/IPC cost.

## Split discipline
For learned B4:
- user/session/time-aware split;
- no row-random leakage across repeated observation histories;
- allow legal personalization as a strong baseline.

## Falsifier
DOWNGRADE/KILL differentiated A if B4-TX captures nearly all B6-Demand value and residual improvement is <~5% or disappears under stronger history/runtime features.

## Promotion condition
Only consider SYSTEM_VALUE after the residual appears on target-relevant phone traces/workloads, not device-free replay alone.

## Hardware boundary
Even a positive DemandState residual does not imply uArch.
Next gate would be whether OS/runtime actuators are insufficient and whether the remaining cause is hardware-timed.
