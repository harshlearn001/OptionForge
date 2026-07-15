"""
============================================================
OptionForge
Scenario Engine
============================================================

Author      : OptionForge
Module      : scenario_engine.py

Purpose
-------
Executes scenario analysis and returns an immutable
ScenarioAnalysis.

============================================================
"""

from __future__ import annotations

from optionforge.research.scenario_analysis import (
    ScenarioAnalysis,
)


class ScenarioEngine:
    """
    Executes scenario analysis.
    """

    def run(
        self,
        scenario_name: str,
        strategy_return: float,
        benchmark_return: float,
        win_rate: float,
        max_drawdown: float,
        sharpe_ratio: float,
    ) -> ScenarioAnalysis:
        """
        Execute scenario analysis.
        """

        excess_return = round(
            strategy_return - benchmark_return,
            10,
        )

        passed = excess_return >= 0.0 and win_rate >= 50.0

        return ScenarioAnalysis(
            scenario_name=scenario_name,
            strategy_return=strategy_return,
            benchmark_return=benchmark_return,
            win_rate=win_rate,
            max_drawdown=max_drawdown,
            sharpe_ratio=sharpe_ratio,
            passed=passed,
        )

    def __repr__(self) -> str:

        return "ScenarioEngine()"

    __str__ = __repr__
