"""
============================================================
OptionForge
Engine Runner
============================================================

Executes registered engines and collects execution results.

Author      : OptionForge
Module      : engine_runner.py
Purpose     : Runtime engine orchestrator.

============================================================
"""

from __future__ import annotations

from time import perf_counter

from optionforge.kernel.engine_context import EngineContext
from optionforge.kernel.execution_result import ExecutionResult
from optionforge.kernel.execution_status import ExecutionStatus
from optionforge.kernel.registry import Registry
from optionforge.kernel.result_collection import ResultCollection


class EngineRunner:
    """
    Executes all registered engines.
    """

    def __init__(
        self,
        registry: Registry,
    ) -> None:

        self._registry = registry

    @property
    def registry(self) -> Registry:

        return self._registry

    def execute(
        self,
        context: EngineContext,
    ) -> ResultCollection:

        results: dict[str, ExecutionResult] = {}

        for engine in self.registry:

            start = perf_counter()

            try:

                value = engine.execute(
                    context.snapshot,
                )

                status = ExecutionStatus.SUCCESS

                exception = None

            except Exception as exc:

                value = None

                status = ExecutionStatus.FAILED

                exception = exc

            duration = perf_counter() - start

            results[engine.name] = ExecutionResult(
                engine=engine.name,
                status=status,
                result=value,
                duration=duration,
                exception=exception,
            )

        return ResultCollection(results)

    def __repr__(self):

        return (
            f"EngineRunner("
            f"{len(self.registry)} engines)"
        )

    __str__ = __repr__