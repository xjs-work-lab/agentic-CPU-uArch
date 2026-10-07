from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def legacy_break_even_events_per_window(
    window_seconds: float,
    dedicated_idle_mw: float,
    dedicated_active_mw: float,
    shared_active_mw: float,
    shared_wake_energy_mj: float,
    active_ms_per_event: float,
    wakes_per_event: float = 1.0,
) -> float:
    """Frozen Stage16A direct-event model kept for historical reproducibility."""
    active_s = active_ms_per_event / 1000.0
    dedicated_base_mj = dedicated_idle_mw * window_seconds
    dedicated_increment_mj = (dedicated_active_mw - dedicated_idle_mw) * active_s
    shared_per_event_mj = shared_active_mw * active_s + wakes_per_event * shared_wake_energy_mj
    advantage_per_event = shared_per_event_mj - dedicated_increment_mj
    if advantage_per_event <= 0:
        return math.inf
    return dedicated_base_mj / advantage_per_event


def break_even_observations_after_gating(
    window_seconds: float,
    dedicated_idle_mw: float,
    dedicated_gate_active_mw: float,
    dedicated_gate_ms_per_observation: float,
    baseline_gate_energy_mj_per_observation: float,
    acceptance_rate: float,
    dedicated_handoff_energy_mj_per_accepted: float = 0.0,
    baseline_handoff_energy_mj_per_accepted: float = 0.0,
) -> float:
    """V2.2 residual model after lightweight intervene/no-intervene gating."""
    if not 0.0 <= acceptance_rate <= 1.0:
        raise ValueError("acceptance_rate must be in [0, 1]")
    if dedicated_gate_active_mw < dedicated_idle_mw:
        raise ValueError("dedicated gate active power must be >= idle power")

    gate_s = dedicated_gate_ms_per_observation / 1000.0
    dedicated_base_mj = dedicated_idle_mw * window_seconds
    dedicated_gate_increment_mj = (dedicated_gate_active_mw - dedicated_idle_mw) * gate_s

    dedicated_per_observation_mj = (
        dedicated_gate_increment_mj
        + acceptance_rate * dedicated_handoff_energy_mj_per_accepted
    )
    baseline_per_observation_mj = (
        baseline_gate_energy_mj_per_observation
        + acceptance_rate * baseline_handoff_energy_mj_per_accepted
    )
    advantage_per_observation_mj = baseline_per_observation_mj - dedicated_per_observation_mj
    if advantage_per_observation_mj <= 0:
        return math.inf
    return dedicated_base_mj / advantage_per_observation_mj


def default_grid() -> list[dict]:
    """Synthetic sensitivity grid; values are not product measurements."""
    rows = []
    window_seconds = 3600.0
    for dedicated_idle in (5.0, 20.0, 50.0):
        for baseline_gate_energy in (0.5, 4.0, 8.0):
            for acceptance_rate in (0.05, 0.20, 0.50):
                observations = break_even_observations_after_gating(
                    window_seconds=window_seconds,
                    dedicated_idle_mw=dedicated_idle,
                    dedicated_gate_active_mw=100.0,
                    dedicated_gate_ms_per_observation=2.0,
                    baseline_gate_energy_mj_per_observation=baseline_gate_energy,
                    acceptance_rate=acceptance_rate,
                    dedicated_handoff_energy_mj_per_accepted=8.0,
                    baseline_handoff_energy_mj_per_accepted=0.0,
                )
                rows.append({
                    "window_seconds": window_seconds,
                    "dedicated_idle_mw": dedicated_idle,
                    "dedicated_gate_active_mw": 100.0,
                    "dedicated_gate_ms_per_observation": 2.0,
                    "baseline_gate_energy_mj_per_observation": baseline_gate_energy,
                    "acceptance_rate": acceptance_rate,
                    "dedicated_handoff_energy_mj_per_accepted": 8.0,
                    "baseline_handoff_energy_mj_per_accepted": 0.0,
                    "break_even_observations_per_hour": observations,
                    "break_even_observations_per_second": observations / window_seconds if math.isfinite(observations) else math.inf,
                    "boundary": "synthetic_post_gating_residual_model",
                })
    return rows


def main() -> None:
    ap = argparse.ArgumentParser(description="CG-07 post-gating residual break-even model; default values are synthetic.")
    ap.add_argument("--out", type=Path, default=Path("analysis/stage16a/results/cg07-post-gating-break-even.csv"))
    args = ap.parse_args()
    rows = default_grid()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
