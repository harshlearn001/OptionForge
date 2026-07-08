"""
============================================================
OptionForge
Execution Plan
============================================================

Author      : OptionForge
Module      : execution_plan.py
Purpose     : Immutable execution plan for an options
              strategy.

ExecutionPlan contains the practical instructions
required to execute a selected strategy.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, Mapping

from optionforge.strategy.strategy import Strategy


@dataclass(
    frozen=True,
    slots=True,
)
class ExecutionPlan:
    """
    Immutable execution plan.
    """

    # -----------------------------------------------------
    # Strategy
    # -----------------------------------------------------

    strategy: Strategy

    # -----------------------------------------------------
    # Entry
    # -----------------------------------------------------

    entry_rule: str

    entry_price: str

    # -----------------------------------------------------
    # Exit
    # -----------------------------------------------------

    target_rule: str

    stop_loss_rule: str

    # -----------------------------------------------------
    # Position
    # -----------------------------------------------------

    position_size: str

    max_capital: str

    # -----------------------------------------------------
    # Risk
    # -----------------------------------------------------

    max_risk: str

    expected_reward: str

    # -----------------------------------------------------
    # Notes
    # -----------------------------------------------------

    notes: tuple[str, ...] = ()

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
    # Serialization
    # -----------------------------------------------------

    def to_dict(self) -> dict[str, Any]:

        return {

            "strategy": self.strategy.to_dict(),

            "entry_rule": self.entry_rule,

            "entry_price": self.entry_price,

            "target_rule": self.target_rule,

            "stop_loss_rule": self.stop_loss_rule,

            "position_size": self.position_size,

            "max_capital": self.max_capital,

            "max_risk": self.max_risk,

            "expected_reward": self.expected_reward,

            "notes": list(self.notes),

            "timestamp": self.timestamp.isoformat(),

            "metadata": dict(self.metadata),

        }

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(self) -> str:

        return (

            f"ExecutionPlan("

            f"{self.strategy.title})"

        )

    def __repr__(self) -> str:

        return (

            f"ExecutionPlan("

            f"strategy={self.strategy.type.name})"

        )