"""
==============================================================
OptionForge
tests/intelligence/test_iv_rank.py
--------------------------------------------------------------
IV Rank Intelligence Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import IVRank


print("=" * 60)
print("OPTIONFORGE")
print("IV RANK TEST")
print("=" * 60)

print()

result = IVRank.calculate(

    current_iv=18.0,

    low_iv=10.0,

    high_iv=30.0,

)

print("Current IV :", result.current_iv)
print("Lowest IV  :", result.low_iv)
print("Highest IV :", result.high_iv)

print()

print("IV Rank :", round(result.iv_rank, 2), "%")

print()

print("Status :", result.status)

print()

print("Interpretation")

print(result.interpretation)

print()

print("MISSION COMPLETE")