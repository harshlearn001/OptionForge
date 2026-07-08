"""
============================================================
OptionForge
Strategy Builder Tests
============================================================
"""

from optionforge.decision.confidence_level import (
    ConfidenceLevel,
)
from optionforge.decision.decision import Decision
from optionforge.decision.decision_type import (
    DecisionType,
)
from optionforge.decision.strategy_type import (
    StrategyType,
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
from optionforge.marketdna.liquidity_regime import (
    LiquidityRegime,
)

from optionforge.strategy.strategy import Strategy
from optionforge.strategy.strategy_builder import (
    StrategyBuilder,
)
from optionforge.strategy.strategy_selector import (
    StrategySelector,
)
from optionforge.strategy.risk_profile import (
    RiskProfile,
)


# ==========================================================
# Helpers
# ==========================================================

def dna():

    return MarketDNA(

        regime=MarketRegime.STRONGLY_BULLISH,

        trend=TrendRegime.STRONG_UPTREND,

        volatility=VolatilityRegime.COMPRESSED,

        liquidity=LiquidityRegime.HIGH,

        dealer_position="LONG GAMMA",

        evidence_score=92.0,

        confidence=94.0,

    )


def decision():

    return Decision(

        decision=DecisionType.STRONG_BUY,

        strategy=StrategyType.LONG_CALL,

        confidence_level=ConfidenceLevel.VERY_HIGH,

        confidence=94.0,

        market_dna=dna(),

        recommendation="Long Call",

        rationale=("Demo",),

    )


# ==========================================================
# Result
# ==========================================================

def test_returns_strategy():

    builder = StrategyBuilder()

    result = builder.build(

        decision(),

    )

    assert isinstance(

        result,

        Strategy,

    )


# ==========================================================
# Strategy
# ==========================================================

def test_strategy_type():

    result = StrategyBuilder().build(

        decision(),

    )

    assert isinstance(

        result.type,

        StrategyType,

    )


def test_strategy_title():

    result = StrategyBuilder().build(

        decision(),

    )

    assert len(result.title) > 0


def test_strategy_summary():

    result = StrategyBuilder().build(

        decision(),

    )

    assert len(result.summary) > 0


# ==========================================================
# Classification
# ==========================================================

def test_direction():

    result = StrategyBuilder().build(

        decision(),

    )

    assert result.direction == "Bullish"


def test_market_environment():

    result = StrategyBuilder().build(

        decision(),

    )

    assert isinstance(

        result.market_environment,

        str,

    )


# ==========================================================
# Confidence
# ==========================================================

def test_confidence():

    result = StrategyBuilder().build(

        decision(),

    )

    assert result.confidence == 94.0


# ==========================================================
# Probability
# ==========================================================

def test_probability():

    result = StrategyBuilder().build(

        decision(),

    )

    assert (

        0.0

        <= result.probability_of_profit

        <= 100.0

    )


# ==========================================================
# Risk Reward
# ==========================================================

def test_risk_reward():

    result = StrategyBuilder().build(

        decision(),

    )

    assert isinstance(

        result.risk_reward,

        str,

    )


# ==========================================================
# Serialization
# ==========================================================

def test_to_dict():

    result = StrategyBuilder().build(

        decision(),

    )

    data = result.to_dict()

    assert isinstance(

        data,

        dict,

    )


# ==========================================================
# Risk Profile
# ==========================================================

def test_conservative_profile():

    builder = StrategyBuilder(

        StrategySelector(

            RiskProfile.CONSERVATIVE,

        )

    )

    result = builder.build(

        decision(),

    )

    assert result.type == StrategyType.BULL_PUT_SPREAD


def test_aggressive_profile():

    builder = StrategyBuilder(

        StrategySelector(

            RiskProfile.AGGRESSIVE,

        )

    )

    result = builder.build(

        decision(),

    )

    assert result.type == StrategyType.LONG_CALL


# ==========================================================
# Deterministic
# ==========================================================

def test_builder_is_deterministic():

    builder = StrategyBuilder()

    first = builder.build(

        decision(),

    )

    second = builder.build(

        decision(),

    )

    assert first == second