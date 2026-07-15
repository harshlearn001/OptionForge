"""
============================================================
OptionForge
Portfolio Tests
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
from optionforge.portfolio.portfolio import (
    Portfolio,
)
from optionforge.portfolio.portfolio_risk import (
    PortfolioRisk,
)
from optionforge.portfolio.portfolio_type import (
    PortfolioType,
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


def portfolio():

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

    strategy_result = StrategyEngine().build(
        decision,
    )

    position = Position(
        symbol="NIFTY",
        strategy_result=strategy_result,
        lots=2,
        quantity=100,
        entry_price=250.0,
        current_price=275.0,
        capital_used=25000.0,
        unrealized_pnl=2500.0,
        realized_pnl=500.0,
    )

    allocation = Allocation(
        position=position,
        allocated_capital=25000.0,
        available_capital=75000.0,
        portfolio_value=100000.0,
    )

    return Portfolio(
        name="Demo Portfolio",
        portfolio_type=PortfolioType.DIRECTIONAL,
        portfolio_risk=PortfolioRisk.BALANCED,
        positions=(position,),
        allocations=(allocation,),
        total_capital=100000.0,
    )


# ==========================================================
# Result
# ==========================================================


def test_returns_portfolio():

    assert isinstance(
        portfolio(),
        Portfolio,
    )


# ==========================================================
# Identity
# ==========================================================


def test_name():

    assert portfolio().name == "Demo Portfolio"


def test_portfolio_type():

    assert portfolio().portfolio_type is PortfolioType.DIRECTIONAL


def test_portfolio_risk():

    assert portfolio().portfolio_risk is PortfolioRisk.BALANCED


# ==========================================================
# Holdings
# ==========================================================


def test_position_count():

    assert portfolio().position_count == 1


def test_allocation_count():

    assert portfolio().allocation_count == 1


# ==========================================================
# Capital
# ==========================================================


def test_total_capital():

    assert portfolio().total_capital == 100000.0


def test_allocated_capital():

    assert portfolio().allocated_capital == 25000.0


def test_available_capital():

    assert portfolio().available_capital == 75000.0


def test_capital_utilization():

    assert portfolio().capital_utilization == 25.0


# ==========================================================
# Market Value
# ==========================================================


def test_market_value():

    assert portfolio().market_value == 27500.0


# ==========================================================
# Profit & Loss
# ==========================================================


def test_unrealized_pnl():

    assert portfolio().unrealized_pnl == 2500.0


def test_realized_pnl():

    assert portfolio().realized_pnl == 500.0


def test_total_pnl():

    assert portfolio().total_pnl == 3000.0


def test_return_percentage():

    assert portfolio().return_percentage == 3.0


# ==========================================================
# Convenience
# ==========================================================


def test_is_profitable():

    assert portfolio().is_profitable


def test_not_loss():

    assert not portfolio().is_loss


def test_not_flat():

    assert not portfolio().is_flat


def test_not_empty():

    assert not portfolio().is_empty


def test_not_fully_invested():

    assert not portfolio().is_fully_invested


# ==========================================================
# Serialization
# ==========================================================


def test_to_dict():

    data = portfolio().to_dict()

    assert isinstance(
        data,
        dict,
    )

    assert data["name"] == "Demo Portfolio"

    assert data["position_count"] == 1

    assert data["allocation_count"] == 1

    assert data["allocated_capital"] == 25000.0

    assert data["available_capital"] == 75000.0

    assert data["market_value"] == 27500.0

    assert data["total_pnl"] == 3000.0


# ==========================================================
# Representation
# ==========================================================


def test_str():

    assert "Portfolio" in str(
        portfolio(),
    )


def test_repr():

    assert "Portfolio" in repr(
        portfolio(),
    )


# ==========================================================
# Validation
# ==========================================================


def test_invalid_name():

    import pytest

    with pytest.raises(ValueError):

        Portfolio(
            name="",
            portfolio_type=PortfolioType.DIRECTIONAL,
            portfolio_risk=PortfolioRisk.BALANCED,
            total_capital=100000.0,
        )


def test_invalid_total_capital():

    import pytest

    with pytest.raises(ValueError):

        Portfolio(
            name="Demo",
            portfolio_type=PortfolioType.DIRECTIONAL,
            portfolio_risk=PortfolioRisk.BALANCED,
            total_capital=-1.0,
        )


# ==========================================================
# Deterministic
# ==========================================================


def test_portfolio_is_deterministic():

    first = portfolio()

    second = portfolio()

    assert first == second
