"""
============================================================
OptionForge
RiskEngine Tests
============================================================
"""

from types import SimpleNamespace

from optionforge.risk.risk import Risk
from optionforge.risk.risk_builder import RiskBuilder
from optionforge.risk.risk_engine import RiskEngine


def portfolio():

    return SimpleNamespace(
        total_capital=100000.0,
        capital_utilization=40.0,
        return_percentage=-5.0,
    )


def test_returns_risk():

    risk = RiskEngine().evaluate(
        portfolio=portfolio(),
    )

    assert isinstance(
        risk,
        Risk,
    )


def test_builder_property():

    engine = RiskEngine()

    assert isinstance(
        engine.builder,
        RiskBuilder,
    )


def test_score_range():

    risk = RiskEngine().evaluate(
        portfolio=portfolio(),
    )

    assert 0.0 <= risk.risk_score <= 100.0


def test_position_size_range():

    risk = RiskEngine().evaluate(
        portfolio=portfolio(),
    )

    assert 0.0 <= risk.recommended_position_size <= 100.0


def test_capital_range():

    risk = RiskEngine().evaluate(
        portfolio=portfolio(),
    )

    assert 0.0 <= risk.max_capital_allocation <= 100.0


def test_warning_count():

    risk = RiskEngine().evaluate(
        portfolio=portfolio(),
    )

    assert risk.warning_count >= 0


def test_reason_count():

    risk = RiskEngine().evaluate(
        portfolio=portfolio(),
    )

    assert risk.reason_count >= 0


def test_repr():

    assert "RiskEngine" in repr(
        RiskEngine(),
    )
