"""
============================================================
OptionForge
Repository Context
============================================================

Author      : OptionForge
Module      : marketforge_root: str | Path
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

    def __post_init__(self):

        root = Path(self.marketforge_root)

        object.__setattr__(

            self,

            "marketforge_root",

            root,

        )

        if not root.exists():

            raise FileNotFoundError(

                f"MarketForge root not found: {root}"

            )