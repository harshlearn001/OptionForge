"""
============================================================
OptionForge
Strategy Tests
============================================================
"""

from optionforge.decision.strategy_type import (
    StrategyType,
)

from optionforge.strategy.strategy import (
    Strategy,
)
from optionforge.strategy.strategy_risk import (
    StrategyRisk,
)


# ==========================================================
# Helper
# ==========================================================

def strategy() -> Strategy:

    return Strategy(

        type=StrategyType.LONG_CALL,

        title="Long Call",

        summary="Bullish directional strategy.",

        direction="Bullish",

        volatility_view="Normal",

        market_environment="Bull Market",

        max_profit="Unlimited",

        max_loss="Premium Paid",

        probability_of_profit=45.0,

        risk_reward="1:3",

        confidence=92.0,

        risk=StrategyRisk.MODERATE,

        capital_required=25000.0,

        rationale=(

            "Bullish trend",

            "Low volatility",

        ),

    )


# ==========================================================
# Tests
# ==========================================================

def test_strategy_creation():

    s = strategy()

    assert s.type == StrategyType.LONG_CALL

    assert s.confidence == 92.0

    assert s.risk == StrategyRisk.MODERATE


def test_bullish():

    assert strategy().is_bullish


def test_not_bearish():

    assert not strategy().is_bearish


def test_probability():

    assert strategy().probability_of_profit == 45.0


def test_capital():

    assert strategy().capital_required == 25000.0


def test_dict():

    data = strategy().to_dict()

    assert data["title"] == "Long Call"

    assert data["confidence"] == 92.0

    assert data["risk"] == "MODERATE"


def test_invalid_confidence():

    import pytest

    with pytest.raises(ValueError):

        Strategy(

            type=StrategyType.LONG_CALL,

            title="Bad",

            summary="",

            direction="Bullish",

            volatility_view="Normal",

            market_environment="",

            max_profit="Unlimited",

            max_loss="Premium",

            probability_of_profit=50,

            risk_reward="1:2",

            confidence=120,

            risk=StrategyRisk.MODERATE,

            capital_required=10000,

        )


def test_invalid_probability():

    import pytest

    with pytest.raises(ValueError):

        Strategy(

            type=StrategyType.LONG_CALL,

            title="Bad",

            summary="",

            direction="Bullish",

            volatility_view="Normal",

            market_environment="",

            max_profit="Unlimited",

            max_loss="Premium",

            probability_of_profit=150,

            risk_reward="1:2",

            confidence=80,

            risk=StrategyRisk.MODERATE,

            capital_required=10000,

        )


def test_invalid_risk_reward():

    import pytest

    with pytest.raises(ValueError):

        Strategy(

            type=StrategyType.LONG_CALL,

            title="Bad",

            summary="",

            direction="Bullish",

            volatility_view="Normal",

            market_environment="",

            max_profit="Unlimited",

            max_loss="Premium",

            probability_of_profit=50,

            risk_reward="",

            confidence=80,

            risk=StrategyRisk.MODERATE,

            capital_required=10000,

        )