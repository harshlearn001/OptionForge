"""
============================================================
OptionForge
ResearchRegistry Tests
============================================================
"""

from optionforge.research.research_builder import (
    ResearchBuilder,
)
from optionforge.research.research_registry import (
    ResearchRegistry,
)


def registry():

    return ResearchRegistry()


def test_returns_builder():

    assert isinstance(

        registry().builder,

        ResearchBuilder,

    )


def test_get_builder():

    assert isinstance(

        registry().get_builder(),

        ResearchBuilder,

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

        == "ResearchBuilder"

    )


def test_repr():

    assert (

        "ResearchRegistry"

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