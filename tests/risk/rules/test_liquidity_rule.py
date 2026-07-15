"""
============================================================
OptionForge
Liquidity Rule Tests
============================================================
"""

from types import SimpleNamespace

from optionforge.risk.rule_result import RuleResult
from optionforge.risk.rules.liquidity_rule import LiquidityRule


def portfolio(
    utilization: float,
):

    return SimpleNamespace(
        capital_utilization=utilization,
    )


def test_returns_rule_result():

    result = LiquidityRule().evaluate(
        portfolio=portfolio(
            40.0,
        ),
    )

    assert isinstance(
        result,
        RuleResult,
    )


def test_within_limit():

    result = LiquidityRule(
        min_liquidity=25.0,
    ).evaluate(
        portfolio=portfolio(
            40.0,
        ),
    )

    assert result.passed

    assert result.score == 5.0


def test_below_limit():

    result = LiquidityRule(
        min_liquidity=25.0,
    ).evaluate(
        portfolio=portfolio(
            90.0,
        ),
    )

    assert not result.passed

    assert result.score == 90.0


def test_exact_boundary():

    result = LiquidityRule(
        min_liquidity=25.0,
    ).evaluate(
        portfolio=portfolio(
            75.0,
        ),
    )

    assert result.passed


def test_property():

    rule = LiquidityRule(
        min_liquidity=20.0,
    )

    assert rule.min_liquidity == 20.0


def test_rule_name():

    result = LiquidityRule().evaluate(
        portfolio=portfolio(
            40.0,
        ),
    )

    assert result.rule_name == "LiquidityRule"


def test_repr():

    assert "LiquidityRule" in repr(
        LiquidityRule(),
    )
