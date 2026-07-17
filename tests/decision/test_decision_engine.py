"""
============================================================
OptionForge
Decision Engine Tests
============================================================
"""

from optionforge.decision.decision_builder import (
    DecisionBuilder,
)
from optionforge.decision.decision_engine import (
    DecisionEngine,
)
from optionforge.decision.rules.decision_rule import (
    DecisionRule,
)

from optionforge.decision.decision import (
    Decision,
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


def dna() -> MarketDNA:

    return MarketDNA(
        regime=MarketRegime.STRONGLY_BULLISH,
        trend=TrendRegime.STRONG_UPTREND,
        volatility=VolatilityRegime.COMPRESSED,
        liquidity=LiquidityRegime.HIGH,
        dealer_position="LONG GAMMA",
        evidence_score=92.0,
        confidence=95.0,
    )


class DummyDecisionRule(DecisionRule):

    def evaluate(
        self,
        *,
        market_dna: MarketDNA,
        builder: DecisionBuilder,
    ) -> Decision | None:

        return builder.build(
            market_dna=market_dna,
        )


class NullDecisionRule(DecisionRule):

    def evaluate(
        self,
        *,
        market_dna: MarketDNA,
        builder: DecisionBuilder,
    ):

        return None


# ==========================================================
# Tests
# ==========================================================


def test_engine_executes_rule():

    engine = DecisionEngine(
        [
            DummyDecisionRule(),
        ]
    )

    registry = engine.build(dna())

    assert len(registry) == 1


def test_engine_ignores_none():

    engine = DecisionEngine(
        [
            NullDecisionRule(),
        ]
    )

    registry = engine.build(dna())

    assert len(registry) == 0


def test_engine_multiple_rules():

    engine = DecisionEngine(
        [
            DummyDecisionRule(),
            DummyDecisionRule(),
        ]
    )

    registry = engine.build(dna())

    assert len(registry) >= 1


def test_rule_count():

    engine = DecisionEngine(
        [
            DummyDecisionRule(),
            NullDecisionRule(),
        ]
    )

    assert engine.rule_count == 2


def test_len():

    engine = DecisionEngine(
        [
            DummyDecisionRule(),
            DummyDecisionRule(),
        ]
    )

    assert len(engine) == 2


def test_repr():

    engine = DecisionEngine(
        [
            DummyDecisionRule(),
        ]
    )

    assert "DecisionEngine" in repr(engine)


def test_engine_is_deterministic():

    engine = DecisionEngine(
        [
            DummyDecisionRule(),
        ]
    )

    first = engine.build(dna())

    second = engine.build(dna())

    assert first.best == second.best
