"""
============================================================
OptionForge
Portfolio Engine Integration Tests
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
# Integration
# ==========================================================


def test_end_to_end_pipeline():

    engine = PortfolioEngine(
        portfolio_risk=PortfolioRisk.BALANCED,
    )

    result = engine.build(
        name="Institutional",
        portfolio_type=PortfolioType.DIRECTIONAL,
        positions=(position(),),
        total_capital=100000.0,
    )

    assert isinstance(
        result,
        PortfolioResult,
    )


def test_contains_portfolio():

    result = PortfolioEngine(
        portfolio_risk=PortfolioRisk.BALANCED,
    ).build(
        name="Institutional",
        portfolio_type=PortfolioType.DIRECTIONAL,
        positions=(position(),),
        total_capital=100000.0,
    )

    assert result.portfolio is not None


def test_position_count():

    result = PortfolioEngine(
        portfolio_risk=PortfolioRisk.BALANCED,
    ).build(
        name="Institutional",
        portfolio_type=PortfolioType.DIRECTIONAL,
        positions=(position(),),
        total_capital=100000.0,
    )

    assert result.position_count == 1


def test_allocation_count():

    result = PortfolioEngine(
        portfolio_risk=PortfolioRisk.BALANCED,
    ).build(
        name="Institutional",
        portfolio_type=PortfolioType.DIRECTIONAL,
        positions=(position(),),
        total_capital=100000.0,
    )

    assert result.allocation_count == 1


# ==========================================================
# Portfolio Metrics
# ==========================================================


def test_total_capital():

    result = PortfolioEngine(
        portfolio_risk=PortfolioRisk.BALANCED,
    ).build(
        name="Institutional",
        portfolio_type=PortfolioType.DIRECTIONAL,
        positions=(position(),),
        total_capital=100000.0,
    )

    assert result.total_capital == 100000.0


def test_total_pnl():

    result = PortfolioEngine(
        portfolio_risk=PortfolioRisk.BALANCED,
    ).build(
        name="Institutional",
        portfolio_type=PortfolioType.DIRECTIONAL,
        positions=(position(),),
        total_capital=100000.0,
    )

    assert result.total_pnl == 3000.0


def test_return_percentage():

    result = PortfolioEngine(
        portfolio_risk=PortfolioRisk.BALANCED,
    ).build(
        name="Institutional",
        portfolio_type=PortfolioType.DIRECTIONAL,
        positions=(position(),),
        total_capital=100000.0,
    )

    assert result.return_percentage == 3.0


# ==========================================================
# Risk Propagation
# ==========================================================


def test_portfolio_risk():

    result = PortfolioEngine(
        portfolio_risk=PortfolioRisk.AGGRESSIVE,
    ).build(
        name="Institutional",
        portfolio_type=PortfolioType.DIRECTIONAL,
        positions=(position(),),
        total_capital=100000.0,
    )

    assert result.portfolio.portfolio_risk is PortfolioRisk.AGGRESSIVE


# ==========================================================
# Callable
# ==========================================================


def test_callable():

    engine = PortfolioEngine(
        portfolio_risk=PortfolioRisk.BALANCED,
    )

    result = engine(
        name="Institutional",
        portfolio_type=PortfolioType.DIRECTIONAL,
        positions=(position(),),
        total_capital=100000.0,
    )

    assert isinstance(
        result,
        PortfolioResult,
    )


# ==========================================================
# Representation
# ==========================================================


def test_repr():

    engine = PortfolioEngine(
        portfolio_risk=PortfolioRisk.BALANCED,
    )

    assert "PortfolioEngine" in repr(
        engine,
    )


# ==========================================================
# Deterministic
# ==========================================================


def test_engine_is_deterministic():

    engine = PortfolioEngine(
        portfolio_risk=PortfolioRisk.BALANCED,
    )

    first = engine.build(
        name="Institutional",
        portfolio_type=PortfolioType.DIRECTIONAL,
        positions=(position(),),
        total_capital=100000.0,
    )

    second = engine.build(
        name="Institutional",
        portfolio_type=PortfolioType.DIRECTIONAL,
        positions=(position(),),
        total_capital=100000.0,
    )

    assert first == second
