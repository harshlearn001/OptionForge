"""
==============================================================
OptionForge
tests/intelligence/test_oi_wall.py
--------------------------------------------------------------
Open Interest Wall Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

import pandas as pd

from optionforge.intelligence import OIWall


print("=" * 60)
print("OPTIONFORGE")
print("OPEN INTEREST WALL TEST")
print("=" * 60)

# ---------------------------------------------------------
# Sample Option Chain
# ---------------------------------------------------------

df = pd.DataFrame(

    [

        {
            "STRIKE_PRICE":24800,
            "OPTION_TYPE":"CE",
            "OPEN_INTEREST":120000,
        },

        {
            "STRIKE_PRICE":24900,
            "OPTION_TYPE":"CE",
            "OPEN_INTEREST":200000,
        },

        {
            "STRIKE_PRICE":25000,
            "OPTION_TYPE":"CE",
            "OPEN_INTEREST":170000,
        },

        {
            "STRIKE_PRICE":24800,
            "OPTION_TYPE":"PE",
            "OPEN_INTEREST":260000,
        },

        {
            "STRIKE_PRICE":24900,
            "OPTION_TYPE":"PE",
            "OPEN_INTEREST":150000,
        },

        {
            "STRIKE_PRICE":25000,
            "OPTION_TYPE":"PE",
            "OPEN_INTEREST":90000,
        },

    ]

)

result = OIWall.calculate(df)

print()

print(f"Strongest Support     : {result.strongest_support:.0f}")
print(f"Support OI           : {result.support_oi:,}")

print()

print(f"Strongest Resistance : {result.strongest_resistance:.0f}")
print(f"Resistance OI        : {result.resistance_oi:,}")

print()

print(f"Total Put OI         : {result.total_put_oi:,}")
print(f"Total Call OI        : {result.total_call_oi:,}")

print()

print(f"PCR                  : {result.put_call_ratio:.3f}")

print()

print(f"Market Bias          : {result.market_bias}")

print()

print("Interpretation")
print(result.interpretation)

print()

print("MISSION COMPLETE")