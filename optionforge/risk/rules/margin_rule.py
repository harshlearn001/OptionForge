"""
============================================================
OptionForge
Margin Rule
============================================================
"""

from __future__ import annotations

from optionforge.portfolio.portfolio import Portfolio
from optionforge.risk.rule_result import RuleResult
from optionforge.risk.rules.risk_rule import RiskRule


class MarginRule(RiskRule):
    """
    Institutional margin utilization rule.
    """

    def __init__(
        self,
        *,
        max_margin: float = 75.0,
    ) -> None:

        self._max_margin = max_margin

    @property
    def max_margin(self) -> float:

        return self._max_margin

    def evaluate(
        self,
        *,
        portfolio: Portfolio,
    ) -> RuleResult:

        margin = portfolio.capital_utilization

        if margin <= self._max_margin:

            return RuleResult(
                rule_name=self.__class__.__name__,
                score=5.0,
                passed=True,
                warnings=(),
                reasons=("Margin utilization within limits.",),
            )

        return RuleResult(
            rule_name=self.__class__.__name__,
            score=min(
                100.0,
                margin,
            ),
            passed=False,
            warnings=(
                f"Margin utilization "
                f"{margin:.1f}% exceeds "
                f"{self._max_margin:.1f}%",
            ),
            reasons=("Margin utilization exceeds policy.",),
        )

    def __repr__(self) -> str:

        return f"MarginRule(" f"max_margin={self._max_margin})"
