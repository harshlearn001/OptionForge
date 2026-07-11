"""
============================================================
OptionForge
ResearchPipeline Tests
============================================================
"""

from optionforge.research.research_pipeline import (
    ResearchPipeline,
)

from optionforge.research.walk_forward_runner import (
    WalkForwardRunner,
)

from optionforge.research.monte_carlo_engine import (
    MonteCarloEngine,
)

from optionforge.research.benchmark_engine import (
    BenchmarkEngine,
)

from optionforge.research.scenario_engine import (
    ScenarioEngine,
)

from optionforge.research.parameter_sweep_engine import (
    ParameterSweepEngine,
)


def pipeline():

    return ResearchPipeline()


# ==========================================================
# Construction
# ==========================================================

def test_create():

    assert isinstance(

        pipeline(),

        ResearchPipeline,

    )


# ==========================================================
# Components
# ==========================================================

def test_walk_forward():

    assert isinstance(

        pipeline().walk_forward,

        WalkForwardRunner,

    )


def test_monte_carlo():

    assert isinstance(

        pipeline().monte_carlo,

        MonteCarloEngine,

    )


def test_benchmark():

    assert isinstance(

        pipeline().benchmark,

        BenchmarkEngine,

    )


def test_scenario():

    assert isinstance(

        pipeline().scenario,

        ScenarioEngine,

    )


def test_parameter_sweep():

    assert isinstance(

        pipeline().parameter_sweep,

        ParameterSweepEngine,

    )


# ==========================================================
# Representation
# ==========================================================

def test_repr():

    assert (

        "ResearchPipeline"

        in

        repr(

            pipeline(),

        )

    )


def test_str():

    assert (

        "ResearchPipeline"

        in

        str(

            pipeline(),

        )

    )