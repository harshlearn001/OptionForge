"""
============================================================
OptionForge
Dealer Rule Tests
============================================================
"""

from optionforge.evidence.evidence import Evidence
from optionforge.evidence.evidence_direction import EvidenceDirection
from optionforge.evidence.evidence_level import EvidenceLevel
from optionforge.evidence.evidence_registry import EvidenceRegistry
from optionforge.evidence.evidence_source import EvidenceSource

from optionforge.knowledge.knowledge_builder import KnowledgeBuilder
from optionforge.knowledge.rules.dealer_rule import DealerRule


# ==========================================================
# Helpers
# ==========================================================

def dealer_long_gamma() -> Evidence:

    return Evidence(
        id="dealer_long_gamma",
        title="Dealer Long Gamma",
        direction=EvidenceDirection.BULLISH,
        level=EvidenceLevel.VERY_STRONG,
        score=90.0,
        confidence=0.95,
        description="Dealers are long gamma.",
        source=EvidenceSource.DEALER_GAMMA,
    )


def dealer_short_gamma() -> Evidence:

    return Evidence(
        id="dealer_short_gamma",
        title="Dealer Short Gamma",
        direction=EvidenceDirection.BEARISH,
        level=EvidenceLevel.VERY_STRONG,
        score=88.0,
        confidence=0.93,
        description="Dealers are short gamma.",
        source=EvidenceSource.DEALER_GAMMA,
    )


# ==========================================================
# Tests
# ==========================================================

def test_long_gamma():

    registry = EvidenceRegistry()

    registry.add(
        dealer_long_gamma(),
    )

    knowledge = DealerRule().evaluate(
        evidence=registry,
        builder=KnowledgeBuilder(),
    )

    assert knowledge is not None

    assert knowledge.id == "volatility_suppression"

    assert knowledge.name == "Volatility Suppression"


def test_short_gamma():

    registry = EvidenceRegistry()

    registry.add(
        dealer_short_gamma(),
    )

    knowledge = DealerRule().evaluate(
        evidence=registry,
        builder=KnowledgeBuilder(),
    )

    assert knowledge is not None

    assert knowledge.id == "volatility_expansion"

    assert knowledge.name == "Volatility Expansion"


def test_no_dealer_evidence():

    registry = EvidenceRegistry()

    knowledge = DealerRule().evaluate(
        evidence=registry,
        builder=KnowledgeBuilder(),
    )

    assert knowledge is None