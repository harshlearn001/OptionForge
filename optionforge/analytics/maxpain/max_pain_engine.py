"""
============================================================
OptionForge
Max Pain Engine
============================================================

Institutional Max Pain Engine.

Uses:
    - PainCalculator
    - MaxPainResult

============================================================
"""

from __future__ import annotations

from optionforge.analytics.maxpain.pain_calculator import (
    PainCalculator,
)

from optionforge.analytics.maxpain.max_pain_result import (
    MaxPainResult,
)


class MaxPainEngine:
    """
    Institutional Max Pain Engine.
    """

    def calculate(
        self,
        snapshot,
    ) -> MaxPainResult:

        calculator = PainCalculator(

            snapshot.option_chain,

        )

        pain_table = calculator.calculate()

        row = pain_table.loc[
            pain_table["TOTAL_PAIN"].idxmin()
        ]

        spot = float(

            snapshot.spot["CLOSE"].iloc[-1]

        )

        strike = int(

            row["STRIKE_PRICE"]

        )

        return MaxPainResult(

            symbol=snapshot.symbol,

            trade_date=snapshot.trade_date,

            expiry=snapshot.expiry,

            spot=spot,

            max_pain_strike=strike,

            total_pain=float(row["TOTAL_PAIN"]),

            call_pain=float(row["CALL_PAIN"]),

            put_pain=float(row["PUT_PAIN"]),

            distance_from_spot=abs(
                spot - strike
            ),

            contracts=len(snapshot.option_chain),

        )

    # -----------------------------------------------------

    def __repr__(self):

        return "MaxPainEngine()"

    __str__ = __repr__