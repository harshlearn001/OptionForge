"""
============================================================
OptionForge
Portfolio Engine Tests
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

from optionforge.portfolio.portfolio_engine import (
    PortfolioEngine,
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

    engine = PortfolioEngine(

        portfolio_risk=PortfolioRisk.BALANCED,

    )

    assert (

        engine.allocator.portfolio_risk

        is PortfolioRisk.BALANCED

    )


# ==========================================================
# Build
# ==========================================================

def test_returns_portfolio_result():

    engine = PortfolioEngine(

        portfolio_risk=PortfolioRisk.BALANCED,

    )

    result = engine.build(

        name="Demo",

        portfolio_type=PortfolioType.DIRECTIONAL,

        positions=(

            position(),

        ),

        total_capital=100000.0,

    )

    assert isinstance(

        result,

        PortfolioResult,

    )


def test_portfolio_name():

    engine = PortfolioEngine(

        portfolio_risk=PortfolioRisk.BALANCED,

    )

    result = engine.build(

        name="Demo",

        portfolio_type=PortfolioType.DIRECTIONAL,

        positions=(

            position(),

        ),

        total_capital=100000.0,

    )

    assert (

        result.portfolio.name

        == "Demo"

    )


def test_position_count():

    engine = PortfolioEngine(

        portfolio_risk=PortfolioRisk.BALANCED,

    )

    result = engine.build(

        name="Demo",

        portfolio_type=PortfolioType.DIRECTIONAL,

        positions=(

            position(),

        ),

        total_capital=100000.0,

    )

    assert (

        result.position_count

        == 1

    )
# ==========================================================
# Callable
# ==========================================================

def test_callable():

    engine = PortfolioEngine(

        portfolio_risk=PortfolioRisk.BALANCED,

    )

    result = engine(

        name="Demo",

        portfolio_type=PortfolioType.DIRECTIONAL,

        positions=(

            position(),

        ),

        total_capital=100000.0,

    )

    assert isinstance(

        result,

        PortfolioResult,

    )


# ==========================================================
# Allocation
# ==========================================================

def test_allocation_created():

    engine = PortfolioEngine(

        portfolio_risk=PortfolioRisk.BALANCED,

    )

    result = engine.build(

        name="Demo",

        portfolio_type=PortfolioType.DIRECTIONAL,

        positions=(

            position(),

        ),

        total_capital=100000.0,

    )

    assert (

        result.allocation_count

        == 1

    )


def test_risk_profile_propagation():

    engine = PortfolioEngine(

        portfolio_risk=PortfolioRisk.AGGRESSIVE,

    )

    result = engine.build(

        name="Demo",

        portfolio_type=PortfolioType.DIRECTIONAL,

        positions=(

            position(),

        ),

        total_capital=100000.0,

    )

    assert (

        result.portfolio.portfolio_risk

        is PortfolioRisk.AGGRESSIVE

    )


# ==========================================================
# Portfolio Metrics
# ==========================================================

def test_total_capital():

    engine = PortfolioEngine(

        portfolio_risk=PortfolioRisk.BALANCED,

    )

    result = engine.build(

        name="Demo",

        portfolio_type=PortfolioType.DIRECTIONAL,

        positions=(

            position(),

        ),

        total_capital=100000.0,

    )

    assert result.total_capital == 100000.0


def test_total_pnl():

    engine = PortfolioEngine(

        portfolio_risk=PortfolioRisk.BALANCED,

    )

    result = engine.build(

        name="Demo",

        portfolio_type=PortfolioType.DIRECTIONAL,

        positions=(

            position(),

        ),

        total_capital=100000.0,

    )

    assert result.total_pnl == 3000.0


# ==========================================================
# Properties
# ==========================================================

def test_allocator_property():

    engine = PortfolioEngine(

        portfolio_risk=PortfolioRisk.BALANCED,

    )

    assert (

        engine.allocator.portfolio_risk

        is PortfolioRisk.BALANCED

    )


def test_builder_property():

    engine = PortfolioEngine(

        portfolio_risk=PortfolioRisk.BALANCED,

    )

    assert engine.builder is not None


# ==========================================================
# Representation
# ==========================================================

def test_repr():

    engine = PortfolioEngine(

        portfolio_risk=PortfolioRisk.BALANCED,

    )

    assert (

        "PortfolioEngine"

        in repr(

            engine,

        )

    )


# ==========================================================
# Deterministic
# ==========================================================

def test_engine_is_deterministic():

    engine = PortfolioEngine(

        portfolio_risk=PortfolioRisk.BALANCED,

    )

    first = engine.build(

        name="Demo",

        portfolio_type=PortfolioType.DIRECTIONAL,

        positions=(

            position(),

        ),

        total_capital=100000.0,

    )

    second = engine.build(

        name="Demo",

        portfolio_type=PortfolioType.DIRECTIONAL,

        positions=(

            position(),

        ),

        total_capital=100000.0,

    )

    assert first == second