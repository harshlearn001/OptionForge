"""
============================================================
OptionForge
Knowledge Model
============================================================

Author      : OptionForge
Module      : knowledge.py

Purpose
-------
Immutable Knowledge object representing an institutional
market conclusion derived from one or more Evidence objects.

Knowledge is the bridge between Evidence and higher-level
Institutional Intelligence.

Examples
--------
- Volatility Suppression
- Volatility Expansion
- Institutional Accumulation
- Institutional Distribution
- Strong Bullish Structure
- Weak Bearish Structure
- High Liquidity
- Elevated Market Risk

This object is immutable and thread-safe.
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, Mapping

from optionforge.knowledge.knowledge_level import KnowledgeLevel
from optionforge.knowledge.knowledge_type import KnowledgeType


@dataclass(
    frozen=True,
    slots=True,
)
class Knowledge:
    """
    Represents one institutional market conclusion.
    """

    # =====================================================
    # Identity
    # =====================================================

    id: str

    name: str

    # =====================================================
    # Classification
    # =====================================================

    type: KnowledgeType

    level: KnowledgeLevel

    # =====================================================
    # Quantitative
    # =====================================================

    score: float

    confidence: float

    # =====================================================
    # Human Interpretation
    # =====================================================

    description: str

    # =====================================================
    # Explainability
    # =====================================================

    evidence_ids: tuple[str, ...]

    # =====================================================
    # Metadata
    # =====================================================

    metadata: Mapping[str, Any] = field(
        default_factory=dict,
        compare=False,
    )

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC),
        compare=False,
    )

    # =====================================================
    # Validation
    # =====================================================

    def __post_init__(self) -> None:

        if not (0.0 <= self.confidence <= 100.0):

            raise ValueError(
                "Confidence must be between 0 and 100."
            )

    # =====================================================
    # Convenience
    # =====================================================

    @property
    def confidence_ratio(self) -> float:
        """
        Confidence expressed as a ratio.
        """

        return self.confidence / 100.0

    # =====================================================
    # Serialization
    # =====================================================

    def to_dict(self) -> dict[str, Any]:
        """
        Convert to dictionary.
        """

        return {

            "id": self.id,

            "name": self.name,

            "type": self.type.name,

            "level": self.level.name,

            "score": self.score,

            "confidence": self.confidence,

            "description": self.description,

            "evidence_ids": list(self.evidence_ids),

            "timestamp": self.timestamp.isoformat(),

            "metadata": dict(self.metadata),

        }

    # =====================================================
    # Representation
    # =====================================================

    def __str__(self) -> str:

        return (

            f"{self.name}("

            f"score={self.score:.2f}, "

            f"confidence={self.confidence:.1f}%)"

        )

    def __repr__(self) -> str:

        return (

            f"Knowledge("

            f"id={self.id}, "

            f"type={self.type.name}, "

            f"score={self.score}, "

            f"confidence={self.confidence})"

        )