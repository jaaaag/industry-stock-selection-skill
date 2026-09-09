#!/usr/bin/env python3
"""Check that a generated research project contains the required handoff files."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


REQUIRED = (
    "README.md",
    "00_project/project_config.md",
    "00_project/choice_data_request.md",
    "00_project/changelog.md",
    "01_data_audit/data_access_assessment.md",
    "02_industry_map/industry_map.md",
    "02_industry_map/industry_ranking.csv",
    "02_industry_map/profit_pool.md",
    "03_universe_screening/company_universe.csv",
    "03_universe_screening/excluded_companies.csv",
    "03_universe_screening/company_score.csv",
    "04_deep_dive/deep_research_candidates.md",
    "04_deep_dive/company_model.csv",
    "05_final/core_candidates.md",
    "05_final/key_indicators.md",
    "05_final/risk_monitor.md",
    "06_sources/source_registry.csv",
    "07_portfolio/portfolio_ledger.csv",
    "07_portfolio/decision_log.md",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project")
    args = parser.parse_args()
    root = Path(args.project).resolve()
    missing = [item for item in REQUIRED if not (root / item).is_file()]
    if missing:
        raise SystemExit("Missing required files:\n" + "\n".join(missing))

    for relative in REQUIRED:
        path = root / relative
        if path.suffix == ".csv":
            with path.open("r", encoding="utf-8-sig", newline="") as handle:
                header = next(csv.reader(handle), [])
            if not header or any(not column.strip() for column in header):
                raise SystemExit(f"Invalid CSV header: {relative}")
    print(f"Valid project template: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

