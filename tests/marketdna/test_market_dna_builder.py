"""
============================================================
OptionForge
Market DNA Builder Tests
============================================================
"""

from optionforge.evidence.evidence import Evidence
from optionforge.evidence.evidence_level import EvidenceLevel
from optionforge.evidence.evidence_registry import EvidenceRegistry
from optionforge.evidence.evidence_type import EvidenceType

from optionforge.features.feature_id import FeatureId

from optionforge.marketdna.market_dna import MarketDNA
from optionforge.marketdna.market_dna_builder import MarketDNABuilder
from optionforge.marketdna.market_regime import MarketRegime
from optionforge.marketdna.trend_regime import TrendRegime
from optionforge.marketdna.volatility_regime import VolatilityRegime
from optionforge.marketdna.liquidity_regime import LiquidityRegime

# ==========================================================
# Helpers
# ==========================================================


def registry() -> EvidenceRegistry:

    r = EvidenceRegistry()

    r.add(
        Evidence(
            id="dealer_long_gamma",
            name="Dealer Long Gamma",
            type=EvidenceType.DEALER,
            level=EvidenceLevel.VERY_STRONG,
            score=90.0,
            confidence=95.0,
            description=(
                "Dealers are positioned long gamma. "
                "Hedging flows are expected to reduce market volatility."
            ),
            source=FeatureId.DEALER_POSITION,
        )
    )

    r.add(
        Evidence(
            id="iv_rank",
            name="IV Rank",
            type=EvidenceType.VOLATILITY,
            level=EvidenceLevel.STRONG,
            score=82.0,
            confidence=88.0,
            description=(
                "IV Rank is elevated, indicating relatively expensive implied volatility."
            ),
            source=FeatureId.IV_RANK,
        )
    )

    return r


# ==========================================================
# Result
# ==========================================================


def test_returns_market_dna():

    dna = MarketDNABuilder().build(registry())

    assert isinstance(
        dna,
        MarketDNA,
    )


# ==========================================================
# Dealer
# ==========================================================


def test_dealer_position():

    dna = MarketDNABuilder().build(registry())

    assert dna.dealer_position == "Dealer Long Gamma"


# ==========================================================
# Market Regime
# ==========================================================


def test_market_regime():

    dna = MarketDNABuilder().build(registry())

    assert dna.regime == MarketRegime.STRONGLY_BULLISH


# ==========================================================
# Trend
# ==========================================================


def test_trend():

    dna = MarketDNABuilder().build(registry())

    assert dna.trend == TrendRegime.STRONG_UPTREND


# ==========================================================
# Volatility
# ==========================================================


def test_volatility():

    dna = MarketDNABuilder().build(registry())

    assert dna.volatility == VolatilityRegime.EXPANDING


# ==========================================================
# Liquidity
# ==========================================================


def test_liquidity():

    dna = MarketDNABuilder().build(registry())

    assert dna.liquidity == LiquidityRegime.HIGH


# ==========================================================
# Score
# ==========================================================


def test_evidence_score():

    dna = MarketDNABuilder().build(registry())

    assert dna.evidence_score == 172.0


# ==========================================================
# Confidence
# ==========================================================


def test_confidence():

    dna = MarketDNABuilder().build(registry())

    assert dna.confidence == 91.5


# ==========================================================
# Empty Registry
# ==========================================================


def test_empty_registry():

    dna = MarketDNABuilder().build(EvidenceRegistry())

    assert dna.regime == MarketRegime.NEUTRAL

    assert dna.dealer_position == "UNKNOWN"


# ==========================================================
# Deterministic
# ==========================================================


def test_builder_is_deterministic():

    first = MarketDNABuilder().build(registry())

    second = MarketDNABuilder().build(registry())

    assert first == second
