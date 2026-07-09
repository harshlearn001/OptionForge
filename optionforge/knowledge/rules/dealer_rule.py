"""
============================================================
OptionForge
Dealer Knowledge Rule
============================================================

Author      : OptionForge
Module      : dealer_rule.py

Purpose
-------
Transforms Dealer Evidence into institutional
Knowledge.

Responsibilities
----------------
- Evaluate Dealer Evidence
- Produce one Knowledge object
- Return None if no applicable Dealer Evidence exists

This rule contains business reasoning.

It performs NO analytics.
============================================================
"""

from __future__ import annotations

from optionforge.evidence.evidence_type import EvidenceType
from optionforge.evidence.evidence_registry import EvidenceRegistry

from optionforge.knowledge.knowledge import Knowledge
from optionforge.knowledge.knowledge_builder import KnowledgeBuilder
from optionforge.knowledge.knowledge_level import KnowledgeLevel
from optionforge.knowledge.knowledge_type import KnowledgeType

from optionforge.knowledge.rules.knowledge_rule import KnowledgeRule


class DealerRule(KnowledgeRule):
    """
    Produces institutional dealer knowledge.
    """

    def evaluate(
        self,
        *,
        evidence: EvidenceRegistry,
        builder: KnowledgeBuilder,
    ) -> Knowledge | None:

        dealer = evidence.by_type(
            EvidenceType.DEALER
        )

        if not dealer:

            return None

        dealer = dealer[0]

        name = dealer.name.lower()

        # ==================================================
        # Dealer Long Gamma
        # ==================================================

        if "long gamma" in name:

            return builder.build(

                id="volatility_suppression",

                name="Volatility Suppression",

                type=KnowledgeType.DEALER,

                level=KnowledgeLevel.VERY_STRONG,

                score=dealer.score,

                confidence=dealer.confidence,

                description=(
                    "Dealer positioning indicates "
                    "hedging activity is likely to "
                    "suppress short-term volatility."
                ),

                evidence_ids=(dealer.id,),

            )

        # ==================================================
        # Dealer Short Gamma
        # ==================================================

        if "short gamma" in name:

            return builder.build(

                id="volatility_expansion",

                name="Volatility Expansion",

                type=KnowledgeType.DEALER,

                level=KnowledgeLevel.VERY_STRONG,

                score=dealer.score,

                confidence=dealer.confidence,

                description=(
                    "Dealer positioning indicates "
                    "hedging activity may amplify "
                    "market volatility."
                ),

                evidence_ids=(dealer.id,),

            )

        return None