"""
============================================================
OptionForge
Volatility Rule Tests
============================================================
"""

from optionforge.evidence.evidence import Evidence
from optionforge.evidence.evidence_direction import EvidenceDirection
from optionforge.evidence.evidence_level import EvidenceLevel
from optionforge.evidence.evidence_registry import EvidenceRegistry
from optionforge.evidence.evidence_source import EvidenceSource

from optionforge.knowledge.knowledge_builder import KnowledgeBuilder
from optionforge.knowledge.rules.volatility_rule import VolatilityRule


# ==========================================================
# Helpers
# ==========================================================

def volatility(score: float) -> Evidence:

    return Evidence(
        id="iv_rank",
        title="IV Rank",
        source=EvidenceSource.IV_RANK,
        direction=EvidenceDirection.NEUTRAL,
        level=EvidenceLevel.STRONG,
        score=score,
        confidence=0.92,
        description="Implied Volatility",
    )


# ==========================================================
# Tests
# ==========================================================

def test_extreme_volatility():

    registry = EvidenceRegistry()

    registry.add(
        volatility(95),
    )

    knowledge = VolatilityRule().evaluate(
        evidence=registry,
        builder=KnowledgeBuilder(),
    )

    assert knowledge is not None

    assert knowledge.id == "extreme_volatility"

    assert knowledge.name == "Extreme Volatility"


def test_elevated_volatility():

    registry = EvidenceRegistry()

    registry.add(
        volatility(80),
    )

    knowledge = VolatilityRule().evaluate(
        evidence=registry,
        builder=KnowledgeBuilder(),
    )

    assert knowledge is not None

    assert knowledge.id == "elevated_volatility"


def test_compressed_volatility():

    registry = EvidenceRegistry()

    registry.add(
        volatility(20),
    )

    knowledge = VolatilityRule().evaluate(
        evidence=registry,
        builder=KnowledgeBuilder(),
    )

    assert knowledge is not None

    assert knowledge.id == "compressed_volatility"


def test_normal_volatility():

    registry = EvidenceRegistry()

    registry.add(
        volatility(55),
    )

    knowledge = VolatilityRule().evaluate(
        evidence=registry,
        builder=KnowledgeBuilder(),
    )

    assert knowledge is not None

    assert knowledge.id == "normal_volatility"


def test_no_volatility_evidence():

    registry = EvidenceRegistry()

    knowledge = VolatilityRule().evaluate(
        evidence=registry,
        builder=KnowledgeBuilder(),
    )

    assert knowledge is None