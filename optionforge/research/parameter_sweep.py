"""
============================================================
OptionForge
Parameter Sweep
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class ParameterSweep:
    """
    Immutable parameter sweep summary.
    """

    parameter_name: str

    tested_values: int

    best_value: float

    best_score: float

    average_score: float

    stability_score: float

    passed: bool

    def __post_init__(self) -> None:

        if not self.parameter_name.strip():

            raise ValueError("parameter_name cannot be empty.")

        if self.tested_values <= 0:

            raise ValueError("tested_values must be positive.")

        if not (0.0 <= self.stability_score <= 100.0):

            raise ValueError("stability_score must be between 0 and 100.")

    @property
    def score_difference(self) -> float:

        return round(
            self.best_score - self.average_score,
            10,
        )

    def to_dict(self) -> dict:

        return {
            "parameter_name": self.parameter_name,
            "tested_values": self.tested_values,
            "best_value": self.best_value,
            "best_score": self.best_score,
            "average_score": self.average_score,
            "score_difference": self.score_difference,
            "stability_score": self.stability_score,
            "passed": self.passed,
        }

    def __str__(self):

        return f"ParameterSweep(" f"{self.parameter_name})"

    def __repr__(self):

        return f"ParameterSweep(" f"parameter='{self.parameter_name}')"
