> V1 semantic source copied/repacked from frozen baseline `960abb4ef50a8f5b0bd357c067f08346025d`.
> Do not reinterpret this page as V2.2 metadata authority; the compact README owns the Source object.

## PAPER-013 — [Speculative Interaction Agents: Building Real-Time Agents with Asynchronous I/O and Speculative Tool Calling](https://arxiv.org/abs/2605.13360)

**Authors:** Coleman Hooper, Minwoo Kang, Suhong Moon, Nicholas Lee, Eric Wen  
**Venue/status:** arXiv preprint

### Background
Interactive Agents often wait on tool/API results, producing long latency that could potentially be hidden with speculation.

### Problem
Speculatively executing future actions can reduce latency, but unsafe/state-changing operations cannot simply be run and discarded.

### Method
The paper separates safe/read-only speculation from state-modifying actions and introduces asynchronous/speculative tool execution with commit/cancellation rules.

### Main conclusion
Useful Agent work can be started before all uncertainty is resolved, provided the system tracks whether the work is safe, discardable and before/after a commit boundary.

### What we learn
This gives direct semantic support for M4/C1 fields such as:
- speculative;
- discardable;
- side-effect class;
- commit point.

These are much richer control signals than ordinary OS priority.

### Boundary
The work is not mobile-specific and does not show that CPU scheduling should directly consume those semantics.

---

---
