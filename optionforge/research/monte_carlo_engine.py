"""
============================================================
OptionForge
Monte Carlo Engine
============================================================

Author      : OptionForge
Module      : monte_carlo_engine.py

Purpose
-------
Executes a simple deterministic Monte Carlo analysis
and returns an immutable MonteCarloSimulation.

============================================================
"""

from __future__ import annotations

from optionforge.research.monte_carlo import (
    MonteCarloSimulation,
)


class MonteCarloEngine:
    """
    Executes a deterministic Monte Carlo analysis.
    """

    PASS_THRESHOLD = 50.0

    def run(
        self,
        trades: list[float],
    ) -> MonteCarloSimulation:
        """
        Execute Monte Carlo analysis.

        Parameters
        ----------
        trades
            List of trade returns.

        Returns
        -------
        MonteCarloSimulation
        """

        if not trades:
            raise ValueError(
                "trades cannot be empty."
            )

        simulations = len(trades)

        average_return = round(
            sum(trades) / simulations,
            10,
        )

        best_return = max(trades)

        worst_return = min(trades)

        profitable = sum(
            trade > 0
            for trade in trades
        )

        losing = sum(
            trade < 0
            for trade in trades
        )

        probability_of_profit = round(
            (profitable / simulations) * 100.0,
            10,
        )

        probability_of_loss = round(
            (losing / simulations) * 100.0,
            10,
        )

        # Version 1 placeholders
        probability_of_ruin = 0.0

        max_drawdown = 0.0

        passed = (
            probability_of_profit
            >= self.PASS_THRESHOLD
        )

        return MonteCarloSimulation(

            simulations=simulations,

            average_return=average_return,

            best_return=best_return,

            worst_return=worst_return,

            probability_of_profit=probability_of_profit,

            probability_of_loss=probability_of_loss,

            probability_of_ruin=probability_of_ruin,

            max_drawdown=max_drawdown,

            passed=passed,

        )

    def __repr__(self) -> str:

        return (

            "MonteCarloEngine("

            f"pass_threshold={self.PASS_THRESHOLD})"

        )

    __str__ = __repr__