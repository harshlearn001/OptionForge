"""
==============================================================
OptionForge
models/market_snapshot.py
--------------------------------------------------------------
Market Snapshot Model
==============================================================
"""

from __future__ import annotations
from dataclasses import dataclass
from datetime import date
import pandas as pd


@dataclass(slots=True)
class MarketSnapshot:
    """
    Represents the complete option market
    at one point in time.
    """

    symbol: str

    trade_date: date

    spot_price: float

    future_price: float

    option_chain: pd.DataFrame

    # -------------------------------------------------
    # Basic Information
    # -------------------------------------------------

    @property
    def total_contracts(self) -> int:

        return len(self.option_chain)

    @property
    def expiries(self):

        return sorted(
            self.option_chain["EXPIRY_DATE"]
            .drop_duplicates()
            .tolist()
        )

    # -------------------------------------------------
    # Filters
    # -------------------------------------------------

    def calls(self):

        return self.option_chain[
            self.option_chain["OPTION_TYPE"] == "CE"
        ]

    def puts(self):

        return self.option_chain[
            self.option_chain["OPTION_TYPE"] == "PE"
        ]

    def expiry(self, expiry_date):

        return self.option_chain[
            self.option_chain["EXPIRY_DATE"] == expiry_date
        ]

    # -------------------------------------------------
    # Market Statistics
    # -------------------------------------------------

    def total_call_oi(self):

        return self.calls()["OPEN_INTEREST"].sum()

    def total_put_oi(self):

        return self.puts()["OPEN_INTEREST"].sum()

    def total_volume(self):

        return self.option_chain["OPTION_VOLUME"].sum()
    
    def atm(self) -> int:
        """
        Returns the strike nearest to spot.
        """

        strikes = self.option_chain["STRIKE_PRICE"].drop_duplicates()

        return min(
            strikes,
            key=lambda x: abs(x - self.spot_price)
        )
    
    def nearest_expiry(self) -> date:
        """
        Returns the nearest expiry.
        """

        return min(self.expiries)
    
    def max_call_oi(self):

        calls = self.calls()

        row = calls.loc[
            calls["OPEN_INTEREST"].idxmax()
        ]

        return row["STRIKE_PRICE"]
    
    def max_put_oi(self):

        puts = self.puts()

        row = puts.loc[
            puts["OPEN_INTEREST"].idxmax()
        ]

        return row["STRIKE_PRICE"]
    
    def pcr(self):

        call_oi = self.total_call_oi()

        put_oi = self.total_put_oi()

        if call_oi == 0:
            return 0.0

        return put_oi / call_oi
    
    def summary(self):

        return {

            "Symbol": self.symbol,

            "Trade Date": self.trade_date,

            "Spot": self.spot_price,

            "Future": self.future_price,

            "Contracts": self.total_contracts,

            "Expiries": len(self.expiries),

            "ATM": self.atm(),

            "PCR": round(self.pcr(), 3),

            "Call OI": self.total_call_oi(),

            "Put OI": self.total_put_oi(),

            "Volume": self.total_volume(),

            "Max Call OI": self.max_call_oi(),

            "Max Put OI": self.max_put_oi(),

        }