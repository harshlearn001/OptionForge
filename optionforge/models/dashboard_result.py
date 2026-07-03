"""
==============================================================
OptionForge
models/dashboard_result.py
--------------------------------------------------------------
Institutional Dashboard Result
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class DashboardResult:
    """
    Institutional Dashboard Result.
    """

    dealer_bias: str

    dealer_direction: str

    gamma_status: str

    zero_gamma_status: str

    hedging_flow: str

    institutional_score: float

    confidence: str

    market_bias: str

    risk_level: str

    summary: str