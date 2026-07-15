"""
==============================================================
OptionForge
models/dealer_hedging_flow_result.py
--------------------------------------------------------------
Dealer Hedging Flow Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class DealerHedgingFlowResult:
    """
    Professional Dealer Hedging Flow Result.
    """

    hedging_bias: str

    flow_direction: str

    flow_strength: str

    volatility_effect: str

    market_support: str

    trend_effect: str

    institutional_score: float

    confidence: str

    recommendation: str

    interpretation: str
