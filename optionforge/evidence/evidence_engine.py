"""
============================================================
OptionForge
Evidence Engine
============================================================

Author      : OptionForge
Module      : evidence_engine.py
Purpose     : Converts quantitative Features into
              institutional Evidence.

This engine is the bridge between FeatureRegistry
and MarketDNA.
============================================================
"""

from __future__ import annotations

from optionforge.evidence.evidence import Evidence
from optionforge.evidence.evidence_level import EvidenceLevel
from optionforge.evidence.evidence_registry import EvidenceRegistry
from optionforge.evidence.evidence_type import EvidenceType

from optionforge.features.feature_group import FeatureGroup
from optionforge.features.feature_id import FeatureId
from optionforge.features.registry import FeatureRegistry


class EvidenceEngine:
    """
    Builds institutional evidence from Features.
    """

    def build(
        self,
        registry: FeatureRegistry,
    ) -> EvidenceRegistry:

        evidence = EvidenceRegistry()

        for feature in registry:

            generated = self._build_feature_evidence(feature)

            if generated is not None:

                evidence.add(generated)

        return evidence

    # -----------------------------------------------------
    # Feature Routing
    # -----------------------------------------------------

    def _build_feature_evidence(
        self,
        feature,
    ) -> Evidence | None:

        if feature.id == FeatureId.DEALER_POSITION:

            return self._dealer_evidence(feature)

        if feature.group == FeatureGroup.VOLATILITY:

            return self._volatility_evidence(feature)

        return None

    # -----------------------------------------------------
    # Dealer Evidence
    # -----------------------------------------------------

    def _dealer_evidence(
        self,
        feature,
    ) -> Evidence:

        bias = feature.metadata["dealer_bias"]

        confidence = feature.metadata["confidence"]

        score = feature.metadata["institutional_score"]

        if bias == "LONG GAMMA":

            return Evidence(

                id="dealer_long_gamma",

                name="Dealer Long Gamma",

                type=EvidenceType.DEALER,

                level=self._level(score),

                score=score,

                confidence=confidence,

                source=FeatureId.DEALER_POSITION,

                metadata=feature.metadata,

            )

        return Evidence(

            id="dealer_short_gamma",

            name="Dealer Short Gamma",

            type=EvidenceType.DEALER,

            level=self._level(score),

            score=score,

            confidence=confidence,

            source=FeatureId.DEALER_POSITION,

            metadata=feature.metadata,

        )

    # -----------------------------------------------------
    # Volatility Evidence
    # -----------------------------------------------------

    def _volatility_evidence(
        self,
        feature,
    ) -> Evidence:

        return Evidence(

            id=feature.id.name.lower(),

            name=feature.name,

            type=EvidenceType.VOLATILITY,

            level=self._level(feature.confidence),

            score=feature.value,

            confidence=feature.confidence,

            source=feature.id,

            metadata=feature.metadata,

        )

    # -----------------------------------------------------
    # Strength
    # -----------------------------------------------------

    @staticmethod
    def _level(
        score: float,
    ) -> EvidenceLevel:

        if score >= 80:

            return EvidenceLevel.VERY_STRONG

        if score >= 60:

            return EvidenceLevel.STRONG

        if score >= 40:

            return EvidenceLevel.MODERATE

        if score >= 20:

            return EvidenceLevel.WEAK

        return EvidenceLevel.VERY_WEAK