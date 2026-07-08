"""
============================================================
OptionForge
Institutional Metadata
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(
    frozen=True,
    slots=True,
)
class InstitutionalMetadata:
    """
    Metadata describing a snapshot.
    """

    version: str = "2.0.0"

    pipeline_version: str = "3.0"

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    build_time_ms: float = 0.0