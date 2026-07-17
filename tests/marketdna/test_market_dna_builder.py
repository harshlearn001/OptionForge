"""
============================================================
OptionForge
Market DNA Builder Tests
============================================================
"""

from optionforge.evidence.evidence import Evidence
from optionforge.evidence.evidence_direction import (
    EvidenceDirection,
)
from optionforge.evidence.evidence_level import (
    EvidenceLevel,
)
from optionforge.evidence.evidence_registry import (
    EvidenceRegistry,
)
from optionforge.evidence.evidence_source import (
    EvidenceSource,
)

from optionforge.marketdna.liquidity_regime import (
    LiquidityRegime,
)
from optionforge.marketdna.market_dna import (
    MarketDNA,
)
from optionforge.marketdna.market_dna_builder import (
    MarketDNABuilder,
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


# ==========================================================
# Helpers
# ==========================================================


def registry() -> EvidenceRegistry:

    r = EvidenceRegistry()

    r.add(
        Evidence(
            id="dealer_long_gamma",
            title="Dealer Long Gamma",
            source=EvidenceSource.DEALER_GAMMA,
            direction=EvidenceDirection.BULLISH,
            level=EvidenceLevel.VERY_STRONG,
            score=90.0,
            confidence=0.95,
            description=(
                "Dealers are positioned long gamma. "
                "Hedging flows are expected to reduce market volatility."
            ),
        )
    )

    r.add(
        Evidence(
            id="iv_rank",
            title="IV Rank",
            source=EvidenceSource.IV_RANK,
            direction=EvidenceDirection.NEUTRAL,
            level=EvidenceLevel.STRONG,
            score=82.0,
            confidence=0.88,
            description=(
                "IV Rank is elevated, indicating relatively expensive "
                "implied volatility."
            ),
        )
    )

    return r


# ==========================================================
# Result
# ==========================================================


def test_returns_market_dna():

    dna = MarketDNABuilder().build(
        registry(),
    )

    assert isinstance(
        dna,
        MarketDNA,
    )


# ==========================================================
# Dealer
# ==========================================================


def test_dealer_position():

    dna = MarketDNABuilder().build(
        registry(),
    )

    assert dna.dealer_position == "Dealer Long Gamma"


# ==========================================================
# Market Regime
# ==========================================================


def test_market_regime():

    dna = MarketDNABuilder().build(
        registry(),
    )

    assert dna.regime == MarketRegime.STRONGLY_BULLISH


# ==========================================================
# Trend
# ==========================================================


def test_trend():

    dna = MarketDNABuilder().build(
        registry(),
    )

    assert dna.trend == TrendRegime.STRONG_UPTREND


# ==========================================================
# Volatility
# ==========================================================


def test_volatility():

    dna = MarketDNABuilder().build(
        registry(),
    )

    assert dna.volatility == VolatilityRegime.EXPANDING


# ==========================================================
# Liquidity
# ==========================================================


def test_liquidity():

    dna = MarketDNABuilder().build(
        registry(),
    )

    assert dna.liquidity == LiquidityRegime.HIGH


# ==========================================================
# Score
# ==========================================================


def test_evidence_score():

    dna = MarketDNABuilder().build(
        registry(),
    )

    assert dna.evidence_score == 172.0


# ==========================================================
# Confidence
# ==========================================================


def test_confidence():

    dna = MarketDNABuilder().build(
        registry(),
    )

    assert dna.confidence == 0.915


# ==========================================================
# Empty Registry
# ==========================================================


def test_empty_registry():

    dna = MarketDNABuilder().build(
        EvidenceRegistry(),
    )

    assert dna.regime == MarketRegime.NEUTRAL

    assert dna.dealer_position == "UNKNOWN"


# ==========================================================
# Deterministic
# ==========================================================


def test_builder_is_deterministic():

    first = MarketDNABuilder().build(
        registry(),
    )

    second = MarketDNABuilder().build(
        registry(),
    )

    assert first == second