"""
==============================================================
OptionForge
Pipeline
Pipeline Context
==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class PipelineContext:
    """
    Shared state passed between pipeline stages.
    """

    # Raw loaded data
    market_data: Any | None = None

    # Analytics results
    analytics: dict[str, Any] = field(default_factory=dict)

    # Intelligence results
    intelligence: dict[str, Any] = field(default_factory=dict)

    # Institutional decision
    decision: Any | None = None

    # Final snapshot
    snapshot: Any | None = None