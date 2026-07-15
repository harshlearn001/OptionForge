"""
============================================================
OptionForge
Expected Move Engine
============================================================

Institutional Expected Move Engine.

============================================================
"""

from __future__ import annotations

from optionforge.analytics.expected_move.expected_move_calculator import (
    ExpectedMoveCalculator,
)

from optionforge.analytics.expected_move.expected_move_result import (
    ExpectedMoveResult,
)


class ExpectedMoveEngine:
    """
    Institutional Expected Move Engine.
    """

    def __init__(self) -> None:

        self._calculator = ExpectedMoveCalculator()

    @property
    def calculator(self) -> ExpectedMoveCalculator:

        return self._calculator

    def calculate(
        self,
        *,
        symbol: str,
        trade_date: int,
        expiry: int,
        spot: float,
        volatility: float,
        time: float,
    ) -> ExpectedMoveResult:

        expected_move = self.calculator.calculate(
            spot=spot,
            volatility=volatility,
            time=time,
        )

        return ExpectedMoveResult(
            symbol=symbol,
            trade_date=trade_date,
            expiry=expiry,
            spot=spot,
            volatility=volatility,
            time=time,
            expected_move=expected_move,
            upper_bound=spot + expected_move,
            lower_bound=spot - expected_move,
        )

    def __repr__(self):

        return "ExpectedMoveEngine()"

    __str__ = __repr__
