"""
============================================================
OptionForge
Intelligence Builder
============================================================

Author      : OptionForge
Module      : intelligence_builder.py

Purpose
-------
Factory responsible for constructing validated
Intelligence objects.

The builder contains no business reasoning.

Responsibilities
----------------
- Construct Intelligence
- Provide a consistent creation API
============================================================
"""

from __future__ import annotations

from typing import Any
from typing import Mapping

from optionforge.intelligence.intelligence import Intelligence
from optionforge.intelligence.intelligence_level import (
    IntelligenceLevel,
)
from optionforge.intelligence.intelligence_type import (
    IntelligenceType,
)


class IntelligenceBuilder:
    """
    Factory for Intelligence objects.
    """

    def build(
        self,
        *,
        id: str,
        name: str,
        type: IntelligenceType,
        level: IntelligenceLevel,
        score: float,
        confidence: float,
        description: str,
        knowledge_ids: tuple[str, ...],
        metadata: Mapping[str, Any] | None = None,
    ) -> Intelligence:

        return Intelligence(

            id=id,

            name=name,

            type=type,

            level=level,

            score=score,

            confidence=confidence,

            description=description,

            knowledge_ids=knowledge_ids,

            metadata=metadata or {},

        )