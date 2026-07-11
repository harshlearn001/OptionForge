"""
============================================================
OptionForge
Risk Builder
============================================================

Author      : OptionForge
Module      : risk_builder.py

Purpose
-------
Builds the final immutable Risk object from a
RiskResult.

============================================================
"""

from __future__ import annotations

from optionforge.risk.risk import Risk
from optionforge.risk.risk_level import RiskLevel
from optionforge.risk.risk_result import RiskResult
from optionforge.risk.risk_type import RiskType


class RiskBuilder:
    """
    Builds the final institutional Risk object.
    """

    def build(
        self,
        *,
        result: RiskResult,
    ) -> Risk:

        score = result.overall_score

        # -------------------------------------------------
        # Risk Level
        # -------------------------------------------------

        risk_level = RiskLevel.from_score(

            round(score),

        )

        # -------------------------------------------------
        # Approval
        # -------------------------------------------------

        approved = result.passed

        # -------------------------------------------------
        # Risk Type
        # -------------------------------------------------

        if approved:

            risk_type = RiskType.APPROVED

        elif score >= 80.0:

            risk_type = RiskType.REJECTED

        else:

            risk_type = RiskType.REVIEW

        # -------------------------------------------------
        # Institutional Recommendations
        # -------------------------------------------------

        recommended_position_size = max(

            0.0,

            100.0 - score,

        )

        max_capital_allocation = max(

            0.0,

            100.0 - score,

        )

        return Risk(

            risk_score=score,

            risk_level=risk_level,

            risk_type=risk_type,

            approved=approved,

            warnings=result.warnings,

            reasons=result.reasons,

            recommended_position_size=(
                recommended_position_size
            ),

            max_capital_allocation=(
                max_capital_allocation
            ),

        )