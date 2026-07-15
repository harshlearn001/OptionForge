"""
============================================================
OptionForge
Intelligence Level
============================================================

Author      : OptionForge
Module      : intelligence_level.py

Purpose
-------
Defines the confidence / strength of an institutional
intelligence conclusion.

The level is independent of whether the intelligence
is bullish or bearish.
============================================================
"""

from __future__ import annotations

from enum import Enum
from enum import auto


class IntelligenceLevel(Enum):
    """
    Strength of institutional intelligence.
    """

    # -----------------------------------------------------
    # Extremely Weak
    # -----------------------------------------------------

    VERY_WEAK = auto()

    # -----------------------------------------------------
    # Weak
    # -----------------------------------------------------

    WEAK = auto()

    # -----------------------------------------------------
    # Moderate
    # -----------------------------------------------------

    MODERATE = auto()

    # -----------------------------------------------------
    # Strong
    # -----------------------------------------------------

    STRONG = auto()

    # -----------------------------------------------------
    # Extremely Strong
    # -----------------------------------------------------

    VERY_STRONG = auto()
