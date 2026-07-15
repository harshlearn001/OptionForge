"""
============================================================
OptionForge
Kernel
Contracts
============================================================
"""

from __future__ import annotations

from typing import Protocol


class Snapshot(Protocol): ...


class Result(Protocol): ...


class Executable(Protocol):

    def execute(
        self,
        snapshot: Snapshot,
    ) -> Result: ...
