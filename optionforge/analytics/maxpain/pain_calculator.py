"""
============================================================
OptionForge
Pain Calculator
============================================================

Calculate call pain, put pain and total pain for every strike.

============================================================
"""

from __future__ import annotations

import pandas as pd


class PainCalculator:
    """
    Calculates option writer pain.
    """

    def __init__(
        self,
        option_chain: pd.DataFrame,
    ) -> None:

        self._df = option_chain.copy()

    # -----------------------------------------------------

    @property
    def option_chain(self) -> pd.DataFrame:

        return self._df

    # -----------------------------------------------------

    def calculate(
        self,
    ) -> pd.DataFrame:
        """
        Calculate pain at every strike.
        """

        df = self.option_chain

        strikes = sorted(
            df["STRIKE_PRICE"]
            .drop_duplicates()
            .tolist()
        )

        rows = []

        for settlement in strikes:

            call_pain = 0.0
            put_pain = 0.0

            # Calls
            calls = df[df["OPT_TYPE"] == "CE"]

            for _, row in calls.iterrows():

                intrinsic = max(
                    settlement - row["STRIKE_PRICE"],
                    0,
                )

                call_pain += (
                    intrinsic *
                    row["OPEN_INT"]
                )

            # Puts
            puts = df[df["OPT_TYPE"] == "PE"]

            for _, row in puts.iterrows():

                intrinsic = max(
                    row["STRIKE_PRICE"] - settlement,
                    0,
                )

                put_pain += (
                    intrinsic *
                    row["OPEN_INT"]
                )

            rows.append(

                {

                    "STRIKE_PRICE": settlement,

                    "CALL_PAIN": call_pain,

                    "PUT_PAIN": put_pain,

                    "TOTAL_PAIN": call_pain + put_pain,

                }

            )

        return pd.DataFrame(rows)

    # -----------------------------------------------------

    def __repr__(self):

        return "PainCalculator()"

    __str__ = __repr__