"""
============================================================
OptionForge
Research Pipeline
============================================================

Author      : OptionForge
Module      : research_pipeline.py

Purpose
-------
Coordinates all research execution engines.

============================================================
"""

from __future__ import annotations

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


class ResearchPipeline:
    """
    Coordinates research execution engines.
    """

    def __init__(self) -> None:

        self.walk_forward = WalkForwardRunner()

        self.monte_carlo = MonteCarloEngine()

        self.benchmark = BenchmarkEngine()

        self.scenario = ScenarioEngine()

        self.parameter_sweep = ParameterSweepEngine()

    def __repr__(self) -> str:

        return "ResearchPipeline()"

    __str__ = __repr__
