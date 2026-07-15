"""
==============================================================
OptionForge
models/resistance_strength_result.py
--------------------------------------------------------------
Resistance Strength Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ResistanceStrengthResult:
    """
    Resistance Strength Intelligence Result
    """

    resistance: float

    resistance_oi: int

    score: float

    stars: int

    rating: str

    interpretation: str
