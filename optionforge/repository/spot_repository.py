"""
============================================================
OptionForge
Spot Repository
============================================================

Author      : OptionForge
Module      : spot_repository.py
Purpose     : Repository for spot market datasets.

Responsibilities
----------------
- Locate equity/index spot files
- Load CSV datasets
- Validate existence
- Return DataFrames

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from optionforge.repository.file_loader import FileLoader

from optionforge.datasource.path_manager import PathManager

from optionforge.repository.market_repository import (
    MarketRepository,
)

from optionforge.repository.repository_context import (
    RepositoryContext,
)

from optionforge.repository.repository_exception import (
    RepositoryNotFoundError,
)


class SpotRepository(MarketRepository):
    """
    Repository for spot market data.
    """

    def __init__(
        self,
        context: RepositoryContext,
    ) -> None:

        self._context = context

        self._paths = PathManager(
            context.marketforge_root,
        )

    # ======================================================
    # Helpers
    # ======================================================

    def _resolve(
        self,
        symbol: str,
    ) -> Path:
        """
        Resolve spot CSV file.
        """

        symbol = symbol.upper()

        index_file = (

            self._paths.indices_master

            / f"{symbol}.csv"

        )

        if index_file.exists():

            return index_file

        stock_file = (

            self._paths.equity_master

            / f"{symbol}.csv"

        )

        if stock_file.exists():

            return stock_file

        raise RepositoryNotFoundError(

            f"Spot data not found for '{symbol}'."

        )

    # ======================================================
    # Public API
    # ======================================================

    def load(
        self,
        symbol: str,
        **kwargs,
    ) -> pd.DataFrame:
        """
        Load spot dataset.
        """

        return pd.read_csv(

            self._resolve(symbol),

        )

    def exists(
        self,
        symbol: str,
        **kwargs,
    ) -> bool:
        """
        Return True if spot data exists.
        """

        try:

            self._resolve(symbol)

            return True

        except RepositoryNotFoundError:

            return False

    def latest(
        self,
        symbol: str,
        **kwargs,
    ) -> pd.DataFrame:
        """
        Return latest spot dataset.
        """

        return self.load(

            symbol,

        )