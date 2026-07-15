"""
============================================================
OptionForge
Institutional Snapshot Builder
============================================================

Author      : OptionForge
Module      : institutional_snapshot_builder.py
Purpose     : Assemble immutable InstitutionalSnapshot objects.

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from optionforge.institutional.institutional_snapshot import (
    InstitutionalSnapshot,
)

from optionforge.institutional.institutional_metadata import (
    InstitutionalMetadata,
)

from optionforge.institutional.institutional_stage import (
    InstitutionalStage,
)

from optionforge.market_snapshot.market_snapshot import (
    MarketSnapshot,
)


class InstitutionalSnapshotBuilder:
    """
    Builder for immutable InstitutionalSnapshot objects.
    """

    def build(
        self,
        *,
        market_snapshot: MarketSnapshot,
        analytics=None,
        evidence=None,
        market_dna=None,
        decision=None,
        strategy=None,
        execution=None,
    ) -> InstitutionalSnapshot:

        stage = InstitutionalStage.MARKET

        if analytics is not None:
            stage = InstitutionalStage.ANALYTICS

        if evidence is not None:
            stage = InstitutionalStage.EVIDENCE

        if market_dna is not None:
            stage = InstitutionalStage.MARKET_DNA

        if decision is not None:
            stage = InstitutionalStage.DECISION

        if strategy is not None:
            stage = InstitutionalStage.STRATEGY

        if execution is not None:
            stage = InstitutionalStage.COMPLETE

        return InstitutionalSnapshot(
            market_snapshot=market_snapshot,
            analytics=analytics,
            evidence=evidence,
            market_dna=market_dna,
            decision=decision,
            strategy=strategy,
            execution=execution,
            metadata=InstitutionalMetadata(),
            stage=stage,
        )
