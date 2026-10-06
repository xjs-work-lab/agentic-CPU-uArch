+++
id = "PAPER-068"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "FOUNDATIONAL_PEER_REVIEWED"
title = "Energy-Efficient, Utility Accrual Scheduling under Resource Constraints for Mobile Embedded Systems"
primary_url = "https://doi.org/10.1145/1017753.1017768"
priority = "P0"
evidence_role = "foundational prior art for explicit time/utility functions, low-utility abort and energy-aware resource scheduling in mobile embedded systems"
authors = ["Haisang Wu", "Binoy Ravindran", "E. Douglas Jensen", "Peng Li"]
venue = "ACM EMSOFT 2004; extended ACM TECS 2006"
+++

# PAPER-068 — ReUA / Utility-Accrual Scheduling

## 30-second read
- **Why it matters:** Shows that tasks can explicitly expose time-varying utility and schedulers can maximize accrued value/energy efficiency, including aborting infeasible or low-utility work.
- **What it establishes:** Time/utility functions generalize deadlines into application-specific value-vs-completion-time curves; ReUA combines utility, resource dependencies, stochastic cycle demand and DVS for mobile embedded scheduling.
- **Portfolio meaning:** Generic 'task marginal value / tolerance curve → energy/resource scheduling' is foundational prior art. H-FIB cannot claim novelty for a value function or resource budget alone.
- **Boundary:** Classical real-time/embedded task model and simulation; not Agent semantics or smartphone foreground QoE.
- **Primary source:** https://doi.org/10.1145/1017753.1017768
- **Extended journal:** https://doi.org/10.1145/1165780.1165781

See [deep.md](deep.md) for full Paper Insight 10Q.