"""
============================================================
OptionForge
Institutional Stage
============================================================
"""

from __future__ import annotations

from enum import Enum


class InstitutionalStage(str, Enum):
    """
    Pipeline completion stage.
    """

    MARKET = "MARKET"

    ANALYTICS = "ANALYTICS"

    EVIDENCE = "EVIDENCE"

    MARKET_DNA = "MARKET_DNA"

    DECISION = "DECISION"

    STRATEGY = "STRATEGY"

    EXECUTION = "EXECUTION"

    COMPLETE = "COMPLETE"
