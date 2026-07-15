"""
==============================================================
OptionForge
Intelligence
Institutional State
==============================================================

Overall institutional market opinion.

Author : OptionForge
==============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class InstitutionalState(Enum):
    """
    Institutional market opinion.

    Generated after combining multiple
    intelligence engines.
    """

    STRONGLY_BULLISH = auto()

    BULLISH = auto()

    NEUTRAL = auto()

    BEARISH = auto()

    STRONGLY_BEARISH = auto()
