# Round 14-A — LOCAL FULL_10Q result

Date: 2026-10-07
Source: PAPER-104
State: COMPLETE

## Key result
LOCAL is the strongest T7 discriminator so far because multiple Agents can share one model instance, KV state, adapters and a memory budget.

Yet the paper itself decomposes the useful state into software-visible variables:
- token span;
- context namespace;
- logical adapter;
- adapter version;
- pending downstream consumers;
- predicted reuse demand;
- foreground/background priority;
- memory headroom.

Agent identity is provenance rather than an unconditional validity key.

## Product Trend impact
### T5
Strongly strengthened:
versioned validity / refresh / residency is now part of the strongest Agent-state product baseline.

No maturity change because no smartphone SoC is evaluated.

### T7
Product signal strengthened but standalone residual narrowed.

Cross-Agent pre-prefill is useful:
- p99 TTFT 2.042 s → 1.595 s;
- 21.9% reduction in the reported tau-bench run.

But the signal is predicted future consumption of shared context, which maps naturally to C + T5.

T7 stays FRONTIER_SIGNAL / WATCH.

## H-CAL
LOCAL fills one old evidence gap: live inference and local adapter publication can coexist in software.

It does not meet H-CAL's reopen condition because there is still no target-phone residual after the software baseline.

## Hardware gate
No advance.

`STRUCTURAL_SIGNAL → [target-phone SYSTEM_VALUE missing] → SOFTWARE_INSUFFICIENCY not established`

## Next
EcoAgent FULL_10Q.

After EcoAgent:
issue the Round 14-A T7 ownership decision.
