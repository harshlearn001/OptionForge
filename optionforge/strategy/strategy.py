"""
============================================================
OptionForge
Strategy
============================================================

Author      : OptionForge
Module      : strategy.py
Purpose     : Immutable institutional options strategy.

Strategy is the final strategy selected by the
StrategyBuilder after evaluating a Decision.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, Mapping

from optionforge.decision.strategy_type import StrategyType


@dataclass(
    frozen=True,
    slots=True,
)
class Strategy:
    """
    Immutable institutional options strategy.
    """

    # -----------------------------------------------------
    # Identity
    # -----------------------------------------------------

    type: StrategyType

    title: str

    summary: str

    # -----------------------------------------------------
    # Classification
    # -----------------------------------------------------

    direction: str

    volatility_view: str

    market_environment: str

    # -----------------------------------------------------
    # Risk
    # -----------------------------------------------------

    max_profit: str

    max_loss: str

    probability_of_profit: float

    risk_reward: str

    # -----------------------------------------------------
    # Confidence
    # -----------------------------------------------------

    confidence: float

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
            raise ValueError(
                "Confidence must be between 0 and 100."
            )

        if not (
            0.0 <= self.probability_of_profit <= 100.0
        ):
            raise ValueError(
                "Probability of profit must be between 0 and 100."
            )

        if not self.risk_reward.strip():
            raise ValueError(
                "risk_reward cannot be empty."
            )

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def is_bullish(self) -> bool:
        """
        Returns True for bullish strategies.
        """
        return self.type.is_bullish

    @property
    def is_bearish(self) -> bool:
        """
        Returns True for bearish strategies.
        """
        return self.type.is_bearish

    @property
    def is_neutral(self) -> bool:
        """
        Returns True for neutral strategies.
        """
        return self.type.is_neutral

    @property
    def is_volatility(self) -> bool:
        """
        Returns True for volatility strategies.
        """
        return self.type.is_volatility

    @property
    def is_hedge(self) -> bool:
        """
        Returns True for hedging strategies.
        """
        return self.type.is_hedge

    @property
    def is_cash(self) -> bool:
        """
        Returns True when no position is recommended.
        """
        return self.type.is_cash

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(self) -> dict[str, Any]:

        return {

            "type": self.type.name,

            "title": self.title,

            "summary": self.summary,

            "direction": self.direction,

            "volatility_view": self.volatility_view,

            "market_environment": self.market_environment,

            "max_profit": self.max_profit,

            "max_loss": self.max_loss,

            "probability_of_profit":
                self.probability_of_profit,

            "risk_reward": self.risk_reward,

            "confidence": self.confidence,

            "timestamp":
                self.timestamp.isoformat(),

            "metadata":
                dict(self.metadata),

        }

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(self) -> str:

        return (

            f"Strategy("

            f"{self.type.name}, "

            f"{self.confidence:.1f}%)"

        )

    def __repr__(self) -> str:

        return (

            f"Strategy("

            f"type={self.type.name}, "

            f"title={self.title!r}, "

            f"confidence={self.confidence:.1f})"

        )