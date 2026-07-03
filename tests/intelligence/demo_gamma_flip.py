"""
============================================================
OptionForge
Gamma Flip Demo
============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import GammaFlip
from optionforge.models import GammaExposureResult

print("=" * 60)
print("OPTIONFORGE")
print("GAMMA FLIP DEMO")
print("=" * 60)
print()

# ----------------------------------------------------------
# Gamma Exposure Result (Demo)
# ----------------------------------------------------------

gamma = GammaExposureResult(

    total_call_gex=171562500000.0,

    total_put_gex=209062500000.0,

    net_gex=-37500000000.0,

    largest_positive_strike=25000.0,

    largest_negative_strike=25100.0,

    gamma_flip=25050.0,

    market_regime="NEGATIVE GAMMA",

    interpretation="Demo",

)

# ----------------------------------------------------------
# Current Spot
# ----------------------------------------------------------

spot = 24980.0

# ----------------------------------------------------------
# Gamma Flip Intelligence
# ----------------------------------------------------------

result = GammaFlip.calculate(

    gamma=gamma,

    current_spot=spot,

)

# ----------------------------------------------------------
# Report
# ----------------------------------------------------------

print(f"Current Spot     : {result.current_spot:,.2f}")
print(f"Gamma Flip       : {result.gamma_flip:,.2f}")
print(f"Distance         : {result.distance:,.2f}")

print()

print(f"Flip Status      : {result.flip_status}")
print(f"Dealer Regime    : {result.dealer_regime}")

print()

print("Interpretation")
print(result.interpretation)

print()
print("MISSION COMPLETE")