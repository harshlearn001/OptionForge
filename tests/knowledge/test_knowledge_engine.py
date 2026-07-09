"""
============================================================
Knowledge Engine Tests
============================================================
"""

from optionforge.evidence.evidence_registry import EvidenceRegistry
from optionforge.knowledge.knowledge_engine import KnowledgeEngine


def test_empty_engine():

    engine = KnowledgeEngine()

    registry = engine.build(

        EvidenceRegistry()

    )

    assert len(registry) == 0


def test_no_rules():

    engine = KnowledgeEngine()

    assert len(engine) == 0


def test_rules_property():

    engine = KnowledgeEngine()

    assert engine.rules == ()