"""
==============================================================
OptionForge
Market Regime Result
==============================================================

Immutable result returned by the Market Regime Engine.

Author
------
OptionForge Engineering Team
==============================================================
"""

from __future__ import annotations

from dataclasses import asdict
from dataclasses import dataclass

from optionforge.regime.enums.regime_state import (
    RegimeState,
)


@dataclass(slots=True, frozen=True)
class RegimeResult:
    """
    Final market regime result.
    """

    regime: RegimeState

    confidence: float

    # ==========================================================
    # Helpers
    # ==========================================================

    def is_trending(self) -> bool:

        return self.regime in (

            RegimeState.UPTREND,

            RegimeState.STRONG_UPTREND,

            RegimeState.DOWNTREND,

            RegimeState.STRONG_DOWNTREND,

        )

    def is_ranging(self) -> bool:

        return self.regime is RegimeState.RANGE_BOUND

    def is_bullish(self) -> bool:

        return self.regime in (

            RegimeState.UPTREND,

            RegimeState.STRONG_UPTREND,

        )

    def is_bearish(self) -> bool:

        return self.regime in (

            RegimeState.DOWNTREND,

            RegimeState.STRONG_DOWNTREND,

        )

    def is_volatility_expansion(self) -> bool:

        return (
            self.regime
            is RegimeState.VOLATILITY_EXPANSION
        )

    def is_volatility_compression(self) -> bool:

        return (
            self.regime
            is RegimeState.VOLATILITY_COMPRESSION
        )

    # ==========================================================
    # Summary
    # ==========================================================

    def summary(self) -> dict:

        return {

            "regime": self.regime.name,

            "confidence": self.confidence,

        }

    # ==========================================================
    # Dictionary
    # ==========================================================

    def to_dict(self) -> dict:

        d = asdict(self)

        d["regime"] = self.regime.name

        return d

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self) -> str:

        return (

            "RegimeResult("

            f"regime={self.regime.name}, "

            f"confidence={self.confidence:.2f})"

        )