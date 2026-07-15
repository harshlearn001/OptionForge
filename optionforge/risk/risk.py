"""
============================================================
OptionForge
Risk
============================================================

Author      : OptionForge
Module      : risk.py

Purpose
-------
Immutable institutional risk assessment.

Risk represents the final outcome of the complete
risk evaluation process.

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field

from optionforge.risk.risk_level import (
    RiskLevel,
)
from optionforge.risk.risk_type import (
    RiskType,
)


@dataclass(
    frozen=True,
    slots=True,
)
class Risk:
    """
    Immutable institutional risk assessment.
    """

    # =====================================================
    # Core
    # =====================================================

    risk_score: float

    risk_level: RiskLevel

    risk_type: RiskType

    approved: bool

    # =====================================================
    # Diagnostics
    # =====================================================

    warnings: tuple[str, ...] = field(
        default_factory=tuple,
    )

    reasons: tuple[str, ...] = field(
        default_factory=tuple,
    )

    # =====================================================
    # Recommendation
    # =====================================================

    recommended_position_size: float = 0.0

    max_capital_allocation: float = 0.0

    # =====================================================
    # Validation
    # =====================================================

    def __post_init__(
        self,
    ) -> None:
        """
        Validate immutable Risk object.
        """

        if not (0.0 <= self.risk_score <= 100.0):

            raise ValueError("risk_score must be between 0 and 100.")

        if not (0.0 <= self.recommended_position_size <= 100.0):

            raise ValueError("recommended_position_size must be between 0 and 100.")

        if not (0.0 <= self.max_capital_allocation <= 100.0):

            raise ValueError("max_capital_allocation must be between 0 and 100.")

    # =====================================================
    # Convenience
    # =====================================================

    @property
    def requires_review(
        self,
    ) -> bool:

        return self.risk_type.requires_review

    @property
    def is_rejected(
        self,
    ) -> bool:

        return self.risk_type.is_rejected

    @property
    def is_safe(
        self,
    ) -> bool:

        return self.risk_level.is_safe

    @property
    def warning_count(
        self,
    ) -> int:

        return len(
            self.warnings,
        )

    @property
    def reason_count(
        self,
    ) -> int:

        return len(
            self.reasons,
        )

        # =====================================================

    # Serialization
    # =====================================================

    def to_dict(
        self,
    ) -> dict:
        """
        Convert Risk into a serializable dictionary.
        """

        return {
            "risk_score": self.risk_score,
            "risk_level": self.risk_level.name,
            "risk_type": self.risk_type.name,
            "approved": self.approved,
            "warnings": list(
                self.warnings,
            ),
            "reasons": list(
                self.reasons,
            ),
            "recommended_position_size": (self.recommended_position_size),
            "max_capital_allocation": (self.max_capital_allocation),
        }

    # =====================================================
    # Representation
    # =====================================================

    def __str__(
        self,
    ) -> str:
        """
        Human-readable representation.
        """

        return (
            f"Risk("
            f"{self.risk_type.name}, "
            f"{self.risk_level.name}, "
            f"score={self.risk_score:.1f})"
        )

    def __repr__(
        self,
    ) -> str:

        return (
            f"Risk("
            f"risk_score={self.risk_score}, "
            f"risk_level={self.risk_level.name}, "
            f"risk_type={self.risk_type.name}, "
            f"approved={self.approved})"
        )
