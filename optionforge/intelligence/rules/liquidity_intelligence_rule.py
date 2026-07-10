"""
============================================================
OptionForge
Liquidity Intelligence Rule
============================================================

Author      : OptionForge
Module      : liquidity_intelligence_rule.py

Purpose
-------
Evaluates institutional liquidity from Knowledge.

Liquidity Intelligence estimates whether current
market conditions support efficient institutional
execution.

Version 1
---------
Uses Dealer and Volatility knowledge.

Future versions will incorporate:

- Bid/Ask Spread
- Open Interest
- Volume
- Market Depth
- ATM Liquidity
- Execution Quality
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


class LiquidityIntelligenceRule(IntelligenceRule):
    """
    Produces institutional liquidity intelligence.
    """

    def evaluate(
        self,
        *,
        knowledge: KnowledgeRegistry,
        builder: IntelligenceBuilder,
    ) -> Intelligence | None:

        if len(knowledge) == 0:

            return None

        dealer = knowledge.by_type(
            KnowledgeType.DEALER
        )

        volatility = knowledge.by_type(
            KnowledgeType.VOLATILITY
        )

        score = knowledge.score

        confidence = knowledge.confidence

        # --------------------------------------------------
        # Liquidity Assessment
        # --------------------------------------------------

        if dealer and volatility:

            description = (
                "Dealer participation and volatility "
                "indicate healthy institutional liquidity."
            )

        elif dealer:

            description = (
                "Dealer participation supports "
                "market liquidity."
            )

        elif volatility:

            description = (
                "Liquidity is primarily influenced "
                "by current volatility conditions."
            )

        else:

            description = (
                "Institutional liquidity signals "
                "remain neutral."
            )

        # --------------------------------------------------
        # Liquidity Strength
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

            id="institutional_liquidity",

            name="Institutional Liquidity",

            type=IntelligenceType.LIQUIDITY,

            level=level,

            score=score,

            confidence=confidence,

            description=description,

            knowledge_ids=tuple(

                item.id

                for item in knowledge

            ),

            metadata={

                "knowledge_count": len(knowledge),

                "dealer_present": bool(dealer),

                "volatility_present": bool(volatility),

                "execution_quality": (
                    "HIGH"
                    if score >= 80
                    else "MODERATE"
                    if score >= 50
                    else "LOW"
                ),

                "liquidity_version": 1,

            },

        )