"""
============================================================
OptionForge
Evidence Type
============================================================

Author      : OptionForge
Module      : evidence_type.py
Purpose     : High-level classification of institutional
              evidence.

Evidence types are intentionally broad and represent
major market dimensions.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class EvidenceType(Enum):
    """
    High-level evidence categories.
    """

    # -----------------------------------------------------
    # Direction
    # -----------------------------------------------------

    BULLISH = auto()

    BEARISH = auto()

    NEUTRAL = auto()

    # -----------------------------------------------------
    # Market Structure
    # -----------------------------------------------------

    TREND = auto()

    VOLATILITY = auto()

    LIQUIDITY = auto()

    DEALER = auto()

    FLOW = auto()

    MOMENTUM = auto()

    # -----------------------------------------------------
    # Risk
    # -----------------------------------------------------

    RISK = auto()

    OPPORTUNITY = auto()