"""
============================================================
OptionForge
BacktestRegistry Tests
============================================================
"""

from optionforge.backtest.backtest_builder import (
    BacktestBuilder,
)
from optionforge.backtest.backtest_registry import (
    BacktestRegistry,
)


def registry():

    return BacktestRegistry()


def test_returns_builder():

    assert isinstance(
        registry().builder,
        BacktestBuilder,
    )


def test_get_builder():

    assert isinstance(
        registry().get_builder(),
        BacktestBuilder,
    )


def test_same_builder():

    r = registry()

    assert r.builder is r.get_builder()


def test_builder_type():

    assert registry().builder.__class__.__name__ == "BacktestBuilder"


def test_repr():

    assert "BacktestRegistry" in repr(
        registry(),
    )


def test_multiple_calls():

    r = registry()

    assert r.get_builder() is r.get_builder()


def test_registry_exists():

    assert registry() is not None


def test_builder_exists():

    assert registry().builder is not None
