"""
============================================================
OptionForge
Recommendation
============================================================

Author      : OptionForge
Module      : recommendation.py
Purpose     : Immutable trading recommendation.

Recommendation provides execution guidance after a
Decision has been made.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, Mapping

from optionforge.decision.strategy_type import StrategyType


@dataclass(
    frozen=True,
    slots=True,
)
class Recommendation:
    """
    Immutable trading recommendation.
    """

    # -----------------------------------------------------
    # Strategy
    # -----------------------------------------------------

    strategy: StrategyType

    title: str

    summary: str

    # -----------------------------------------------------
    # Execution
    # -----------------------------------------------------

    entry: str

    exit: str

    stop_loss: str

    position_size: str

    # -----------------------------------------------------
    # Risk
    # -----------------------------------------------------

    risk_reward: str

    risk_notes: tuple[str, ...] = ()

    # -----------------------------------------------------
    # Explanation
    # -----------------------------------------------------

    rationale: tuple[str, ...] = ()

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
            "strategy": self.strategy.name,
            "title": self.title,
            "summary": self.summary,
            "entry": self.entry,
            "exit": self.exit,
            "stop_loss": self.stop_loss,
            "position_size": self.position_size,
            "risk_reward": self.risk_reward,
            "risk_notes": list(self.risk_notes),
            "rationale": list(self.rationale),
            "timestamp": self.timestamp.isoformat(),
            "metadata": dict(self.metadata),
        }

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(self) -> str:

        return f"Recommendation(" f"{self.strategy.name}: " f"{self.title})"

    def __repr__(self) -> str:

        return (
            f"Recommendation("
            f"strategy={self.strategy.name}, "
            f"title={self.title!r})"
        )
