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
    # Trade Date Discovery
    # =====================================================

    def trade_dates(
        self,
        symbol: str,
    ) -> list[int]:
        """
        Return all available trade dates.
        """

        df = self.repository.load(symbol)

        return sorted(

            df["TRADE_DATE"]

            .drop_duplicates()

            .astype(int)

            .tolist()

        )

    # -----------------------------------------------------

    def available_trade_dates(
        self,
        symbol: str,
    ) -> list[int]:
        """
        Backward-compatible alias.
        """

        return self.trade_dates(symbol)

    # -----------------------------------------------------

    def latest_trade_date(
        self,
        symbol: str,
    ) -> int:
        """
        Return latest available trade date.
        """

        dates = self.trade_dates(symbol)

        if not dates:

            raise ValueError(

                f"No trade dates found for '{symbol}'."

            )

        return dates[-1]

    # =====================================================
    # Expiry Discovery
    # =====================================================

    def expiries(
        self,
        symbol: str,
        trade_date,
    ) -> list[int]:
        """
        Return expiries available on a trade date.
        """

        df = self.repository.load(symbol)

        df = df.loc[

            df["TRADE_DATE"] == trade_date

        ]

        return sorted(

            df["EXP_DATE"]

            .drop_duplicates()

            .astype(int)

            .tolist()

        )

    # -----------------------------------------------------

    def latest_expiry(
        self,
        symbol: str,
        trade_date,
    ) -> int:
        """
        Return nearest expiry for a trade date.
        """

        expiries = self.expiries(

            symbol,

            trade_date,

        )

        if not expiries:

            raise ValueError(

                f"No expiry found for '{symbol}' on {trade_date}."

            )

        return expiries[0]

    # -----------------------------------------------------

    def expiry_list(
        self,
        symbol: str,
    ) -> list[int]:
        """
        Return all expiries available in the dataset.
        """

        df = self.repository.load(symbol)

        return sorted(

            df["EXP_DATE"]

            .drop_duplicates()

            .astype(int)

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
        Return option chain.

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
    # Strike Discovery
    # =====================================================

    def strikes(
        self,
        symbol: str,
        trade_date,
        expiry,
    ) -> list[int]:
        """
        Return sorted unique strikes.
        """

        chain = self.option_chain(

            symbol=symbol,

            trade_date=trade_date,

            expiry=expiry,

        )

        return sorted(

            chain["STRIKE_PRICE"]

            .drop_duplicates()

            .astype(int)

            .tolist()

        )

    # =====================================================
    # Representation
    # =====================================================

    def __repr__(self) -> str:

        return (

            f"{self.__class__.__name__}("

            f"repository={self.repository.__class__.__name__})"

        )

    __str__ = __repr__