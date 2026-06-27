"""
==============================================================
OptionForge
tests/intelligence/test_strategy.py
--------------------------------------------------------------
Professional Strategy Engine Test
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
)

print("=" * 60)
print("OPTIONFORGE")
print("STRATEGY ENGINE TEST")
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

probability = Probability.calculate(market)

# ---------------------------------------------------------
# Step 3 : Strategy
# ---------------------------------------------------------

strategy = Strategy.calculate(

    probability=probability,

    spot_price=25000,

    expected_move=692,

)

print()

print(f"Action            : {strategy.action}")

print(f"Entry Zone        : {strategy.entry_zone}")

print(f"Stop Loss         : {strategy.stop_loss:.2f}")

print()

print(f"Target 1          : {strategy.target_1:.2f}")

print(f"Target 2          : {strategy.target_2:.2f}")

print()

print(f"Risk Reward       : 1 : {strategy.risk_reward:.2f}")

print()

print(f"Trade Quality     : {strategy.trade_quality}")

print(f"Confidence        : {strategy.confidence}")

print(f"Stars             : {'★' * strategy.stars}")

print()

print("Recommendation")

print(strategy.recommendation)

print()

print("Interpretation")

print(strategy.interpretation)

print()

print("MISSION COMPLETE")