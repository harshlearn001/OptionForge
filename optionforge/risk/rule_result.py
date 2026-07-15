"""
============================================================
OptionForge
Rule Result
============================================================

Author      : OptionForge
Module      : rule_result.py

Purpose
-------
Immutable result produced by an institutional risk rule.

Every risk rule returns a RuleResult instead of a raw
tuple, providing a richer and extensible API.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(
    frozen=True,
    slots=True,
)
class RuleResult:
    """
    Immutable risk rule result.
    """

    # =====================================================
    # Core
    # =====================================================

    rule_name: str

    score: float

    passed: bool

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
    # Validation
    # =====================================================

    def __post_init__(
        self,
    ) -> None:
        """
        Validate RuleResult.
        """

        if not (0.0 <= self.score <= 100.0):

            raise ValueError("score must be between 0 and 100.")

    # =====================================================
    # Convenience
    # =====================================================

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

        return {
            "rule_name": self.rule_name,
            "score": self.score,
            "passed": self.passed,
            "warnings": list(
                self.warnings,
            ),
            "reasons": list(
                self.reasons,
            ),
        }

    # =====================================================
    # Representation
    # =====================================================

    def __str__(
        self,
    ) -> str:

        return f"{self.rule_name}(" f"passed={self.passed}, " f"score={self.score:.1f})"

    def __repr__(
        self,
    ) -> str:

        return (
            f"RuleResult("
            f"rule_name={self.rule_name!r}, "
            f"score={self.score}, "
            f"passed={self.passed})"
        )
