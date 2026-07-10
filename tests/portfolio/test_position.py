"""
============================================================
OptionForge
Position Tests
============================================================
"""

from optionforge.decision.confidence_level import (
    ConfidenceLevel,
)
from optionforge.decision.decision import (
    Decision,
)
from optionforge.decision.decision_type import (
    DecisionType,
)

from optionforge.marketdna.liquidity_regime import (
    LiquidityRegime,
)
from optionforge.marketdna.market_dna import (
    MarketDNA,
)
from optionforge.marketdna.market_regime import (
    MarketRegime,
)
from optionforge.marketdna.trend_regime import (
    TrendRegime,
)
from optionforge.marketdna.volatility_regime import (
    VolatilityRegime,
)

from optionforge.portfolio.position import (
    Position,
)

from optionforge.strategy.strategy_engine import (
    StrategyEngine,
)
from optionforge.strategy.strategy_type import (
    StrategyType,
)


# ==========================================================
# Helpers
# ==========================================================

def strategy_result():

    dna = MarketDNA(

        regime=MarketRegime.STRONGLY_BULLISH,

        trend=TrendRegime.STRONG_UPTREND,

        volatility=VolatilityRegime.COMPRESSED,

        liquidity=LiquidityRegime.HIGH,

        dealer_position="LONG GAMMA",

        evidence_score=95.0,

        confidence=95.0,

    )

    decision = Decision(

        decision=DecisionType.STRONG_BUY,

        strategy=StrategyType.LONG_CALL,

        confidence_level=ConfidenceLevel.VERY_HIGH,

        confidence=95.0,

        market_dna=dna,

        recommendation="Long Call",

        rationale=("Bullish",),

    )

    return StrategyEngine().build(

        decision,

    )


def position():

    return Position(

        symbol="NIFTY",

        strategy_result=strategy_result(),

        lots=2,

        quantity=100,

        entry_price=250.0,

        current_price=275.0,

        capital_used=25000.0,

        unrealized_pnl=2500.0,

        realized_pnl=500.0,

    )


# ==========================================================
# Result
# ==========================================================

def test_returns_position():

    assert isinstance(

        position(),

        Position,

    )


# ==========================================================
# Identity
# ==========================================================

def test_symbol():

    assert (

        position().symbol

        == "NIFTY"

    )


def test_lots():

    assert (

        position().lots

        == 2

    )


def test_quantity():

    assert (

        position().quantity

        == 100

    )


# ==========================================================
# Pricing
# ==========================================================

def test_market_value():

    assert (

        position().market_value

        == 27500.0

    )
# ==========================================================
# Profit / Loss
# ==========================================================

def test_total_pnl():

    assert (

        position().total_pnl

        == 3000.0

    )


def test_return_percentage():

    assert (

        position().return_percentage

        == 12.0

    )


def test_is_profitable():

    assert position().is_profitable


def test_not_loss():

    assert not position().is_loss


def test_not_flat():

    assert not position().is_flat


# ==========================================================
# Serialization
# ==========================================================

def test_to_dict():

    data = position().to_dict()

    assert isinstance(

        data,

        dict,

    )

    assert (

        data["symbol"]

        == "NIFTY"

    )

    assert (

        data["lots"]

        == 2

    )

    assert (

        data["quantity"]

        == 100

    )

    assert (

        data["total_pnl"]

        == 3000.0

    )


# ==========================================================
# Representation
# ==========================================================

def test_str():

    assert (

        "Position"

        in str(

            position(),

        )

    )


def test_repr():

    assert (

        "Position"

        in repr(

            position(),

        )

    )


# ==========================================================
# Validation
# ==========================================================

def test_invalid_symbol():

    import pytest

    with pytest.raises(ValueError):

        Position(

            symbol="",

            strategy_result=strategy_result(),

            lots=1,

            quantity=50,

            entry_price=100.0,

            current_price=100.0,

            capital_used=5000.0,

        )


def test_invalid_lots():

    import pytest

    with pytest.raises(ValueError):

        Position(

            symbol="NIFTY",

            strategy_result=strategy_result(),

            lots=0,

            quantity=50,

            entry_price=100.0,

            current_price=100.0,

            capital_used=5000.0,

        )


def test_invalid_quantity():

    import pytest

    with pytest.raises(ValueError):

        Position(

            symbol="NIFTY",

            strategy_result=strategy_result(),

            lots=1,

            quantity=0,

            entry_price=100.0,

            current_price=100.0,

            capital_used=5000.0,

        )


# ==========================================================
# Deterministic
# ==========================================================

def test_position_is_deterministic():

    first = position()

    second = position()

    assert first == second