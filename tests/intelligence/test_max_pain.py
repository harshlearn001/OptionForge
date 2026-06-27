"""
==============================================================
OptionForge
tests/intelligence/test_max_pain.py
--------------------------------------------------------------
Professional Max Pain Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

import pandas as pd

from optionforge.intelligence.max_pain import MaxPain


print("=" * 60)
print("OPTIONFORGE")
print("PROFESSIONAL MAX PAIN TEST")
print("=" * 60)

# ---------------------------------------------------------
# Sample Option Chain
# ---------------------------------------------------------

df = pd.DataFrame(

    [
        {
            "STRIKE_PRICE": 24800,
            "OPTION_TYPE": "CE",
            "OPEN_INTEREST": 120000,
        },
        {
            "STRIKE_PRICE": 24900,
            "OPTION_TYPE": "CE",
            "OPEN_INTEREST": 200000,
        },
        {
            "STRIKE_PRICE": 25000,
            "OPTION_TYPE": "CE",
            "OPEN_INTEREST": 170000,
        },
        {
            "STRIKE_PRICE": 24800,
            "OPTION_TYPE": "PE",
            "OPEN_INTEREST": 260000,
        },
        {
            "STRIKE_PRICE": 24900,
            "OPTION_TYPE": "PE",
            "OPEN_INTEREST": 150000,
        },
        {
            "STRIKE_PRICE": 25000,
            "OPTION_TYPE": "PE",
            "OPEN_INTEREST": 90000,
        },
    ]
)

result = MaxPain.calculate(df)

print()

print(f"Max Pain Strike      : {result.max_pain:.0f}")
print(f"Total Pain           : {result.total_pain:,.0f}")

print()

print(f"Call Pain            : {result.call_pain:,.0f}")
print(f"Put Pain             : {result.put_pain:,.0f}")

print()

print(f"Support              : {result.support:.0f}")
print(f"Resistance           : {result.resistance:.0f}")

print()

print(f"Highest Put OI       : {result.highest_put_oi:.0f}")
print(f"Highest Call OI      : {result.highest_call_oi:.0f}")

print()

print(f"Total Put OI         : {result.total_put_oi:,}")
print(f"Total Call OI        : {result.total_call_oi:,}")

print()

print(f"Evaluated Strikes    : {result.evaluated_strikes}")

print()

print("Pain Table")
print("-" * 60)
print(result.pain_table)

print()

print("Interpretation")
print(result.interpretation)

print()

print("MISSION COMPLETE")