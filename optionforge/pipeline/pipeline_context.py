"""
==============================================================
OptionForge
Pipeline
Pipeline Context
==============================================================

Shared mutable state used by the OptionForge pipeline.

Contains NO business logic.

Version : 4.0
Author  : OptionForge
==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(
    slots=True,
)
class PipelineContext:
    """
    Shared state passed between pipeline stages.
    """

    # ---------------------------------------------------------
    # Snapshots
    # ---------------------------------------------------------

    market_snapshot: Any | None = None

    institutional_snapshot: Any | None = None

    # ---------------------------------------------------------
    # Analytics
    # ---------------------------------------------------------

    analytics: dict[str, Any] = field(
        default_factory=dict,
    )

    evidence: dict[str, Any] = field(
        default_factory=dict,
    )

    intelligence: dict[str, Any] = field(
        default_factory=dict,
    )

    market_dna: dict[str, Any] = field(
        default_factory=dict,
    )

    # ---------------------------------------------------------
    # Decision
    # ---------------------------------------------------------

    decision: Any | None = None

    strategy: Any | None = None

    execution: Any | None = None
