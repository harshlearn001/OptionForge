"""
============================================================
OptionForge
Knowledge Level
============================================================

Author      : OptionForge
Module      : knowledge_level.py

Purpose
-------
Defines the qualitative strength of institutional
market knowledge.

KnowledgeLevel represents the strength or conviction
of a Knowledge object.

It is intentionally identical in semantics to
EvidenceLevel to maintain consistency across the
reasoning framework.

Examples
--------
VERY_WEAK
WEAK
MODERATE
STRONG
VERY_STRONG
============================================================
"""

from __future__ import annotations

from enum import IntEnum


class KnowledgeLevel(IntEnum):
    """
    Qualitative strength of institutional knowledge.
    """

    # =====================================================
    # Lowest Confidence
    # =====================================================

    VERY_WEAK = 1

    # =====================================================
    # Weak
    # =====================================================

    WEAK = 2

    # =====================================================
    # Moderate
    # =====================================================

    MODERATE = 3

    # =====================================================
    # Strong
    # =====================================================

    STRONG = 4

    # =====================================================
    # Highest Confidence
    # =====================================================

    VERY_STRONG = 5

    # =====================================================
    # Convenience
    # =====================================================

    @property
    def score(self) -> int:
        """
        Numerical representation of the level.
        """

        return int(self)

    @property
    def normalized(self) -> float:
        """
        Returns the level normalized to [0.2, 1.0].
        """

        return self / 5.0
