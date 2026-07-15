"""
============================================================
OptionForge
Volatility Surface Engine
============================================================

Institutional Volatility Surface Engine

============================================================
"""

from __future__ import annotations

from optionforge.analytics.volatility_surface.volatility_surface_calculator import (
    VolatilitySurfaceCalculator,
)

from optionforge.analytics.volatility_surface.volatility_surface_result import (
    VolatilitySurfaceResult,
)


class VolatilitySurfaceEngine:
    """
    Institutional Volatility Surface Engine.
    """

    def __init__(self):

        self._calculator = VolatilitySurfaceCalculator()

    @property
    def calculator(self):

        return self._calculator

    def calculate(
        self,
        *,
        symbol: str,
        trade_date: int,
        strikes: list[float],
        expiries: list[int],
        ivs: list[float],
    ) -> VolatilitySurfaceResult:

        points = self.calculator.calculate(
            strikes=strikes,
            expiries=expiries,
            ivs=ivs,
        )

        return VolatilitySurfaceResult(
            symbol=symbol,
            trade_date=trade_date,
            points=points,
        )

    def __repr__(self):

        return "VolatilitySurfaceEngine()"

    __str__ = __repr__
