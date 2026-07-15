"""
============================================================
OptionForge
Strategy Selector Tests
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

from optionforge.strategy.risk_profile import (
    RiskProfile,
)
from optionforge.strategy.strategy_selector import (
    StrategySelector,
)
from optionforge.strategy.strategy_type import (
    StrategyType,
)

# ==========================================================
# Helpers
# ==========================================================


def decision() -> Decision:
    """
    Strong bullish with LOW volatility.
    """

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


def high_volatility_decision() -> Decision:
    """
    Strong bullish with NON-LOW volatility.

    This exercises the second branch inside
    StrategyRules.
    """

    dna = MarketDNA(
        regime=MarketRegime.STRONGLY_BULLISH,
        trend=TrendRegime.STRONG_UPTREND,
        volatility=VolatilityRegime.HIGH,
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
# Default
# ==========================================================


def test_default_profile():

    selector = StrategySelector()

    assert selector.risk_profile is RiskProfile.MODERATE


# ==========================================================
# Selection
# ==========================================================


def test_select_returns_strategy_type():

    selector = StrategySelector()

    result = selector.select(
        decision(),
    )

    assert isinstance(
        result,
        StrategyType,
    )


def test_callable():

    selector = StrategySelector()

    assert selector(
        decision(),
    ) == selector.select(
        decision(),
    )


# ==========================================================
# Risk Profiles
# ==========================================================


def test_conservative():

    selector = StrategySelector(
        RiskProfile.CONSERVATIVE,
    )

    result = selector.select(
        decision(),
    )

    assert result == StrategyType.BULL_CALL_SPREAD


def test_moderate():

    selector = StrategySelector(
        RiskProfile.MODERATE,
    )

    result = selector.select(
        decision(),
    )

    assert result == StrategyType.BULL_CALL_SPREAD


def test_aggressive():

    selector = StrategySelector(
        RiskProfile.AGGRESSIVE,
    )

    result = selector.select(
        decision(),
    )

    assert result == StrategyType.LONG_CALL


def test_institutional():

    selector = StrategySelector(
        RiskProfile.INSTITUTIONAL,
    )

    result = selector.select(
        decision(),
    )

    assert result == StrategyType.SYNTHETIC_LONG


# ==========================================================
# High Volatility Branch
# ==========================================================


def test_conservative_high_volatility():

    selector = StrategySelector(
        RiskProfile.CONSERVATIVE,
    )

    result = selector.select(
        high_volatility_decision(),
    )

    assert result == StrategyType.BULL_PUT_SPREAD


# ==========================================================
# Deterministic
# ==========================================================


def test_selector_is_deterministic():

    selector = StrategySelector()

    first = selector.select(
        decision(),
    )

    second = selector.select(
        decision(),
    )

    assert first == second


# ==========================================================
# Representation
# ==========================================================


def test_repr():

    selector = StrategySelector()

    assert "StrategySelector" in repr(
        selector,
    )
