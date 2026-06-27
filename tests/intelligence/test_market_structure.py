"""
==============================================================
OptionForge
tests/intelligence/test_market_structure.py
--------------------------------------------------------------
Professional Market Structure Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import MarketStructure


print("=" * 60)
print("OPTIONFORGE")
print("MARKET STRUCTURE TEST")
print("=" * 60)

# ---------------------------------------------------------
# Professional Example
# ---------------------------------------------------------

result = MarketStructure.calculate(

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

print()

print(f"Market Score          : {result.score:.2f}")

print()

print(f"Bias                  : {result.bias}")

print(f"Confidence            : {result.confidence}")

print(f"Stars                 : {'★' * result.stars}")

print()

print(f"Support Strength      : {result.support_strength:.2f}")

print(f"Resistance Strength   : {result.resistance_strength:.2f}")

print()

print(f"Expected Move Score   : {result.expected_move:.2f}")

print(f"IV Rank               : {result.iv_rank:.2f}")

print(f"IV Percentile         : {result.iv_percentile:.2f}")

print(f"Max Pain Score        : {result.max_pain:.2f}")

print()

print("Recommendation")

print(result.recommendation)

print()

print("Interpretation")

print(result.interpretation)

print()

print("MISSION COMPLETE")