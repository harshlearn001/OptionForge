"""
============================================================
OptionForge
Capital Rule
============================================================

Author      : OptionForge
Module      : capital_rule.py

Purpose
-------
Evaluates portfolio capital allocation.

This rule contributes to the institutional risk
assessment by measuring total capital utilization.

============================================================
"""

from __future__ import annotations

from optionforge.portfolio.portfolio import (
    Portfolio,
)

from optionforge.risk.rules.risk_rule import (
    RiskRule,
)
from tests.portfolio.test_portfolio import portfolio


class CapitalRule(RiskRule):
    """
    Institutional capital allocation rule.
    """

    # =====================================================
    # Constructor
    # =====================================================

    def __init__(
        self,
        *,
        max_utilization: float = 80.0,
    ) -> None:

        self._max_utilization = max_utilization

    # =====================================================
    # Public API
    # =====================================================

    def evaluate(
        self,
        *,
        portfolio: Portfolio,
    ) -> tuple[
        float,
        tuple[str, ...],
        tuple[str, ...],
    ]:

        utilization = portfolio.capital_utilization

        if utilization <= self._max_utilization:

            return (

                5.0,

                (),

                (

                    "Capital allocation within limits",

                ),

            )
        warnings = (
                        f"Capital utilization "

            f"{utilization:.1f}% "

            f"exceeds "

            f"{self._max_utilization:.1f}%."

        )

        return (

            min(

                100.0,

                utilization,

            ),

            (

                warning,

            ),

            (

                "Capital allocation exceeds policy.",

            ),

        )

    # =====================================================
    # Convenience
    # =====================================================

    @property
    def max_utilization(
        self,
    ) -> float:
        """
        Maximum permitted capital utilization.
        """

        return self._max_utilization

    # =====================================================
    # Representation
    # =====================================================

    def __repr__(
        self,
    ) -> str:

        return (

            f"{self.__class__.__name__}("

            f"max_utilization="

            f"{self._max_utilization})"

        )
        