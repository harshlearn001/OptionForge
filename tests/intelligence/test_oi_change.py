"""
==============================================================
OptionForge
tests/intelligence/test_oi_change.py
--------------------------------------------------------------
OI Change Intelligence Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import OIChange


print("=" * 60)
print("OPTIONFORGE")
print("OI CHANGE INTELLIGENCE TEST")
print("=" * 60)

tests = [

    # -------------------------------------------------
    # Long Build-up
    # -------------------------------------------------

    ("25000", "CE", 15.40, 18000),

    # -------------------------------------------------
    # Short Build-up
    # -------------------------------------------------

    ("25100", "CE", -12.60, 14500),

    # -------------------------------------------------
    # Short Covering
    # -------------------------------------------------

    ("24900", "PE", 8.25, -9200),

    # -------------------------------------------------
    # Long Unwinding
    # -------------------------------------------------

    ("24800", "PE", -10.80, -13200),

    # -------------------------------------------------
    # Neutral
    # -------------------------------------------------

    ("25050", "CE", 0.00, 0),

]

for strike, option_type, price_change, oi_change in tests:

    result = OIChange.analyze(

        strike=float(strike),

        option_type=option_type,

        price_change=price_change,

        oi_change=oi_change,

    )

    print("-" * 60)

    print(f"Strike          : {result.strike:.0f} {result.option_type}")

    print(f"Price Change    : {result.price_change:+.2f}")

    print(f"OI Change       : {result.oi_change:+,}")

    print()

    print(f"Classification  : {result.classification}")

    print(f"Sentiment       : {result.sentiment}")

    print()

    print("Interpretation")

    print(result.interpretation)

    print()

print("=" * 60)

print("MISSION COMPLETE")