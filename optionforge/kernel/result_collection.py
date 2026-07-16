"""
============================================================
OptionForge
Result Collection
============================================================

Immutable collection of execution results.

Author      : OptionForge
Module      : result_collection.py
Purpose     : Store runtime execution results.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator, Mapping

from optionforge.kernel.execution_result import (
    ExecutionResult,
)


@dataclass(
    frozen=True,
    slots=True,
)
class ResultCollection:
    """
    Immutable collection of execution results.
    """

    results: Mapping[str, ExecutionResult] = field(
        default_factory=dict,
    )

    def get(
        self,
        engine: str,
    ) -> ExecutionResult:

        return self.results[engine]

    def exists(
        self,
        engine: str,
    ) -> bool:

        return engine in self.results

    def names(
        self,
    ) -> tuple[str, ...]:

        return tuple(self.results.keys())

    def values(
        self,
    ):

        return self.results.values()

    def items(
        self,
    ):

        return self.results.items()

    def successful(
        self,
    ) -> tuple[ExecutionResult, ...]:

        return tuple(
            result
            for result in self.results.values()
            if result.succeeded
        )

    def failed(
        self,
    ) -> tuple[ExecutionResult, ...]:

        return tuple(
            result
            for result in self.results.values()
            if result.failed
        )

    def __contains__(
        self,
        engine: str,
    ) -> bool:

        return engine in self.results

    def __len__(
        self,
    ) -> int:

        return len(self.results)

    def __iter__(
        self,
    ) -> Iterator[ExecutionResult]:

        return iter(self.results.values())

    def __repr__(
        self,
    ) -> str:

        return (
            f"ResultCollection("
            f"{len(self.results)} executions)"
        )

    __str__ = __repr__