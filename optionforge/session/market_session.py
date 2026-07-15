"""
============================================================
OptionForge
Market Session
============================================================

Author      : OptionForge
Module      : market_session.py
Purpose     : Public entry point into OptionForge.

Responsibilities
----------------
- Create workflow
- Execute institutional pipeline
- Return MarketSnapshot

Contains NO business logic.

Version : 3.0
Author  : OptionForge
============================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from optionforge.workflow.workflow import WorkflowEngine


class MarketSession:
    """
    Public entry point for OptionForge.

    The session owns the WorkflowEngine and exposes
    a simple symbol-based API.
    """

    def __init__(
        self,
        *,
        marketforge_root: str | Path,
        analytics: dict[str, Any] | None = None,
    ) -> None:

        self._workflow = WorkflowEngine(
            marketforge_root=marketforge_root,
            analytics=analytics,
        )

    # ======================================================
    # Execute
    # ======================================================

    def run(
        self,
        symbol: str,
    ):
        """
        Execute the complete OptionForge workflow.

        Parameters
        ----------
        symbol
            Market symbol (e.g. NIFTY, BANKNIFTY, RELIANCE)

        Returns
        -------
        MarketSnapshot
        """

        return self._workflow.run(
            symbol,
        )
