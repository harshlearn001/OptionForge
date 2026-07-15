"""
============================================================
OptionForge
Decision Engine Integration Tests
============================================================
"""

from optionforge.decision.decision_engine import (
    DecisionEngine,
)

from optionforge.decision.rules.institutional_decision_rule import (
    InstitutionalDecisionRule,
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
        evidence_score=92.0,
        confidence=95.0,
    )


def bearish_dna():

    return MarketDNA(
        regime=MarketRegime.STRONGLY_BEARISH,
        trend=TrendRegime.STRONG_DOWNTREND,
        volatility=VolatilityRegime.EXTREME,
        liquidity=LiquidityRegime.LOW,
        dealer_position="SHORT GAMMA",
        evidence_score=-91.0,
        confidence=94.0,
    )


# ==========================================================
# Integration
# ==========================================================


def test_bullish_pipeline():

    engine = DecisionEngine(
        [
            InstitutionalDecisionRule(),
        ]
    )

    registry = engine.build(bullish_dna())

    assert len(registry) == 1

    assert registry.best is not None

    assert registry.best.market_dna.is_bullish

    assert registry.best.is_buy


def test_bearish_pipeline():

    engine = DecisionEngine(
        [
            InstitutionalDecisionRule(),
        ]
    )

    registry = engine.build(bearish_dna())

    assert len(registry) == 1

    assert registry.best is not None

    assert registry.best.market_dna.is_bearish

    assert registry.best.is_sell


def test_pipeline_is_repeatable():

    engine = DecisionEngine(
        [
            InstitutionalDecisionRule(),
        ]
    )

    first = engine.build(bullish_dna())

    second = engine.build(bullish_dna())

    assert first.best == second.best


def test_registry_contains_decision():

    engine = DecisionEngine(
        [
            InstitutionalDecisionRule(),
        ]
    )

    registry = engine.build(bullish_dna())

    assert registry.best is not None

    assert registry.confidence == 95.0
