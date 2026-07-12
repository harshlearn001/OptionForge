"""
============================================================
OptionForge
Option Provider
============================================================

Author      : OptionForge
Module      : option_provider.py

Purpose
-------
Business access layer for option market data.

Responsibilities
----------------
✓ Provide option expiries
✓ Provide available trade dates
✓ Provide option chains
✓ Never read files
✓ Never validate data
✓ Never perform analytics

============================================================
"""

from __future__ import annotations

import pandas as pd

from optionforge.repository.option_repository import (
    OptionRepository,
)


class OptionProvider:
    """
    Business provider for option market data.
    """

    def __init__(
        self,
        repository: OptionRepository,
    ) -> None:

        self._repository = repository

    # =====================================================
    # Properties
    # =====================================================

    @property
    def repository(self) -> OptionRepository:
        """
        Underlying option repository.
        """

        return self._repository

    # =====================================================
    # Discovery
    # =====================================================

    def available_trade_dates(
        self,
        symbol: str,
    ) -> list:
        """
        Return all available trade dates.
        """

        df = self.repository.load(symbol)

        return sorted(
            df["TRADE_DATE"]
            .drop_duplicates()
            .tolist()
        )

    # -----------------------------------------------------

    def expiry_list(
        self,
        symbol: str,
    ) -> list:
        """
        Return all available expiries.
        """

        df = self.repository.load(symbol)

        return sorted(
            df["EXP_DATE"]
            .drop_duplicates()
            .tolist()
        )

    # =====================================================
    # Option Chain
    # =====================================================

    def option_chain(
        self,
        symbol: str,
        trade_date,
        expiry=None,
    ) -> pd.DataFrame:
        """
        Return option chain for a trade date.

        Parameters
        ----------
        symbol
            Market symbol.

        trade_date
            Trade date.

        expiry
            Optional expiry filter.
        """

        df = self.repository.load(symbol)

        chain = df.loc[
            df["TRADE_DATE"] == trade_date
        ]

        if expiry is not None:

            chain = chain.loc[
                chain["EXP_DATE"] == expiry
            ]

        return chain.reset_index(drop=True)

    # =====================================================
    # Representation
    # =====================================================

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}("
            f"repository={self.repository.__class__.__name__})"
        )

    __str__ = __repr__