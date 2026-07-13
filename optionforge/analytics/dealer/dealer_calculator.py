"""
============================================================
OptionForge
Dealer Calculator
============================================================

Calculate dealer positioning statistics.

============================================================
"""

from __future__ import annotations

import pandas as pd


class DealerCalculator:
    """
    Dealer positioning calculations.
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

    def total_call_oi(self) -> int:
        """
        Total Call Open Interest.
        """

        return int(

            self.option_chain.loc[
                self.option_chain["OPT_TYPE"] == "CE",
                "OPEN_INT",
            ].sum()

        )

    # -----------------------------------------------------

    def total_put_oi(self) -> int:
        """
        Total Put Open Interest.
        """

        return int(

            self.option_chain.loc[
                self.option_chain["OPT_TYPE"] == "PE",
                "OPEN_INT",
            ].sum()

        )

    # -----------------------------------------------------

    def major_call_strike(self) -> int:
        """
        Strike with maximum Call OI.
        """

        calls = self.option_chain.loc[
            self.option_chain["OPT_TYPE"] == "CE"
        ]

        row = calls.loc[
            calls["OPEN_INT"].idxmax()
        ]

        return int(row["STRIKE_PRICE"])

    # -----------------------------------------------------

    def major_put_strike(self) -> int:
        """
        Strike with maximum Put OI.
        """

        puts = self.option_chain.loc[
            self.option_chain["OPT_TYPE"] == "PE"
        ]

        row = puts.loc[
            puts["OPEN_INT"].idxmax()
        ]

        return int(row["STRIKE_PRICE"])

    # -----------------------------------------------------

    def call_put_difference(self) -> int:
        """
        Net Put OI minus Call OI.
        """

        return (

            self.total_put_oi()

            -

            self.total_call_oi()

        )

    # -----------------------------------------------------

    def __repr__(self):

        return "DealerCalculator()"

    __str__ = __repr__