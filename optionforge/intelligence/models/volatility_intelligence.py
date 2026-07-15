"""
==============================================================
OptionForge
Intelligence
Volatility Intelligence
==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from optionforge.intelligence.enums.volatility_state import (
    VolatilityState,
)

from optionforge.intelligence.models.intelligence_result import (
    IntelligenceResult,
)


@dataclass(frozen=True, slots=True)
class VolatilityIntelligence(IntelligenceResult):
    """
    Institutional interpretation of
    current volatility conditions.
    """

    state: VolatilityState
