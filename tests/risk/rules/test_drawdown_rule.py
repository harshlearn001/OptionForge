"""
============================================================
OptionForge
Drawdown Rule Tests
============================================================
"""

from types import SimpleNamespace

from optionforge.risk.rule_result import RuleResult
from optionforge.risk.rules.drawdown_rule import DrawdownRule


def portfolio(
    return_percentage: float,
):

    return SimpleNamespace(

        return_percentage=return_percentage,

    )


def test_returns_rule_result():

    result = DrawdownRule().evaluate(

        portfolio=portfolio(

            -10.0,

        ),

    )

    assert isinstance(

        result,

        RuleResult,

    )


def test_within_limit():

    result = DrawdownRule(

        max_drawdown=20.0,

    ).evaluate(

        portfolio=portfolio(

            -10.0,

        ),

    )

    assert result.passed

    assert result.score == 5.0


def test_above_limit():

    result = DrawdownRule(

        max_drawdown=20.0,

    ).evaluate(

        portfolio=portfolio(

            -30.0,

        ),

    )

    assert not result.passed

    assert result.score == 30.0


def test_exact_boundary():

    result = DrawdownRule(

        max_drawdown=20.0,

    ).evaluate(

        portfolio=portfolio(

            -20.0,

        ),

    )

    assert result.passed


def test_property():

    rule = DrawdownRule(

        max_drawdown=15.0,

    )

    assert rule.max_drawdown == 15.0


def test_rule_name():

    result = DrawdownRule().evaluate(

        portfolio=portfolio(

            -5.0,

        ),

    )

    assert result.rule_name == "DrawdownRule"


def test_repr():

    assert (

        "DrawdownRule"

        in repr(

            DrawdownRule(),

        )

    )