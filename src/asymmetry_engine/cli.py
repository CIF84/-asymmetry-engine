from __future__ import annotations

import argparse
from pathlib import Path

from .db import Repository
from .pipeline import run_collection
from .sources.stackexchange import StackExchangeCollector


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(prog="asymmetry-engine")
    subcommands = result.add_subparsers(dest="command", required=True)
    collect = subcommands.add_parser("collect-stackexchange")
    collect.add_argument("--site", default="money")
    collect.add_argument("--sample-size", type=int, default=25)
    collect.add_argument("--database", type=Path, default=Path("asymmetry.db"))
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    if args.command == "collect-stackexchange":
        args.database.parent.mkdir(parents=True, exist_ok=True)
        repository = Repository(args.database)
        try:
            result = run_collection(
                StackExchangeCollector(site=args.site, sample_size=args.sample_size),
                repository,
            )
        finally:
            repository.close()
        print(
            f"run={result.run_id} status={result.status} fetched={result.fetched_count} "
            f"inserted={result.inserted_count} duplicates={result.duplicate_count} "
            f"database={args.database}"
        )
        if result.error:
            print(f"error={result.error}")
        return 0 if result.status == "succeeded" else 1
    return 2
