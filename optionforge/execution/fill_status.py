"""
============================================================
OptionForge
Fill Status
============================================================

Author      : OptionForge
Module      : fill_status.py

Purpose
-------
Institutional fill status.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class FillStatus(Enum):
    """
    Institutional fill status.
    """

    PARTIAL = auto()

    COMPLETE = auto()

    CANCELLED = auto()

    REJECTED = auto()

    @property
    def is_partial(self) -> bool:

        return self is FillStatus.PARTIAL

    @property
    def is_complete(self) -> bool:

        return self is FillStatus.COMPLETE

    @property
    def is_cancelled(self) -> bool:

        return self is FillStatus.CANCELLED

    @property
    def is_rejected(self) -> bool:

        return self is FillStatus.REJECTED

    def __str__(self) -> str:

        return self.name.title()
