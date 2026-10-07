+++
id = "PAPER-083"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "PRIOR_ART_BASELINE"
independence_assessment = "PEER_REVIEWED_MOBILE_SECURITY_ARCHITECTURE"
title = "PORTAL: Fast and Secure Device Access with Arm CCA for Modern Arm Mobile System-on-Chips (SoCs)"
primary_url = "https://doi.org/10.1109/SP61157.2025.00236"
priority = "P0"
evidence_role = "mobile-SoC baseline for secure CCA Realm-to-integrated-device/GPU I/O using GPC/SMMU isolation without per-transfer memory encryption"
authors = ["Fan Sang", "Jaehyuk Lee", "Xiaokuan Zhang", "Taesoo Kim"]
venue = "IEEE Symposium on Security and Privacy 2025"
+++

# PAPER-083 — PORTAL

## 30-second read
- **Why it matters:** Direct mobile-SoC prior art for the secure accelerator/device path a confidential smartphone Agent would need.
- **Mechanism:** protected plaintext memory regions accessible only to designated Realm VMs and devices, enforced with CCA Granule Protection Checks + SMMU stage-2 isolation.
- **Platform:** Arm FVP + Orange Pi 5 Plus / Mali-G610; Apple M1 measurements motivate integrated-memory behavior.
- **Reported result:** ~9.8% one-time runtime-device-management overhead; 1.07×–9.07× improvement on selected data-intensive GPU benchmarks vs encryption-based secure I/O.
- **Portfolio meaning:** 'secure Agent needs protected NPU/GPU/device access' is not a new mechanism by itself.
- **Boundary:** no LLM Agent workload and not a production smartphone CCA/NPU deployment.
- **Primary source:** https://doi.org/10.1109/SP61157.2025.00236

See [deep.md](deep.md) for full Paper Insight 10Q.