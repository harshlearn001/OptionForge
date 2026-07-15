"""
============================================================
OptionForge
Monte Carlo Simulation
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class MonteCarloSimulation:
    """
    Immutable Monte Carlo simulation summary.
    """

    simulations: int

    average_return: float

    best_return: float

    worst_return: float

    probability_of_profit: float

    probability_of_loss: float

    probability_of_ruin: float

    max_drawdown: float

    passed: bool

    def __post_init__(self) -> None:

        if self.simulations <= 0:
            raise ValueError("simulations must be positive.")

        for name in (
            "probability_of_profit",
            "probability_of_loss",
            "probability_of_ruin",
            "max_drawdown",
        ):

            value = getattr(self, name)

            if not (0.0 <= value <= 100.0):

                raise ValueError(f"{name} must be between 0 and 100.")

    @property
    def expected_survival_rate(self) -> float:

        return 100.0 - self.probability_of_ruin

    def to_dict(self) -> dict:

        return {
            "simulations": self.simulations,
            "average_return": self.average_return,
            "best_return": self.best_return,
            "worst_return": self.worst_return,
            "probability_of_profit": self.probability_of_profit,
            "probability_of_loss": self.probability_of_loss,
            "probability_of_ruin": self.probability_of_ruin,
            "expected_survival_rate": self.expected_survival_rate,
            "max_drawdown": self.max_drawdown,
            "passed": self.passed,
        }

    def __str__(self):

        return f"MonteCarloSimulation(" f"survival={self.expected_survival_rate:.1f}%)"

    def __repr__(self):

        return f"MonteCarloSimulation(" f"simulations={self.simulations})"
