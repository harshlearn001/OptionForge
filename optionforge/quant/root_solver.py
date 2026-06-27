"""
==============================================================
OptionForge
quant/root_solver.py
--------------------------------------------------------------
Generic Numerical Root Solvers
==============================================================
"""

from typing import Callable


class RootSolver:
    """
    Generic Root Solver
    """

    @staticmethod
    def bisection(
        func: Callable[[float], float],
        lower: float,
        upper: float,
        tolerance: float = 1e-8,
        max_iterations: int = 100,
    ) -> float:
        """
        Solve f(x)=0 using the Bisection Method.
        """

        f_lower = func(lower)
        f_upper = func(upper)

        if f_lower * f_upper > 0:
            raise ValueError(
                "Root is not bracketed. "
                "f(lower) and f(upper) must have opposite signs."
            )

        for _ in range(max_iterations):

            midpoint = (lower + upper) / 2.0

            f_mid = func(midpoint)

            if abs(f_mid) < tolerance:
                return midpoint

            if f_lower * f_mid < 0:
                upper = midpoint
                f_upper = f_mid
            else:
                lower = midpoint
                f_lower = f_mid

        return (lower + upper) / 2.0