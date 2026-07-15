"""
============================================================
OptionForge
Scenario Analysis
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class ScenarioAnalysis:
    """
    Immutable scenario analysis summary.
    """

    scenario_name: str

    strategy_return: float

    benchmark_return: float

    win_rate: float

    max_drawdown: float

    sharpe_ratio: float

    passed: bool

    def __post_init__(self) -> None:

        if not self.scenario_name.strip():

            raise ValueError("scenario_name cannot be empty.")

        if not (0.0 <= self.win_rate <= 100.0):

            raise ValueError("win_rate must be between 0 and 100.")

        if self.max_drawdown < 0:

            raise ValueError("max_drawdown cannot be negative.")

    @property
    def excess_return(self) -> float:

        return round(
            self.strategy_return - self.benchmark_return,
            10,
        )

    def to_dict(self) -> dict:

        return {
            "scenario_name": self.scenario_name,
            "strategy_return": self.strategy_return,
            "benchmark_return": self.benchmark_return,
            "excess_return": self.excess_return,
            "win_rate": self.win_rate,
            "max_drawdown": self.max_drawdown,
            "sharpe_ratio": self.sharpe_ratio,
            "passed": self.passed,
        }

    def __str__(self):

        return f"ScenarioAnalysis(" f"{self.scenario_name})"

    def __repr__(self):

        return f"ScenarioAnalysis(" f"scenario='{self.scenario_name}')"
