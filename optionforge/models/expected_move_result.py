"""
==============================================================
OptionForge
models/expected_move_result.py
--------------------------------------------------------------
Expected Move Result Model
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ExpectedMoveResult:
    """
    Result returned by ExpectedMove engine.
    """

    expected_move: float

    upper_68: float
    lower_68: float

    upper_95: float
    lower_95: float

    one_day_move: float
    weekly_move: float
    monthly_move: float
