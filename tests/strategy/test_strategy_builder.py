"""
============================================================
OptionForge
Strategy Builder Tests
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
from optionforge.strategy.strategy import (
    Strategy,
)
from optionforge.strategy.strategy_builder import (
    StrategyBuilder,
)
from optionforge.strategy.strategy_risk import (
    StrategyRisk,
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


def dna() -> MarketDNA:

    return MarketDNA(
        regime=MarketRegime.STRONGLY_BULLISH,
        trend=TrendRegime.STRONG_UPTREND,
        volatility=VolatilityRegime.COMPRESSED,
        liquidity=LiquidityRegime.HIGH,
        dealer_position="LONG GAMMA",
        evidence_score=92.0,
        confidence=94.0,
    )


def decision() -> Decision:

    return Decision(
        decision=DecisionType.STRONG_BUY,
        strategy=StrategyType.LONG_CALL,
        confidence_level=ConfidenceLevel.VERY_HIGH,
        confidence=94.0,
        market_dna=dna(),
        recommendation="Long Call",
        rationale=(
            "Bullish Trend",
            "Dealer Long Gamma",
        ),
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


def test_strategy_is_bullish():

    result = StrategyBuilder().build(
        decision(),
    )

    assert result.type.is_bullish


def test_strategy_title():

    result = StrategyBuilder().build(
        decision(),
    )

    assert (
        len(
            result.title,
        )
        > 0
    )


def test_strategy_summary():

    result = StrategyBuilder().build(
        decision(),
    )

    assert (
        len(
            result.summary,
        )
        > 0
    )


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


def test_volatility_view():

    result = StrategyBuilder().build(
        decision(),
    )

    assert isinstance(
        result.volatility_view,
        str,
    )


def test_risk():

    result = StrategyBuilder().build(
        decision(),
    )

    assert isinstance(
        result.risk,
        StrategyRisk,
    )


# ==========================================================
# Trading Metrics
# ==========================================================


def test_confidence():

    result = StrategyBuilder().build(
        decision(),
    )

    assert result.confidence == 94.0


def test_probability():

    result = StrategyBuilder().build(
        decision(),
    )

    assert 0.0 <= result.probability_of_profit <= 100.0


def test_capital_required():

    result = StrategyBuilder().build(
        decision(),
    )

    assert result.capital_required >= 0


def test_risk_reward():

    result = StrategyBuilder().build(
        decision(),
    )

    assert isinstance(
        result.risk_reward,
        str,
    )


def test_max_profit():

    result = StrategyBuilder().build(
        decision(),
    )

    assert isinstance(
        result.max_profit,
        str,
    )


def test_max_loss():

    result = StrategyBuilder().build(
        decision(),
    )

    assert isinstance(
        result.max_loss,
        str,
    )


# ==========================================================
# Rationale
# ==========================================================


def test_rationale():

    result = StrategyBuilder().build(
        decision(),
    )

    assert (
        len(
            result.rationale,
        )
        > 0
    )


# ==========================================================
# Metadata
# ==========================================================


def test_metadata():

    result = StrategyBuilder().build(
        decision(),
    )

    assert isinstance(
        result.metadata,
        dict,
    )

    assert "builder" in result.metadata

    assert result.metadata["builder"] == "StrategyBuilder"


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

    assert data["type"] == result.type.name

    assert data["risk"] == result.risk.name

    assert data["confidence"] == 94.0

    assert data["capital_required"] == result.capital_required


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

    assert result.type == StrategyType.BULL_CALL_SPREAD


def test_moderate_profile():

    builder = StrategyBuilder(
        StrategySelector(
            RiskProfile.MODERATE,
        )
    )

    result = builder.build(
        decision(),
    )

    assert result.type == StrategyType.BULL_CALL_SPREAD


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


def test_institutional_profile():

    builder = StrategyBuilder(
        StrategySelector(
            RiskProfile.INSTITUTIONAL,
        )
    )

    result = builder.build(
        decision(),
    )

    assert result.type == StrategyType.SYNTHETIC_LONG


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


# ==========================================================
# Strategy Risk
# ==========================================================


def test_strategy_risk():

    result = StrategyBuilder().build(
        decision(),
    )

    assert isinstance(
        result.risk,
        StrategyRisk,
    )


# ==========================================================
# Capital
# ==========================================================


def test_capital_required_is_positive():

    result = StrategyBuilder().build(
        decision(),
    )

    assert result.capital_required > 0


# ==========================================================
# Confidence
# ==========================================================


def test_confidence_matches_decision():

    result = StrategyBuilder().build(
        decision(),
    )

    assert result.confidence == decision().confidence
