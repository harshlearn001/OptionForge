"""
==============================================================
OptionForge
models/analytics_result.py
--------------------------------------------------------------
Analytics Result Model
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class AnalyticsResult:
    """
    Stores complete option analytics.
    """

    implied_volatility: float

    delta: float

    gamma: float

    theta: float

    vega: float

    intrinsic_value: float

    time_value: float