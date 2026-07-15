"""
============================================================
OptionForge
Dealer Engine
============================================================

Institutional Dealer Position Engine.

============================================================
"""

from __future__ import annotations

from optionforge.analytics.dealer.dealer_calculator import (
    DealerCalculator,
)

from optionforge.analytics.dealer.dealer_result import (
    DealerResult,
)


class DealerEngine:
    """
    Institutional Dealer Position Engine.
    """

    def calculate(
        self,
        snapshot,
    ) -> DealerResult:

        calc = DealerCalculator(
            snapshot.option_chain,
        )

        total_call = calc.total_call_oi()

        total_put = calc.total_put_oi()

        major_call = calc.major_call_strike()

        major_put = calc.major_put_strike()

        net = calc.call_put_difference()

        spot = float(snapshot.spot["CLOSE"].iloc[-1])

        if net > 0:

            bias = "Bullish"

        elif net < 0:

            bias = "Bearish"

        else:

            bias = "Neutral"

        total = max(
            total_call + total_put,
            1,
        )

        confidence = round(
            abs(net) / total * 100,
            2,
        )

        return DealerResult(
            symbol=snapshot.symbol,
            trade_date=snapshot.trade_date,
            expiry=snapshot.expiry,
            spot=spot,
            major_call_strike=major_call,
            major_put_strike=major_put,
            total_call_oi=total_call,
            total_put_oi=total_put,
            net_oi=net,
            dealer_bias=bias,
            confidence=confidence,
            contracts=len(snapshot.option_chain),
        )

    def __repr__(self):

        return "DealerEngine()"

    __str__ = __repr__
