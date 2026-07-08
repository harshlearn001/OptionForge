"""
============================================================
OptionForge
Liquidity Regime
============================================================

Author      : OptionForge
Module      : liquidity_regime.py
Purpose     : Defines the institutional liquidity regime.

Liquidity represents how easily large institutional
orders can be absorbed by the market.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class LiquidityRegime(Enum):
    """
    Institutional liquidity classification.
    """

    # -----------------------------------------------------
    # High Liquidity
    # -----------------------------------------------------

    EXTREMELY_HIGH = auto()

    HIGH = auto()

    ABOVE_AVERAGE = auto()

    # -----------------------------------------------------
    # Normal
    # -----------------------------------------------------

    NORMAL = auto()

    # -----------------------------------------------------
    # Low Liquidity
    # -----------------------------------------------------

    BELOW_AVERAGE = auto()

    LOW = auto()

    EXTREMELY_LOW = auto()

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def is_high(self) -> bool:
        """
        Returns True for high-liquidity regimes.
        """

        return self in (
            LiquidityRegime.EXTREMELY_HIGH,
            LiquidityRegime.HIGH,
            LiquidityRegime.ABOVE_AVERAGE,
        )

    @property
    def is_low(self) -> bool:
        """
        Returns True for low-liquidity regimes.
        """

        return self in (
            LiquidityRegime.BELOW_AVERAGE,
            LiquidityRegime.LOW,
            LiquidityRegime.EXTREMELY_LOW,
        )

    @property
    def is_normal(self) -> bool:
        """
        Returns True for normal liquidity.
        """

        return self is LiquidityRegime.NORMAL

    @property
    def score(self) -> int:
        """
        Numerical liquidity score.
        """

        return {
            LiquidityRegime.EXTREMELY_LOW: -3,
            LiquidityRegime.LOW: -2,
            LiquidityRegime.BELOW_AVERAGE: -1,
            LiquidityRegime.NORMAL: 0,
            LiquidityRegime.ABOVE_AVERAGE: 1,
            LiquidityRegime.HIGH: 2,
            LiquidityRegime.EXTREMELY_HIGH: 3,
        }[self]

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return self.name.replace("_", " ").title()