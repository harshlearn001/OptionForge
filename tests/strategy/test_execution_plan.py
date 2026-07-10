"""
============================================================
OptionForge
Execution Plan Tests
============================================================
"""

from optionforge.strategy.execution_plan import (
    ExecutionPlan,
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
# Creation
# ==========================================================

def test_create_execution_plan():

    plan = ExecutionPlan(

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

    assert isinstance(

        plan,

        ExecutionPlan,

    )


def test_strategy_reference():

    plan = ExecutionPlan(

        strategy=strategy(),

        entry_rule="Entry",

        entry_price="Market",

        target_rule="Target",

        stop_loss_rule="SL",

        position_size="1 Lot",

        max_capital="₹25,000",

        max_risk="₹5,000",

        expected_reward="Unlimited",

    )

    assert plan.strategy.type == StrategyType.LONG_CALL


# ==========================================================
# Fields
# ==========================================================

def test_entry_rule():

    plan = ExecutionPlan(

        strategy=strategy(),

        entry_rule="Breakout",

        entry_price="Market",

        target_rule="Target",

        stop_loss_rule="SL",

        position_size="1 Lot",

        max_capital="₹25,000",

        max_risk="₹5,000",

        expected_reward="Unlimited",

    )

    assert plan.entry_rule == "Breakout"


def test_stop_loss():

    plan = ExecutionPlan(

        strategy=strategy(),

        entry_rule="Entry",

        entry_price="Market",

        target_rule="Target",

        stop_loss_rule="Premium -50%",

        position_size="1 Lot",

        max_capital="₹25,000",

        max_risk="₹5,000",

        expected_reward="Unlimited",

    )

    assert plan.stop_loss_rule == "Premium -50%"

# ==========================================================
# Notes
# ==========================================================

def test_notes():

    plan = ExecutionPlan(

        strategy=strategy(),

        entry_rule="Entry",

        entry_price="Market",

        target_rule="Target",

        stop_loss_rule="SL",

        position_size="1 Lot",

        max_capital="₹25,000",

        max_risk="₹5,000",

        expected_reward="Unlimited",

        notes=(

            "Wait for confirmation",

            "Avoid earnings",

        ),

    )

    assert len(plan.notes) == 2


# ==========================================================
# Metadata
# ==========================================================

def test_metadata():

    plan = ExecutionPlan(

        strategy=strategy(),

        entry_rule="Entry",

        entry_price="Market",

        target_rule="Target",

        stop_loss_rule="SL",

        position_size="1 Lot",

        max_capital="₹25,000",

        max_risk="₹5,000",

        expected_reward="Unlimited",

        metadata={

            "engine": "StrategyEngine",

        },

    )

    assert plan.metadata["engine"] == "StrategyEngine"


# ==========================================================
# Serialization
# ==========================================================

def test_to_dict():

    plan = ExecutionPlan(

        strategy=strategy(),

        entry_rule="Entry",

        entry_price="Market",

        target_rule="Target",

        stop_loss_rule="SL",

        position_size="1 Lot",

        max_capital="₹25,000",

        max_risk="₹5,000",

        expected_reward="Unlimited",

    )

    data = plan.to_dict()

    assert isinstance(

        data,

        dict,

    )

    assert data["strategy"]["type"] == "LONG_CALL"

    assert data["entry_rule"] == "Entry"

    assert data["position_size"] == "1 Lot"


# ==========================================================
# Timestamp
# ==========================================================

def test_timestamp():

    plan = ExecutionPlan(

        strategy=strategy(),

        entry_rule="Entry",

        entry_price="Market",

        target_rule="Target",

        stop_loss_rule="SL",

        position_size="1 Lot",

        max_capital="₹25,000",

        max_risk="₹5,000",

        expected_reward="Unlimited",

    )

    assert plan.timestamp is not None


# ==========================================================
# Representation
# ==========================================================

def test_str():

    plan = ExecutionPlan(

        strategy=strategy(),

        entry_rule="Entry",

        entry_price="Market",

        target_rule="Target",

        stop_loss_rule="SL",

        position_size="1 Lot",

        max_capital="₹25,000",

        max_risk="₹5,000",

        expected_reward="Unlimited",

    )

    assert "ExecutionPlan" in str(

        plan,

    )


def test_repr():

    plan = ExecutionPlan(

        strategy=strategy(),

        entry_rule="Entry",

        entry_price="Market",

        target_rule="Target",

        stop_loss_rule="SL",

        position_size="1 Lot",

        max_capital="₹25,000",

        max_risk="₹5,000",

        expected_reward="Unlimited",

    )

    assert "ExecutionPlan" in repr(

        plan,

    )


# ==========================================================
# Deterministic
# ==========================================================

def test_execution_plan_deterministic():

    first = ExecutionPlan(

        strategy=strategy(),

        entry_rule="Entry",

        entry_price="Market",

        target_rule="Target",

        stop_loss_rule="SL",

        position_size="1 Lot",

        max_capital="₹25,000",

        max_risk="₹5,000",

        expected_reward="Unlimited",

    )

    second = ExecutionPlan(

        strategy=strategy(),

        entry_rule="Entry",

        entry_price="Market",

        target_rule="Target",

        stop_loss_rule="SL",

        position_size="1 Lot",

        max_capital="₹25,000",

        max_risk="₹5,000",

        expected_reward="Unlimited",

    )

    assert first == second