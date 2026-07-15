"""
============================================================
OptionForge
Risk Result
============================================================

Author      : OptionForge
Module      : risk_result.py

Purpose
-------
Immutable result produced by the Risk Engine.

RiskResult stores the outcome of every individual
risk rule before a final Risk object is built.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from optionforge.risk.rule_result import RuleResult


@dataclass(
    frozen=True,
    slots=True,
)
class RiskResult:
    """
    Immutable institutional risk evaluation.
    """

    # -----------------------------------------------------
    # Rule Results
    # -----------------------------------------------------

    rule_results: tuple[RuleResult, ...] = ()

    # -----------------------------------------------------
    # Metadata
    # -----------------------------------------------------

    metadata: Mapping[str, Any] = field(
        default_factory=dict,
        compare=False,
    )

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def rule_count(self) -> int:
        """
        Number of evaluated rules.
        """

        return len(self.rule_results)

    @property
    def overall_score(self) -> float:
        """
        Average score across all rules.
        """

        if not self.rule_results:
            return 0.0

        return sum(rule.score for rule in self.rule_results) / len(self.rule_results)

    @property
    def passed(self) -> bool:
        """
        True if every rule passed.
        """

        return all(rule.passed for rule in self.rule_results)

    @property
    def warnings(self) -> tuple[str, ...]:
        """
        Combined warnings.
        """

        return tuple(warning for rule in self.rule_results for warning in rule.warnings)

    @property
    def reasons(self) -> tuple[str, ...]:
        """
        Combined reasons.
        """

        return tuple(reason for rule in self.rule_results for reason in rule.reasons)

    @property
    def warning_count(self) -> int:

        return len(self.warnings)

    @property
    def reason_count(self) -> int:

        return len(self.reasons)

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(
        self,
    ) -> dict[str, Any]:

        return {
            "rule_results": [rule.to_dict() for rule in self.rule_results],
            "rule_count": self.rule_count,
            "overall_score": self.overall_score,
            "passed": self.passed,
            "warnings": list(self.warnings),
            "reasons": list(self.reasons),
            "metadata": dict(self.metadata),
        }

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(
        self,
    ) -> str:

        return (
            f"RiskResult("
            f"{self.rule_count} rules, "
            f"score={self.overall_score:.1f})"
        )

    def __repr__(
        self,
    ) -> str:

        return f"RiskResult(" f"rules={self.rule_count}, " f"passed={self.passed})"
