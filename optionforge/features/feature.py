"""
============================================================
OptionForge
Feature Model
============================================================

Author      : OptionForge
Module      : feature.py
Purpose     : Immutable Feature object used throughout
              OptionForge Feature Registry.

Every calculated quantitative metric is represented as
a Feature.

Examples
--------
Gamma Exposure
Delta Exposure
IV Rank
PCR
Expected Move
Max Pain
Dealer Position

This object is immutable and thread-safe.
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, Mapping

from optionforge.features.feature_group import FeatureGroup
from optionforge.features.feature_id import FeatureId


@dataclass(frozen=True, slots=True)
class Feature:
    """
    Represents a single quantitative feature.
    """

    id: FeatureId

    group: FeatureGroup

    value: float

    confidence: float = 100.0

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC),
        compare=False,
    )

    metadata: Mapping[str, Any] = field(
        default_factory=dict,
        compare=False,
    )

    def __post_init__(self) -> None:
        """
        Validate Feature.
        """

        if not (0.0 <= self.confidence <= 100.0):
            raise ValueError("Confidence must be between 0 and 100.")

    @property
    def name(self) -> str:
        """
        Human-readable feature name.
        """
        return self.id.name.replace("_", " ").title()

    @property
    def confidence_ratio(self) -> float:
        """
        Confidence expressed between 0 and 1.
        """
        return self.confidence / 100.0

    def is_high_confidence(
        self,
        threshold: float = 80.0,
    ) -> bool:
        """
        Returns True if confidence exceeds threshold.
        """
        return self.confidence >= threshold

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize Feature.
        """

        return {
            "id": self.id.name,
            "group": self.group.name,
            "name": self.name,
            "value": self.value,
            "confidence": self.confidence,
            "timestamp": self.timestamp.isoformat(),
            "metadata": dict(self.metadata),
        }

    def __str__(self) -> str:
        return (
            f"{self.name}("
            f"value={self.value:.4f}, "
            f"confidence={self.confidence:.1f}%)"
        )

    def __repr__(self) -> str:
        return (
            f"Feature("
            f"id={self.id.name}, "
            f"value={self.value}, "
            f"confidence={self.confidence})"
        )
