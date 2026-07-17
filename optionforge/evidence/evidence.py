"""
============================================================
OptionForge
Evidence
============================================================

Author      : OptionForge
Module      : evidence.py
Purpose     : Immutable institutional evidence.

Evidence is the normalized output of an analytical
engine. It represents one observable market fact.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime
from typing import Any
from typing import Mapping

from optionforge.evidence.evidence_direction import (
    EvidenceDirection,
)

from optionforge.evidence.evidence_level import (
    EvidenceLevel,
)

from optionforge.evidence.evidence_source import (
    EvidenceSource,
)


@dataclass(
    frozen=True,
    slots=True,
)
class Evidence:
    """
    Immutable institutional evidence.
    """

    # -----------------------------------------------------
    # Identity
    # -----------------------------------------------------

    id: str

    title: str

    # -----------------------------------------------------
    # Classification
    # -----------------------------------------------------

    source: EvidenceSource

    direction: EvidenceDirection

    level: EvidenceLevel

    # -----------------------------------------------------
    # Quantitative
    # -----------------------------------------------------

    score: float

    confidence: float

    # -----------------------------------------------------
    # Human Explanation
    # -----------------------------------------------------

    description: str

    # -----------------------------------------------------
    # Optional Metadata
    # -----------------------------------------------------

    metadata: Mapping[str, Any] = field(
        default_factory=dict,
    )

    # -----------------------------------------------------
    # Timestamp
    # -----------------------------------------------------

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC),
        compare=False,
    )

    # -----------------------------------------------------

    def __post_init__(self) -> None:

        if not self.id.strip():

            raise ValueError("Evidence id cannot be empty.")

        if not self.title.strip():

            raise ValueError("Evidence title cannot be empty.")

        if not (0.0 <= self.confidence <= 1.0):

            raise ValueError(
                "Confidence must be between 0 and 1."
            )

    # -----------------------------------------------------

    @property
    def confidence_percent(self) -> float:
        """
        Confidence expressed as percentage.
        """

        return self.confidence * 100.0

    # -----------------------------------------------------

    @property
    def is_bullish(self) -> bool:

        return self.direction.is_bullish

    # -----------------------------------------------------

    @property
    def is_bearish(self) -> bool:

        return self.direction.is_bearish

    # -----------------------------------------------------

    @property
    def is_neutral(self) -> bool:

        return self.direction.is_neutral

    # -----------------------------------------------------

    def to_dict(self) -> dict[str, Any]:
        """
        Convert to serializable dictionary.
        """

        return {

            "id": self.id,

            "title": self.title,

            "source": self.source.value,

            "direction": self.direction.name,

            "level": self.level.name,

            "score": self.score,

            "confidence": self.confidence,

            "confidence_percent": self.confidence_percent,

            "description": self.description,

            "timestamp": self.timestamp.isoformat(),

            "metadata": dict(self.metadata),
        }

    # -----------------------------------------------------

    def __repr__(self):

        return (

            f"Evidence("

            f"title='{self.title}', "

            f"source={self.source.name}, "

            f"direction={self.direction.name}, "

            f"level={self.level.name}, "

            f"confidence={self.confidence:.2f}"

            f")"

        )

    __str__ = __repr__