"""
============================================================
OptionForge
Strategy Result Tests
============================================================
"""

from optionforge.strategy.execution_plan import (
    ExecutionPlan,
)
from optionforge.strategy.strategy import (
    Strategy,
)
from optionforge.strategy.strategy_result import (
    StrategyResult,
)
from optionforge.strategy.strategy_risk import (
    StrategyRisk,
)
from optionforge.strategy.strategy_type import (
    StrategyType,
)

# ==========================================================
# Helpers
# ==========================================================


def strategy() -> Strategy:

    return Strategy(
        type=StrategyType.LONG_CALL,
        title="Long Call",
        summary="Bullish strategy.",
        direction="Bullish",
        volatility_view="Normal",
        market_environment="Bull Market",
        risk=StrategyRisk.MODERATE,
        capital_required=25000.0,
        max_profit="Unlimited",
        max_loss="Premium Paid",
        probability_of_profit=45.0,
        risk_reward="1:3",
        confidence=92.0,
        rationale=("Bullish Trend",),
    )


def execution_plan() -> ExecutionPlan:

    return ExecutionPlan(
        strategy=strategy(),
        entry_rule="Buy above breakout",
        entry_price="Market",
        target_rule="Trail profits",
        stop_loss_rule="Premium -50%",
        position_size="2 Lots",
        max_capital="₹50,000",
        max_risk="₹10,000",
        expected_reward="Unlimited",
    )


# ==========================================================
# Creation
# ==========================================================


def test_create_strategy_result():

    result = StrategyResult(
        strategy=strategy(),
        execution_plan=execution_plan(),
    )

    assert isinstance(
        result,
        StrategyResult,
    )


# ==========================================================
# Convenience
# ==========================================================


def test_confidence():

    result = StrategyResult(
        strategy=strategy(),
        execution_plan=execution_plan(),
    )

    assert result.confidence == 92.0


def test_strategy_type():

    result = StrategyResult(
        strategy=strategy(),
        execution_plan=execution_plan(),
    )

    assert result.strategy_type == StrategyType.LONG_CALL


def test_probability_of_profit():

    result = StrategyResult(
        strategy=strategy(),
        execution_plan=execution_plan(),
    )

    assert result.probability_of_profit == 45.0


# ==========================================================
# Serialization
# ==========================================================


def test_to_dict():

    result = StrategyResult(
        strategy=strategy(),
        execution_plan=execution_plan(),
    )

    data = result.to_dict()

    assert isinstance(
        data,
        dict,
    )

    assert data["strategy"]["type"] == "LONG_CALL"

    assert data["execution_plan"]["entry_rule"] == "Buy above breakout"


# ==========================================================
# Metadata
# ==========================================================


def test_metadata():

    result = StrategyResult(
        strategy=strategy(),
        execution_plan=execution_plan(),
        metadata={
            "engine": "StrategyEngine",
        },
    )

    assert result.metadata["engine"] == "StrategyEngine"


# ==========================================================
# Timestamp
# ==========================================================


def test_timestamp():

    result = StrategyResult(
        strategy=strategy(),
        execution_plan=execution_plan(),
    )

    assert result.timestamp is not None


# ==========================================================
# Representation
# ==========================================================


def test_str():

    result = StrategyResult(
        strategy=strategy(),
        execution_plan=execution_plan(),
    )

    assert "StrategyResult" in str(
        result,
    )


def test_repr():

    result = StrategyResult(
        strategy=strategy(),
        execution_plan=execution_plan(),
    )

    assert "StrategyResult" in repr(
        result,
    )


# ==========================================================
# Deterministic
# ==========================================================


def test_strategy_result_deterministic():

    first = StrategyResult(
        strategy=strategy(),
        execution_plan=execution_plan(),
    )

    second = StrategyResult(
        strategy=strategy(),
        execution_plan=execution_plan(),
    )

    assert first == second
