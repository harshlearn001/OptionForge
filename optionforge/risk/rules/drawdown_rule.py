"""
============================================================
OptionForge
Drawdown Rule
============================================================
"""

from __future__ import annotations

from optionforge.portfolio.portfolio import Portfolio
from optionforge.risk.rule_result import RuleResult
from optionforge.risk.rules.risk_rule import RiskRule


class DrawdownRule(RiskRule):
    """
    Institutional portfolio drawdown rule.
    """

    def __init__(
        self,
        *,
        max_drawdown: float = 20.0,
    ) -> None:

        self._max_drawdown = max_drawdown

    @property
    def max_drawdown(self) -> float:

        return self._max_drawdown

    def evaluate(
        self,
        *,
        portfolio: Portfolio,
    ) -> RuleResult:

        drawdown = abs(min(portfolio.return_percentage, 0.0))

        if drawdown <= self._max_drawdown:

            return RuleResult(
                rule_name=self.__class__.__name__,
                score=5.0,
                passed=True,
                warnings=(),
                reasons=("Portfolio drawdown within limits.",),
            )

        return RuleResult(
            rule_name=self.__class__.__name__,
            score=min(
                100.0,
                drawdown,
            ),
            passed=False,
            warnings=(
                f"Portfolio drawdown "
                f"{drawdown:.1f}% exceeds "
                f"{self._max_drawdown:.1f}%",
            ),
            reasons=("Portfolio drawdown exceeds policy.",),
        )

    def __repr__(self) -> str:

        return f"DrawdownRule(" f"max_drawdown={self._max_drawdown})"
