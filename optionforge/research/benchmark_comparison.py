"""
============================================================
OptionForge
Benchmark Comparison
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class BenchmarkComparison:
    """
    Immutable benchmark comparison summary.
    """

    benchmark_name: str

    strategy_return: float

    benchmark_return: float

    alpha: float

    tracking_error: float

    information_ratio: float

    outperformed: bool

    passed: bool

    def __post_init__(self) -> None:

        if not self.benchmark_name.strip():

            raise ValueError(
                "benchmark_name cannot be empty."
            )

        if self.tracking_error < 0:

            raise ValueError(
                "tracking_error cannot be negative."
            )

    @property
    def excess_return(self) -> float:
        """
        Strategy return minus benchmark return.
        """

        return round(

            self.strategy_return

            - self.benchmark_return,

            10,

        )

    def to_dict(self) -> dict:

        return {

            "benchmark_name":

                self.benchmark_name,

            "strategy_return":

                self.strategy_return,

            "benchmark_return":

                self.benchmark_return,

            "alpha":

                self.alpha,

            "tracking_error":

                self.tracking_error,

            "information_ratio":

                self.information_ratio,

            "excess_return":

                self.excess_return,

            "outperformed":

                self.outperformed,

            "passed":

                self.passed,

        }

    def __str__(self):

        return (

            f"BenchmarkComparison("

            f"alpha={self.alpha:.2f})"

        )

    def __repr__(self):

        return (

            f"BenchmarkComparison("

            f"benchmark='{self.benchmark_name}')"

        )