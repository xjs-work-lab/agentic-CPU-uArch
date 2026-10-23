#!/usr/bin/env python3
"""Apply the reviewed Academic CPU Insight profile and export a non-sensitive SlidePoise canvas snapshot.

Windows CMD:
    curl.exe -fL -o configure-slidepoise.py https://raw.githubusercontent.com/xjs-work-lab/agentic-CPU-uArch/main/09-roadmap/leadership-decision-pack/slidepoise-prep/scripts/configure-slidepoise.py
    "%USERPROFILE%\\.slidepoise\\python\\Scripts\\python.exe" configure-slidepoise.py

This does not send credentials or upload anything. It does not modify the built-in Consulting profile.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen

PROFILE_ID = "academic-cpu-insight"
RUN_NAME = "agentic-cpu-sample"
BASE = "https://raw.githubusercontent.com/xjs-work-lab/agentic-CPU-uArch/main/09-roadmap/leadership-decision-pack/slidepoise-prep"
PATCH_URL = BASE + "/profile-blue/academic-cpu-insight.profile-update.json"


def cli_path() -> Path:
    choices = [
        Path(sys.executable).with_name("slidepoise.exe"),
        Path.home() / ".slidepoise" / "python" / "Scripts" / "slidepoise.exe",
    ]
    for candidate in choices:
        if candidate.is_file():
            return candidate
    raise RuntimeError("Cannot find slidepoise.exe; rerun this with the Python under %USERPROFILE%\\.slidepoise\\python\\Scripts.")


CLI = cli_path()


def call(*args: str) -> dict | list:
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    proc = subprocess.run(
        [str(CLI), *args],
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        env=env,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"slidepoise {' '.join(args[:3])} failed (exit {proc.returncode}):\n{proc.stderr or proc.stdout}")
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"SlidePoise returned non-JSON output: {proc.stdout[:500]}") from e


def fetch_patch() -> dict:
    try:
        with urlopen(PATCH_URL, timeout=30) as response:
            obj = json.loads(response.read().decode("utf-8-sig"))
    except Exception as e:
        raise RuntimeError(f"Failed to download the project-controlled profile patch: {PATCH_URL}\n{e}") from e
    if not isinstance(obj, dict) or "design_overrides" not in obj or "hard_rules" not in obj:
        raise RuntimeError("Profile patch is missing expected sections.")
    if "profile_id" in obj or "schema_version" in obj:
        raise RuntimeError("Unsafe attempt to replace profile identity or schema.")
    return obj


def select_run() -> str:
    runs = call("run", "list")
    if isinstance(runs, list):
        for entry in runs:
            if entry.get("name") != RUN_NAME or not entry.get("path"):
                continue
            p = Path(entry["path"])
            try:
                overrides = json.loads((p / "session-overrides.json").read_text(encoding="utf-8"))
                if overrides.get("profile") == PROFILE_ID:
                    print(f"Reusing existing SlidePoise run: {p}")
                    return str(p)
            except (OSError, ValueError):
                pass
    created = call("run", "create", RUN_NAME, "--profile", PROFILE_ID)
    path = created.get("path") if isinstance(created, dict) else None
    if not path:
        raise RuntimeError("Run was created but the CLI did not report a run path.")
    print(f"Created new SlidePoise run: {path}")
    return path


def main() -> None:
    print(f"SlidePoise executable: {CLI}")
    current = call("profile", "show", PROFILE_ID)
    patch = fetch_patch()
    actual_profile = current.get("profile", {})
    needs_update = any(actual_profile.get(k) != v for k, v in patch.items())
    if needs_update:
        payload = json.dumps(patch, ensure_ascii=False, separators=(",", ":"))
        print(f"Applying blue profile patch (approx. {len(payload)} characters)...")
        call("profile", "update", PROFILE_ID, "--json", payload, "--expected", current["revision"])
    else:
        print("Academic CPU Insight profile already matches reviewed patch; no update needed.")

    updated = call("profile", "show", PROFILE_ID)
    profile = updated.get("profile", {})
    design = profile.get("design_overrides", {})
    style = design.get("style", {})
    palette = style.get("accent_colors", [])
    if style.get("body_font") != "Microsoft YaHei" or "#102C55" not in palette:
        raise RuntimeError("The new Profile did not resolve to the expected Chinese/blue style.")
    print(f"Verified Profile: {PROFILE_ID}; palette={palette[:3]}; font={style.get('body_font')}")

    run_root = select_run()
    target = Path(run_root) / "work" / "resolved-config.json"
    call("run", "resolve", run_root, "--output", str(target))
    resolved = json.loads(target.read_text(encoding="utf-8"))
    d = resolved["design"]
    derived = resolved.get("derived", {})
    frame = d.get("frame", {})
    canvas = derived.get("generation_region_px")
    if not canvas:
        raise RuntimeError("Resolved configuration lacks derived.generation_region_px; inspect the original run file.")
    summary = {
        "source": "local_slidepoise_run_resolve",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "profile_id": profile.get("profile_id"),
        "profile_revision": updated["revision"],
        "profile_schema_version": profile.get("schema_version"),
        "design": {
            "full_slide_px": d.get("full_slide_px"),
            "frame": {
                "header": {k: frame.get("header", {}).get(k) for k in ("enabled", "height_px", "font_family", "font_size_px", "text_color", "rule_color", "left_text", "right_text")},
                "footer": {k: frame.get("footer", {}).get(k) for k in ("enabled", "height_px", "font_family", "font_size_px", "text_color", "rule_color", "left_text", "center_text", "slide_number")},
            },
            "style": {k: d.get("style", {}).get(k) for k in ("background", "display_font", "body_font", "density", "accent_colors", "neutral_colors")},
            "title": {k: d.get("title", {}).get(k) for k in ("font_family", "nominal_size_px", "color", "anchor_px", "max_width_px")},
            "connectors": d.get("connectors", {}),
        },
        "derived": {k: derived.get(k) for k in ("generation_region_px", "generation_offset_y_px", "generation_aspect_ratio", "header_height_px", "footer_height_px")},
        "speaker_notes_write_readback": "NOT_TESTED",
        "note": "Sanitized environment/design summary only. The actual resolved-config.json stays in the local run.",
    }
    dest = Path.cwd() / "slidepoise-preflight-export.json"
    dest.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Substantive content canvas: {canvas}, ratio={derived.get('generation_aspect_ratio')}")
    print(f"Safe-to-share summary written to: {dest}")
    print("Upload only this summary JSON to the GitHub research repo's slidepoise-config directory.")
    print("Do not upload the full local resolved-config.json unless reviewed for private paths or credentials.")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
