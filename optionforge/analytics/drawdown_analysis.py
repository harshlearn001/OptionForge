"""
============================================================
OptionForge
Drawdown Analysis
============================================================

Author      : OptionForge
Module      : drawdown_analysis.py

Purpose
-------
Immutable institutional drawdown analysis.

Contains drawdown statistics derived from an EquityCurve.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from optionforge.analytics.equity_curve import (
    EquityCurve,
)


@dataclass(
    frozen=True,
    slots=True,
)
class DrawdownAnalysis:
    """
    Immutable drawdown analysis.
    """

    equity_curve: EquityCurve

    max_drawdown: float

    current_drawdown: float

    peak_equity: float

    lowest_equity: float

    recovered: bool

    metadata: Mapping[str, Any] = field(
        default_factory=dict,
        compare=False,
    )

    def __post_init__(self) -> None:

        if not (0.0 <= self.max_drawdown <= 100.0):

            raise ValueError(
                "max_drawdown must be between 0 and 100."
            )

        if not (0.0 <= self.current_drawdown <= 100.0):

            raise ValueError(
                "current_drawdown must be between 0 and 100."
            )

        if self.peak_equity < 0:

            raise ValueError(
                "peak_equity cannot be negative."
            )

        if self.lowest_equity < 0:

            raise ValueError(
                "lowest_equity cannot be negative."
            )

    @property
    def has_drawdown(self) -> bool:

        return self.max_drawdown > 0

    @property
    def is_recovered(self) -> bool:

        return self.recovered

    def to_dict(self) -> dict[str, Any]:

        return {

            "max_drawdown": self.max_drawdown,

            "current_drawdown": self.current_drawdown,

            "peak_equity": self.peak_equity,

            "lowest_equity": self.lowest_equity,

            "recovered": self.recovered,

            "equity_curve": self.equity_curve.to_dict(),

            "metadata": dict(self.metadata),

        }

    def __str__(self) -> str:

        return (

            f"DrawdownAnalysis("

            f"max={self.max_drawdown:.2f}%)"

        )

    def __repr__(self) -> str:

        return (

            f"DrawdownAnalysis("

            f"max_drawdown={self.max_drawdown:.2f}, "

            f"recovered={self.recovered})"

        )