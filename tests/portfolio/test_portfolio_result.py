"""
============================================================
OptionForge
Portfolio Result Tests
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
from optionforge.portfolio.portfolio_result import (
    PortfolioResult,
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
# Helper
# ==========================================================


def portfolio() -> Portfolio:

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


def result() -> PortfolioResult:

    return PortfolioResult(
        portfolio=portfolio(),
    )


# ==========================================================
# Result
# ==========================================================


def test_returns_portfolio_result():

    assert isinstance(
        result(),
        PortfolioResult,
    )


# ==========================================================
# Portfolio
# ==========================================================


def test_contains_portfolio():

    assert result().portfolio is not None


def test_total_capital():

    assert result().total_capital == 100000.0


def test_total_pnl():

    assert result().total_pnl == 3000.0


def test_return_percentage():

    assert result().return_percentage == 3.0


def test_position_count():

    assert result().position_count == 1


# ==========================================================
# Convenience
# ==========================================================


def test_allocation_count():

    assert result().allocation_count == 1


def test_is_profitable():

    assert result().is_profitable


def test_not_empty():

    assert not result().is_empty


# ==========================================================
# Serialization
# ==========================================================


def test_to_dict():

    data = result().to_dict()

    assert isinstance(
        data,
        dict,
    )

    assert data["portfolio"]["name"] == "Demo Portfolio"

    assert data["portfolio"]["position_count"] == 1

    assert data["portfolio"]["allocation_count"] == 1

    assert data["portfolio"]["total_pnl"] == 3000.0


# ==========================================================
# Representation
# ==========================================================


def test_str():

    assert "PortfolioResult" in str(
        result(),
    )


def test_repr():

    assert "PortfolioResult" in repr(
        result(),
    )


# ==========================================================
# Deterministic
# ==========================================================


def test_result_is_deterministic():

    first = result()

    second = result()

    assert first == second
