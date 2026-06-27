"""
OptionForge
quant/distributions.py
"""

import math


class NormalDistribution:
    """
    Standard Normal Distribution
    """

    @staticmethod
    def pdf(x: float) -> float:
        """
        Probability Density Function
        """

        return (
            math.exp(-0.5 * x * x)
            /
            math.sqrt(2.0 * math.pi)
        )

    @staticmethod
    def cdf(x: float) -> float:
        """
        Cumulative Distribution Function
        """

        return 0.5 * (
            1.0 +
            math.erf(
                x /
                math.sqrt(2.0)
            )
        )