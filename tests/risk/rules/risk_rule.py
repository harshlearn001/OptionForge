"""
============================================================
OptionForge
Risk Rule
============================================================

Author      : OptionForge
Module      : risk_rule.py

Purpose
-------
Abstract base class for institutional risk rules.

Every risk rule evaluates a portfolio (or position)
and contributes to the overall Risk assessment.

============================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from optionforge.portfolio.portfolio import (
    Portfolio,
)


class RiskRule(ABC):
    """
    Base class for all institutional risk rules.
    """

    @abstractmethod
    def evaluate(
        self,
        *,
        portfolio: Portfolio,
    ) -> tuple[
        float,
        tuple[str, ...],
        tuple[str, ...],
    ]:
        """
        Evaluate a portfolio.

        Returns
        -------
        tuple

            (
                score,
                warnings,
                reasons,
            )
        """

        raise NotImplementedError
