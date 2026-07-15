"""
============================================================
OptionForge
Risk Intelligence Rule
============================================================

Author      : OptionForge
Module      : risk_intelligence_rule.py

Purpose
-------
Evaluates institutional market risk from
Knowledge objects.

Responsibilities
----------------
- Evaluate Knowledge
- Produce Risk Intelligence
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


class RiskIntelligenceRule(IntelligenceRule):
    """
    Produces institutional market risk.
    """

    def evaluate(
        self,
        *,
        knowledge: KnowledgeRegistry,
        builder: IntelligenceBuilder,
    ) -> Intelligence | None:

        if len(knowledge) == 0:

            return None

        dealer = knowledge.by_type(KnowledgeType.DEALER)

        volatility = knowledge.by_type(KnowledgeType.VOLATILITY)

        score = knowledge.score

        confidence = knowledge.confidence

        # --------------------------------------------------
        # Risk Assessment
        # --------------------------------------------------

        if dealer and volatility:

            description = (
                "Dealer positioning and volatility both "
                "contribute to institutional market risk."
            )

        elif volatility:

            description = (
                "Volatility is the primary source of " "institutional market risk."
            )

        elif dealer:

            description = (
                "Dealer positioning is the dominant " "institutional risk factor."
            )

        else:

            description = "No significant institutional risk " "drivers detected."

        # --------------------------------------------------
        # Risk Level
        # --------------------------------------------------

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
            id="institutional_risk",
            name="Institutional Market Risk",
            type=IntelligenceType.RISK,
            level=level,
            score=score,
            confidence=confidence,
            description=description,
            knowledge_ids=tuple(item.id for item in knowledge),
            metadata={
                "knowledge_count": len(knowledge),
                "dealer_present": bool(dealer),
                "volatility_present": bool(volatility),
                "risk_version": 1,
            },
        )
