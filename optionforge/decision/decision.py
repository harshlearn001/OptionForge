"""
============================================================
OptionForge
Decision
============================================================

Author      : OptionForge
Module      : decision.py
Purpose     : Immutable institutional trading decision.

Decision is the final reasoning object produced by the
DecisionBuilder.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, Mapping

from optionforge.decision.confidence_level import (
    ConfidenceLevel,
)
from optionforge.decision.decision_type import (
    DecisionType,
)
from optionforge.decision.strategy_type import (
    StrategyType,
)
from optionforge.marketdna.market_dna import (
    MarketDNA,
)


@dataclass(
    frozen=True,
    slots=True,
)
class Decision:
    """
    Immutable institutional trading decision.
    """

    # -----------------------------------------------------
    # Core Decision
    # -----------------------------------------------------

    decision: DecisionType

    strategy: StrategyType

    confidence_level: ConfidenceLevel

    # -----------------------------------------------------
    # Numerical Confidence
    # -----------------------------------------------------

    confidence: float

    # -----------------------------------------------------
    # Supporting Context
    # -----------------------------------------------------

    market_dna: MarketDNA

    recommendation: str

    rationale: tuple[str, ...] = ()

    # -----------------------------------------------------
    # Metadata
    # -----------------------------------------------------

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC),
        compare=False,
    )

    metadata: Mapping[str, Any] = field(
        default_factory=dict,
        compare=False,
    )

    # -----------------------------------------------------
    # Validation
    # -----------------------------------------------------

    def __post_init__(self) -> None:

        if not (0.0 <= self.confidence <= 100.0):

            raise ValueError("Confidence must be between 0 and 100.")

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def is_tradeable(self) -> bool:
        """
        Returns True if the decision is suitable
        for execution.
        """

        return self.confidence_level.is_tradeable

    @property
    def is_buy(self) -> bool:
        """
        Returns True for bullish decisions.
        """

        return self.decision.is_bullish

    @property
    def is_sell(self) -> bool:
        """
        Returns True for bearish decisions.
        """

        return self.decision.is_bearish

    @property
    def requires_confirmation(self) -> bool:
        """
        Returns True if additional confirmation
        is recommended before execution.
        """

        return self.confidence_level.requires_confirmation

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(self) -> dict[str, Any]:

        return {
            "decision": self.decision.name,
            "strategy": self.strategy.name,
            "confidence_level": self.confidence_level.name,
            "confidence": self.confidence,
            "recommendation": self.recommendation,
            "rationale": list(self.rationale),
            "market_dna": self.market_dna.to_dict(),
            "timestamp": self.timestamp.isoformat(),
            "metadata": dict(self.metadata),
        }

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(self) -> str:

        return (
            f"Decision("
            f"{self.decision.name}, "
            f"{self.strategy.name}, "
            f"{self.confidence:.1f}%)"
        )

    def __repr__(self) -> str:

        return (
            f"Decision("
            f"decision={self.decision.name}, "
            f"strategy={self.strategy.name}, "
            f"confidence={self.confidence:.1f})"
        )
