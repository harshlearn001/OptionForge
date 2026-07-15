"""
==============================================================
OptionForge
Dealer Pressure Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class DealerPressureResult:
    """
    Dealer Pressure Result.
    """

    pressure_score: float

    pressure_level: str

    pressure_direction: str

    volatility_bias: str

    confidence: str

    interpretation: str
