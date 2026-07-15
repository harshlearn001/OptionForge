"""
============================================================
OptionForge
Intelligence Engine Integration Tests
============================================================
"""

from optionforge.intelligence.intelligence_builder import (
    IntelligenceBuilder,
)
from optionforge.intelligence.intelligence_engine import (
    IntelligenceEngine,
)
from optionforge.intelligence.rules.institutional_bias_rule import (
    InstitutionalBiasRule,
)

from optionforge.knowledge.knowledge import Knowledge
from optionforge.knowledge.knowledge_level import KnowledgeLevel
from optionforge.knowledge.knowledge_registry import (
    KnowledgeRegistry,
)
from optionforge.knowledge.knowledge_type import (
    KnowledgeType,
)

# ==========================================================
# Helpers
# ==========================================================


def dealer() -> Knowledge:

    return Knowledge(
        id="dealer",
        name="Dealer Long Gamma",
        type=KnowledgeType.DEALER,
        level=KnowledgeLevel.VERY_STRONG,
        score=92.0,
        confidence=95.0,
        description="Dealer positioning suppresses volatility.",
        evidence_ids=("dealer_long_gamma",),
    )


def volatility() -> Knowledge:

    return Knowledge(
        id="volatility",
        name="Elevated Volatility",
        type=KnowledgeType.VOLATILITY,
        level=KnowledgeLevel.STRONG,
        score=82.0,
        confidence=90.0,
        description="Implied volatility is elevated.",
        evidence_ids=("iv_rank",),
    )


# ==========================================================
# Tests
# ==========================================================


def test_engine_executes_registered_rules():

    registry = KnowledgeRegistry()

    registry.add(dealer())

    registry.add(volatility())

    engine = IntelligenceEngine(
        rules=(InstitutionalBiasRule(),),
    )

    intelligence = engine.build(registry)

    assert len(intelligence) == 1

    assert intelligence.exists("institutional_bias")


def test_engine_empty_registry():

    engine = IntelligenceEngine(
        rules=(InstitutionalBiasRule(),),
    )

    intelligence = engine.build(KnowledgeRegistry())

    assert len(intelligence) == 0


def test_engine_score():

    registry = KnowledgeRegistry()

    registry.add(dealer())

    registry.add(volatility())

    engine = IntelligenceEngine(
        rules=(InstitutionalBiasRule(),),
    )

    intelligence = engine.build(registry)

    assert intelligence.score > 0


def test_engine_confidence():

    registry = KnowledgeRegistry()

    registry.add(dealer())

    registry.add(volatility())

    engine = IntelligenceEngine(
        rules=(InstitutionalBiasRule(),),
    )

    intelligence = engine.build(registry)

    assert intelligence.confidence > 0
