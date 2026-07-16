"""
============================================================
OptionForge
Engine Context
============================================================

Runtime context shared with every engine.

Author      : OptionForge
Module      : engine_context.py
Purpose     : Immutable execution context.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from optionforge.snapshot.institutional_snapshot import (
    InstitutionalSnapshot,
)


@dataclass(
    frozen=True,
    slots=True,
)
class EngineContext:
    """
    Runtime context shared by all engines.
    """

    snapshot: InstitutionalSnapshot

    configuration: Any | None = None

    services: Any | None = None

    metadata: dict[str, Any] | None = None

    @property
    def symbol(self) -> str:
        return self.snapshot.symbol

    @property
    def trade_date(self):
        return self.snapshot.trade_date

    @property
    def expiry(self):
        return self.snapshot.expiry

    def __repr__(self) -> str:

        return (
            "EngineContext("
            f"symbol='{self.symbol}', "
            f"trade_date={self.trade_date})"
        )

    __str__ = __repr__