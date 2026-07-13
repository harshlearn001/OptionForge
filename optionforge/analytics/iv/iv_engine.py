"""
============================================================
OptionForge
IV Engine
============================================================

Institutional Implied Volatility Engine.

Calculates IV for every option contract in a snapshot.

============================================================
"""

from __future__ import annotations

import pandas as pd

from optionforge.analytics.iv.iv_calculator import (
    IVCalculator,
)

from optionforge.analytics.iv.iv_chain_result import (
    IVChainResult,
)


class IVEngine:
    """
    Institutional IV Engine.
    """

    def __init__(self) -> None:

        self._calculator = IVCalculator()

    @property
    def calculator(self) -> IVCalculator:

        return self._calculator

    def calculate(
        self,
        *,
        symbol: str,
        trade_date: int,
        expiry: int,
        spot: float,
        option_chain: pd.DataFrame,
        time: float,
        rate: float,
    ) -> IVChainResult:

        rows = []

        for _, row in option_chain.iterrows():

            analytics = self.calculator.calculate(

                spot=spot,

                strike=float(row["STRIKE_PRICE"]),

                time=time,

                rate=rate,

                option_type=row["OPT_TYPE"],

                market_price=float(row["CLOSE_PRICE"]),

            )

            rows.append(

                {

                    "STRIKE_PRICE": row["STRIKE_PRICE"],

                    "OPT_TYPE": row["OPT_TYPE"],

                    "CLOSE_PRICE": row["CLOSE_PRICE"],

                    "IV": analytics.implied_volatility,

                    "DELTA": analytics.delta,

                    "GAMMA": analytics.gamma,

                    "THETA": analytics.theta,

                    "VEGA": analytics.vega,

                }

            )

        chain = pd.DataFrame(rows)

        return IVChainResult(

            symbol=symbol,

            trade_date=trade_date,

            expiry=expiry,

            spot=spot,

            chain=chain,

        )

    def __repr__(self):

        return "IVEngine()"

    __str__ = __repr__