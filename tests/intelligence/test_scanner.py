"""
==============================================================
OptionForge
tests/intelligence/test_scanner.py
--------------------------------------------------------------
Professional Market Scanner Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import (
    MarketStructure,
    Probability,
    Strategy,
    Scanner,
)

print("=" * 60)
print("OPTIONFORGE")
print("MARKET SCANNER TEST")
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

# ---------------------------------------------------------
# Ranking
# ---------------------------------------------------------

results.sort(
    key=lambda x: x.market_score,
    reverse=True,
)

for rank, result in enumerate(results, start=1):

    result.rank = rank

print()

print(f"{'Rank':<6}{'Symbol':<15}{'Score':<10}{'Action':<12}")

print("-" * 45)

for result in results:

    print(
        f"{result.rank:<6}"
        f"{result.symbol:<15}"
        f"{result.market_score:<10.2f}"
        f"{result.action:<12}"
    )

print()

print("MISSION COMPLETE")
