"""
==============================================================
OptionForge
intelligence/expected_move.py
--------------------------------------------------------------
Expected Move Intelligence Engine
==============================================================
"""

from math import sqrt

from optionforge.models import ExpectedMoveResult


class ExpectedMove:
    """
    Institutional Expected Move Calculator
    """

    @staticmethod
    def calculate(
        *,
        spot: float,
        atm_iv: float,
        days: int,
    ) -> ExpectedMoveResult:

        if spot <= 0:
            raise ValueError("Spot price must be positive.")

        if atm_iv <= 0:
            raise ValueError("ATM IV must be positive.")

        if days <= 0:
            raise ValueError("Days must be positive.")

        # --------------------------------------------------
        # Expected Move
        # --------------------------------------------------

        expected_move = spot * atm_iv * sqrt(days / 365)

        # --------------------------------------------------
        # Standard Deviation Ranges
        # --------------------------------------------------

        upper_68 = spot + expected_move
        lower_68 = spot - expected_move

        upper_95 = spot + (2 * expected_move)
        lower_95 = spot - (2 * expected_move)

        # --------------------------------------------------
        # Daily / Weekly / Monthly Expected Move
        # --------------------------------------------------

        one_day_move = spot * atm_iv * sqrt(1 / 365)

        weekly_move = spot * atm_iv * sqrt(7 / 365)

        monthly_move = spot * atm_iv * sqrt(30 / 365)

        return ExpectedMoveResult(
            expected_move=expected_move,
            upper_68=upper_68,
            lower_68=lower_68,
            upper_95=upper_95,
            lower_95=lower_95,
            one_day_move=one_day_move,
            weekly_move=weekly_move,
            monthly_move=monthly_move,
        )
