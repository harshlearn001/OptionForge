"""
============================================================
OptionForge
Volatility Knowledge Rule
============================================================

Author      : OptionForge
Module      : volatility_rule.py

Purpose
-------
Transforms Volatility Evidence into institutional
Knowledge.

Responsibilities
----------------
- Evaluate Volatility Evidence
- Produce one Knowledge object
- Return None if no applicable Volatility Evidence exists

This rule contains business reasoning.

It performs NO analytics.
============================================================
"""

from __future__ import annotations

from optionforge.evidence.evidence_registry import EvidenceRegistry
from optionforge.evidence.evidence_type import EvidenceType

from optionforge.knowledge.knowledge import Knowledge
from optionforge.knowledge.knowledge_builder import KnowledgeBuilder
from optionforge.knowledge.knowledge_level import KnowledgeLevel
from optionforge.knowledge.knowledge_type import KnowledgeType
from optionforge.knowledge.rules.knowledge_rule import KnowledgeRule


class VolatilityRule(KnowledgeRule):
    """
    Produces institutional volatility knowledge.
    """

    def evaluate(
        self,
        *,
        evidence: EvidenceRegistry,
        builder: KnowledgeBuilder,
    ) -> Knowledge | None:

        volatility = evidence.by_type(EvidenceType.VOLATILITY)

        if not volatility:

            return None

        volatility = volatility[0]

        score = volatility.score

        # ==================================================
        # Extreme Volatility
        # ==================================================

        if score >= 90:

            return builder.build(
                id="extreme_volatility",
                name="Extreme Volatility",
                type=KnowledgeType.VOLATILITY,
                level=KnowledgeLevel.VERY_STRONG,
                score=score,
                confidence=volatility.confidence,
                description=(
                    "Implied volatility is extremely elevated. "
                    "Expect unusually large price swings."
                ),
                evidence_ids=(volatility.id,),
            )

        # ==================================================
        # Elevated Volatility
        # ==================================================

        if score >= 75:

            return builder.build(
                id="elevated_volatility",
                name="Elevated Volatility",
                type=KnowledgeType.VOLATILITY,
                level=KnowledgeLevel.STRONG,
                score=score,
                confidence=volatility.confidence,
                description=(
                    "Implied volatility is elevated. "
                    "Larger-than-normal market movement is expected."
                ),
                evidence_ids=(volatility.id,),
            )

        # ==================================================
        # Compressed Volatility
        # ==================================================

        if score <= 25:

            return builder.build(
                id="compressed_volatility",
                name="Compressed Volatility",
                type=KnowledgeType.VOLATILITY,
                level=KnowledgeLevel.STRONG,
                score=score,
                confidence=volatility.confidence,
                description=(
                    "Implied volatility is compressed. " "Expansion risk is increasing."
                ),
                evidence_ids=(volatility.id,),
            )

        # ==================================================
        # Normal Volatility
        # ==================================================

        return builder.build(
            id="normal_volatility",
            name="Normal Volatility",
            type=KnowledgeType.VOLATILITY,
            level=KnowledgeLevel.MODERATE,
            score=score,
            confidence=volatility.confidence,
            description=("Volatility is within its historical range."),
            evidence_ids=(volatility.id,),
        )
