"""
============================================================
OptionForge
IV Rank Engine
============================================================

Institutional IV Rank Engine.

============================================================
"""

from __future__ import annotations

from optionforge.analytics.iv_rank.iv_rank_calculator import (
    IVRankCalculator,
)

from optionforge.analytics.iv_rank.iv_rank_result import (
    IVRankResult,
)


class IVRankEngine:
    """
    Institutional IV Rank Engine.
    """

    def __init__(self) -> None:

        self._calculator = IVRankCalculator()

    @property
    def calculator(self) -> IVRankCalculator:

        return self._calculator

    def calculate(
        self,
        *,
        symbol: str,
        trade_date: int,
        expiry: int,
        current_iv: float,
        historical_iv: list[float],
    ) -> IVRankResult:

        if not historical_iv:
            raise ValueError("historical_iv cannot be empty.")

        lowest_iv = min(historical_iv)

        highest_iv = max(historical_iv)

        iv_rank = self.calculator.calculate(
            current_iv=current_iv,
            lowest_iv=lowest_iv,
            highest_iv=highest_iv,
        )

        return IVRankResult(
            symbol=symbol,
            trade_date=trade_date,
            expiry=expiry,
            current_iv=current_iv,
            lowest_iv=lowest_iv,
            highest_iv=highest_iv,
            iv_rank=iv_rank,
        )

    def __repr__(self):

        return "IVRankEngine()"

    __str__ = __repr__
