"""
============================================================
OptionForge
Research
============================================================

Author      : OptionForge
Module      : research.py

Purpose
-------
Immutable institutional research configuration.

Represents a completed research study or experiment.

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(
    frozen=True,
    slots=True,
)
class Research:
    """
    Immutable research configuration.
    """

    # =====================================================
    # Identity
    # =====================================================

    name: str

    strategy_name: str

    description: str = ""

    # =====================================================
    # Study
    # =====================================================

    start_date: str = ""

    end_date: str = ""

    symbol: str = ""

    timeframe: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    metadata: Mapping[str, Any] = field(
        default_factory=dict,
        compare=False,
    )

    # =====================================================
    # Validation
    # =====================================================

    def __post_init__(self) -> None:

        if not self.name.strip():

            raise ValueError("name cannot be empty.")

        if not self.strategy_name.strip():

            raise ValueError("strategy_name cannot be empty.")

    # =====================================================
    # Serialization
    # =====================================================

    def to_dict(self) -> dict[str, Any]:

        return {
            "name": self.name,
            "strategy_name": self.strategy_name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "symbol": self.symbol,
            "timeframe": self.timeframe,
            "metadata": dict(self.metadata),
        }

    # =====================================================
    # Representation
    # =====================================================

    def __str__(self) -> str:

        return f"Research(" f"{self.name})"

    def __repr__(self) -> str:

        return f"Research(" f"name={self.name!r}, " f"strategy={self.strategy_name!r})"
