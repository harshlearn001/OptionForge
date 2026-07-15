"""
============================================================
OptionForge
Decision Builder Tests
============================================================
"""

from optionforge.decision.confidence_level import (
    ConfidenceLevel,
)
from optionforge.decision.decision import Decision
from optionforge.decision.decision_builder import (
    DecisionBuilder,
)
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

# ==========================================================
# Helpers
# ==========================================================


def bullish_dna():

    return MarketDNA(
        regime=MarketRegime.STRONGLY_BULLISH,
        trend=TrendRegime.STRONG_UPTREND,
        volatility=VolatilityRegime.COMPRESSED,
        liquidity=LiquidityRegime.HIGH,
        dealer_position="LONG GAMMA",
        evidence_score=91.0,
        confidence=95.0,
    )


def bearish_dna():

    return MarketDNA(
        regime=MarketRegime.STRONGLY_BEARISH,
        trend=TrendRegime.STRONG_DOWNTREND,
        volatility=VolatilityRegime.EXTREME,
        liquidity=LiquidityRegime.LOW,
        dealer_position="SHORT GAMMA",
        evidence_score=-92.0,
        confidence=94.0,
    )


def neutral_dna():

    return MarketDNA(
        regime=MarketRegime.NEUTRAL,
        trend=TrendRegime.SIDEWAYS,
        volatility=VolatilityRegime.NORMAL,
        liquidity=LiquidityRegime.NORMAL,
        dealer_position="UNKNOWN",
        evidence_score=0.0,
        confidence=55.0,
    )


# ==========================================================
# Result
# ==========================================================


def test_returns_decision():

    result = DecisionBuilder().build(bullish_dna())

    assert isinstance(
        result,
        Decision,
    )


# ==========================================================
# Bullish
# ==========================================================


def test_strong_buy():

    result = DecisionBuilder().build(bullish_dna())

    assert result.decision == DecisionType.STRONG_BUY


def test_bullish_strategy():

    result = DecisionBuilder().build(bullish_dna())

    assert result.strategy == StrategyType.LONG_CALL


# ==========================================================
# Bearish
# ==========================================================


def test_strong_sell():

    result = DecisionBuilder().build(bearish_dna())

    assert result.decision == DecisionType.STRONG_SELL


def test_bearish_strategy():

    result = DecisionBuilder().build(bearish_dna())

    assert result.strategy == StrategyType.LONG_PUT


# ==========================================================
# Neutral
# ==========================================================


def test_hold():

    result = DecisionBuilder().build(neutral_dna())

    assert result.decision == DecisionType.HOLD


def test_cash_strategy():

    result = DecisionBuilder().build(neutral_dna())

    assert result.strategy == StrategyType.CASH


# ==========================================================
# Confidence
# ==========================================================


def test_confidence_level():

    result = DecisionBuilder().build(bullish_dna())

    assert result.confidence_level == ConfidenceLevel.VERY_HIGH


def test_confidence_propagation():

    result = DecisionBuilder().build(bullish_dna())

    assert result.confidence == 95.0


# ==========================================================
# Recommendation
# ==========================================================


def test_recommendation():

    result = DecisionBuilder().build(bullish_dna())

    assert isinstance(
        result.recommendation,
        str,
    )


# ==========================================================
# Rationale
# ==========================================================


def test_rationale():

    result = DecisionBuilder().build(bullish_dna())

    assert len(result.rationale) > 0


# ==========================================================
# Deterministic
# ==========================================================


def test_builder_is_deterministic():

    first = DecisionBuilder().build(bullish_dna())

    second = DecisionBuilder().build(bullish_dna())

    assert first == second
