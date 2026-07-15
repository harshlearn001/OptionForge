"""
============================================================
OptionForge
Greeks Calculator
============================================================

Business layer wrapper around the quantitative API.

============================================================
"""

from __future__ import annotations

from optionforge.quant.analytics import (
    AnalyticsResult,
    OptionAnalytics,
)


class GreeksCalculator:
    """
    Calculator for option Greeks.
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
        volatility: float,
        option_type: str,
        market_price: float | None = None,
    ) -> AnalyticsResult:

        return self.analytics.calculate(
            spot=spot,
            strike=strike,
            time=time,
            rate=rate,
            volatility=volatility,
            option_type=option_type,
            market_price=market_price,
        )

    def __repr__(self):

        return "GreeksCalculator()"

    __str__ = __repr__
