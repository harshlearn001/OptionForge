"""
==============================================================
OptionForge
Intelligence
Institutional Decision
==============================================================

Immutable institutional decision.

Author : OptionForge
==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from optionforge.intelligence.enums.institutional_state import (
    InstitutionalState,
)
from optionforge.intelligence.models.intelligence_result import (
    IntelligenceResult,
)


@dataclass(frozen=True, slots=True)
class InstitutionalDecision(IntelligenceResult):
    """
    Final institutional opinion produced by
    combining multiple intelligence engines.
    """

    state: InstitutionalState
