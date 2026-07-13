"""
============================================================
OptionForge
Analytics Configuration
============================================================

Central configuration for quantitative analytics.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class AnalyticsConfig:
    """
    Global analytics configuration.
    """

    risk_free_rate: float = 0.06

    trading_days_per_year: int = 252

    calendar_days_per_year: int = 365

    default_volatility: float = 0.20

    iv_precision: int = 6

    def __repr__(self):

        return (

            f"AnalyticsConfig("

            f"risk_free_rate={self.risk_free_rate}, "

            f"default_volatility={self.default_volatility})"

        )

    __str__ = __repr__