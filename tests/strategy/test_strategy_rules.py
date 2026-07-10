"""
============================================================
OptionForge
Strategy Rules Tests
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
from optionforge.strategy.strategy_rules import (
    StrategyRules,
)
from optionforge.strategy.strategy_type import (
    StrategyType,
)


# ==========================================================
# Helpers
# ==========================================================

def build_decision(

    decision_type: DecisionType,

    volatility: VolatilityRegime,

) -> Decision:

    dna = MarketDNA(

        regime=MarketRegime.STRONGLY_BULLISH,

        trend=TrendRegime.STRONG_UPTREND,

        volatility=volatility,

        liquidity=LiquidityRegime.HIGH,

        dealer_position="LONG GAMMA",

        evidence_score=95.0,

        confidence=95.0,

    )

    return Decision(

        decision=decision_type,

        strategy=StrategyType.LONG_CALL,

        confidence_level=ConfidenceLevel.VERY_HIGH,

        confidence=95.0,

        market_dna=dna,

        recommendation="Demo",

        rationale=("Demo",),

    )


# ==========================================================
# Strong Buy
# ==========================================================

def test_strong_buy_conservative_low_vol():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.STRONG_BUY,

            VolatilityRegime.COMPRESSED,

        ),

        risk=RiskProfile.CONSERVATIVE,

    )

    assert result == StrategyType.BULL_CALL_SPREAD


def test_strong_buy_moderate_low_vol():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.STRONG_BUY,

            VolatilityRegime.COMPRESSED,

        ),

        risk=RiskProfile.MODERATE,

    )

    assert result == StrategyType.BULL_CALL_SPREAD


def test_strong_buy_aggressive_low_vol():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.STRONG_BUY,

            VolatilityRegime.COMPRESSED,

        ),

        risk=RiskProfile.AGGRESSIVE,

    )

    assert result == StrategyType.LONG_CALL


def test_strong_buy_institutional_low_vol():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.STRONG_BUY,

            VolatilityRegime.COMPRESSED,

        ),

        risk=RiskProfile.INSTITUTIONAL,

    )

    assert result == StrategyType.SYNTHETIC_LONG

# ==========================================================
# Strong Buy (Non-Low Volatility)
# ==========================================================

def test_strong_buy_conservative_high_vol():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.STRONG_BUY,

            VolatilityRegime.HIGH,

        ),

        risk=RiskProfile.CONSERVATIVE,

    )

    assert result == StrategyType.BULL_PUT_SPREAD


def test_strong_buy_moderate_high_vol():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.STRONG_BUY,

            VolatilityRegime.HIGH,

        ),

        risk=RiskProfile.MODERATE,

    )

    assert result == StrategyType.BULL_PUT_SPREAD


def test_strong_buy_aggressive_high_vol():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.STRONG_BUY,

            VolatilityRegime.HIGH,

        ),

        risk=RiskProfile.AGGRESSIVE,

    )

    assert result == StrategyType.LONG_CALL


# ==========================================================
# Bullish
# ==========================================================

def test_buy_conservative():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.BUY,

            VolatilityRegime.NORMAL,

        ),

        risk=RiskProfile.CONSERVATIVE,

    )

    assert result == StrategyType.BULL_CALL_SPREAD


def test_buy_aggressive():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.BUY,

            VolatilityRegime.NORMAL,

        ),

        risk=RiskProfile.AGGRESSIVE,

    )

    assert result == StrategyType.LONG_CALL


def test_accumulate():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.ACCUMULATE,

            VolatilityRegime.NORMAL,

        ),

        risk=RiskProfile.MODERATE,

    )

    assert result == StrategyType.BULL_CALL_SPREAD


# ==========================================================
# Strong Bearish
# ==========================================================

def test_strong_sell_conservative():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.STRONG_SELL,

            VolatilityRegime.EXTREME,

        ),

        risk=RiskProfile.CONSERVATIVE,

    )

    assert result == StrategyType.BEAR_PUT_SPREAD


def test_strong_sell_aggressive():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.STRONG_SELL,

            VolatilityRegime.EXTREME,

        ),

        risk=RiskProfile.AGGRESSIVE,

    )

    assert result == StrategyType.LONG_PUT 
# ==========================================================
# Bearish
# ==========================================================

def test_sell_conservative():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.SELL,

            VolatilityRegime.NORMAL,

        ),

        risk=RiskProfile.CONSERVATIVE,

    )

    assert result == StrategyType.BEAR_PUT_SPREAD


def test_sell_aggressive():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.SELL,

            VolatilityRegime.NORMAL,

        ),

        risk=RiskProfile.AGGRESSIVE,

    )

    assert result == StrategyType.LONG_PUT


# ==========================================================
# Hold
# ==========================================================

def test_hold_low_volatility():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.HOLD,

            VolatilityRegime.COMPRESSED,

        ),

        risk=RiskProfile.MODERATE,

    )

    assert result == StrategyType.IRON_CONDOR


def test_hold_normal_volatility():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.HOLD,

            VolatilityRegime.NORMAL,

        ),

        risk=RiskProfile.MODERATE,

    )

    assert result == StrategyType.CALENDAR_SPREAD


# ==========================================================
# Risk Actions
# ==========================================================

def test_hedge_high_volatility():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.HEDGE,

            VolatilityRegime.HIGH,

        ),

        risk=RiskProfile.MODERATE,

    )

    assert result == StrategyType.PROTECTIVE_PUT


def test_hedge_normal_volatility():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.HEDGE,

            VolatilityRegime.NORMAL,

        ),

        risk=RiskProfile.MODERATE,

    )

    assert result == StrategyType.COLLAR


def test_reduce():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.REDUCE,

            VolatilityRegime.NORMAL,

        ),

        risk=RiskProfile.MODERATE,

    )

    assert result == StrategyType.COVERED_CALL


def test_exit():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.EXIT,

            VolatilityRegime.NORMAL,

        ),

        risk=RiskProfile.MODERATE,

    )

    assert result == StrategyType.NO_POSITION


def test_no_action():

    result = StrategyRules.select(

        decision=build_decision(

            DecisionType.NO_ACTION,

            VolatilityRegime.NORMAL,

        ),

        risk=RiskProfile.MODERATE,

    )

    assert result == StrategyType.CASH


# ==========================================================
# Deterministic
# ==========================================================

def test_strategy_rules_are_deterministic():

    decision = build_decision(

        DecisionType.STRONG_BUY,

        VolatilityRegime.COMPRESSED,

    )

    first = StrategyRules.select(

        decision=decision,

        risk=RiskProfile.MODERATE,

    )

    second = StrategyRules.select(

        decision=decision,

        risk=RiskProfile.MODERATE,

    )

    assert first == second