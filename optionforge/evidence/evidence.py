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
    Immutable institutional evidence.

    Evidence is the normalized output of an analytical
    engine. It contains both quantitative measurements
    and a human-readable explanation.
    """

    # Identity
    id: str
    name: str

    # Classification
    type: EvidenceType
    level: EvidenceLevel

    # Quantitative
    score: float
    confidence: float

    # Human explanation
    description: str

    # Source
    source: FeatureId

    # Optional metadata
    metadata: Mapping[str, Any] = field(default_factory=dict)

    # Timestamp
    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC),
        compare=False,
    )

    def __post_init__(self) -> None:

        if not (0.0 <= self.confidence <= 100.0):
            raise ValueError("Confidence must be between 0 and 100.")

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

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type.name,
            "level": self.level.name,
            "score": self.score,
            "confidence": self.confidence,
            "description": self.description,
            "source": self.source.name,
            "timestamp": self.timestamp.isoformat(),
            "metadata": dict(self.metadata),
        }
