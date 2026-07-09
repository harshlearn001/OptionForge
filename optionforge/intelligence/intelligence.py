"""
============================================================
OptionForge
Institutional Intelligence Model
============================================================

Author      : OptionForge
Module      : intelligence.py

Purpose
-------
Immutable Intelligence object representing the
highest-level institutional reasoning derived from
one or more Knowledge objects.

Intelligence is the bridge between Knowledge and
Decision.

This object is immutable and thread-safe.
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any
from typing import Mapping

from optionforge.intelligence.intelligence_level import (
    IntelligenceLevel,
)
from optionforge.intelligence.intelligence_type import (
    IntelligenceType,
)


@dataclass(
    frozen=True,
    slots=True,
)
class Intelligence:
    """
    Represents one piece of institutional intelligence.
    """

    # -----------------------------------------------------
    # Identity
    # -----------------------------------------------------

    id: str

    name: str

    # -----------------------------------------------------
    # Classification
    # -----------------------------------------------------

    type: IntelligenceType

    level: IntelligenceLevel

    # -----------------------------------------------------
    # Numerical
    # -----------------------------------------------------

    score: float

    confidence: float

    # -----------------------------------------------------
    # Interpretation
    # -----------------------------------------------------

    description: str

    # -----------------------------------------------------
    # Knowledge Sources
    # -----------------------------------------------------

    knowledge_ids: tuple[str, ...]

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
    # Validation
    # -----------------------------------------------------

    def __post_init__(self) -> None:

        if not (0.0 <= self.confidence <= 100.0):

            raise ValueError(

                "Confidence must be between 0 and 100."

            )

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def confidence_ratio(
        self,
    ) -> float:

        return self.confidence / 100.0

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(
        self,
    ) -> dict[str, Any]:

        return {

            "id": self.id,

            "name": self.name,

            "type": self.type.name,

            "level": self.level.name,

            "score": self.score,

            "confidence": self.confidence,

            "description": self.description,

            "knowledge_ids": self.knowledge_ids,

            "timestamp": self.timestamp.isoformat(),

            "metadata": dict(self.metadata),

        }

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(
        self,
    ) -> str:

        return (

            f"{self.name}("

            f"score={self.score:.2f}, "

            f"confidence={self.confidence:.1f}%)"

        )

    def __repr__(
        self,
    ) -> str:

        return (

            f"Intelligence("

            f"id={self.id}, "

            f"type={self.type.name}, "

            f"score={self.score}, "

            f"confidence={self.confidence})"

        )