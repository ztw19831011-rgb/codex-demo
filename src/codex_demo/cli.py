from __future__ import annotations

import argparse
import json
from typing import Any

__version__ = "0.1.0"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="codex-demo",
        description="A minimal Codex-generated demo CLI (packaged via pyproject.toml).",
    )
    parser.add_argument(
        "--name",
        default="codex-demo",
        help="Project name to print (default: codex-demo).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output project info as JSON.",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Print version and exit.",
    )
    return parser


def render_info(name: str) -> dict[str, Any]:
    return {
        "project": {
            "name": name,
            "entry": "src/codex_demo/cli.py",
            "tool": "codex-demo",
        }
    }


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.version:
        print(__version__)
        return 0

    info = render_info(args.name)

    if args.json:
        print(json.dumps(info, ensure_ascii=False, indent=2))
        return 0

    # Human-readable output (compatible with your current style)
    print("Project Info")
    print(f"Name: {info['project']['name']}")
    print(f"Entry: {info['project']['entry']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

