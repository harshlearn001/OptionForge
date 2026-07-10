"""
============================================================
OptionForge
Strategy Engine Integration Tests
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

from optionforge.strategy.strategy_engine import (
    StrategyEngine,
)
from optionforge.strategy.strategy_result import (
    StrategyResult,
)
from optionforge.strategy.strategy_type import (
    StrategyType,
)


# ==========================================================
# Helper
# ==========================================================

def decision() -> Decision:

    dna = MarketDNA(

        regime=MarketRegime.STRONGLY_BULLISH,

        trend=TrendRegime.STRONG_UPTREND,

        volatility=VolatilityRegime.COMPRESSED,

        liquidity=LiquidityRegime.HIGH,

        dealer_position="LONG GAMMA",

        evidence_score=95.0,

        confidence=95.0,

    )

    return Decision(

        decision=DecisionType.STRONG_BUY,

        strategy=StrategyType.LONG_CALL,

        confidence_level=ConfidenceLevel.VERY_HIGH,

        confidence=95.0,

        market_dna=dna,

        recommendation="Long Call",

        rationale=("Bullish",),

    )


# ==========================================================
# Integration
# ==========================================================

def test_returns_strategy_result():

    result = StrategyEngine().build(

        decision(),

    )

    assert isinstance(

        result,

        StrategyResult,

    )


def test_contains_strategy():

    result = StrategyEngine().build(

        decision(),

    )

    assert result.strategy is not None


def test_contains_execution_plan():

    result = StrategyEngine().build(

        decision(),

    )

    assert result.execution_plan is not None


def test_strategy_type():

    result = StrategyEngine().build(

        decision(),

    )

    assert result.strategy.type == StrategyType.BULL_CALL_SPREAD


def test_confidence():

    result = StrategyEngine().build(

        decision(),

    )

    assert result.confidence == 95.0


def test_probability():

    result = StrategyEngine().build(

        decision(),

    )

    assert (

        0.0

        <= result.probability_of_profit

        <= 100.0

    )


def test_to_dict():

    result = StrategyEngine().build(

        decision(),

    )

    data = result.to_dict()

    assert isinstance(

        data,

        dict,

    )


def test_engine_is_deterministic():

    engine = StrategyEngine()

    first = engine.build(

        decision(),

    )

    second = engine.build(

        decision(),

    )

    assert first == second