"""
============================================================
OptionForge
Strategy Registry Tests
============================================================
"""

from optionforge.decision.strategy_type import (
    StrategyType,
)

from optionforge.strategy.strategy import (
    Strategy,
)
from optionforge.strategy.strategy_registry import (
    StrategyRegistry,
)
from optionforge.strategy.strategy_risk import (
    StrategyRisk,
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
# Empty Registry
# ==========================================================


def test_empty_registry():

    registry = StrategyRegistry()

    assert registry.empty

    assert registry.count == 0

    assert registry.latest is None


# ==========================================================
# Add
# ==========================================================


def test_add_strategy():

    registry = StrategyRegistry()

    registry = registry.add(
        strategy(),
    )

    assert registry.count == 1

    assert not registry.empty


def test_latest():

    s = strategy()

    registry = StrategyRegistry().add(
        s,
    )

    assert registry.latest == s


# ==========================================================
# Extend
# ==========================================================


def test_extend():

    s = strategy()

    registry = StrategyRegistry().extend(
        (
            s,
            s,
        )
    )

    assert registry.count == 2


# ==========================================================
# Collection
# ==========================================================


def test_length():

    registry = StrategyRegistry().add(
        strategy(),
    )

    assert (
        len(
            registry,
        )
        == 1
    )


def test_iteration():

    registry = StrategyRegistry().add(
        strategy(),
    )

    assert (
        len(
            list(registry),
        )
        == 1
    )


def test_getitem():

    s = strategy()

    registry = StrategyRegistry().add(
        s,
    )

    assert registry[0] == s


# ==========================================================
# Serialization
# ==========================================================


def test_to_dict():

    registry = StrategyRegistry().add(
        strategy(),
    )

    data = registry.to_dict()

    assert data["count"] == 1

    assert (
        len(
            data["strategies"],
        )
        == 1
    )


# ==========================================================
# Deterministic
# ==========================================================


def test_registry_is_deterministic():

    s = strategy()

    first = StrategyRegistry().add(
        s,
    )

    second = StrategyRegistry().add(
        s,
    )

    assert first == second


# ==========================================================
# Representation
# ==========================================================


def test_str():

    registry = StrategyRegistry()

    assert "StrategyRegistry" in str(
        registry,
    )


def test_repr():

    registry = StrategyRegistry()

    assert "StrategyRegistry" in repr(
        registry,
    )
