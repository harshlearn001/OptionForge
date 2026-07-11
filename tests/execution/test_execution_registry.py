"""
============================================================
OptionForge
ExecutionRegistry Tests
============================================================
"""

from optionforge.execution.execution_builder import (
    ExecutionBuilder,
)
from optionforge.execution.execution_registry import (
    ExecutionRegistry,
)


def registry():

    return ExecutionRegistry()


def test_returns_builder():

    assert isinstance(

        registry().builder,

        ExecutionBuilder,

    )


def test_get_builder():

    assert isinstance(

        registry().get_builder(),

        ExecutionBuilder,

    )


def test_same_builder():

    r = registry()

    assert (

        r.builder

        is

        r.get_builder()

    )


def test_builder_type():

    assert (

        registry()

        .builder

        .__class__.__name__

        == "ExecutionBuilder"

    )


def test_repr():

    assert (

        "ExecutionRegistry"

        in repr(

            registry(),

        )

    )


def test_multiple_calls():

    r = registry()

    assert (

        r.get_builder()

        is

        r.get_builder()

    )


def test_registry_exists():

    assert registry() is not None


def test_builder_exists():

    assert registry().builder is not None