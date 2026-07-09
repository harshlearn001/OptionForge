"""
============================================================
OptionForge
Institutional Bias Rule
============================================================

Author      : OptionForge
Module      : institutional_bias_rule.py

Purpose
-------
Combines multiple Knowledge objects into a single
Institutional Intelligence conclusion.

This is the first Intelligence Rule.

Responsibilities
----------------
- Evaluate Knowledge
- Produce Institutional Intelligence
- Return None when insufficient knowledge exists

Contains NO analytics.
============================================================
"""

from __future__ import annotations

from optionforge.intelligence.intelligence import Intelligence
from optionforge.intelligence.intelligence_builder import (
    IntelligenceBuilder,
)
from optionforge.intelligence.intelligence_level import (
    IntelligenceLevel,
)
from optionforge.intelligence.intelligence_type import (
    IntelligenceType,
)
from optionforge.intelligence.rules.intelligence_rule import (
    IntelligenceRule,
)

from optionforge.knowledge.knowledge_registry import (
    KnowledgeRegistry,
)
from optionforge.knowledge.knowledge_type import (
    KnowledgeType,
)


class InstitutionalBiasRule(IntelligenceRule):
    """
    Produces a high-level institutional market bias.
    """

    def evaluate(
        self,
        *,
        knowledge: KnowledgeRegistry,
        builder: IntelligenceBuilder,
    ) -> Intelligence | None:

        if len(knowledge) == 0:

            return None

        score = knowledge.score

        confidence = knowledge.confidence

        dealer = knowledge.by_type(
            KnowledgeType.DEALER
        )

        volatility = knowledge.by_type(
            KnowledgeType.VOLATILITY
        )

        # ---------------------------------------------
        # Bias
        # ---------------------------------------------

        if dealer and volatility:

            bias = (
                "Institutional positioning supports "
                "the current market environment."
            )

        elif dealer:

            bias = (
                "Dealer positioning is the dominant "
                "institutional signal."
            )

        elif volatility:

            bias = (
                "Volatility conditions are the dominant "
                "institutional signal."
            )

        else:

            bias = (
                "Institutional market bias remains "
                "neutral."
            )

        # ---------------------------------------------
        # Strength
        # ---------------------------------------------

        if score >= 80:

            level = IntelligenceLevel.VERY_STRONG

        elif score >= 60:

            level = IntelligenceLevel.STRONG

        elif score >= 40:

            level = IntelligenceLevel.MODERATE

        elif score >= 20:

            level = IntelligenceLevel.WEAK

        else:

            level = IntelligenceLevel.VERY_WEAK

        return builder.build(

            id="institutional_bias",

            name="Institutional Market Bias",

            type=IntelligenceType.INSTITUTIONAL,

            level=level,

            score=score,

            confidence=confidence,

            description=bias,

            knowledge_ids=tuple(

                item.id

                for item in knowledge

            ),

            metadata={

                "knowledge_count": len(knowledge),

                "dealer_present": bool(dealer),

                "volatility_present": bool(volatility),

            },

        )