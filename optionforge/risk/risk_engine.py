"""
============================================================
OptionForge
Risk Engine
============================================================

Author      : OptionForge
Module      : risk_engine.py

Purpose
-------
Institutional Risk Engine.

Evaluates a Portfolio by executing all registered
risk rules and produces the final Risk object.

============================================================
"""

from __future__ import annotations

from optionforge.portfolio.portfolio import Portfolio
from optionforge.risk.risk import Risk
from optionforge.risk.risk_builder import RiskBuilder
from optionforge.risk.risk_registry import RiskRegistry
from optionforge.risk.risk_result import RiskResult


class RiskEngine:
    """
    Institutional Risk Engine.
    """

    def __init__(
        self,
        *,
        builder: RiskBuilder | None = None,
    ) -> None:

        self._builder = builder or RiskBuilder()

    @property
    def builder(
        self,
    ) -> RiskBuilder:

        return self._builder

    def evaluate(
        self,
        *,
        portfolio: Portfolio,
    ) -> Risk:
        """
        Evaluate a portfolio.
        """

        rule_results = tuple(

            rule.evaluate(

                portfolio=portfolio,

            )

            for rule in RiskRegistry.default_rules()

        )

        result = RiskResult(

            rule_results=rule_results,

        )

        return self._builder.build(

            result=result,

        )

    def __repr__(
        self,
    ) -> str:

        return (

            f"RiskEngine("

            f"builder={self._builder.__class__.__name__})"

        )