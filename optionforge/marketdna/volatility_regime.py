"""
============================================================
OptionForge
Volatility Regime
============================================================

Author      : OptionForge
Module      : volatility_regime.py
Purpose     : Defines the institutional volatility regime.

The VolatilityRegime represents the current volatility
environment after evaluating IV Rank, IV Percentile,
Expected Move and related evidence.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class VolatilityRegime(Enum):
    """
    Institutional volatility regime.
    """

    # -----------------------------------------------------
    # Low Volatility
    # -----------------------------------------------------

    EXTREMELY_COMPRESSED = auto()

    COMPRESSED = auto()

    LOW = auto()

    # -----------------------------------------------------
    # Normal
    # -----------------------------------------------------

    NORMAL = auto()

    # -----------------------------------------------------
    # High Volatility
    # -----------------------------------------------------

    HIGH = auto()

    EXPANDING = auto()

    EXTREME = auto()

    @property
    def is_low(self) -> bool:
        """
        Returns True for low volatility regimes.
        """

        return self in (
            VolatilityRegime.EXTREMELY_COMPRESSED,
            VolatilityRegime.COMPRESSED,
            VolatilityRegime.LOW,
        )

    @property
    def is_high(self) -> bool:
        """
        Returns True for elevated volatility regimes.
        """

        return self in (
            VolatilityRegime.HIGH,
            VolatilityRegime.EXPANDING,
            VolatilityRegime.EXTREME,
        )

    @property
    def is_normal(self) -> bool:
        """
        Returns True for normal volatility.
        """

        return self is VolatilityRegime.NORMAL

    @property
    def is_expanding(self) -> bool:
        """
        Returns True when volatility is expanding.
        """

        return self in (
            VolatilityRegime.EXPANDING,
            VolatilityRegime.EXTREME,
        )

    @property
    def is_compressed(self) -> bool:
        """
        Returns True when volatility is compressed.
        """

        return self in (
            VolatilityRegime.EXTREMELY_COMPRESSED,
            VolatilityRegime.COMPRESSED,
        )

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return self.name.replace("_", " ").title()
