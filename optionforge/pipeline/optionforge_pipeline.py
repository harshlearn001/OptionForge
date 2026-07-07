"""
==============================================================
OptionForge
Pipeline
OptionForge Pipeline
==============================================================

Central orchestration pipeline.

Responsibilities
----------------
- Coordinate execution
- Delegate work to analytics
- Delegate work to intelligence
- Delegate work to decision layer
- Build final snapshot

Contains NO business logic.

Version : 2.1
Author  : OptionForge
==============================================================
"""

from __future__ import annotations

from typing import Any

from optionforge.pipeline.pipeline_context import PipelineContext


class OptionForgePipeline:
    """
    Main orchestration pipeline.

    This class coordinates the complete OptionForge workflow.
    It never performs calculations itself.
    """

    def __init__(
        self,
        *,
        loader: Any,
        analytics: dict[str, Any],
    ) -> None:

        self.loader = loader
        self.analytics_engines = analytics

        self._context = PipelineContext()

    # ==========================================================
    # Stage 1
    # ==========================================================

    def load(
        self,
        *,
        option_file: str,
        future_file: str,
        spot_file: str,
    ):
        """
        Load all required market datasets.
        """

        self._context.market_data = {

            "option": self.loader.load_option(option_file),

            "future": self.loader.load_future(future_file),

            "spot": self.loader.load_spot(spot_file),

        }

        return self._context.market_data

    # ==========================================================
    # Stage 2
    # ==========================================================

    def analytics(self) -> None:
        """
        Register analytics engines.

        Analytics execution will be integrated
        incrementally in future sprints.
        """

        self._context.analytics = {

            "volatility": {},

            "greeks": {},

            "oi": {},

            "market": {},

            "registry": self.analytics_engines,

        }

    # ==========================================================
    # Stage 3
    # ==========================================================

    def intelligence(self) -> None:
        """
        Execute intelligence layer.
        """
        pass

    # ==========================================================
    # Stage 4
    # ==========================================================

    def decision(self) -> None:
        """
        Execute institutional decision layer.
        """
        pass

    # ==========================================================
    # Stage 5
    # ==========================================================

    def snapshot(self):
        """
        Return the final Institutional Snapshot.
        """

        return self._context.snapshot

    # ==========================================================
    # Complete Pipeline
    # ==========================================================

    def run(
        self,
        *,
        option_file: str,
        future_file: str,
        spot_file: str,
    ):

        self.load(
            option_file=option_file,
            future_file=future_file,
            spot_file=spot_file,
        )

        self.analytics()

        self.intelligence()

        self.decision()

        return self.snapshot()