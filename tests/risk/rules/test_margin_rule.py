"""
============================================================
OptionForge
Margin Rule Tests
============================================================
"""

from types import SimpleNamespace

from optionforge.risk.rule_result import RuleResult
from optionforge.risk.rules.margin_rule import MarginRule


def portfolio(
    utilization: float,
):

    return SimpleNamespace(
        capital_utilization=utilization,
    )


def test_returns_rule_result():

    result = MarginRule().evaluate(
        portfolio=portfolio(
            40.0,
        ),
    )

    assert isinstance(
        result,
        RuleResult,
    )


def test_within_limit():

    result = MarginRule(
        max_margin=75.0,
    ).evaluate(
        portfolio=portfolio(
            50.0,
        ),
    )

    assert result.passed

    assert result.score == 5.0


def test_above_limit():

    result = MarginRule(
        max_margin=75.0,
    ).evaluate(
        portfolio=portfolio(
            90.0,
        ),
    )

    assert not result.passed

    assert result.score == 90.0


def test_exact_boundary():

    result = MarginRule(
        max_margin=75.0,
    ).evaluate(
        portfolio=portfolio(
            75.0,
        ),
    )

    assert result.passed


def test_property():

    rule = MarginRule(
        max_margin=60.0,
    )

    assert rule.max_margin == 60.0


def test_rule_name():

    result = MarginRule().evaluate(
        portfolio=portfolio(
            40.0,
        ),
    )

    assert result.rule_name == "MarginRule"


def test_repr():

    assert "MarginRule" in repr(
        MarginRule(),
    )
