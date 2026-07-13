"""
============================================================
OptionForge
IV Percentile Engine
============================================================

Institutional IV Percentile Engine.

============================================================
"""

from __future__ import annotations

from optionforge.analytics.iv_percentile.iv_percentile_calculator import (
    IVPercentileCalculator,
)

from optionforge.analytics.iv_percentile.iv_percentile_result import (
    IVPercentileResult,
)


class IVPercentileEngine:
    """
    Institutional IV Percentile Engine.
    """

    def __init__(self) -> None:

        self._calculator = IVPercentileCalculator()

    @property
    def calculator(self) -> IVPercentileCalculator:

        return self._calculator

    def calculate(
        self,
        *,
        symbol: str,
        trade_date: int,
        expiry: int,
        current_iv: float,
        historical_iv: list[float],
    ) -> IVPercentileResult:

        if not historical_iv:
            raise ValueError(
                "historical_iv cannot be empty."
            )

        percentile = self.calculator.calculate(

            current_iv=current_iv,

            historical_iv=historical_iv,

        )

        return IVPercentileResult(

            symbol=symbol,

            trade_date=trade_date,

            expiry=expiry,

            current_iv=current_iv,

            historical_observations=len(historical_iv),

            iv_percentile=percentile,

        )

    def __repr__(self):

        return "IVPercentileEngine()"

    __str__ = __repr__