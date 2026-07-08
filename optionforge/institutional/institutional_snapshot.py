"""
============================================================
OptionForge
Institutional Snapshot
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from optionforge.market_snapshot.market_snapshot import (
    MarketSnapshot,
)

from optionforge.institutional.institutional_metadata import (
    InstitutionalMetadata,
)

from optionforge.institutional.institutional_stage import (
    InstitutionalStage,
)


@dataclass(
    frozen=True,
    slots=True,
)
class InstitutionalSnapshot:
    """
    Immutable institutional snapshot.
    """

    market_snapshot: MarketSnapshot

    analytics: Any | None = None

    evidence: Any | None = None

    market_dna: Any | None = None

    decision: Any | None = None

    strategy: Any | None = None

    execution: Any | None = None

    metadata: InstitutionalMetadata = InstitutionalMetadata()

    stage: InstitutionalStage = InstitutionalStage.MARKET

    @property
    def symbol(self) -> str:

        return self.market_snapshot.symbol