"""
==============================================================
OptionForge
tests/intelligence/test_probability.py
--------------------------------------------------------------
Professional Probability Engine Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import (
    MarketStructure,
    Probability,
)

print("=" * 60)
print("OPTIONFORGE")
print("PROBABILITY ENGINE TEST")
print("=" * 60)

# ---------------------------------------------------------
# Step 1 : Market Structure
# ---------------------------------------------------------

market = MarketStructure.calculate(

    support_strength=96,

    resistance_strength=91,

    expected_move=82,

    iv_rank=42,

    iv_percentile=51,

    max_pain=88,

    oi_wall_score=90,

    oi_shift_score=84,

    oi_change_score=80,

)

# ---------------------------------------------------------
# Step 2 : Probability
# ---------------------------------------------------------

result = Probability.calculate(market)

print()

print(f"Bullish Probability : {result.bullish_probability:.2f}%")

print(f"Bearish Probability : {result.bearish_probability:.2f}%")

print()

print(f"Confidence          : {result.confidence}")

print(f"Stars               : {'★' * result.stars}")

print()

print(f"Trade Quality       : {result.trade_quality}")

print(f"Risk Level          : {result.risk_level}")

print()

print("Recommendation")

print(result.recommendation)

print()

print("Interpretation")

print(result.interpretation)

print()

print("MISSION COMPLETE")