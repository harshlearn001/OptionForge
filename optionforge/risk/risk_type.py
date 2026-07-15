"""
============================================================
OptionForge
Risk Type
============================================================

Author      : OptionForge
Module      : risk_type.py

Purpose
-------
Institutional classification of portfolio risk.

RiskType represents the overall outcome of the
risk evaluation process.

============================================================
"""

from __future__ import annotations

from enum import Enum, auto


class RiskType(Enum):
    """
    Institutional risk classification.
    """

    # -----------------------------------------------------
    # Risk Decisions
    # -----------------------------------------------------

    APPROVED = auto()

    REVIEW = auto()

    REJECTED = auto()

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def is_approved(self) -> bool:
        """
        Portfolio is approved.
        """

        return self is RiskType.APPROVED

    @property
    def requires_review(self) -> bool:
        """
        Portfolio requires manual review.
        """

        return self is RiskType.REVIEW

    @property
    def is_rejected(self) -> bool:
        """
        Portfolio has been rejected.
        """

        return self is RiskType.REJECTED

    @classmethod
    def from_score(
        cls,
        score: float,
    ) -> "RiskType":
        """
        Convert a numerical risk score into a
        RiskType.

        Parameters
        ----------
        score
            Risk score between 0 and 100.

        Returns
        -------
        RiskType
        """

        if score <= 30:

            return cls.APPROVED

        if score <= 70:

            return cls.REVIEW

        return cls.REJECTED

    def __str__(
        self,
    ) -> str:
        """
        Human-readable representation.
        """

        return self.name.replace(
            "_",
            " ",
        ).title()
