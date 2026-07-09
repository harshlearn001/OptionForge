"""
============================================================
Knowledge Registry Tests
============================================================
"""

from optionforge.knowledge.knowledge import Knowledge
from optionforge.knowledge.knowledge_level import KnowledgeLevel
from optionforge.knowledge.knowledge_registry import KnowledgeRegistry
from optionforge.knowledge.knowledge_type import KnowledgeType


def make_knowledge():

    return Knowledge(

        id="dealer",

        name="Dealer",

        type=KnowledgeType.DEALER,

        level=KnowledgeLevel.STRONG,

        score=90,

        confidence=95,

        description="",

        evidence_ids=(),

    )


def test_add():

    registry = KnowledgeRegistry()

    registry.add(make_knowledge())

    assert len(registry) == 1


def test_get():

    registry = KnowledgeRegistry()

    registry.add(make_knowledge())

    assert registry.get("dealer") is not None


def test_exists():

    registry = KnowledgeRegistry()

    registry.add(make_knowledge())

    assert registry.exists("dealer")


def test_score():

    registry = KnowledgeRegistry()

    registry.add(make_knowledge())

    assert registry.score == 90


def test_confidence():

    registry = KnowledgeRegistry()

    registry.add(make_knowledge())

    assert registry.confidence == 95


def test_remove():

    registry = KnowledgeRegistry()

    registry.add(make_knowledge())

    registry.remove("dealer")

    assert len(registry) == 0