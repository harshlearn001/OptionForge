"""
============================================================
OptionForge
Capital Rule
============================================================
"""

from __future__ import annotations


from optionforge.portfolio.portfolio import Portfolio
from optionforge.risk.rule_result import RuleResult
from optionforge.risk.rules.risk_rule import RiskRule


class CapitalRule(RiskRule):
    """
    Institutional capital utilization policy.
    """

    def __init__(
        self,
        *,
        max_utilization: float = 80.0,
    ) -> None:

        self._max_utilization = max_utilization

    @property
    def max_utilization(self) -> float:

        return self._max_utilization

    def evaluate(
        self,
        *,
        portfolio: Portfolio,
    ) -> RuleResult:

        utilization = portfolio.capital_utilization

        if utilization <= self._max_utilization:

            return RuleResult(
                rule_name=self.__class__.__name__,
                score=5.0,
                passed=True,
                warnings=(),
                reasons=("Capital allocation within limits",),
            )

        return RuleResult(
            rule_name=self.__class__.__name__,
            score=min(
                100.0,
                utilization,
            ),
            passed=False,
            warnings=(
                f"Capital utilization "
                f"{utilization:.1f}% exceeds "
                f"{self._max_utilization:.1f}%",
            ),
            reasons=("Capital allocation exceeds policy.",),
        )

    def __repr__(self) -> str:

        return f"CapitalRule(" f"max_utilization={self._max_utilization})"
