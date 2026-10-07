# Evidence Rescue 1A — PT-A deep audit

Date: 2026-10-07
Scope: PAPER-037 / 038 / 039 / 040 / 042 plus adversarial/verification counter-evidence PAPER-101 / 102.

## Executive result
**PT-A survives, but the reason changes.**

The old formulation—heterogeneous action surfaces + verification/recovery—was directionally right but incomplete.

The deeper evidence supports a stricter platform control loop:

`capability & authority → route → observe → bind action to fresh context → act → outcome receipt → verify → recover`

No lane/score/maturity promotion follows.

## Source-by-source correction

| Source | Deep-read correction | Decision effect |
|---|---|---|
| PAPER-037 ClawMobile | real phone runtime, but model inference is remote; six-task study; comparator deployment asymmetric | KEEP real-phone runtime feasibility; no on-device-AI/energy inference |
| PAPER-038 Beyond GUI | strong CLI reachability evidence, but ADB/rooted benchmark infrastructure can exceed retail authority | KEEP capability heterogeneity; add entitlement boundary |
| PAPER-039 HybridCUA | naive GUI+CLI access drops base accuracy 38.8→18.4; training is required | strongest baseline becomes selective learned routing |
| PAPER-040 PhoneHarness | 75% result combines action access, routing, model choice and verifier stack; reference artifact is emulator/host-proxy based | KEEP mixed-action platform evidence; narrow verification causality |
| PAPER-042 UIAnchor | full system includes verification/recovery, but accessible audit evidence does not isolate their contribution from parser/edge-cloud design | KEEP full-system evidence; do not attribute 75.5% latency / 52.4% energy solely to verification |
| PAPER-101 Action Rebinding | observation→action gap can redirect an already-decided action; recovery/confirmation can be exploited | NEW PT-A context-integrity claim |
| PAPER-102 VeriGUI | verification-aware SFT/RL has causal recovery benefit | raises strongest software baseline; generic verification is less differentiated |

## Three important conclusions

### 1. Heterogeneous action surfaces are real, but authority is part of the mechanism
ADB/CLI/tool reachability should not be treated as an unconditional phone capability.
The PT-A contract must state what the Agent is authorized to invoke.

### 2. Routing is a learned/control problem, not a menu of tools
HybridCUA demonstrates that simply adding CLI can make a base Agent worse.
PT-A should optimize selective routing under capability, task state and execution feedback.

### 3. Verification is valuable but not equivalent to context integrity
PAPER-101 is the decisive negative evidence.
A correct decision based on state S(t0) can be delivered to a different app/component at t1.
Post-action verification detects the problem only after a potentially irreversible effect.

This creates a new discriminating question:
> Is cheap fresh-state validation enough, or does mobile Agent actuation need a stronger target-bound execution contract?

## Residual classification
- Agent-specific structural signal: **YES**
- direct system/security value: **YES**
- software/OS insufficiency: **NOT ESTABLISHED**
- hardware-specific cause: **NO**
- uArch candidate: **NO**

Therefore the residual remains inside PT-A Platform Track.

## Next
Execute EXP-PTA-002 conceptually/design-wise before considering any lower-layer mechanism.
Finish Rescue-1B for A before Frontier Round 14.
