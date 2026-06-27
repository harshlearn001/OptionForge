"""
==============================================================
OptionForge
tests/intelligence/test_expected_move.py
--------------------------------------------------------------
Expected Move Intelligence Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import ExpectedMove


print("=" * 60)
print("OPTIONFORGE")
print("EXPECTED MOVE TEST")
print("=" * 60)

print()

result = ExpectedMove.calculate(

    spot=25000,

    atm_iv=0.20,

    days=7,

)

print("Expected Move :", round(result.expected_move, 2))

print()

print("68% Range")

print("Upper :", round(result.upper_68, 2))
print("Lower :", round(result.lower_68, 2))

print()

print("95% Range")

print("Upper :", round(result.upper_95, 2))
print("Lower :", round(result.lower_95, 2))

print()

print("Daily Move   :", round(result.one_day_move, 2))
print("Weekly Move  :", round(result.weekly_move, 2))
print("Monthly Move :", round(result.monthly_move, 2))

print()

print("MISSION COMPLETE")