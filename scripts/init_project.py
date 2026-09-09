#!/usr/bin/env python3
"""Instantiate a research project from the bundled text/CSV template."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("destination", help="New or empty destination directory")
    parser.add_argument("--industry", required=True, help="User-confirmed industry name")
    parser.add_argument("--market", default="A股", help="Investable market")
    parser.add_argument("--as-of", required=True, help="Initial data date, YYYY-MM-DD")
    args = parser.parse_args()

    source = Path(__file__).resolve().parents[1] / "assets" / "project-template"
    destination = Path(args.destination).resolve()
    if destination.exists() and any(destination.iterdir()):
        raise SystemExit(f"Refusing to overwrite non-empty directory: {destination}")
    destination.mkdir(parents=True, exist_ok=True)

    for item in source.rglob("*"):
        relative = item.relative_to(source)
        target = destination / relative
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        text = item.read_text(encoding="utf-8")
        text = text.replace("{{INDUSTRY_NAME}}", args.industry)
        text = text.replace("{{INVESTABLE_MARKET}}", args.market)
        text = text.replace("{{AS_OF_DATE}}", args.as_of)
        target.write_text(text, encoding="utf-8", newline="")

    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

