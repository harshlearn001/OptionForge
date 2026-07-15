"""
============================================================
OptionForge
Parameter Sweep Engine
============================================================

Author      : OptionForge
Module      : parameter_sweep_engine.py

Purpose
-------
Executes parameter sweep analysis and returns an immutable
ParameterSweep.

============================================================
"""

from __future__ import annotations

from optionforge.research.parameter_sweep import (
    ParameterSweep,
)


class ParameterSweepEngine:
    """
    Executes parameter sweep analysis.
    """

    PASS_THRESHOLD = 70.0

    def run(
        self,
        parameter_name: str,
        scores: list[float],
    ) -> ParameterSweep:
        """
        Execute parameter sweep.
        """

        if not scores:
            raise ValueError("scores cannot be empty.")

        tested_values = len(scores)

        best_score = max(scores)

        average_score = round(
            sum(scores) / tested_values,
            10,
        )

        best_value = scores.index(best_score) + 1

        stability_score = average_score

        passed = stability_score >= self.PASS_THRESHOLD

        return ParameterSweep(
            parameter_name=parameter_name,
            tested_values=tested_values,
            best_value=best_value,
            best_score=best_score,
            average_score=average_score,
            stability_score=stability_score,
            passed=passed,
        )

    def __repr__(self) -> str:

        return "ParameterSweepEngine(" f"pass_threshold={self.PASS_THRESHOLD})"

    __str__ = __repr__
