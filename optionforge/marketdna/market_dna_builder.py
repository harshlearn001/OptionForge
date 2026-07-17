"""
============================================================
OptionForge
Market DNA Builder
============================================================

Author      : OptionForge
Module      : market_dna_builder.py

Purpose
-------
Converts an EvidenceRegistry into a single immutable
MarketDNA object.

This is the ONLY component responsible for producing
MarketDNA.
============================================================
"""

from __future__ import annotations

from optionforge.evidence.evidence_registry import EvidenceRegistry
from optionforge.evidence.evidence_source import EvidenceSource

from optionforge.marketdna.liquidity_regime import LiquidityRegime
from optionforge.marketdna.market_dna import MarketDNA
from optionforge.marketdna.market_regime import MarketRegime
from optionforge.marketdna.trend_regime import TrendRegime
from optionforge.marketdna.volatility_regime import VolatilityRegime


class MarketDNABuilder:
    """
    Builds immutable MarketDNA.
    """

    def build(
        self,
        registry: EvidenceRegistry,
    ) -> MarketDNA:

        dealer = self._dealer_position(registry)

        regime = self._market_regime(registry)

        trend = self._trend(registry)

        volatility = self._volatility(registry)

        liquidity = self._liquidity(registry)

        return MarketDNA(
            regime=regime,
            trend=trend,
            volatility=volatility,
            liquidity=liquidity,
            dealer_position=dealer,
            evidence_score=registry.score,
            confidence=registry.confidence,
        )

    # --------------------------------------------------

    @staticmethod
    def _dealer_position(
        registry: EvidenceRegistry,
    ) -> str:

        dealer = registry.by_source(
            EvidenceSource.DEALER_GAMMA,
        )

        if not dealer:
            return "UNKNOWN"

        return dealer[0].title

    # --------------------------------------------------

    @staticmethod
    def _market_regime(
        registry: EvidenceRegistry,
    ) -> MarketRegime:

        score = registry.score

        if score >= 80:
            return MarketRegime.STRONGLY_BULLISH

        if score >= 60:
            return MarketRegime.BULLISH

        if score <= -80:
            return MarketRegime.STRONGLY_BEARISH

        if score <= -60:
            return MarketRegime.BEARISH

        return MarketRegime.NEUTRAL

    # --------------------------------------------------

    @staticmethod
    def _trend(
        registry: EvidenceRegistry,
    ) -> TrendRegime:

        score = registry.score

        if score >= 80:
            return TrendRegime.STRONG_UPTREND

        if score >= 60:
            return TrendRegime.UPTREND

        if score >= 30:
            return TrendRegime.WEAK_UPTREND

        if score <= -80:
            return TrendRegime.STRONG_DOWNTREND

        if score <= -60:
            return TrendRegime.DOWNTREND

        if score <= -30:
            return TrendRegime.WEAK_DOWNTREND

        return TrendRegime.SIDEWAYS

    # --------------------------------------------------

    @staticmethod
    def _volatility(
        registry: EvidenceRegistry,
    ) -> VolatilityRegime:

        volatility = registry.by_source(
            EvidenceSource.IV_RANK,
        )

        if not volatility:
            return VolatilityRegime.NORMAL

        score = volatility[0].score

        if score >= 90:
            return VolatilityRegime.EXTREME

        if score >= 75:
            return VolatilityRegime.EXPANDING

        if score >= 60:
            return VolatilityRegime.HIGH

        if score <= 10:
            return VolatilityRegime.EXTREMELY_COMPRESSED

        if score <= 25:
            return VolatilityRegime.COMPRESSED

        if score <= 40:
            return VolatilityRegime.LOW

        return VolatilityRegime.NORMAL

    # --------------------------------------------------

    @staticmethod
    def _liquidity(
        registry: EvidenceRegistry,
    ) -> LiquidityRegime:

        confidence = registry.confidence

        if confidence >= 0.95:
            return LiquidityRegime.EXTREMELY_HIGH

        if confidence >= 0.85:
            return LiquidityRegime.HIGH

        if confidence >= 0.70:
            return LiquidityRegime.ABOVE_AVERAGE

        if confidence >= 0.50:
            return LiquidityRegime.NORMAL

        if confidence >= 0.35:
            return LiquidityRegime.BELOW_AVERAGE

        if confidence >= 0.20:
            return LiquidityRegime.LOW

        return LiquidityRegime.EXTREMELY_LOW