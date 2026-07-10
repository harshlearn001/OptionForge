"""
============================================================
OptionForge
Exposure Rule
============================================================
"""

from __future__ import annotations

from optionforge.portfolio.portfolio import Portfolio
from optionforge.risk.rule_result import RuleResult
from optionforge.risk.rules.risk_rule import RiskRule


class ExposureRule(RiskRule):
    """
    Institutional portfolio exposure rule.
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

        exposure = portfolio.capital_utilization

        if exposure <= self._max_exposure:

            return RuleResult(

                rule_name=self.__class__.__name__,

                score=5.0,

                passed=True,

                warnings=(),

                reasons=(

                    "Portfolio exposure within limits.",

                ),

            )

        return RuleResult(

            rule_name=self.__class__.__name__,

            score=min(
                100.0,
                exposure,
            ),

            passed=False,

            warnings=(

                f"Portfolio exposure "
                f"{exposure:.1f}% exceeds "
                f"{self._max_exposure:.1f}%",

            ),

            reasons=(

                "Portfolio exposure exceeds policy.",

            ),

        )

    def __repr__(self) -> str:

        return (

            f"ExposureRule("

            f"max_exposure={self._max_exposure})"

        )