"""
==============================================================
OptionForge
Institutional Intelligence Engine
--------------------------------------------------------------

Combines all institutional analytics into one final
InstitutionalResult.

==============================================================
"""

from __future__ import annotations

from optionforge.intelligence.confidence_classifier import (
    ConfidenceClassifier,
)
from optionforge.intelligence.institutional_bias_classifier import (
    InstitutionalBiasClassifier,
)
from optionforge.intelligence.institutional_result import (
    InstitutionalResult,
)
from optionforge.intelligence.institutional_score import (
    InstitutionalScore,
)


class InstitutionalEngine:
    """
    Institutional Intelligence Engine.
    """

    def __init__(
        self,
        *,
        summary: float,
        change: float,
        buildup: float,
        wall: float,
        concentration: float,
        shift: float,
        trend: float,
    ) -> None:

        self.summary = summary
        self.change = change
        self.buildup = buildup
        self.wall = wall
        self.concentration = concentration
        self.shift = shift
        self.trend = trend

    # ==========================================================
    # Calculate
    # ==========================================================

    def calculate(
        self,
    ) -> InstitutionalResult:

        score = InstitutionalScore(

            summary=self.summary,

            change=self.change,

            buildup=self.buildup,

            wall=self.wall,

            concentration=self.concentration,

            shift=self.shift,

            trend=self.trend,

        ).calculate()

        confidence = ConfidenceClassifier.classify(score)

        bias = InstitutionalBiasClassifier.classify(score)

        return InstitutionalResult(

            score=score,

            confidence=confidence,

            bias=bias,

        )

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self) -> str:

        return (
            "InstitutionalEngine("
            f"summary={self.summary}, "
            f"change={self.change}, "
            f"buildup={self.buildup}, "
            f"wall={self.wall}, "
            f"concentration={self.concentration}, "
            f"shift={self.shift}, "
            f"trend={self.trend})"
        )