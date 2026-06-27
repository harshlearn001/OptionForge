"""
==============================================================
OptionForge
tests/intelligence/test_oi_shift.py
--------------------------------------------------------------
OI Shift Intelligence Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import OIShift


print("=" * 60)
print("OPTIONFORGE")
print("OI SHIFT INTELLIGENCE TEST")
print("=" * 60)

tests = [

    # ---------------------------------------------------------
    # Strongly Bullish
    # ---------------------------------------------------------

    (24800, 24900, 25200, 25100),

    # ---------------------------------------------------------
    # Strongly Bearish
    # ---------------------------------------------------------

    (24900, 24800, 25100, 25200),

    # ---------------------------------------------------------
    # Bullish (Support Higher)
    # ---------------------------------------------------------

    (24800, 24900, 25200, 25200),

    # ---------------------------------------------------------
    # Bearish (Resistance Higher)
    # ---------------------------------------------------------

    (24800, 24800, 25100, 25200),

    # ---------------------------------------------------------
    # Neutral
    # ---------------------------------------------------------

    (24800, 24800, 25200, 25200),

]

for previous_support, current_support, previous_resistance, current_resistance in tests:

    result = OIShift.analyze(

        previous_support=previous_support,

        current_support=current_support,

        previous_resistance=previous_resistance,

        current_resistance=current_resistance,

    )

    print("-" * 60)

    print(f"Previous Support    : {result.previous_support:.0f}")
    print(f"Current Support     : {result.current_support:.0f}")
    print(f"Support Shift       : {result.support_shift:+.0f}")

    print()

    print(f"Previous Resistance : {result.previous_resistance:.0f}")
    print(f"Current Resistance  : {result.current_resistance:.0f}")
    print(f"Resistance Shift    : {result.resistance_shift:+.0f}")

    print()

    print(f"Support Direction   : {result.support_direction}")
    print(f"Resistance Direction: {result.resistance_direction}")

    print()

    print(f"Market Bias         : {result.market_bias}")

    print()

    print("Interpretation")
    print(result.interpretation)

    print()

print("=" * 60)
print("MISSION COMPLETE")