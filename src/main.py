#!/usr/bin/env python3
"""Simple CLI entry point."""

import argparse
from pathlib import Path


def get_project_name() -> str:
    return Path(__file__).resolve().parents[1].name


def main() -> None:
    parser = argparse.ArgumentParser(description="Print project info")
    parser.add_argument("--name-only", action="store_true", help="print just the project name")
    args = parser.parse_args()

    project_name = get_project_name()

    if args.name_only:
        print(project_name)
        return

    print("Project Info")
    print(f"Name: {project_name}")
    print("Entry: src/main.py")


if __name__ == "__main__":
    main()
