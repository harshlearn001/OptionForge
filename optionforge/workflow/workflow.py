"""
============================================================
OptionForge
Workflow Engine
============================================================

Professional Workflow Engine (v2)

Responsibilities
----------------
- Resolve market data paths
- Construct pipeline
- Execute institutional pipeline

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from pathlib import Path

from optionforge.datasource.path_manager import (
    PathManager,
)
from optionforge.pipeline.optionforge_pipeline import (
    OptionForgePipeline,
)


class WorkflowEngine:
    """
    Professional Workflow Engine.
    """

    def __init__(
        self,
        *,
        loader,
        analytics: dict,
        marketforge_root: str | Path,
    ) -> None:

        self._paths = PathManager(
            marketforge_root,
        )

        self._pipeline = OptionForgePipeline(

            loader=loader,

            analytics=analytics,

        )

    # -----------------------------------------------------

    def run(
        self,
        *,
        option_file: str | Path,
        future_file: str | Path,
        spot_file: str | Path,
    ):
        """
        Execute complete institutional pipeline.
        """

        return self._pipeline.run(

            option_file=str(option_file),

            future_file=str(future_file),

            spot_file=str(spot_file),

        )