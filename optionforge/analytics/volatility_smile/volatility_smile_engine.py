"""
============================================================
OptionForge
Volatility Smile Engine
============================================================

Institutional Volatility Smile Engine

============================================================
"""

from __future__ import annotations

from optionforge.analytics.volatility_smile.volatility_smile_calculator import (
    VolatilitySmileCalculator,
)

from optionforge.analytics.volatility_smile.volatility_smile_result import (
    VolatilitySmileResult,
)


class VolatilitySmileEngine:
    """
    Institutional Volatility Smile Engine.
    """

    def __init__(self):

        self._calculator = VolatilitySmileCalculator()

    @property
    def calculator(self):

        return self._calculator

    def calculate(
        self,
        *,
        symbol: str,
        trade_date: int,
        expiry: int,
        strikes: list[float],
        ivs: list[float],
    ) -> VolatilitySmileResult:

        points = self.calculator.calculate(

            strikes=strikes,

            ivs=ivs,

        )

        return VolatilitySmileResult(

            symbol=symbol,

            trade_date=trade_date,

            expiry=expiry,

            points=points,

        )

    def __repr__(self):

        return "VolatilitySmileEngine()"

    __str__ = __repr__