"""
==============================================================
OptionForge
models/support_strength_result.py
--------------------------------------------------------------
Support Strength Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class SupportStrengthResult:
    """
    Support Strength Intelligence Result
    """

    support: float

    support_oi: int

    score: float

    stars: int

    rating: str

    interpretation: str