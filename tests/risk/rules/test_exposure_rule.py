"""
============================================================
OptionForge
Exposure Rule Tests
============================================================
"""

from types import SimpleNamespace

from optionforge.risk.rule_result import RuleResult
from optionforge.risk.rules.exposure_rule import ExposureRule


def portfolio(
    exposure: float,
):

    return SimpleNamespace(

        capital_utilization=exposure,

    )


def test_returns_rule_result():

    result = ExposureRule().evaluate(

        portfolio=portfolio(

            40.0,

        ),

    )

    assert isinstance(

        result,

        RuleResult,

    )


def test_within_limit():

    result = ExposureRule(

        max_exposure=75.0,

    ).evaluate(

        portfolio=portfolio(

            50.0,

        ),

    )

    assert result.passed

    assert result.score == 5.0


def test_above_limit():

    result = ExposureRule(

        max_exposure=75.0,

    ).evaluate(

        portfolio=portfolio(

            90.0,

        ),

    )

    assert not result.passed

    assert result.score == 90.0


def test_exact_boundary():

    result = ExposureRule(

        max_exposure=75.0,

    ).evaluate(

        portfolio=portfolio(

            75.0,

        ),

    )

    assert result.passed


def test_property():

    rule = ExposureRule(

        max_exposure=60.0,

    )

    assert rule.max_exposure == 60.0


def test_rule_name():

    result = ExposureRule().evaluate(

        portfolio=portfolio(

            40.0,

        ),

    )

    assert result.rule_name == "ExposureRule"


def test_repr():

    assert (

        "ExposureRule"

        in repr(

            ExposureRule(),

        )

    )