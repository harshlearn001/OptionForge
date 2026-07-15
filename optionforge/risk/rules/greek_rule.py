"""
============================================================
OptionForge
Greek Rule
============================================================
"""

from __future__ import annotations

from optionforge.portfolio.portfolio import Portfolio
from optionforge.risk.rule_result import RuleResult
from optionforge.risk.rules.risk_rule import RiskRule


class GreekRule(RiskRule):
    """
    Institutional portfolio Greeks rule.

    Currently evaluates aggregate Greek exposure.
    """

    def __init__(
        self,
        *,
        max_exposure: float = 75.0,
    ) -> None:

        self._max_exposure = max_exposure

    @property
    def max_exposure(self) -> float:
        return self._max_exposure

    def evaluate(
        self,
        *,
        portfolio: Portfolio,
    ) -> RuleResult:

        greek_exposure = portfolio.capital_utilization

        if greek_exposure <= self._max_exposure:

            return RuleResult(
                rule_name=self.__class__.__name__,
                score=5.0,
                passed=True,
                warnings=(),
                reasons=("Greek exposure within limits.",),
            )

        return RuleResult(
            rule_name=self.__class__.__name__,
            score=min(
                100.0,
                greek_exposure,
            ),
            passed=False,
            warnings=(
                f"Greek exposure "
                f"{greek_exposure:.1f}% exceeds "
                f"{self._max_exposure:.1f}%",
            ),
            reasons=("Greek exposure exceeds policy.",),
        )

    def __repr__(self) -> str:

        return f"GreekRule(" f"max_exposure={self._max_exposure})"
