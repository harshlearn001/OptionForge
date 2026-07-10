"""
============================================================
OptionForge
Liquidity Rule
============================================================
"""

from __future__ import annotations

from optionforge.portfolio.portfolio import Portfolio
from optionforge.risk.rule_result import RuleResult
from optionforge.risk.rules.risk_rule import RiskRule


class LiquidityRule(RiskRule):
    """
    Institutional portfolio liquidity rule.
    """

    def __init__(
        self,
        *,
        min_liquidity: float = 25.0,
    ) -> None:

        self._min_liquidity = min_liquidity

    @property
    def min_liquidity(self) -> float:

        return self._min_liquidity

    def evaluate(
        self,
        *,
        portfolio: Portfolio,
    ) -> RuleResult:

        liquidity = 100.0 - portfolio.capital_utilization

        if liquidity >= self._min_liquidity:

            return RuleResult(

                rule_name=self.__class__.__name__,

                score=5.0,

                passed=True,

                warnings=(),

                reasons=(

                    "Portfolio liquidity within limits.",

                ),

            )

        return RuleResult(

            rule_name=self.__class__.__name__,

            score=min(
                100.0,
                100.0 - liquidity,
            ),

            passed=False,

            warnings=(

                f"Available liquidity "
                f"{liquidity:.1f}% is below "
                f"{self._min_liquidity:.1f}%",

            ),

            reasons=(

                "Portfolio liquidity below policy.",

            ),

        )

    def __repr__(self) -> str:

        return (

            f"LiquidityRule("

            f"min_liquidity={self._min_liquidity})"

        )