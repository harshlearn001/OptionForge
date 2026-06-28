"""
==============================================================
OptionForge
Professional Option Chain Engine
==============================================================
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from optionforge.adapters.option_adapter import OptionAdapter


class OptionChain:
    """
    Professional Option Chain

    Responsibilities
    ----------------
    • Load MarketForge option data
    • Standardize schema
    • Hold complete option chain
    • Provide chain operations

    Future
    ------
    latest()
    expiry()
    atm()
    calls()
    puts()
    weekly()
    monthly()
    """

    def __init__(self, dataframe: pd.DataFrame):

        self.df = dataframe.copy()

    # ---------------------------------------------------------

    @classmethod
    def from_parquet(cls, file: str | Path):

        dataframe = OptionAdapter.convert(file)

        return cls(dataframe)

    # ---------------------------------------------------------

    def dataframe(self) -> pd.DataFrame:

        return self.df.copy()
    
        # ---------------------------------------------------------
    # Latest Trading Day
    # ---------------------------------------------------------

    def latest(self) -> "OptionChain":
        """
        Returns only the latest trading day.
        """

        latest_date = self.df["TRADE_DATE"].max()

        dataframe = (
            self.df[self.df["TRADE_DATE"] == latest_date]
            .copy()
            .reset_index(drop=True)
        )

        return OptionChain(dataframe)

    # ---------------------------------------------------------

    def latest_date(self):
        """
        Returns latest available trading date.
        """

        return self.df["TRADE_DATE"].max()
    
        # ---------------------------------------------------------
    # Available Expiries
    # ---------------------------------------------------------

    def expiries(self):
        """
        Returns all available expiry dates
        for the current OptionChain.
        """

        return (
            self.df["EXPIRY"]
            .drop_duplicates()
            .sort_values()
            .reset_index(drop=True)
        )

    # ---------------------------------------------------------

    def __len__(self):

        return len(self.df)

    # ---------------------------------------------------------

    def __repr__(self):

        return (
            f"OptionChain("
            f"rows={len(self.df)}, "
            f"columns={len(self.df.columns)})"
        )
    
        # ---------------------------------------------------------
    # Current Weekly Expiry
    # ---------------------------------------------------------

    def current_weekly(self) -> "OptionChain":
        """
        Returns the nearest available expiry.
        """

        expiry = self.expiries().iloc[0]

        df = (
            self.df[self.df["EXPIRY"] == expiry]
            .copy()
            .reset_index(drop=True)
        )

        return OptionChain(df)
    
        # ---------------------------------------------------------
    # Next Weekly Expiry
    # ---------------------------------------------------------

    def next_weekly(self) -> "OptionChain":

        expiries = self.expiries()

        if len(expiries) < 2:
            raise ValueError("Next weekly expiry not available.")

        expiry = expiries.iloc[1]

        df = (
            self.df[self.df["EXPIRY"] == expiry]
            .copy()
            .reset_index(drop=True)
        )

        return OptionChain(df)
    
        # ---------------------------------------------------------
    # Current Monthly Expiry
    # ---------------------------------------------------------

    def current_monthly(self) -> "OptionChain":

        expiries = self.expiries()

        first = expiries.iloc[0]

        year = first.year
        month = first.month

        current_month = expiries[
            (expiries.dt.year == year) &
            (expiries.dt.month == month)
        ]

        expiry = current_month.iloc[-1]

        df = (
            self.df[self.df["EXPIRY"] == expiry]
            .copy()
            .reset_index(drop=True)
        )

        return OptionChain(df)
    
        # ---------------------------------------------------------
    # Next Monthly Expiry
    # ---------------------------------------------------------

    def next_monthly(self) -> "OptionChain":

        expiries = self.expiries()

        first = expiries.iloc[0]

        year = first.year
        month = first.month

        current_month = expiries[
            (expiries.dt.year == year) &
            (expiries.dt.month == month)
        ]

        last_current = current_month.iloc[-1]

        future = expiries[expiries > last_current]

        next_month = future[
            (future.dt.year == future.iloc[0].year) &
            (future.dt.month == future.iloc[0].month)
        ]

        expiry = next_month.iloc[-1]

        df = (
            self.df[self.df["EXPIRY"] == expiry]
            .copy()
            .reset_index(drop=True)
        )

        return OptionChain(df)
    
        # ---------------------------------------------------------
    # LEAPS
    # ---------------------------------------------------------

    def leaps(self):

        expiries = self.expiries()

        first = expiries.iloc[0]

        return expiries[
            expiries.dt.year > first.year
        ]
    
        # ---------------------------------------------------------
    # Far Month
    # ---------------------------------------------------------

    def far_month(self) -> "OptionChain":

        expiry = self.expiries().iloc[-1]

        df = (
            self.df[self.df["EXPIRY"] == expiry]
            .copy()
            .reset_index(drop=True)
        )

        return OptionChain(df)