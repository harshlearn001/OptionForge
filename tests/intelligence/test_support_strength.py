"""
==============================================================
OptionForge
tests/intelligence/test_support_strength.py
--------------------------------------------------------------
Support Strength Intelligence Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import SupportStrength


print("=" * 60)
print("OPTIONFORGE")
print("SUPPORT STRENGTH TEST")
print("=" * 60)

# ---------------------------------------------------------
# Sample Data
# ---------------------------------------------------------

result = SupportStrength.calculate(

    support=24800,

    support_oi=520000,

    max_put_oi=520000,

    spot_price=24875,

)

print()

print(f"Support            : {result.support:.0f}")

print(f"Support OI         : {result.support_oi:,}")

print()

print(f"Strength Score     : {result.score:.2f}")

print(f"Stars              : {'★' * result.stars}")

print(f"Rating             : {result.rating}")

print()

print("Interpretation")
print(result.interpretation)

print()

print("MISSION COMPLETE")