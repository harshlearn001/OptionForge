"""
============================================================
OptionForge
Workflow Engine
============================================================

Author      : OptionForge
Module      : workflow.py
Purpose     : Composition root for OptionForge.

Responsibilities
----------------
- Build infrastructure
- Wire dependencies
- Execute pipeline

Contains NO business logic.

Version : 4.0
============================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from optionforge.repository import (
    RepositoryContext,
    RepositoryFactory,
)

from optionforge.utils.loader import Loader

from optionforge.market_snapshot.snapshot_builder import (
    SnapshotBuilder,
)

from optionforge.institutional import (
    InstitutionalSnapshotBuilder,
)

from optionforge.pipeline.optionforge_pipeline import (
    OptionForgePipeline,
)


class WorkflowEngine:
    """
    Composition root for OptionForge.
    """

    def __init__(
        self,
        *,
        marketforge_root: str | Path,
        analytics: dict[str, Any] | None = None,
    ) -> None:

        self._marketforge_root = Path(
            marketforge_root,
        )

        self._analytics = analytics or {}

    # ======================================================
    # Execute
    # ======================================================

    def run(
        self,
        symbol: str,
    ):

        # -------------------------------------------------
        # Repository Layer
        # -------------------------------------------------

        context = RepositoryContext(

            marketforge_root=self._marketforge_root,

        )

        repository_factory = RepositoryFactory(

            context,

        )

        # -------------------------------------------------
        # Loader
        # -------------------------------------------------

        loader = Loader(

            repository_factory,

        )

        # -------------------------------------------------
        # Snapshot Builder
        # -------------------------------------------------

        snapshot_builder = SnapshotBuilder(

            loader,

        )

        # -------------------------------------------------
        # Institutional Snapshot Builder
        # -------------------------------------------------

        institutional_snapshot_builder = (

            InstitutionalSnapshotBuilder()

        )

        # -------------------------------------------------
        # Pipeline
        # -------------------------------------------------

        pipeline = OptionForgePipeline(

            snapshot_builder=snapshot_builder,

            institutional_snapshot_builder=(
                institutional_snapshot_builder
            ),

            analytics=self._analytics,

        )

        # -------------------------------------------------
        # Execute
        # -------------------------------------------------

        return pipeline.execute(

            symbol,

        )