# Frontier Round 9 — Confidential Agent Execution / Isolation Coverage — 2026-10-07

## Decision question
Does confidential / isolated Agent execution expose a new differentiated smartphone CPU/system/uArch direction after strongest software and Arm CCA baselines?

## FULL_10Q source set
### Agent-native / workload
- PAPER-080 — AgenTEE — EuroMLSys 2026
- PAPER-084 — IsolateGPT — NDSS 2025
- PAPER-085 — CaMeL — IEEE SaTML 2026
- PAPER-086 — multi-CaMeL — arXiv preprint 2026-10-05

### Generic/mobile confidential-computing strongest baselines
- PAPER-081 — Aster / Bringing Confidential Computing to Android — MobiSys 2026
- PAPER-082 — CAEC — EuroS&P 2026
- PAPER-083 — PORTAL — IEEE S&P 2025

## What is genuinely Agent-new
Agent pipelines combine dynamic components and trust domains:
- Agent/runtime provider;
- model provider;
- third-party tools/apps;
- user/private data;
- potentially child Agents invoked as tools.

Natural-language/data boundaries create new attack surfaces, and trust/provenance must survive dynamic collaboration.

This is a real **workload/security requirement**.

## Strongest software baseline
### IsolateGPT
Already represents dynamic app/tool collaboration as:
- isolated app identity/context;
- hub-mediated collaboration;
- structured messages;
- explicit user permissions.

### CaMeL
Already represents:
- trusted control flow;
- untrusted data flow;
- dependency/provenance graph;
- capabilities;
- deterministic tool-call policy.

### multi-CaMeL
Extends the same ideas across hierarchical Agent-as-tool boundaries:
- trusted instruction channel;
- separate untrusted data channel;
- provenance/capability propagation;
- runtime instruction-channel integrity.

Reported MultiAgentDojo ASR:
- no CaMeL: 12.9%;
- independently protected Agents: 0.2%;
- multi-CaMeL: 0.0%.

Therefore the broad 'dynamic trust graph is invisible to software' thesis does not survive.

## Strongest hardware/platform baseline
### Aster
Android protected-VM lifecycle, launch policy, attestation, rollback and CCA-backed memory isolation.

### CAEC
Mutually attested confidential shared memory with create/share/attach/revoke/destroy and large-object sharing.

### PORTAL
Protected Realm-to-device/GPU I/O on mobile-style Arm SoCs using CCA GPC + SMMU isolation.

Therefore the broad 'Agents need new hardware isolation primitives' thesis also does not survive.

## Decision
**SECURITY / CONFIDENTIAL EXECUTION = KEEP AS PLATFORM REQUIREMENT + RESEARCH RADAR.**

**DO NOT OPEN A NEW HYPOTHESIS OR DIRECTION.**

Reason:
no Agent-specific CPU/uArch control variable remains publicly evidenced after software trust/provenance enforcement plus generic CCA substrate.

## Portfolio ownership
- verified action authorization / effect safety → PT-A where applicable;
- generic protected execution / CCA / pVM / secure device I/O → platform/security baseline, not a differentiated research lane;
- Agent provenance/capability policy → runtime strongest baseline;
- no A/C/CG score changes.

## Reopen condition for CPU/uArch research
Only reopen if direct smartphone evidence shows at least one of:
1. realistic Agent trust-domain/tool churn makes pVM/realm lifecycle or attestation materially too slow/energy-expensive;
2. secure CPU↔NPU/GPU/device assignment/data sharing is an adoption or QoE bottleneck not captured by PORTAL/ACAI-class mechanisms;
3. software provenance/capability enforcement cannot provide the required security property and a hardware-specific cause is demonstrated;
4. confidential execution introduces material foreground QoE, memory-capacity or thermal pressure that requires a reusable CPU/system control point.

## Portfolio impact
- second differentiated Primary Bet remains unfilled;
- no new Direction;
- no uArch candidate;
- security coverage blind spot is now closed at seed/strongest-baseline level.

## Next
Continue frontier reset outside:
- generic system-control;
- persistent Agent memory;
- confidential execution/isolation;
- already-owned A/PT-A/B/R1/R2/CG mechanisms.