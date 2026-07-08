"""
============================================================
OptionForge
Repository Context
============================================================

Author      : OptionForge
Module      : repository_context.py
Purpose     : Immutable repository configuration.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(
    frozen=True,
    slots=True,
)
class RepositoryContext:
    """
    Repository configuration.
    """

    marketforge_root: Path

    use_parquet: bool = True

    use_cache: bool = True

    validate_schema: bool = True

    def __post_init__(self) -> None:

        if not self.marketforge_root.exists():

            raise FileNotFoundError(

                self.marketforge_root

            )