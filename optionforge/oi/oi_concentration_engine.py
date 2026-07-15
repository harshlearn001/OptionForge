"""
==============================================================
OptionForge
OI Concentration Engine
--------------------------------------------------------------
Institutional OI Concentration Analytics Engine.

Consumes the canonical OIByStrike table and classifies
each strike according to its OI concentration.

Returns an immutable OIConcentrationResult.
==============================================================
"""

from __future__ import annotations

from optionforge.oi.concentration_classifier import (
    ConcentrationClassifier,
)
from optionforge.oi.oi_by_strike import OIByStrike
from optionforge.oi.oi_concentration_result import (
    OIConcentrationResult,
)


class OIConcentrationEngine:
    """
    Institutional OI Concentration Engine.
    """

    def __init__(
        self,
        oi: OIByStrike,
    ) -> None:

        self.oi = oi

    # ==========================================================
    # Calculate
    # ==========================================================

    def calculate(
        self,
    ) -> OIConcentrationResult:
        """
        Calculate concentration analytics.
        """

        df = self.oi.dataframe()

        df["CONCENTRATION"] = df["OI_SHARE"].apply(
            lambda share: ConcentrationClassifier.classify(
                share,
            ).value
        )

        return OIConcentrationResult(df)

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self) -> str:

        return (
            "OIConcentrationEngine("
            f"rows={len(self.oi.dataframe())})"
        )