"""
==============================================================
OptionForge
tests/intelligence/test_iv_percentile.py
--------------------------------------------------------------
IV Percentile Intelligence Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import IVPercentile


print("=" * 60)
print("OPTIONFORGE")
print("IV PERCENTILE TEST")
print("=" * 60)

print()

historical_iv = [

    12.0,
    15.0,
    18.0,
    14.0,
    16.0,
    20.0,
    25.0,
    22.0,
    17.0,
    19.0,

]

result = IVPercentile.calculate(

    current_iv=18.0,

    historical_iv=historical_iv,

)

print("Current IV :", result.current_iv)

print("Historical Observations :", result.observations)

print("IV Below Current :", result.below_count)

print()

print("IV Percentile :", round(result.iv_percentile, 2), "%")

print()

print("Status :", result.status)

print()

print("Interpretation")

print(result.interpretation)

print()

print("MISSION COMPLETE")