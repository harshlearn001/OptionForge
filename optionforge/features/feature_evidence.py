"""
============================================================
OptionForge
Feature Evidence Model
============================================================

Author      : OptionForge
Module      : feature_evidence.py

Purpose
-------
Represents a single piece of market evidence generated
from one quantitative feature.

Examples
--------
Gamma Exposure
    -> Bullish
    -> Strength 18
    -> Confidence 92%

PCR
    -> Bearish
    -> Strength -12
    -> Confidence 81%

Every analytics engine converts raw Features into
FeatureEvidence objects.

These objects are consumed by:

    Evidence Engine
    MarketDNA
    Decision Engine
    Dashboard
    Research
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Mapping

from optionforge.features.feature_id import FeatureId


class EvidenceDirection(str, Enum):
    """Market direction implied by a feature."""

    BULLISH = "Bullish"
    BEARISH = "Bearish"
    NEUTRAL = "Neutral"


@dataclass(frozen=True, slots=True)
class FeatureEvidence:
    """
    Immutable evidence generated from a single feature.
    """

    feature_id: FeatureId

    direction: EvidenceDirection

    strength: float

    confidence: float

    reason: str

    timestamp: datetime = field(default_factory=datetime.utcnow)

    metadata: Mapping[str, Any] = field(default_factory=dict)

    @property
    def signed_strength(self) -> float:
        """
        Positive for bullish,
        negative for bearish,
        zero for neutral.
        """

        if self.direction == EvidenceDirection.BULLISH:
            return self.strength

        if self.direction == EvidenceDirection.BEARISH:
            return -self.strength

        return 0.0

    @property
    def confidence_ratio(self) -> float:
        """
        Returns confidence between 0 and 1.
        """

        return self.confidence / 100.0

    def is_high_confidence(self, threshold: float = 80.0) -> bool:
        return self.confidence >= threshold

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize evidence.
        """

        return {
            "feature_id": self.feature_id.name,
            "direction": self.direction.value,
            "strength": self.strength,
            "signed_strength": self.signed_strength,
            "confidence": self.confidence,
            "timestamp": self.timestamp.isoformat(),
            "reason": self.reason,
            "metadata": dict(self.metadata),
        }

    def __repr__(self) -> str:
        return (
            "FeatureEvidence("
            f"{self.feature_id.name}, "
            f"{self.direction.value}, "
            f"strength={self.strength:.2f}, "
            f"confidence={self.confidence:.1f})"
        )