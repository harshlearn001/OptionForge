"""
============================================================
OptionForge
Evidence Registry
============================================================

Author      : OptionForge
Module      : evidence_registry.py

Purpose
-------
Central immutable registry for all market evidence.

The EvidenceRegistry stores FeatureEvidence objects generated
from quantitative features and provides aggregation methods
used by:

    - MarketDNA
    - Decision Engine
    - Dashboard
    - Reports
    - Research
    - Backtesting

============================================================
"""

from __future__ import annotations

from typing import Dict, Iterable

from optionforge.evidence.feature_evidence import (
    EvidenceDirection,
    FeatureEvidence,
)
from optionforge.features.feature_id import FeatureId


class EvidenceRegistry:
    """
    Registry containing all market evidence.

    Each FeatureId may contribute only one FeatureEvidence.
    """

    def __init__(self) -> None:

        self._evidence: Dict[FeatureId, FeatureEvidence] = {}

    # ---------------------------------------------------------
    # Add
    # ---------------------------------------------------------

    def add(self, evidence: FeatureEvidence) -> None:
        """
        Register evidence.

        Raises
        ------
        ValueError
            If evidence already exists.
        """

        if evidence.feature_id in self._evidence:
            raise ValueError(
                f"Evidence already registered: " f"{evidence.feature_id.name}"
            )

        self._evidence[evidence.feature_id] = evidence

    # ---------------------------------------------------------
    # Replace
    # ---------------------------------------------------------

    def replace(self, evidence: FeatureEvidence) -> None:
        """
        Replace existing evidence.
        """

        self._evidence[evidence.feature_id] = evidence

    # ---------------------------------------------------------
    # Get
    # ---------------------------------------------------------

    def get(
        self,
        feature_id: FeatureId,
    ) -> FeatureEvidence:

        return self._evidence[feature_id]

    # ---------------------------------------------------------
    # Exists
    # ---------------------------------------------------------

    def has(
        self,
        feature_id: FeatureId,
    ) -> bool:

        return feature_id in self._evidence

    # ---------------------------------------------------------
    # Remove
    # ---------------------------------------------------------

    def remove(
        self,
        feature_id: FeatureId,
    ) -> None:

        self._evidence.pop(feature_id, None)

    # ---------------------------------------------------------
    # Collections
    # ---------------------------------------------------------

    def values(self) -> Iterable[FeatureEvidence]:

        return self._evidence.values()

    def items(self):

        return self._evidence.items()

    # ---------------------------------------------------------
    # Aggregations
    # ---------------------------------------------------------

    def bullish(self) -> list[FeatureEvidence]:

        return [
            e
            for e in self._evidence.values()
            if e.direction == EvidenceDirection.BULLISH
        ]

    def bearish(self) -> list[FeatureEvidence]:

        return [
            e
            for e in self._evidence.values()
            if e.direction == EvidenceDirection.BEARISH
        ]

    def neutral(self) -> list[FeatureEvidence]:

        return [
            e
            for e in self._evidence.values()
            if e.direction == EvidenceDirection.NEUTRAL
        ]

    def bullish_strength(self) -> float:

        return sum(e.strength for e in self.bullish())

    def bearish_strength(self) -> float:

        return sum(e.strength for e in self.bearish())

    def net_strength(self) -> float:

        return self.bullish_strength() - self.bearish_strength()

    def average_confidence(self) -> float:

        if not self._evidence:
            return 0.0

        return sum(e.confidence for e in self._evidence.values()) / len(self._evidence)

    # ---------------------------------------------------------
    # Export
    # ---------------------------------------------------------

    def to_dict(self) -> dict:

        return {
            evidence.feature_id.name: evidence.to_dict()
            for evidence in self._evidence.values()
        }

    # ---------------------------------------------------------
    # Summary
    # ---------------------------------------------------------

    def summary(self) -> dict:

        return {
            "total": len(self._evidence),
            "bullish": len(self.bullish()),
            "bearish": len(self.bearish()),
            "neutral": len(self.neutral()),
            "bullish_strength": self.bullish_strength(),
            "bearish_strength": self.bearish_strength(),
            "net_strength": self.net_strength(),
            "average_confidence": self.average_confidence(),
        }

    # ---------------------------------------------------------
    # Magic Methods
    # ---------------------------------------------------------

    def __contains__(self, feature_id: FeatureId) -> bool:

        return feature_id in self._evidence

    def __len__(self) -> int:

        return len(self._evidence)

    def __iter__(self):

        return iter(self._evidence.values())

    def __repr__(self) -> str:

        return f"EvidenceRegistry(" f"{len(self._evidence)} evidence)"
