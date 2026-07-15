"""
============================================================
OptionForge
Equity Curve
============================================================

Author      : OptionForge
Module      : equity_curve.py

Purpose
-------
Immutable institutional equity curve.

Represents the equity values generated during a
backtest.

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
class EquityCurve:
    """
    Immutable equity curve.
    """

    # =====================================================
    # Data
    # =====================================================

    values: tuple[float, ...]

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

        if len(self.values) == 0:

            raise ValueError("Equity curve cannot be empty.")

        if any(value < 0 for value in self.values):

            raise ValueError("Equity values cannot be negative.")

    # =====================================================
    # Convenience
    # =====================================================

    @property
    def length(self) -> int:

        return len(
            self.values,
        )

    @property
    def start_value(self) -> float:

        return self.values[0]

    @property
    def end_value(self) -> float:

        return self.values[-1]

    @property
    def highest_value(self) -> float:

        return max(
            self.values,
        )

    @property
    def lowest_value(self) -> float:

        return min(
            self.values,
        )

    @property
    def total_return(self) -> float:

        if self.start_value == 0:

            return 0.0

        return ((self.end_value - self.start_value) / self.start_value) * 100.0

    # =====================================================
    # Serialization
    # =====================================================

    def to_dict(self) -> dict[str, Any]:

        return {
            "values": list(
                self.values,
            ),
            "length": self.length,
            "start_value": self.start_value,
            "end_value": self.end_value,
            "highest_value": self.highest_value,
            "lowest_value": self.lowest_value,
            "total_return": self.total_return,
            "metadata": dict(
                self.metadata,
            ),
        }

    # =====================================================
    # Representation
    # =====================================================

    def __str__(self) -> str:

        return f"EquityCurve(" f"{self.length} points)"

    def __repr__(self) -> str:

        return (
            f"EquityCurve("
            f"points={self.length}, "
            f"return={self.total_return:.2f}%)"
        )
