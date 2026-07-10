"""
============================================================
OptionForge
Portfolio Builder Tests
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
from optionforge.portfolio.portfolio_builder import (
    PortfolioBuilder,
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


def allocation() -> Allocation:

    return Allocation(

        position=position(),

        allocated_capital=25000.0,

        available_capital=75000.0,

        portfolio_value=100000.0,

    )


# ==========================================================
# Build
# ==========================================================

def test_returns_portfolio():

    builder = PortfolioBuilder()

    result = builder.build(

        name="Demo",

        portfolio_type=PortfolioType.DIRECTIONAL,

        portfolio_risk=PortfolioRisk.BALANCED,

        positions=(

            position(),

        ),

        allocations=(

            allocation(),

        ),

        total_capital=100000.0,

    )

    assert isinstance(

        result,

        Portfolio,

    )


def test_name():

    builder = PortfolioBuilder()

    result = builder.build(

        name="Demo",

        portfolio_type=PortfolioType.DIRECTIONAL,

        portfolio_risk=PortfolioRisk.BALANCED,

        positions=(

            position(),

        ),

        allocations=(

            allocation(),

        ),

        total_capital=100000.0,

    )

    assert result.name == "Demo"
# ==========================================================
# Empty Portfolio
# ==========================================================

def test_empty():

    builder = PortfolioBuilder()

    result = builder.empty(

        name="Empty",

        portfolio_type=PortfolioType.CASH,

        portfolio_risk=PortfolioRisk.CONSERVATIVE,

        total_capital=50000.0,

    )

    assert result.position_count == 0

    assert result.allocation_count == 0

    assert result.total_capital == 50000.0

    assert result.is_empty


# ==========================================================
# From Positions
# ==========================================================

def test_from_positions():

    builder = PortfolioBuilder()

    pos = position()

    alloc = allocation()

    result = builder.from_positions(

        name="Demo",

        portfolio_type=PortfolioType.DIRECTIONAL,

        portfolio_risk=PortfolioRisk.BALANCED,

        positions=(

            pos,

        ),

        allocations=(

            alloc,

        ),

        total_capital=100000.0,

    )

    assert result.position_count == 1

    assert result.allocation_count == 1

    assert result.market_value == 27500.0


# ==========================================================
# Callable
# ==========================================================

def test_callable():

    builder = PortfolioBuilder()

    result = builder(

        name="Callable",

        portfolio_type=PortfolioType.DIRECTIONAL,

        portfolio_risk=PortfolioRisk.BALANCED,

        positions=(

            position(),

        ),

        allocations=(

            allocation(),

        ),

        total_capital=100000.0,

    )

    assert isinstance(

        result,

        Portfolio,

    )


# ==========================================================
# Portfolio Metrics
# ==========================================================

def test_metrics():

    builder = PortfolioBuilder()

    result = builder.build(

        name="Demo",

        portfolio_type=PortfolioType.DIRECTIONAL,

        portfolio_risk=PortfolioRisk.BALANCED,

        positions=(

            position(),

        ),

        allocations=(

            allocation(),

        ),

        total_capital=100000.0,

    )

    assert result.allocated_capital == 25000.0

    assert result.available_capital == 75000.0

    assert result.capital_utilization == 25.0

    assert result.total_pnl == 3000.0


# ==========================================================
# Representation
# ==========================================================

def test_repr():

    builder = PortfolioBuilder()

    assert (

        "PortfolioBuilder"

        in repr(

            builder,

        )

    )


# ==========================================================
# Deterministic
# ==========================================================

def test_builder_is_deterministic():

    builder = PortfolioBuilder()

    first = builder.build(

        name="Demo",

        portfolio_type=PortfolioType.DIRECTIONAL,

        portfolio_risk=PortfolioRisk.BALANCED,

        positions=(

            position(),

        ),

        allocations=(

            allocation(),

        ),

        total_capital=100000.0,

    )

    second = builder.build(

        name="Demo",

        portfolio_type=PortfolioType.DIRECTIONAL,

        portfolio_risk=PortfolioRisk.BALANCED,

        positions=(

            position(),

        ),

        allocations=(

            allocation(),

        ),

        total_capital=100000.0,

    )

    assert first == second