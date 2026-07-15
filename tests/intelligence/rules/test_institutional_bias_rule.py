"""
============================================================
OptionForge
Institutional Bias Rule Tests
============================================================
"""

from optionforge.intelligence.intelligence_builder import (
    IntelligenceBuilder,
)
from optionforge.intelligence.intelligence_level import (
    IntelligenceLevel,
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


def test_empty_registry():

    registry = KnowledgeRegistry()

    intelligence = InstitutionalBiasRule().evaluate(
        knowledge=registry,
        builder=IntelligenceBuilder(),
    )

    assert intelligence is None


def test_dealer_only():

    registry = KnowledgeRegistry()

    registry.add(dealer())

    intelligence = InstitutionalBiasRule().evaluate(
        knowledge=registry,
        builder=IntelligenceBuilder(),
    )

    assert intelligence is not None

    assert intelligence.id == "institutional_bias"

    assert intelligence.metadata["dealer_present"] is True

    assert intelligence.metadata["volatility_present"] is False


def test_volatility_only():

    registry = KnowledgeRegistry()

    registry.add(volatility())

    intelligence = InstitutionalBiasRule().evaluate(
        knowledge=registry,
        builder=IntelligenceBuilder(),
    )

    assert intelligence is not None

    assert intelligence.metadata["dealer_present"] is False

    assert intelligence.metadata["volatility_present"] is True


def test_dealer_and_volatility():

    registry = KnowledgeRegistry()

    registry.add(dealer())

    registry.add(volatility())

    intelligence = InstitutionalBiasRule().evaluate(
        knowledge=registry,
        builder=IntelligenceBuilder(),
    )

    assert intelligence is not None

    assert intelligence.metadata["knowledge_count"] == 2

    assert intelligence.metadata["dealer_present"] is True

    assert intelligence.metadata["volatility_present"] is True


def test_level_assignment():

    registry = KnowledgeRegistry()

    registry.add(dealer())

    registry.add(volatility())

    intelligence = InstitutionalBiasRule().evaluate(
        knowledge=registry,
        builder=IntelligenceBuilder(),
    )

    assert intelligence.level == IntelligenceLevel.VERY_STRONG
