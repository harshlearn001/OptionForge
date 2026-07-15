"""
============================================================
OptionForge
RiskRegistry Tests
============================================================
"""

from optionforge.risk.risk_registry import RiskRegistry
from optionforge.risk.rules.capital_rule import CapitalRule
from optionforge.risk.rules.drawdown_rule import DrawdownRule
from optionforge.risk.rules.exposure_rule import ExposureRule
from optionforge.risk.rules.greek_rule import GreekRule
from optionforge.risk.rules.liquidity_rule import LiquidityRule
from optionforge.risk.rules.margin_rule import MarginRule
from optionforge.risk.rules.risk_rule import RiskRule


def test_returns_tuple():

    rules = RiskRegistry.default_rules()

    assert isinstance(
        rules,
        tuple,
    )


def test_rule_count():

    rules = RiskRegistry.default_rules()

    assert len(rules) == 6


def test_all_are_risk_rules():

    rules = RiskRegistry.default_rules()

    assert all(
        isinstance(
            rule,
            RiskRule,
        )
        for rule in rules
    )


def test_contains_capital_rule():

    assert any(
        isinstance(
            rule,
            CapitalRule,
        )
        for rule in RiskRegistry.default_rules()
    )


def test_contains_margin_rule():

    assert any(
        isinstance(
            rule,
            MarginRule,
        )
        for rule in RiskRegistry.default_rules()
    )


def test_contains_exposure_rule():

    assert any(
        isinstance(
            rule,
            ExposureRule,
        )
        for rule in RiskRegistry.default_rules()
    )


def test_contains_liquidity_rule():

    assert any(
        isinstance(
            rule,
            LiquidityRule,
        )
        for rule in RiskRegistry.default_rules()
    )


def test_contains_greek_rule():

    assert any(
        isinstance(
            rule,
            GreekRule,
        )
        for rule in RiskRegistry.default_rules()
    )


def test_contains_drawdown_rule():

    assert any(
        isinstance(
            rule,
            DrawdownRule,
        )
        for rule in RiskRegistry.default_rules()
    )


def test_no_duplicate_rule_types():

    rules = RiskRegistry.default_rules()

    names = [type(rule).__name__ for rule in rules]

    assert len(names) == len(set(names))
