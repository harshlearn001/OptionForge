"""
============================================================
OptionForge
Volatility Rule Tests
============================================================
"""

from optionforge.evidence.evidence import Evidence
from optionforge.evidence.evidence_level import EvidenceLevel
from optionforge.evidence.evidence_registry import EvidenceRegistry
from optionforge.evidence.evidence_type import EvidenceType

from optionforge.features.feature_id import FeatureId

from optionforge.knowledge.knowledge_builder import KnowledgeBuilder
from optionforge.knowledge.rules.volatility_rule import VolatilityRule


# ==========================================================
# Helpers
# ==========================================================

def volatility(score: float) -> Evidence:

    return Evidence(

        id="iv_rank",

        name="IV Rank",

        type=EvidenceType.VOLATILITY,

        level=EvidenceLevel.STRONG,

        score=score,

        confidence=92.0,

        description="Implied Volatility",

        source=FeatureId.IV_RANK,

    )


# ==========================================================
# Tests
# ==========================================================

def test_extreme_volatility():

    registry = EvidenceRegistry()

    registry.add(

        volatility(95)

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

        volatility(80)

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

        volatility(20)

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

        volatility(55)

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