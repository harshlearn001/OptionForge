"""
============================================================
OptionForge
Portfolio Registry Tests
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
from optionforge.portfolio.portfolio_registry import (
    PortfolioRegistry,
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


def portfolio_result() -> PortfolioResult:

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

    portfolio = Portfolio(
        name="Demo Portfolio",
        portfolio_type=PortfolioType.DIRECTIONAL,
        portfolio_risk=PortfolioRisk.BALANCED,
        positions=(position,),
        allocations=(allocation,),
        total_capital=100000.0,
    )

    return PortfolioResult(
        portfolio=portfolio,
    )


# ==========================================================
# Result
# ==========================================================


def test_returns_registry():

    registry = PortfolioRegistry()

    assert isinstance(
        registry,
        PortfolioRegistry,
    )


# ==========================================================
# Empty
# ==========================================================


def test_empty():

    registry = PortfolioRegistry()

    assert registry.empty

    assert registry.count == 0

    assert registry.latest is None


# ==========================================================
# Collection
# ==========================================================


def test_add():

    registry = PortfolioRegistry()

    registry = registry.add(
        portfolio_result(),
    )

    assert registry.count == 1

    assert registry.latest is not None


def test_length():

    registry = PortfolioRegistry()

    registry = registry.add(
        portfolio_result(),
    )

    assert (
        len(
            registry,
        )
        == 1
    )


def test_getitem():

    registry = PortfolioRegistry()

    registry = registry.add(
        portfolio_result(),
    )

    assert isinstance(
        registry[0],
        PortfolioResult,
    )


# ==========================================================
# Iteration
# ==========================================================


def test_iteration():

    registry = PortfolioRegistry()

    registry = registry.add(
        portfolio_result(),
    )

    assert list(
        registry,
    )


# ==========================================================
# Extend
# ==========================================================


def test_extend():

    registry = PortfolioRegistry()

    registry = registry.extend(
        (
            portfolio_result(),
            portfolio_result(),
        ),
    )

    assert registry.count == 2

    assert (
        len(
            registry,
        )
        == 2
    )


# ==========================================================
# Serialization
# ==========================================================


def test_to_dict():

    registry = PortfolioRegistry()

    registry = registry.add(
        portfolio_result(),
    )

    data = registry.to_dict()

    assert isinstance(
        data,
        dict,
    )

    assert data["count"] == 1

    assert (
        len(
            data["results"],
        )
        == 1
    )


# ==========================================================
# Representation
# ==========================================================


def test_str():

    registry = PortfolioRegistry()

    assert "PortfolioRegistry" in str(
        registry,
    )


def test_repr():

    registry = PortfolioRegistry()

    assert "PortfolioRegistry" in repr(
        registry,
    )


# ==========================================================
# Deterministic
# ==========================================================


def test_registry_is_deterministic():

    first = PortfolioRegistry().add(
        portfolio_result(),
    )

    second = PortfolioRegistry().add(
        portfolio_result(),
    )

    assert first == second
