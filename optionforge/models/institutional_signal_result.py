"""
==============================================================
OptionForge
models/institutional_signal_result.py
--------------------------------------------------------------
Institutional Signal Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class InstitutionalSignalResult:
    """
    Institutional Signal Result.
    """

    overall_signal: str

    signal_strength: float

    market_regime: str

    volatility_outlook: str

    dealer_regime: str

    risk_level: str

    confidence: str

    action: str

    summary: str