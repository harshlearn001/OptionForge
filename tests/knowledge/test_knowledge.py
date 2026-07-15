"""
============================================================
Knowledge Model Tests
============================================================
"""

from optionforge.knowledge.knowledge import Knowledge
from optionforge.knowledge.knowledge_level import KnowledgeLevel
from optionforge.knowledge.knowledge_type import KnowledgeType


def make_knowledge() -> Knowledge:

    return Knowledge(
        id="volatility",
        name="Volatility Suppression",
        type=KnowledgeType.VOLATILITY,
        level=KnowledgeLevel.STRONG,
        score=92.5,
        confidence=95.0,
        description="Dealer hedging suppresses volatility.",
        evidence_ids=("dealer_long_gamma",),
    )


def test_create():

    knowledge = make_knowledge()

    assert knowledge.id == "volatility"

    assert knowledge.score == 92.5

    assert knowledge.confidence == 95.0


def test_confidence_ratio():

    knowledge = make_knowledge()

    assert knowledge.confidence_ratio == 0.95


def test_to_dict():

    knowledge = make_knowledge()

    data = knowledge.to_dict()

    assert data["id"] == "volatility"

    assert data["confidence"] == 95.0


def test_invalid_confidence():

    import pytest

    with pytest.raises(ValueError):

        Knowledge(
            id="bad",
            name="Bad",
            type=KnowledgeType.RISK,
            level=KnowledgeLevel.WEAK,
            score=1,
            confidence=150,
            description="",
            evidence_ids=(),
        )
