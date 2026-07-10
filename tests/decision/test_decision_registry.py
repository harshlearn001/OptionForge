"""
============================================================
OptionForge
Decision Registry Tests
============================================================
"""

from optionforge.decision.confidence_level import (
    ConfidenceLevel,
)
from optionforge.decision.decision import (
    Decision,
)
from optionforge.decision.decision_registry import (
    DecisionRegistry,
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

def dna(confidence: float = 90.0):

    return MarketDNA(

        regime=MarketRegime.STRONGLY_BULLISH,

        trend=TrendRegime.STRONG_UPTREND,

        volatility=VolatilityRegime.COMPRESSED,

        liquidity=LiquidityRegime.HIGH,

        dealer_position="LONG GAMMA",

        evidence_score=90.0,

        confidence=confidence,

    )


def decision(

    dtype: DecisionType = DecisionType.BUY,

    confidence: float = 90.0,

):

    return Decision(

        decision=dtype,

        strategy=StrategyType.LONG_CALL,

        confidence_level=ConfidenceLevel.from_score(

            confidence,

        ),

        confidence=confidence,

        market_dna=dna(confidence),

        recommendation="Long Call",

        rationale=("Bullish",),

    )


# ==========================================================
# Tests
# ==========================================================

def test_add():

    registry = DecisionRegistry()

    registry.add(

        decision()

    )

    assert len(registry) == 1


def test_get():

    registry = DecisionRegistry()

    obj = decision()

    registry.add(obj)

    assert registry.get(

        DecisionType.BUY.name

    ) == obj


def test_exists():

    registry = DecisionRegistry()

    registry.add(

        decision()

    )

    assert registry.exists(

        DecisionType.BUY.name

    )


def test_by_type():

    registry = DecisionRegistry()

    obj = decision()

    registry.add(obj)

    assert registry.by_type(

        DecisionType.BUY

    ) == obj


def test_best():

    registry = DecisionRegistry()

    registry.add(

        decision(

            DecisionType.BUY,

            82,

        )

    )

    registry.add(

        decision(

            DecisionType.STRONG_BUY,

            95,

        )

    )

    assert (

        registry.best.confidence

        == 95

    )


def test_average_confidence():

    registry = DecisionRegistry()

    registry.add(

        decision(

            DecisionType.BUY,

            80,

        )

    )

    registry.add(

        decision(

            DecisionType.STRONG_BUY,

            100,

        )

    )

    assert (

        registry.average_confidence

        == 90.0

    )


def test_clear():

    registry = DecisionRegistry()

    registry.add(

        decision()

    )

    registry.clear()

    assert len(registry) == 0


def test_iteration():

    registry = DecisionRegistry()

    registry.add(

        decision()

    )

    count = 0

    for _ in registry:

        count += 1

    assert count == 1


def test_to_dict():

    registry = DecisionRegistry()

    registry.add(

        decision()

    )

    data = registry.to_dict()

    assert len(data) == 1

    assert data[0]["decision"] == "BUY"