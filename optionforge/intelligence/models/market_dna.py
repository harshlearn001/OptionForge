"""
============================================================
OptionForge
MarketDNA
============================================================

Author      : OptionForge
Module      : market_dna.py

Purpose
-------
Immutable representation of the market after all
analytics and evidence have been computed.

MarketDNA is the single source of truth consumed by:

    • Decision Engine
    • Strategy Engine
    • Dashboard
    • Reports
    • Research
    • Backtesting
    • API

This class contains NO business logic.
It is a domain model only.
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Mapping

from optionforge.evidence.evidence_registry import EvidenceRegistry
from optionforge.features.registry import FeatureRegistry


# ==========================================================
# ENUMS
# ==========================================================

class MarketState(str, Enum):
    UNKNOWN = "Unknown"

    ACCUMULATION = "Accumulation"
    DISTRIBUTION = "Distribution"

    MARKUP = "Markup"
    MARKDOWN = "Markdown"

    CONSOLIDATION = "Consolidation"

    BREAKOUT = "Breakout"
    BREAKDOWN = "Breakdown"


class Trend(str, Enum):
    BULLISH = "Bullish"
    BEARISH = "Bearish"
    SIDEWAYS = "Sideways"


class DealerState(str, Enum):
    LONG_GAMMA = "Long Gamma"
    SHORT_GAMMA = "Short Gamma"
    NEUTRAL = "Neutral"


class InstitutionalState(str, Enum):
    BUYING = "Buying"
    SELLING = "Selling"
    NEUTRAL = "Neutral"


class VolatilityState(str, Enum):
    LOW = "Low"

    NORMAL = "Normal"

    HIGH = "High"

    EXTREME = "Extreme"


class RiskState(str, Enum):
    LOW = "Low"

    MEDIUM = "Medium"

    HIGH = "High"


# ==========================================================
# MARKET DNA
# ==========================================================

@dataclass(frozen=True, slots=True)
class MarketDNA:
    """
    Complete interpretation of the market.

    This object should be created exactly once for every
    InstitutionalSnapshot.
    """

    # ------------------------------------------------------
    # Identity
    # ------------------------------------------------------

    symbol: str

    expiry: str

    timestamp: datetime

    spot_price: float

    # ------------------------------------------------------
    # Market Classification
    # ------------------------------------------------------

    market_state: MarketState

    trend: Trend

    dealer_state: DealerState

    institutional_state: InstitutionalState

    volatility_state: VolatilityState

    risk_state: RiskState

    # ------------------------------------------------------
    # Intelligence
    # ------------------------------------------------------

    confidence: float

    expected_move: float

    strategy: str

    # ------------------------------------------------------
    # Registries
    # ------------------------------------------------------

    features: FeatureRegistry

    evidence: EvidenceRegistry

    # ------------------------------------------------------
    # Human Explanation
    # ------------------------------------------------------

    summary: str

    reasons: tuple[str, ...] = ()

    warnings: tuple[str, ...] = ()

    metadata: Mapping[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------
    # Helpers
    # ------------------------------------------------------

    @property
    def confidence_ratio(self) -> float:
        return self.confidence / 100.0

    @property
    def bullish(self) -> bool:
        return self.trend == Trend.BULLISH

    @property
    def bearish(self) -> bool:
        return self.trend == Trend.BEARISH

    @property
    def neutral(self) -> bool:
        return self.trend == Trend.SIDEWAYS

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize MarketDNA.
        """

        return {
            "symbol": self.symbol,
            "expiry": self.expiry,
            "timestamp": self.timestamp.isoformat(),
            "spot_price": self.spot_price,

            "market_state": self.market_state.value,
            "trend": self.trend.value,
            "dealer_state": self.dealer_state.value,
            "institutional_state": self.institutional_state.value,
            "volatility_state": self.volatility_state.value,
            "risk_state": self.risk_state.value,

            "confidence": self.confidence,
            "expected_move": self.expected_move,
            "strategy": self.strategy,

            "summary": self.summary,

            "reasons": list(self.reasons),
            "warnings": list(self.warnings),

            "metadata": dict(self.metadata),
        }

    def __repr__(self) -> str:

        return (
            f"MarketDNA("
            f"symbol='{self.symbol}', "
            f"trend='{self.trend.value}', "
            f"confidence={self.confidence:.1f}%, "
            f"market_state='{self.market_state.value}')"
        )