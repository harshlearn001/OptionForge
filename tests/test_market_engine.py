"""
==============================================================
OptionForge
Test
Market Engine
==============================================================
"""

from optionforge.intelligence.market_engine import MarketEngine

from optionforge.models import (
    MarketStructureResult,
    ProbabilityResult,
)


def main():

    # ======================================================
    # Market Structure Result
    # ======================================================

    market = MarketStructureResult(

        score=88.0,

        bias="STRONGLY BULLISH",

        confidence="HIGH",

        stars=4,

        recommendation="Buying dips is preferred.",

        support_strength=82.0,

        resistance_strength=74.0,

        expected_move=1.60,

        iv_rank=42.0,

        iv_percentile=48.0,

        max_pain=25000.0,

        interpretation="Bullish market structure.",

    )

    # ======================================================
    # Probability Result
    # ======================================================

    probability = ProbabilityResult(

        bullish_probability=88.0,

        bearish_probability=12.0,

        confidence="HIGH",

        stars=4,

        trade_quality="A",

        risk_level="LOW",

        recommendation="Bullish setup.",

        interpretation="Bullish probability is high.",

    )

    # ======================================================
    # Engine
    # ======================================================

    intelligence = MarketEngine.evaluate(

        market_structure=market,

        probability=probability,

    )

    # ======================================================
    # Output
    # ======================================================

    print()

    print("=" * 60)
    print("MARKET ENGINE")
    print("=" * 60)

    print(intelligence)

    print("=" * 60)

    # ======================================================
    # Assertions
    # ======================================================

    assert intelligence.state.name == "BULLISH_TREND"

    assert intelligence.confidence == 90.0

    print("\nPASS : Market Engine Test Successful")


if __name__ == "__main__":
    main()