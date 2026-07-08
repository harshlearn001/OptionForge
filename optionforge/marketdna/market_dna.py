"""
============================================================
OptionForge
Market DNA
============================================================

Author      : OptionForge
Module      : market_dna.py
Purpose     : Immutable institutional market state.

MarketDNA is the final output of the MarketDNABuilder.

It represents the current identity of the market after
evaluating all institutional evidence.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, Mapping

from optionforge.marketdna.liquidity_regime import (
    LiquidityRegime,
)
from optionforge.marketdna.market_regime import (
    MarketRegime,
)
from optionforge.marketdna.trend_regime import (
    TrendRegime,
)
from optionforge.marketdna.volatility_regime import (
    VolatilityRegime,
)


@dataclass(
    frozen=True,
    slots=True,
)
class MarketDNA:
    """
    Immutable institutional market description.
    """

    # -----------------------------------------------------
    # Regimes
    # -----------------------------------------------------

    regime: MarketRegime

    trend: TrendRegime

    volatility: VolatilityRegime

    liquidity: LiquidityRegime

    # -----------------------------------------------------
    # Dealer
    # -----------------------------------------------------

    dealer_position: str

    # -----------------------------------------------------
    # Quantitative Summary
    # -----------------------------------------------------

    evidence_score: float

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

    # -----------------------------------------------------
    # Convenience
    # -----------------------------------------------------

    @property
    def is_bullish(self) -> bool:

        return self.regime.is_bullish

    @property
    def is_bearish(self) -> bool:

        return self.regime.is_bearish

    @property
    def is_neutral(self) -> bool:

        return self.regime.is_neutral

    @property
    def is_high_liquidity(self) -> bool:

        return self.liquidity.is_high

    @property
    def is_low_liquidity(self) -> bool:

        return self.liquidity.is_low

    @property
    def is_high_volatility(self) -> bool:

        return self.volatility.is_high

    @property
    def is_low_volatility(self) -> bool:

        return self.volatility.is_low

    @property
    def trend_strength(self) -> int:

        return self.trend.strength

    @property
    def liquidity_score(self) -> int:

        return self.liquidity.score

    # -----------------------------------------------------
    # Serialization
    # -----------------------------------------------------

    def to_dict(self) -> dict[str, Any]:

        return {

            "regime": self.regime.name,

            "trend": self.trend.name,

            "volatility": self.volatility.name,

            "liquidity": self.liquidity.name,

            "dealer_position": self.dealer_position,

            "evidence_score": self.evidence_score,

            "confidence": self.confidence,

            "timestamp": self.timestamp.isoformat(),

            "metadata": dict(self.metadata),

        }

    # -----------------------------------------------------
    # Representation
    # -----------------------------------------------------

    def __str__(self) -> str:

        return (

            f"MarketDNA("

            f"{self.regime.name}, "

            f"{self.trend.name}, "

            f"{self.volatility.name}, "

            f"confidence={self.confidence:.1f}%)"

        )

    def __repr__(self) -> str:

        return (

            f"MarketDNA("

            f"regime={self.regime.name}, "

            f"trend={self.trend.name}, "

            f"volatility={self.volatility.name}, "

            f"liquidity={self.liquidity.name})"

        )