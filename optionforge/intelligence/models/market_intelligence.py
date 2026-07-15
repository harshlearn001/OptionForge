"""
==============================================================
OptionForge
Intelligence
Market Intelligence
==============================================================

Immutable market interpretation.

Author : OptionForge
==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from optionforge.intelligence.enums.market_state import MarketState
from optionforge.intelligence.models.intelligence_result import (
    IntelligenceResult,
)


@dataclass(frozen=True, slots=True)
class MarketIntelligence(IntelligenceResult):
    """
    Institutional interpretation of
    the overall market regime.
    """

    state: MarketState
