"""
============================================================
OptionForge
IV Calculator
============================================================

Calculate implied volatility for an option contract.

============================================================
"""

from __future__ import annotations

from optionforge.quant.analytics import (
    AnalyticsResult,
    OptionAnalytics,
)


class IVCalculator:
    """
    Business layer wrapper around OptionAnalytics.
    """

    def __init__(self) -> None:

        self._analytics = OptionAnalytics()

    @property
    def analytics(self) -> OptionAnalytics:

        return self._analytics

    def calculate(
        self,
        *,
        spot: float,
        strike: float,
        time: float,
        rate: float,
        option_type: str,
        market_price: float,
    ) -> AnalyticsResult:

        return self.analytics.calculate(

            spot=spot,

            strike=strike,

            time=time,

            rate=rate,

            volatility=0.20,

            option_type=option_type,

            market_price=market_price,

        )

    def __repr__(self):

        return "IVCalculator()"

    __str__ = __repr__