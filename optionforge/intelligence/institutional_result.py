"""
==============================================================
OptionForge
Institutional Result
--------------------------------------------------------------

Immutable institutional intelligence result.

==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, asdict

from optionforge.intelligence.enums.institutional_state import (
    InstitutionalState,
)


@dataclass(slots=True, frozen=True)
class InstitutionalResult:
    """
    Final institutional intelligence result.
    """

    score: float

    confidence: int

    bias: InstitutionalState

    # ==========================================================
    # Helpers
    # ==========================================================

    def is_bullish(self) -> bool:

        return self.bias in (
            InstitutionalState.BULLISH,
            InstitutionalState.STRONGLY_BULLISH,
        )

    def is_bearish(self) -> bool:

        return self.bias in (
            InstitutionalState.BEARISH,
            InstitutionalState.STRONGLY_BEARISH,
        )

    def is_neutral(self) -> bool:

        return self.bias is InstitutionalState.NEUTRAL

    # ==========================================================
    # Summary
    # ==========================================================

    def summary(self) -> dict:

        return {
            "score": self.score,
            "confidence": self.confidence,
            "bias": self.bias.name,
        }

    # ==========================================================
    # Dictionary
    # ==========================================================

    def to_dict(self) -> dict:

        d = asdict(self)

        d["bias"] = self.bias.name

        return d

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self) -> str:

        return (
            "InstitutionalResult("
            f"score={self.score:.4f}, "
            f"confidence={self.confidence}, "
            f"bias={self.bias.name})"
        )