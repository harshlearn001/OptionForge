"""
==============================================================
OptionForge
Market Explosion Risk Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class MarketExplosionRiskResult:
    """
    Market Explosion Risk Result.
    """

    explosion_score: float

    explosion_probability: str

    market_state: str

    expected_behavior: str

    recommendation: str

    confidence: str

    interpretation: str
