"""
============================================================
OptionForge
Capital Allocator Tests
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

from optionforge.portfolio.capital_allocator import (
    CapitalAllocator,
)
from optionforge.portfolio.portfolio_risk import (
    PortfolioRisk,
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


def position() -> Position:

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

    return Position(
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


# ==========================================================
# Constructor
# ==========================================================


def test_constructor():

    allocator = CapitalAllocator(
        PortfolioRisk.BALANCED,
    )

    assert allocator.portfolio_risk is PortfolioRisk.BALANCED


# ==========================================================
# Allocation
# ==========================================================


def test_allocate():

    allocator = CapitalAllocator(
        PortfolioRisk.INSTITUTIONAL,
    )

    result = allocator.allocate(
        position=position(),
        portfolio_value=100000.0,
    )

    assert result.allocated_capital == 20000.0

    assert result.available_capital == 80000.0

    assert result.portfolio_value == 100000.0


def test_callable():

    allocator = CapitalAllocator(
        PortfolioRisk.INSTITUTIONAL,
    )

    result = allocator(
        position=position(),
        portfolio_value=100000.0,
    )

    assert result.allocated_capital == 20000.0


# ==========================================================
# Validation
# ==========================================================


def test_can_allocate_true():

    allocator = CapitalAllocator(
        PortfolioRisk.INSTITUTIONAL,
    )

    assert allocator.can_allocate(
        position=position(),
        portfolio_value=200000.0,
    )


def test_can_allocate_false():

    allocator = CapitalAllocator(
        PortfolioRisk.CONSERVATIVE,
    )

    assert not allocator.can_allocate(
        position=position(),
        portfolio_value=100000.0,
    )


def test_remaining_capacity():

    allocator = CapitalAllocator(
        PortfolioRisk.BALANCED,
    )

    remaining = allocator.remaining_capacity(
        portfolio_value=100000.0,
        allocated_capital=25000.0,
    )

    assert remaining == 75000.0


# ==========================================================
# Risk Profiles
# ==========================================================


def test_conservative_allocation():

    allocator = CapitalAllocator(
        PortfolioRisk.CONSERVATIVE,
    )

    result = allocator.allocate(
        position=position(),
        portfolio_value=100000.0,
    )

    assert result.allocated_capital == 2000.0


def test_balanced_allocation():

    allocator = CapitalAllocator(
        PortfolioRisk.BALANCED,
    )

    result = allocator.allocate(
        position=position(),
        portfolio_value=100000.0,
    )

    assert result.allocated_capital == 5000.0


def test_aggressive_allocation():

    allocator = CapitalAllocator(
        PortfolioRisk.AGGRESSIVE,
    )

    result = allocator.allocate(
        position=position(),
        portfolio_value=100000.0,
    )

    assert result.allocated_capital == 10000.0


def test_institutional_allocation():

    allocator = CapitalAllocator(
        PortfolioRisk.INSTITUTIONAL,
    )

    result = allocator.allocate(
        position=position(),
        portfolio_value=100000.0,
    )

    assert result.allocated_capital == 20000.0


# ==========================================================
# Representation
# ==========================================================


def test_repr():

    allocator = CapitalAllocator(
        PortfolioRisk.BALANCED,
    )

    assert "CapitalAllocator" in repr(
        allocator,
    )


# ==========================================================
# Deterministic
# ==========================================================


def test_allocator_is_deterministic():

    allocator = CapitalAllocator(
        PortfolioRisk.AGGRESSIVE,
    )

    first = allocator.allocate(
        position=position(),
        portfolio_value=100000.0,
    )

    second = allocator.allocate(
        position=position(),
        portfolio_value=100000.0,
    )

    assert first == second
