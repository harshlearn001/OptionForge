"""
==============================================================
OptionForge
Test
Volatility Engine
==============================================================
"""

from optionforge.intelligence.volatility_engine import (
    VolatilityEngine,
)

from optionforge.models import (
    IVRankResult,
    IVPercentileResult,
    ExpectedMoveResult,
)


def main():

    # ======================================================
    # Sample Analytics
    # ======================================================

    iv_rank = IVRankResult(

    current_iv=18.0,

    low_iv=12.0,

    high_iv=40.0,

    iv_rank=25.0,

    status="LOW",

    interpretation="IV Rank is relatively low.",

)

    iv_percentile = IVPercentileResult(

    current_iv=18.0,

    observations=252,

    below_count=76,

    iv_percentile=30.0,

    status="LOW",

    interpretation="IV Percentile is below average.",

)

    expected_move = ExpectedMoveResult(

    expected_move=1.80,

    upper_68=25200,

    lower_68=24800,

    upper_95=25400,

    lower_95=24600,

    one_day_move=0.80,

    weekly_move=1.80,

    monthly_move=4.20,

)

    # ======================================================
    # Engine
    # ======================================================

    intelligence = VolatilityEngine.evaluate(
        iv_rank=iv_rank,
        iv_percentile=iv_percentile,
        expected_move=expected_move,
    )

    # ======================================================
    # Output
    # ======================================================

    print()
    print("=" * 60)
    print("VOLATILITY ENGINE")
    print("=" * 60)

    print(intelligence)

    print("=" * 60)

    # ======================================================
    # Assertions
    # ======================================================

    assert intelligence.state.name == "CHEAP"

    assert intelligence.confidence == 88.0

    print("\nPASS : Volatility Engine Test Successful")


if __name__ == "__main__":
    main()