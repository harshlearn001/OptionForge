"""
============================================================
OptionForge
Loader V2
============================================================

Repository-backed market data loader.

Responsibilities
----------------
- Load option market data
- Load future market data
- Load spot market data
- Return synchronized datasets

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from optionforge.repository import RepositoryFactory


@dataclass(frozen=True, slots=True)
class MarketData:
    """
    Loaded market datasets.
    """

    option: pd.DataFrame
    future: pd.DataFrame
    spot: pd.DataFrame


class Loader:
    """
    Repository-backed market loader.
    """

    def __init__(
        self,
        repository_factory: RepositoryFactory,
    ) -> None:

        self._repository_factory = repository_factory

    def load(
        self,
        symbol: str,
    ) -> MarketData:
        """
        Load all market datasets for a symbol.
        """

        option = self._repository_factory.option().load(symbol)

        future = self._repository_factory.future().load(symbol)

        spot = self._repository_factory.spot().load(symbol)

        return MarketData(
            option=option,
            future=future,
            spot=spot,
        )

    def load_option(
        self,
        symbol: str,
    ) -> pd.DataFrame:

        return self._repository_factory.option().load(symbol)

    def load_future(
        self,
        symbol: str,
    ) -> pd.DataFrame:

        return self._repository_factory.future().load(symbol)

    def load_spot(
        self,
        symbol: str,
    ) -> pd.DataFrame:

        return self._repository_factory.spot().load(symbol)