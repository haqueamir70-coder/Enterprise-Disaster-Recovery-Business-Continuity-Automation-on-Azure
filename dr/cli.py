"""Command-line interface for the BCDR lab."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .models import parse_plan
from .validator import validate_plan


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a synthetic Azure BCDR recovery plan.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate = subparsers.add_parser("validate", help="validate a JSON recovery plan")
    validate.add_argument("--plan", required=True, help="path to a JSON recovery plan")
    validate.add_argument("--output", help="optional path to write the JSON report")
    args = parser.parse_args()

    try:
        raw = json.loads(Path(args.plan).read_text(encoding="utf-8"))
        report = validate_plan(parse_plan(raw))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}, indent=2))
        return 2

    rendered = json.dumps(report, indent=2)
    print(rendered)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
