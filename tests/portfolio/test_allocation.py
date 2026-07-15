"""
============================================================
OptionForge
Allocation Tests
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

from optionforge.portfolio.allocation import (
    Allocation,
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


def position():

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

    result = StrategyEngine().build(
        decision,
    )

    return Position(
        symbol="NIFTY",
        strategy_result=result,
        lots=2,
        quantity=100,
        entry_price=250.0,
        current_price=275.0,
        capital_used=25000.0,
        unrealized_pnl=2500.0,
        realized_pnl=500.0,
    )


def allocation():

    return Allocation(
        position=position(),
        allocated_capital=25000.0,
        available_capital=75000.0,
        portfolio_value=100000.0,
    )


# ==========================================================
# Result
# ==========================================================


def test_returns_allocation():

    assert isinstance(
        allocation(),
        Allocation,
    )


# ==========================================================
# Capital
# ==========================================================


def test_allocated_capital():

    assert allocation().allocated_capital == 25000.0


def test_available_capital():

    assert allocation().available_capital == 75000.0


def test_portfolio_value():

    assert allocation().portfolio_value == 100000.0


# ==========================================================
# Percentages
# ==========================================================


def test_allocation_percentage():

    assert allocation().allocation_percentage == 25.0


def test_remaining_percentage():

    assert allocation().remaining_percentage == 75.0


# ==========================================================
# Convenience
# ==========================================================


def test_utilization_percentage():

    assert allocation().utilization_percentage == 25.0


def test_is_under_allocated():

    assert allocation().is_under_allocated


def test_not_fully_allocated():

    assert not allocation().is_fully_allocated


# ==========================================================
# Serialization
# ==========================================================


def test_to_dict():

    data = allocation().to_dict()

    assert isinstance(
        data,
        dict,
    )

    assert data["allocated_capital"] == 25000.0

    assert data["available_capital"] == 75000.0

    assert data["portfolio_value"] == 100000.0

    assert data["allocation_percentage"] == 25.0


# ==========================================================
# Representation
# ==========================================================


def test_str():

    assert "Allocation" in str(
        allocation(),
    )


def test_repr():

    assert "Allocation" in repr(
        allocation(),
    )


# ==========================================================
# Validation
# ==========================================================


def test_negative_allocated_capital():

    import pytest

    with pytest.raises(ValueError):

        Allocation(
            position=position(),
            allocated_capital=-1.0,
            available_capital=1000.0,
            portfolio_value=10000.0,
        )


def test_negative_available_capital():

    import pytest

    with pytest.raises(ValueError):

        Allocation(
            position=position(),
            allocated_capital=1000.0,
            available_capital=-1.0,
            portfolio_value=10000.0,
        )


def test_invalid_portfolio_value():

    import pytest

    with pytest.raises(ValueError):

        Allocation(
            position=position(),
            allocated_capital=1000.0,
            available_capital=9000.0,
            portfolio_value=0.0,
        )


def test_allocated_exceeds_portfolio():

    import pytest

    with pytest.raises(ValueError):

        Allocation(
            position=position(),
            allocated_capital=110000.0,
            available_capital=0.0,
            portfolio_value=100000.0,
        )


# ==========================================================
# Deterministic
# ==========================================================


def test_allocation_is_deterministic():

    first = allocation()

    second = allocation()

    assert first == second
