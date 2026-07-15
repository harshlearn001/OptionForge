"""
============================================================
OptionForge
Knowledge Engine Integration Tests
============================================================
"""

from optionforge.evidence.evidence import Evidence
from optionforge.evidence.evidence_level import EvidenceLevel
from optionforge.evidence.evidence_registry import EvidenceRegistry
from optionforge.evidence.evidence_type import EvidenceType

from optionforge.features.feature_id import FeatureId

from optionforge.knowledge.knowledge_engine import KnowledgeEngine

from optionforge.knowledge.rules.dealer_rule import DealerRule
from optionforge.knowledge.rules.volatility_rule import VolatilityRule

# ==========================================================
# Helpers
# ==========================================================


def dealer() -> Evidence:

    return Evidence(
        id="dealer_long_gamma",
        name="Dealer Long Gamma",
        type=EvidenceType.DEALER,
        level=EvidenceLevel.VERY_STRONG,
        score=92,
        confidence=96,
        description="",
        source=FeatureId.DEALER_POSITION,
    )


def volatility() -> Evidence:

    return Evidence(
        id="iv_rank",
        name="IV Rank",
        type=EvidenceType.VOLATILITY,
        level=EvidenceLevel.STRONG,
        score=90,
        confidence=91,
        description="",
        source=FeatureId.IV_RANK,
    )


# ==========================================================
# Tests
# ==========================================================


def test_engine_executes_multiple_rules():

    registry = EvidenceRegistry()

    registry.add(dealer())

    registry.add(volatility())

    engine = KnowledgeEngine(
        rules=[
            DealerRule(),
            VolatilityRule(),
        ]
    )

    knowledge = engine.build(registry)

    assert len(knowledge) == 2

    assert knowledge.exists("volatility_suppression")

    assert knowledge.exists("extreme_volatility")


def test_engine_without_matching_evidence():

    engine = KnowledgeEngine(
        rules=[
            DealerRule(),
            VolatilityRule(),
        ]
    )

    knowledge = engine.build(EvidenceRegistry())

    assert len(knowledge) == 0
