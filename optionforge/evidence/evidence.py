"""
============================================================
OptionForge
Evidence Model
============================================================

Author      : OptionForge
Module      : evidence.py
Purpose     : Immutable Evidence object representing
              institutional reasoning derived from one
              or more Features.

Evidence is the bridge between quantitative Features
and higher-level MarketDNA / DecisionEngine.

Examples
--------
Bullish Evidence
Bearish Evidence
Dealer Evidence
Volatility Evidence
Liquidity Evidence
Trend Evidence

This object is immutable and thread-safe.
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, Mapping

from optionforge.evidence.evidence_level import EvidenceLevel
from optionforge.evidence.evidence_type import EvidenceType
from optionforge.features.feature_id import FeatureId


@dataclass(
    frozen=True,
    slots=True,
)
class Evidence:
    """
    Represents one piece of institutional evidence.
    """

    # -----------------------------------------------------
    # Identity
    # -----------------------------------------------------

    id: str

    name: str

    # -----------------------------------------------------
    # Classification
    # -----------------------------------------------------

    type: EvidenceType

    level: EvidenceLevel

    # -----------------------------------------------------
    # Numerical
    # -----------------------------------------------------

    score: float

    confidence: float

    # -----------------------------------------------------
    # Source
    # -----------------------------------------------------

    source: FeatureId

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
    def confidence_ratio(self) -> float:

        return self.confidence / 100.0

    @property
    def is_bullish(self) -> bool:

        return self.type == EvidenceType.BULLISH

    @property
    def is_bearish(self) -> bool:

        return self.type == EvidenceType.BEARISH

    @property
    def is_neutral(self) -> bool:

        return self.type == EvidenceType.NEUTRAL

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(self) -> dict[str, Any]:

        return {

            "id": self.id,

            "name": self.name,

            "type": self.type.name,

            "level": self.level.name,

            "score": self.score,

            "confidence": self.confidence,

            "source": self.source.name,

            "timestamp": self.timestamp.isoformat(),

            "metadata": dict(self.metadata),

        }

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(self) -> str:

        return (

            f"{self.name}("

            f"score={self.score:.2f}, "

            f"confidence={self.confidence:.1f}%)"

        )

    def __repr__(self) -> str:

        return (

            f"Evidence("

            f"id={self.id}, "

            f"type={self.type.name}, "

            f"score={self.score}, "

            f"confidence={self.confidence})"

        )