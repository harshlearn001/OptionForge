"""
============================================================
OptionForge
Knowledge Builder
============================================================

Author      : OptionForge
Module      : knowledge_builder.py

Purpose
-------
Constructs immutable Knowledge objects.

Responsibilities
----------------
- Validate inputs
- Normalize data
- Create immutable Knowledge objects

The builder contains NO business logic.

Business reasoning belongs to Knowledge Rules.
============================================================
"""

from __future__ import annotations

from typing import Any

from optionforge.knowledge.knowledge import Knowledge
from optionforge.knowledge.knowledge_level import KnowledgeLevel
from optionforge.knowledge.knowledge_type import KnowledgeType


class KnowledgeBuilder:
    """
    Factory responsible for constructing Knowledge objects.
    """

    def build(
        self,
        *,
        id: str,
        name: str,
        type: KnowledgeType,
        level: KnowledgeLevel,
        score: float,
        confidence: float,
        description: str,
        evidence_ids: tuple[str, ...] = (),
        metadata: dict[str, Any] | None = None,
    ) -> Knowledge:
        """
        Build a validated immutable Knowledge object.
        """

        return Knowledge(

            id=id,

            name=name,

            type=type,

            level=level,

            score=score,

            confidence=confidence,

            description=description,

            evidence_ids=evidence_ids,

            metadata=metadata or {},

        )