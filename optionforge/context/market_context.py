"""
============================================================
OptionForge
Market Context
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from optionforge.market.market_snapshot import MarketSnapshot
from optionforge.research.institutional_snapshot import InstitutionalSnapshot


@dataclass(frozen=True, slots=True)
class MarketContext:
    """
    Complete market context used throughout OptionForge.

    This object is immutable and shared by providers,
    classifiers, decision engine and research modules.
    """

    market: MarketSnapshot

    snapshot: InstitutionalSnapshot

    metadata: Mapping[str, Any] = field(default_factory=dict)