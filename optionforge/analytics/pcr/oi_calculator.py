"""
============================================================
OptionForge
OI Calculator
============================================================

Reusable Open Interest calculator.

============================================================
"""

from __future__ import annotations

import pandas as pd


class OICalculator:

    def __init__(
        self,
        option_chain: pd.DataFrame,
    ) -> None:

        self.df = option_chain.copy()

    # -----------------------------------------------------

    @property
    def calls(self) -> pd.DataFrame:

        return self.df[
            self.df["OPT_TYPE"] == "CE"
        ]

    # -----------------------------------------------------

    @property
    def puts(self) -> pd.DataFrame:

        return self.df[
            self.df["OPT_TYPE"] == "PE"
        ]

    # -----------------------------------------------------

    def total_call_oi(self) -> int:

        return int(

            self.calls["OPEN_INT"].sum()

        )

    # -----------------------------------------------------

    def total_put_oi(self) -> int:

        return int(

            self.puts["OPEN_INT"].sum()

        )

    # -----------------------------------------------------

    def call_oi(
        self,
        strike: int,
    ) -> int:

        df = self.calls

        return int(

            df.loc[
                df["STRIKE_PRICE"] == strike,
                "OPEN_INT",
            ].sum()

        )

    # -----------------------------------------------------

    def put_oi(
        self,
        strike: int,
    ) -> int:

        df = self.puts

        return int(

            df.loc[
                df["STRIKE_PRICE"] == strike,
                "OPEN_INT",
            ].sum()

        )

    # -----------------------------------------------------

    def max_call_oi(self) -> int:

        return int(

            self.calls["OPEN_INT"].max()

        )

    # -----------------------------------------------------

    def max_put_oi(self) -> int:

        return int(

            self.puts["OPEN_INT"].max()

        )

    # -----------------------------------------------------

    def classic_pcr(self) -> float:

        call = self.total_call_oi()

        put = self.total_put_oi()

        if call == 0:

            return 0.0

        return round(

            put / call,

            4,

        )

    # -----------------------------------------------------

    def __repr__(self):

        return (

            f"OICalculator("

            f"{len(self.df):,} contracts)"

        )

    __str__ = __repr__