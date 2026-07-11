"""
============================================================
OptionForge
Walk Forward Runner
============================================================

Author      : OptionForge
Module      : walk_forward_runner.py

Purpose
-------
Executes a simple walk-forward analysis and returns an
immutable WalkForwardAnalysis result.

============================================================
"""

from __future__ import annotations

from optionforge.research.walk_forward import (
    WalkForwardAnalysis,
)


class WalkForwardRunner:
    """
    Executes a simple walk-forward evaluation.
    """

    PASS_THRESHOLD = 70.0

    def run(
        self,
        windows: list[bool],
    ) -> WalkForwardAnalysis:
        """
        Execute walk-forward analysis.

        Parameters
        ----------
        windows
            List of pass/fail window results.

        Returns
        -------
        WalkForwardAnalysis
        """

        if not windows:
            raise ValueError(
                "windows cannot be empty."
            )

        successful = sum(windows)

        failed = len(windows) - successful

        success_rate = (
            successful / len(windows)
        ) * 100.0

        stability_score = round(
            success_rate,
            10,
        )

        passed = (
            success_rate
            >= self.PASS_THRESHOLD
        )

        return WalkForwardAnalysis(

            windows=len(windows),

            successful_windows=successful,

            failed_windows=failed,

            stability_score=stability_score,

            passed=passed,

        )

    def __repr__(self) -> str:

        return (

            "WalkForwardRunner("

            f"pass_threshold={self.PASS_THRESHOLD})"

        )

    __str__ = __repr__