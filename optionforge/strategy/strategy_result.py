"""
============================================================
OptionForge
Strategy Result
============================================================

Author      : OptionForge
Module      : strategy_result.py

Purpose
-------
Immutable result produced by the StrategyEngine.

A StrategyResult groups the selected Strategy together
with its ExecutionPlan and provides a single object for
downstream Portfolio, Execution and Reporting engines.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, Mapping

from optionforge.strategy.execution_plan import (
    ExecutionPlan,
)
from optionforge.strategy.strategy import (
    Strategy,
)


@dataclass(
    frozen=True,
    slots=True,
)
class StrategyResult:
    """
    Final output of the Strategy Engine.
    """

    # -----------------------------------------------------
    # Core
    # -----------------------------------------------------

    strategy: Strategy

    execution_plan: ExecutionPlan

    # -----------------------------------------------------
    # Metadata
    # -----------------------------------------------------

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC),
        compare=False,
    )

    metadata: Mapping[str, Any] = field(
        default_factory=dict,
        compare=False,
    )

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def confidence(self) -> float:
        """
        Strategy confidence.
        """

        return self.strategy.confidence

    @property
    def strategy_type(self):
        """
        Strategy type.
        """

        return self.strategy.type

    @property
    def probability_of_profit(self) -> float:
        """
        Estimated probability of profit.
        """

        return self.strategy.probability_of_profit

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(self) -> dict[str, Any]:

        return {
            "strategy": self.strategy.to_dict(),
            "execution_plan": (self.execution_plan.to_dict()),
            "timestamp": (self.timestamp.isoformat()),
            "metadata": dict(self.metadata),
        }

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(self) -> str:

        return (
            f"StrategyResult("
            f"{self.strategy.title}, "
            f"{self.strategy.confidence:.1f}%)"
        )

    def __repr__(self) -> str:

        return f"StrategyResult(" f"strategy={self.strategy.type.name})"
