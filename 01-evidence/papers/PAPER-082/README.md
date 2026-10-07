+++
id = "PAPER-082"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "PRIOR_ART_BASELINE"
independence_assessment = "PEER_REVIEWED_SECURITY_SYSTEM"
title = "CAEC: Confidential, Attestable, and Efficient Inter-CVM Communication with Arm CCA"
primary_url = "https://arxiv.org/abs/2512.01594"
priority = "P0"
evidence_role = "strong baseline for mutually attested multi-CVM confidential shared memory, dynamic share/attach/revoke and large-object sharing"
authors = ["Sina Abdollahi", "Amir Al Sadi", "David Kotz", "Marios Kogias", "Hamed Haddadi"]
venue = "EuroS&P 2026"
+++

# PAPER-082 — CAEC

## 30-second read
- **Why it matters:** Directly pressure-tests AgenTEE's apparent Agent-specific need for mutually distrustful components to communicate confidentially.
- **Mechanism:** CCA-compatible Confidential Shared Memory with attestable realm identifiers, explicit provider/consumer consent, access permissions, attach/revoke/destroy lifecycle.
- **Reported result:** up to ~209× fewer CPU cycles than encrypted normal-world shared-memory communication; model sharing cuts total memory footprint ~16.6–28.3% for 2–3 realms, with native-like inference time in the tested setup.
- **Portfolio meaning:** multi-realm attestation, confidential communication and dynamic sharing are generic confidential-computing primitives already available below the Agent runtime.
- **Boundary:** CCA prototype environment; not smartphone Agent workload.
- **Primary source:** https://arxiv.org/abs/2512.01594

See [deep.md](deep.md) for full Paper Insight 10Q.