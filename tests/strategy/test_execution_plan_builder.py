"""
============================================================
OptionForge
Execution Plan Builder Tests
============================================================
"""

from optionforge.strategy.execution_plan import (
    ExecutionPlan,
)
from optionforge.strategy.execution_plan_builder import (
    ExecutionPlanBuilder,
)
from optionforge.strategy.strategy import (
    Strategy,
)
from optionforge.strategy.strategy_risk import (
    StrategyRisk,
)
from optionforge.strategy.strategy_type import (
    StrategyType,
)

# ==========================================================
# Helper
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


# ==========================================================
# Build
# ==========================================================


def test_returns_execution_plan():

    result = ExecutionPlanBuilder().build(
        strategy(),
    )

    assert isinstance(
        result,
        ExecutionPlan,
    )


def test_strategy_propagation():

    result = ExecutionPlanBuilder().build(
        strategy(),
    )

    assert result.strategy == strategy()


def test_entry_rule():

    result = ExecutionPlanBuilder().build(
        strategy(),
    )

    assert isinstance(
        result.entry_rule,
        str,
    )


def test_stop_loss():

    result = ExecutionPlanBuilder().build(
        strategy(),
    )

    assert isinstance(
        result.stop_loss_rule,
        str,
    )


# ==========================================================
# Position
# ==========================================================


def test_position_size():

    result = ExecutionPlanBuilder().build(
        strategy(),
    )

    assert isinstance(
        result.position_size,
        str,
    )


def test_max_capital():

    result = ExecutionPlanBuilder().build(
        strategy(),
    )

    assert result.max_capital == "₹25,000"


def test_max_risk():

    result = ExecutionPlanBuilder().build(
        strategy(),
    )

    assert isinstance(
        result.max_risk,
        str,
    )


# ==========================================================
# Notes
# ==========================================================


def test_notes():

    result = ExecutionPlanBuilder().build(
        strategy(),
    )

    assert (
        len(
            result.notes,
        )
        > 0
    )


# ==========================================================
# Metadata
# ==========================================================


def test_metadata():

    result = ExecutionPlanBuilder().build(
        strategy(),
    )

    assert result.metadata["builder"] == "ExecutionPlanBuilder"

    assert result.metadata["strategy"] == StrategyType.LONG_CALL.name


# ==========================================================
# Serialization
# ==========================================================


def test_to_dict():

    result = ExecutionPlanBuilder().build(
        strategy(),
    )

    data = result.to_dict()

    assert isinstance(
        data,
        dict,
    )

    assert data["strategy"]["type"] == "LONG_CALL"


# ==========================================================
# Deterministic
# ==========================================================


def test_builder_is_deterministic():

    builder = ExecutionPlanBuilder()

    first = builder.build(
        strategy(),
    )

    second = builder.build(
        strategy(),
    )

    assert first == second


# ==========================================================
# Representation
# ==========================================================


def test_repr():

    builder = ExecutionPlanBuilder()

    assert "ExecutionPlanBuilder" in repr(builder)
