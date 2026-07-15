"""
============================================================
OptionForge
Risk-Free Rate Provider
============================================================

Provides risk-free interest rates for quantitative analytics.

============================================================
"""

from __future__ import annotations


class RiskFreeRateProvider:
    """
    Risk-free rate provider.

    Future versions can load:

    • RBI Repo Rate
    • Treasury Yield
    • Historical Yield Curve
    """

    DEFAULT_RATE = 0.06

    def current_rate(self) -> float:
        """
        Return current annualized risk-free rate.
        """

        return self.DEFAULT_RATE

    def __repr__(self):

        return f"RiskFreeRateProvider(" f"default_rate={self.DEFAULT_RATE})"

    __str__ = __repr__
