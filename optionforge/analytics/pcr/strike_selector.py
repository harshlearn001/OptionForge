"""
============================================================
OptionForge
Strike Selector
============================================================

Selects important strikes from an option chain.

============================================================
"""

from __future__ import annotations

import pandas as pd


class StrikeSelector:

    def __init__(
        self,
        option_chain: pd.DataFrame,
    ) -> None:

        self.df = option_chain.copy()

    # -----------------------------------------------------

    def available_strikes(self) -> list[int]:

        return sorted(self.df["STRIKE_PRICE"].drop_duplicates().tolist())

    # -----------------------------------------------------

    def atm_strike(
        self,
        spot_price: float,
    ) -> int:

        strikes = self.available_strikes()

        return min(
            strikes,
            key=lambda strike: abs(strike - spot_price),
        )

    # -----------------------------------------------------

    def major_call_strike(self) -> int:

        calls = self.df[self.df["OPT_TYPE"] == "CE"]

        idx = calls["OPEN_INT"].idxmax()

        return int(
            calls.loc[
                idx,
                "STRIKE_PRICE",
            ]
        )

    # -----------------------------------------------------

    def major_put_strike(self) -> int:

        puts = self.df[self.df["OPT_TYPE"] == "PE"]

        idx = puts["OPEN_INT"].idxmax()

        return int(
            puts.loc[
                idx,
                "STRIKE_PRICE",
            ]
        )

    # -----------------------------------------------------

    def nearest_strikes(
        self,
        center: int,
        count: int = 5,
    ) -> list[int]:

        strikes = self.available_strikes()

        strikes.sort()

        if center not in strikes:

            raise ValueError(f"{center} not found.")

        index = strikes.index(center)

        start = max(
            0,
            index - count,
        )

        end = min(
            len(strikes),
            index + count + 1,
        )

        return strikes[start:end]

    # -----------------------------------------------------

    def __repr__(self):

        return f"StrikeSelector(" f"{len(self.df):,} contracts)"

    __str__ = __repr__
