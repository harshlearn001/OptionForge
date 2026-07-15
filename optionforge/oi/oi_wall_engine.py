"""
==============================================================
OptionForge
OI Wall Engine
--------------------------------------------------------------
Institutional OI Wall Analytics Engine.

Consumes the canonical OIByStrike table and classifies
each strike as a Call Wall, Put Wall, or Balanced.

Returns an immutable OIWallResult.
==============================================================
"""

from __future__ import annotations

from optionforge.oi.oi_by_strike import OIByStrike
from optionforge.oi.wall_classifier import WallClassifier
from optionforge.oi.oi_wall_result import OIWallResult


class OIWallEngine:
    """
    Institutional OI Wall Engine.
    """

    def __init__(
        self,
        oi: OIByStrike,
    ):

        self.oi = oi

    # ==========================================================
    # Calculate
    # ==========================================================

    def calculate(
        self,
    ) -> OIWallResult:
        """
        Calculate wall classifications.
        """

        df = self.oi.dataframe()

        df["WALL"] = df.apply(
            lambda row: WallClassifier.classify(
                call_share=row["CALL_SHARE"],
                put_share=row["PUT_SHARE"],
            ).value,
            axis=1,
        )

        return OIWallResult(df)

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self) -> str:

        return (
            "OIWallEngine("
            f"rows={len(self.oi.dataframe())})"
        )