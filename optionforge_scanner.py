"""
==============================================================
OptionForge
Professional Market Scanner
==============================================================
"""

from optionforge.intelligence import (
    MarketStructure,
    Probability,
    Strategy,
    Scanner,
)


def main():

    print("=" * 60)
    print("OPTIONFORGE")
    print("PROFESSIONAL MARKET SCANNER")
    print("=" * 60)

    symbols = [

        ("NIFTY", 96),

        ("RELIANCE", 90),

        ("ICICIBANK", 85),

        ("SBIN", 75),

        ("TCS", 60),

    ]

    results = []

    for symbol, support in symbols:

        market = MarketStructure.calculate(

            support_strength=support,

            resistance_strength=91,

            expected_move=82,

            iv_rank=42,

            iv_percentile=51,

            max_pain=88,

            oi_wall_score=90,

            oi_shift_score=84,

            oi_change_score=80,

        )

        probability = Probability.calculate(market)

        strategy = Strategy.calculate(

            probability=probability,

            spot_price=25000,

            expected_move=692,

        )

        result = Scanner.calculate(

            symbol=symbol,

            probability=probability,

            strategy=strategy,

        )

        results.append(result)

    # -------------------------------------------------
    # Ranking
    # -------------------------------------------------

    results.sort(

        key=lambda x: x.market_score,

        reverse=True,

    )

    print()

    print(f"{'Rank':<6}{'Symbol':<15}{'Score':<10}{'Action':<15}")

    print("-" * 50)

    for rank, result in enumerate(results, start=1):

        result.rank = rank

        print(

            f"{rank:<6}"

            f"{result.symbol:<15}"

            f"{result.market_score:<10.2f}"

            f"{result.action:<15}"

        )

    print()

    print("=" * 60)
    print("SCAN COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()