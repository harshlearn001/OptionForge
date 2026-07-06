"""
==============================================================
Dealer Intelligence
==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from optionforge.intelligence.enums.dealer_state import DealerState
from optionforge.intelligence.models.intelligence_result import (
    IntelligenceResult,
)


@dataclass(frozen=True, slots=True)
class DealerIntelligence(IntelligenceResult):
    """
    Institutional interpretation of dealer positioning.
    """

    state: DealerState