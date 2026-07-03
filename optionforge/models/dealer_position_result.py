"""
==============================================================
OptionForge
models/dealer_position_result.py
--------------------------------------------------------------
Dealer Position Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class DealerPositionResult:
    """
    Overall Dealer Positioning Result.
    """

    dealer_bias: str

    dealer_direction: str

    market_condition: str

    market_stability: str

    directional_risk: str

    institutional_score: float

    confidence: str

    recommendation: str

    interpretation: str