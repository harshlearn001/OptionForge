"""
============================================================
OptionForge
Option Repository
============================================================

Author      : OptionForge
Module      : option_repository.py
Purpose     : Repository for option chain datasets.

Responsibilities
----------------
- Locate option chain files
- Load parquet datasets
- Validate existence
- Return DataFrames

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

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
from optionforge.repository.file_loader import FileLoader

class OptionRepository(MarketRepository):
    """
    Repository for option chain data.
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
        Resolve option chain file.
        """

        symbol = symbol.upper()

        index_file = (

            self._paths.option_indices

            / f"{symbol}.parquet"

        )

        if index_file.exists():

            return index_file

        stock_file = (

            self._paths.option_stocks

            / f"{symbol}.parquet"

        )

        if stock_file.exists():

            return stock_file

        raise RepositoryNotFoundError(

            f"Option data not found for '{symbol}'."

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
        Load option chain.
        """



        return FileLoader.load(

        self._resolve(symbol),

        )

    def exists(
        self,
        symbol: str,
        **kwargs,
    ) -> bool:
        """
        Check whether option data exists.
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
        Return latest available dataset.

        Current implementation simply loads
        the latest stored file.
        """

        return self.load(

            symbol,

        )