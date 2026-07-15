"""
==============================================================
OptionForge
tests/intelligence/test_resistance_strength.py
--------------------------------------------------------------
Resistance Strength Intelligence Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import ResistanceStrength

print("=" * 60)
print("OPTIONFORGE")
print("RESISTANCE STRENGTH TEST")
print("=" * 60)

# ---------------------------------------------------------
# Sample Data
# ---------------------------------------------------------

result = ResistanceStrength.calculate(
    resistance=25100,
    resistance_oi=510000,
    max_call_oi=510000,
    spot_price=24980,
)

print()

print(f"Resistance         : {result.resistance:.0f}")

print(f"Resistance OI      : {result.resistance_oi:,}")

print()

print(f"Strength Score     : {result.score:.2f}")

print(f"Stars              : {'★' * result.stars}")

print(f"Rating             : {result.rating}")

print()

print("Interpretation")
print(result.interpretation)

print()

print("MISSION COMPLETE")
