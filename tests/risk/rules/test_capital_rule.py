"""
============================================================
OptionForge
Capital Rule Tests
============================================================
"""

from types import SimpleNamespace

from optionforge.risk.rule_result import RuleResult
from optionforge.risk.rules.capital_rule import CapitalRule


# ==========================================================
# Helper
# ==========================================================

def portfolio(
    utilization: float,
):

    return SimpleNamespace(

        capital_utilization=utilization,

    )


# ==========================================================
# Tests
# ==========================================================

def test_returns_rule_result():

    result = CapitalRule().evaluate(

        portfolio=portfolio(

            40.0,

        ),

    )

    assert isinstance(

        result,

        RuleResult,

    )


def test_within_limit():

    result = CapitalRule(

        max_utilization=80.0,

    ).evaluate(

        portfolio=portfolio(

            40.0,

        ),

    )

    assert result.passed

    assert result.score == 5.0


def test_above_limit():

    result = CapitalRule(

        max_utilization=80.0,

    ).evaluate(

        portfolio=portfolio(

            90.0,

        ),

    )

    assert not result.passed

    assert result.score == 90.0


def test_exact_boundary():

    result = CapitalRule(

        max_utilization=80.0,

    ).evaluate(

        portfolio=portfolio(

            80.0,

        ),

    )

    assert result.passed


def test_max_utilization():

    rule = CapitalRule(

        max_utilization=75.0,

    )

    assert rule.max_utilization == 75.0


def test_rule_name():

    result = CapitalRule().evaluate(

        portfolio=portfolio(

            40.0,

        ),

    )

    assert result.rule_name == "CapitalRule"


def test_repr():

    assert (

        "CapitalRule"

        in repr(

            CapitalRule(),

        )

    )