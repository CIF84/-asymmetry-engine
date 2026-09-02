from __future__ import annotations

import argparse
from pathlib import Path

from .db import Repository
from .pipeline import run_collection
from .sources.azure_prices import AzureRetailPriceCollector
from .sources.cfpb import CFPBCollector
from .reasoning import ReasoningError, build_cn75_argument
from .sources.comext import ComextCN75Collector, ComextCollector
from .sources.dataforseo import DataForSEOKeywordCollector
from .sources.eurostat import EurostatCollector
from .sources.openalex import OpenAlexCollector
from .sources.stackexchange import StackExchangeCollector
from .sources.ted import TEDCollector


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(prog="asymmetry-engine")
    subcommands = result.add_subparsers(dest="command", required=True)
    collect = subcommands.add_parser("collect-stackexchange")
    collect.add_argument("--site", default="money")
    collect.add_argument("--sample-size", type=int, default=25)
    collect.add_argument("--database", type=Path, default=Path("asymmetry.db"))
    cfpb = subcommands.add_parser("collect-cfpb")
    cfpb.add_argument("--sample-size", type=int, default=25)
    cfpb.add_argument("--database", type=Path, default=Path("asymmetry.db"))
    keyword_demand = subcommands.add_parser("collect-keyword-demand")
    keyword_demand.add_argument("--database", type=Path, default=Path("asymmetry.db"))
    ted = subcommands.add_parser("collect-ted")
    ted.add_argument("--database", type=Path, default=Path("asymmetry.db"))
    eurostat = subcommands.add_parser("collect-eurostat")
    eurostat.add_argument("--database", type=Path, default=Path("asymmetry.db"))
    azure = subcommands.add_parser("collect-azure-prices")
    azure.add_argument("--database", type=Path, default=Path("asymmetry.db"))
    comext = subcommands.add_parser("collect-comext")
    comext.add_argument("--database", type=Path, default=Path("asymmetry.db"))
    cn75 = subcommands.add_parser("collect-comext-cn75")
    cn75.add_argument("--database", type=Path, default=Path("asymmetry.db"))
    openalex = subcommands.add_parser("collect-openalex")
    openalex.add_argument("--database", type=Path, default=Path("asymmetry.db"))
    reason_cn75 = subcommands.add_parser("reason-cn75")
    reason_cn75.add_argument("--database", type=Path, default=Path("asymmetry.db"))
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    if args.command == "reason-cn75":
        repository = Repository(args.database)
        try:
            argument = build_cn75_argument(repository)
        except ReasoningError as exc:
            print(f"error={exc}")
            return 1
        finally:
            repository.close()
        print(argument.render())
        return 0
    if args.command == "collect-stackexchange":
        collector = StackExchangeCollector(site=args.site, sample_size=args.sample_size)
    elif args.command == "collect-cfpb":
        collector = CFPBCollector(sample_size=args.sample_size)
    elif args.command == "collect-keyword-demand":
        collector = DataForSEOKeywordCollector()
    elif args.command == "collect-ted":
        collector = TEDCollector()
    elif args.command == "collect-eurostat":
        collector = EurostatCollector()
    elif args.command == "collect-azure-prices":
        collector = AzureRetailPriceCollector()
    elif args.command == "collect-comext":
        collector = ComextCollector()
    elif args.command == "collect-comext-cn75":
        collector = ComextCN75Collector()
    elif args.command == "collect-openalex":
        collector = OpenAlexCollector()
    else:
        return 2
    args.database.parent.mkdir(parents=True, exist_ok=True)
    repository = Repository(args.database)
    try:
        result = run_collection(collector, repository)
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
