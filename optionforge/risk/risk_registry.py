"""
============================================================
OptionForge
Risk Registry
============================================================

Author      : OptionForge
Module      : risk_registry.py

Purpose
-------
Registry of institutional risk rules.

Provides the default collection of rules used by the
Risk Engine.

============================================================
"""

from __future__ import annotations

from optionforge.risk.rules.capital_rule import CapitalRule
from optionforge.risk.rules.drawdown_rule import DrawdownRule
from optionforge.risk.rules.exposure_rule import ExposureRule
from optionforge.risk.rules.greek_rule import GreekRule
from optionforge.risk.rules.liquidity_rule import LiquidityRule
from optionforge.risk.rules.margin_rule import MarginRule
from optionforge.risk.rules.risk_rule import RiskRule


class RiskRegistry:
    """
    Registry of institutional risk rules.
    """

    @staticmethod
    def default_rules() -> tuple[RiskRule, ...]:
        """
        Return the default institutional rule set.
        """

        return (

            CapitalRule(),

            MarginRule(),

            ExposureRule(),

            LiquidityRule(),

            GreekRule(),

            DrawdownRule(),

        )