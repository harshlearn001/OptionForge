"""
============================================================
OptionForge
Risk Rule
============================================================

Author      : OptionForge
Module      : risk_rule.py

Purpose
-------
Abstract base class for all institutional risk rules.
============================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from optionforge.portfolio.portfolio import Portfolio
from optionforge.risk.rule_result import RuleResult


class RiskRule(ABC):
    """
    Base class for all institutional risk rules.
    """

    @abstractmethod
    def evaluate(
        self,
        *,
        portfolio: Portfolio,
    ) -> RuleResult:
        """
        Evaluate a portfolio.

        Returns
        -------
        RuleResult
            Result produced by the rule.
        """
        raise NotImplementedError