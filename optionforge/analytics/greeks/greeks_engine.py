"""
============================================================
OptionForge
Greeks Engine
============================================================

Institutional Greeks Engine.

============================================================
"""

from __future__ import annotations

from optionforge.analytics.greeks.greeks_calculator import (
    GreeksCalculator,
)

from optionforge.analytics.greeks.greeks_result import (
    GreeksResult,
)


class GreeksEngine:
    """
    Institutional Greeks Engine.
    """

    def __init__(self) -> None:

        self._calculator = GreeksCalculator()

    @property
    def calculator(self) -> GreeksCalculator:

        return self._calculator

    def calculate(
        self,
        *,
        symbol: str,
        trade_date: int,
        expiry: int,
        spot: float,
        strike: float,
        time: float,
        rate: float,
        volatility: float,
        option_type: str,
        market_price: float | None = None,
    ) -> GreeksResult:

        analytics = self.calculator.calculate(

            spot=spot,

            strike=strike,

            time=time,

            rate=rate,

            volatility=volatility,

            option_type=option_type,

            market_price=market_price,

        )

        return GreeksResult(

            symbol=symbol,

            trade_date=trade_date,

            expiry=expiry,

            strike=strike,

            spot=spot,

            option_type=option_type,

            option_price=analytics.price,

            implied_volatility=analytics.implied_volatility,

            delta=analytics.delta,

            gamma=analytics.gamma,

            theta=analytics.theta,

            vega=analytics.vega,

        )

    def __repr__(self):

        return "GreeksEngine()"

    __str__ = __repr__