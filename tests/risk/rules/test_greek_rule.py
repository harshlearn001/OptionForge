"""
============================================================
OptionForge
Greek Rule Tests
============================================================
"""

from types import SimpleNamespace

from optionforge.risk.rule_result import RuleResult
from optionforge.risk.rules.greek_rule import GreekRule


def portfolio(
    exposure: float,
):

    return SimpleNamespace(
        capital_utilization=exposure,
    )


def test_returns_rule_result():

    result = GreekRule().evaluate(
        portfolio=portfolio(
            40.0,
        ),
    )

    assert isinstance(
        result,
        RuleResult,
    )


def test_within_limit():

    result = GreekRule(
        max_exposure=75.0,
    ).evaluate(
        portfolio=portfolio(
            50.0,
        ),
    )

    assert result.passed

    assert result.score == 5.0


def test_above_limit():

    result = GreekRule(
        max_exposure=75.0,
    ).evaluate(
        portfolio=portfolio(
            90.0,
        ),
    )

    assert not result.passed

    assert result.score == 90.0


def test_exact_boundary():

    result = GreekRule(
        max_exposure=75.0,
    ).evaluate(
        portfolio=portfolio(
            75.0,
        ),
    )

    assert result.passed


def test_property():

    rule = GreekRule(
        max_exposure=60.0,
    )

    assert rule.max_exposure == 60.0


def test_rule_name():

    result = GreekRule().evaluate(
        portfolio=portfolio(
            40.0,
        ),
    )

    assert result.rule_name == "GreekRule"


def test_repr():

    assert "GreekRule" in repr(GreekRule())
