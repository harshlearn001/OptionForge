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
    • Hold complete option chain
    • Provide filtering operations
    """

    # ==========================================================
    # Constructor
    # ==========================================================

    def __init__(self, dataframe: pd.DataFrame):

        self.df = dataframe.copy()

    # ==========================================================
    # Loaders
    # ==========================================================

    @classmethod
    def from_parquet(cls, file: str | Path):
        """
        Load MarketForge parquet file.
        """

        dataframe = OptionAdapter.convert(file)

        return cls(dataframe)

    @classmethod
    def load(cls, file: str | Path):
        """
        Universal loader.
        """

        return cls.from_parquet(file)

    # ==========================================================
    # Data
    # ==========================================================

    def to_dataframe(self) -> pd.DataFrame:
        """
        Return the option chain using the canonical
        OptionForge column names.

        This provides a stable schema for every
        analytics engine regardless of the original
        MarketForge parquet column names.
        """

        df = self.df.copy()

        rename_map = {
            # Dates
            "TRADE_DATE": "trading_date",
            "EXPIRY": "expiry_date",
            # Identity
            "SYMBOL": "symbol",
            "INSTRUMENT": "instrument",
            # Strike
            "STRIKE": "strike_price",
            "STRIKE_PRICE": "strike_price",
            # Option Type
            "OPTION_TYPE": "option_type",
            "OPT_TYPE": "option_type",
            # OI
            "OI": "open_interest",
            "OPEN_INT": "open_interest",
            # Change OI
            "CHANGE_IN_OI": "change_in_open_interest",
            "CHG_IN_OI": "change_in_open_interest",
            # Volume
            "VOLUME": "volume",
            "TRD_QTY": "volume",
            # Contracts
            "CONTRACTS": "contracts",
            "NO_OF_CONT": "contracts",
            # Trades
            "TRADES": "trades",
            "NO_OF_TRADE": "trades",
            # Prices
            "OPEN": "open",
            "OPEN_PRICE": "open",
            "HIGH": "high",
            "HI_PRICE": "high",
            "LOW": "low",
            "LO_PRICE": "low",
            "CLOSE": "close",
            "CLOSE_PRICE": "close",
            # Values
            "NOTIONAL_VALUE": "notional_value",
            "NOTION_VAL": "notional_value",
            "PREMIUM_VALUE": "premium_value",
            "PR_VAL": "premium_value",
        }

        available = {old: new for old, new in rename_map.items() if old in df.columns}

        df = df.rename(columns=available)
        print("\nDEBUG COLUMNS")

        return df

    def dataframe(self) -> pd.DataFrame:
        """
        Backward-compatible alias.
        """
        return self.to_dataframe()

    # ==========================================================
    # Latest Trading Day
    # ==========================================================

    def latest(self) -> "OptionChain":

        latest_date = self.df["TRADE_DATE"].max()

        dataframe = (
            self.df[self.df["TRADE_DATE"] == latest_date].copy().reset_index(drop=True)
        )

        return OptionChain(dataframe)

    def latest_date(self):

        return self.df["TRADE_DATE"].max()

    # ==========================================================
    # Expiry Information
    # ==========================================================

    def expiries(self):

        return self.df["EXPIRY"].drop_duplicates().sort_values().reset_index(drop=True)

    # ---------------------------------------------------------
    # Metadata
    # ---------------------------------------------------------

    def trade_date(self):
        """
        Returns the trading date of the current chain.
        """
        return self.df["TRADE_DATE"].iloc[0]

    def expiry(self):
        """
        Returns the expiry date of the current chain.
        """
        return self.df["EXPIRY"].iloc[0]

    def symbol(self):
        """
        Returns the underlying symbol.
        """
        return self.df["SYMBOL"].iloc[0]

    def instrument(self):
        """
        Returns the instrument type.
        """
        return self.df["INSTRUMENT"].iloc[0]

    # ==========================================================
    # Magic Methods
    # ==========================================================

    def __len__(self):

        return len(self.df)

    def __repr__(self):

        return (
            f"OptionChain(" f"rows={len(self.df)}, " f"columns={len(self.df.columns)})"
        )

    # ==========================================================
    # Current Weekly
    # ==========================================================

    def current_weekly(self) -> "OptionChain":
        """
        Returns the nearest available expiry.
        """

        expiry = self.expiries().iloc[0]

        dataframe = self.df[self.df["EXPIRY"] == expiry].copy().reset_index(drop=True)

        return OptionChain(dataframe)

    # ==========================================================
    # Next Weekly
    # ==========================================================

    def next_weekly(self) -> "OptionChain":
        """
        Returns the second available expiry.
        """

        expiries = self.expiries()

        if len(expiries) < 2:
            raise ValueError("Next weekly expiry not available.")

        expiry = expiries.iloc[1]

        dataframe = self.df[self.df["EXPIRY"] == expiry].copy().reset_index(drop=True)

        return OptionChain(dataframe)

    # ==========================================================
    # Current Monthly
    # ==========================================================

    def current_monthly(self) -> "OptionChain":
        """
        Returns the last expiry of the current month.
        """

        expiries = self.expiries()

        first = expiries.iloc[0]

        current_month = expiries[
            (expiries.dt.year == first.year) & (expiries.dt.month == first.month)
        ]

        expiry = current_month.iloc[-1]

        dataframe = self.df[self.df["EXPIRY"] == expiry].copy().reset_index(drop=True)

        return OptionChain(dataframe)

    # ==========================================================
    # Next Monthly
    # ==========================================================

    def next_monthly(self) -> "OptionChain":
        """
        Returns the last expiry of the next month.
        """

        expiries = self.expiries()

        first = expiries.iloc[0]

        current_month = expiries[
            (expiries.dt.year == first.year) & (expiries.dt.month == first.month)
        ]

        last_current = current_month.iloc[-1]

        future = expiries[expiries > last_current]

        if future.empty:
            raise ValueError("Next monthly expiry not available.")

        next_year = future.iloc[0].year
        next_month = future.iloc[0].month

        next_month_expiries = future[
            (future.dt.year == next_year) & (future.dt.month == next_month)
        ]

        expiry = next_month_expiries.iloc[-1]

        dataframe = self.df[self.df["EXPIRY"] == expiry].copy().reset_index(drop=True)

        return OptionChain(dataframe)

    # ==========================================================
    # LEAPS
    # ==========================================================

    def leaps(self) -> pd.Series:
        """
        Returns all expiries beyond the current year.
        """

        expiries = self.expiries()

        first = expiries.iloc[0]

        return expiries[expiries.dt.year > first.year]

    # ==========================================================
    # Far Month
    # ==========================================================

    def far_month(self) -> "OptionChain":
        """
        Returns the farthest available expiry.
        """

        expiry = self.expiries().iloc[-1]

        dataframe = self.df[self.df["EXPIRY"] == expiry].copy().reset_index(drop=True)

        return OptionChain(dataframe)

    # ==========================================================
    # Expiry Selector
    # ==========================================================

    def by_expiry(
        self,
        expiry_date,
    ) -> "OptionChain":
        """
        Returns a chain for any expiry date.
        """

        expiry = pd.Timestamp(expiry_date)

        dataframe = (
            self.df[self.df["EXPIRY"] == expiry]
            .copy()
            .reset_index(drop=True)
        )

        return OptionChain(dataframe)

    # ==========================================================
    # Calls
    # ==========================================================

    def calls(self) -> "OptionChain":
        """
        Returns only Call Options.
        """

        dataframe = (
            self.df[self.df["OPTION_TYPE"] == "CE"].copy().reset_index(drop=True)
        )

        return OptionChain(dataframe)

    # ==========================================================
    # Puts
    # ==========================================================

    def puts(self) -> "OptionChain":
        """
        Returns only Put Options.
        """

        dataframe = (
            self.df[self.df["OPTION_TYPE"] == "PE"].copy().reset_index(drop=True)
        )

        return OptionChain(dataframe)

    # ==========================================================
    # Available Strikes
    # ==========================================================

    def strikes(self):
        """
        Returns all available strikes.
        """

        return self.df["STRIKE"].drop_duplicates().sort_values().reset_index(drop=True)

    # ==========================================================
    # ATM Strike
    # ==========================================================

    def atm(self, spot: float):
        """
        Returns nearest ATM strike.
        """

        strikes = self.strikes()

        idx = (strikes - spot).abs().idxmin()

        return strikes.loc[idx]

    # ==========================================================
    # Strike Window
    # ==========================================================

    def window(self, spot: float, width: int = 5) -> "OptionChain":
        """
        Returns strikes around ATM.

        width=5 means:
        5 ITM + ATM + 5 OTM
        """

        strikes = self.strikes()

        atm = self.atm(spot)

        atm_index = strikes[strikes == atm].index[0]

        start = max(0, atm_index - width)
        end = min(len(strikes), atm_index + width + 1)

        selected = strikes.iloc[start:end]

        dataframe = (
            self.df[self.df["STRIKE"].isin(selected)].copy().reset_index(drop=True)
        )

        return OptionChain(dataframe)

    # ==========================================================
    # Summary
    # ==========================================================

    def summary(self):

        return {
            "rows": len(self.df),
            "expiries": len(self.expiries()),
            "strikes": len(self.strikes()),
            "calls": len(self.calls()),
            "puts": len(self.puts()),
        }

    # ==========================================================
    # Copy
    # ==========================================================

    def copy(self) -> "OptionChain":
        """
        Returns a deep copy of the current OptionChain.
        """

        return OptionChain(self.df.copy())

    # ==========================================================
    # Sort
    # ==========================================================

    def sort(self, by, ascending=True) -> "OptionChain":
        """
        Sort by one or more columns.
        """

        dataframe = self.df.sort_values(by=by, ascending=ascending).reset_index(
            drop=True
        )

        return OptionChain(dataframe)

    # ==========================================================
    # Filter
    # ==========================================================

    def filter(self, mask) -> "OptionChain":
        """
        Generic dataframe filter.
        """

        dataframe = self.df[mask].copy().reset_index(drop=True)

        return OptionChain(dataframe)

    # ==========================================================
    # Head
    # ==========================================================

    def head(self, n=5):

        return self.df.head(n)

    # ==========================================================
    # Tail
    # ==========================================================

    def tail(self, n=5):

        return self.df.tail(n)
