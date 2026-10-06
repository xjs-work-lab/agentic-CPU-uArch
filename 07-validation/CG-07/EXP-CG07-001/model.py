from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def break_even_events_per_window(
    window_seconds: float,
    dedicated_idle_mw: float,
    dedicated_active_mw: float,
    shared_active_mw: float,
    shared_wake_energy_mj: float,
    active_ms_per_event: float,
    wakes_per_event: float = 1.0,
) -> float:
    active_s = active_ms_per_event / 1000.0
    dedicated_base_mj = dedicated_idle_mw * window_seconds

    dedicated_increment_mj = (
        (dedicated_active_mw - dedicated_idle_mw) * active_s
    )
    shared_per_event_mj = (
        shared_active_mw * active_s
        + wakes_per_event * shared_wake_energy_mj
    )

    advantage_per_event = shared_per_event_mj - dedicated_increment_mj
    if advantage_per_event <= 0:
        return math.inf

    return dedicated_base_mj / advantage_per_event


def default_grid() -> list[dict]:
    rows = []
    window_seconds = 3600.0
    for dedicated_idle in (5.0, 20.0, 50.0):
        for wake_energy in (1.0, 4.0, 8.0, 16.0):
            for active_ms in (5.0, 20.0, 100.0):
                events = break_even_events_per_window(
                    window_seconds=window_seconds,
                    dedicated_idle_mw=dedicated_idle,
                    dedicated_active_mw=200.0,
                    shared_active_mw=700.0,
                    shared_wake_energy_mj=wake_energy,
                    active_ms_per_event=active_ms,
                )
                rows.append(
                    {
                        "window_seconds": window_seconds,
                        "dedicated_idle_mw": dedicated_idle,
                        "dedicated_active_mw": 200.0,
                        "shared_active_mw": 700.0,
                        "shared_wake_energy_mj": wake_energy,
                        "active_ms_per_event": active_ms,
                        "break_even_events_per_hour": events,
                        "break_even_events_per_second": (
                            events / window_seconds
                            if math.isfinite(events)
                            else math.inf
                        ),
                        "boundary": "synthetic_parameter_model",
                    }
                )
    return rows


def main() -> None:
    ap = argparse.ArgumentParser(
        description=(
            "Dedicated always-on vs shared-NPU break-even model. "
            "Default values are synthetic."
        )
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=Path("analysis/stage16a/results/cg07-break-even.csv"),
    )
    args = ap.parse_args()

    rows = default_grid()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
