"""
============================================================
Knowledge Builder Tests
============================================================
"""

from optionforge.knowledge.knowledge_builder import KnowledgeBuilder
from optionforge.knowledge.knowledge_level import KnowledgeLevel
from optionforge.knowledge.knowledge_type import KnowledgeType


def test_builder():

    builder = KnowledgeBuilder()

    knowledge = builder.build(
        id="dealer",
        name="Dealer",
        type=KnowledgeType.DEALER,
        level=KnowledgeLevel.STRONG,
        score=88,
        confidence=91,
        description="Dealer Long Gamma",
        evidence_ids=("dealer",),
    )

    assert knowledge.id == "dealer"

    assert knowledge.score == 88

    assert knowledge.confidence == 91
