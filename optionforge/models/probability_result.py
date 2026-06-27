"""
==============================================================
OptionForge
models/probability_result.py
--------------------------------------------------------------
Probability Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ProbabilityResult:
    """
    Professional Probability Intelligence Result
    """

    bullish_probability: float

    bearish_probability: float

    confidence: str

    stars: int

    trade_quality: str

    risk_level: str

    recommendation: str

    interpretation: str