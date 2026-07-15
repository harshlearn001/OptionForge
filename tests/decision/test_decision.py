"""
============================================================
OptionForge
Decision Tests
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
# Helper
# ==========================================================


def market_dna() -> MarketDNA:

    return MarketDNA(
        regime=MarketRegime.STRONGLY_BULLISH,
        trend=TrendRegime.STRONG_UPTREND,
        volatility=VolatilityRegime.COMPRESSED,
        liquidity=LiquidityRegime.HIGH,
        dealer_position="LONG GAMMA",
        evidence_score=91.0,
        confidence=92.0,
    )


# ==========================================================
# Tests
# ==========================================================


def test_decision_creation():

    decision = Decision(
        decision=DecisionType.STRONG_BUY,
        strategy=StrategyType.LONG_CALL,
        confidence_level=ConfidenceLevel.VERY_HIGH,
        confidence=92.0,
        market_dna=market_dna(),
        recommendation="Long Call",
        rationale=("Bullish",),
    )

    assert decision.confidence == 92.0

    assert decision.decision is DecisionType.STRONG_BUY

    assert decision.strategy is StrategyType.LONG_CALL


def test_tradeable():

    decision = Decision(
        decision=DecisionType.STRONG_BUY,
        strategy=StrategyType.LONG_CALL,
        confidence_level=ConfidenceLevel.VERY_HIGH,
        confidence=95.0,
        market_dna=market_dna(),
        recommendation="Long Call",
        rationale=(),
    )

    assert decision.is_tradeable


def test_buy():

    decision = Decision(
        decision=DecisionType.BUY,
        strategy=StrategyType.BULL_CALL_SPREAD,
        confidence_level=ConfidenceLevel.HIGH,
        confidence=80.0,
        market_dna=market_dna(),
        recommendation="Bull Call Spread",
        rationale=(),
    )

    assert decision.is_buy

    assert not decision.is_sell


def test_dict():

    decision = Decision(
        decision=DecisionType.HOLD,
        strategy=StrategyType.CASH,
        confidence_level=ConfidenceLevel.MODERATE,
        confidence=60.0,
        market_dna=market_dna(),
        recommendation="Cash",
        rationale=("Neutral",),
    )

    data = decision.to_dict()

    assert data["decision"] == "HOLD"

    assert data["strategy"] == "CASH"

    assert data["confidence_level"] == "MODERATE"

    assert data["confidence"] == 60.0


def test_invalid_confidence():

    import pytest

    with pytest.raises(ValueError):

        Decision(
            decision=DecisionType.BUY,
            strategy=StrategyType.LONG_CALL,
            confidence_level=ConfidenceLevel.HIGH,
            confidence=120.0,
            market_dna=market_dna(),
            recommendation="Long Call",
            rationale=(),
        )
