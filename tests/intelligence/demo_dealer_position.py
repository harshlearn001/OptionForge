"""
============================================================
OptionForge
Dealer Positioning Demo
============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import DealerPosition
from optionforge.models import (
    GammaExposureResult,
    DeltaExposureResult,
    VannaExposureResult,
    CharmExposureResult,
)

print("=" * 60)
print("OPTIONFORGE")
print("DEALER POSITIONING DEMO")
print("=" * 60)
print()

# ----------------------------------------------------------
# Gamma Exposure
# ----------------------------------------------------------

gamma = GammaExposureResult(

    total_call_gex=100.0,

    total_put_gex=-150.0,

    net_gex=-50.0,

    largest_positive_strike=25000.0,

    largest_negative_strike=25100.0,

    gamma_flip=25050.0,

    market_regime="NEGATIVE GAMMA",

    interpretation="Demo",
)

# ----------------------------------------------------------
# Delta Exposure
# ----------------------------------------------------------

delta = DeltaExposureResult(

    total_call_dex=120.0,

    total_put_dex=-180.0,

    net_dex=-60.0,

    largest_positive_strike=25000.0,

    largest_negative_strike=25100.0,

    dealer_position="SHORT DELTA",

    interpretation="Demo",
)

# ----------------------------------------------------------
# Vanna Exposure
# ----------------------------------------------------------

vanna = VannaExposureResult(

    total_call_vanna=50.0,

    total_put_vanna=-80.0,

    net_vanna=-30.0,

    largest_positive_strike=25000.0,

    largest_negative_strike=25100.0,

    vanna_regime="NEGATIVE VANNA",

    interpretation="Demo",
)

# ----------------------------------------------------------
# Charm Exposure
# ----------------------------------------------------------

charm = CharmExposureResult(

    total_call_charm=40.0,

    total_put_charm=-70.0,

    net_charm=-30.0,

    largest_positive_strike=25000.0,

    largest_negative_strike=25100.0,

    charm_regime="NEGATIVE CHARM",

    interpretation="Demo",
)

# ----------------------------------------------------------
# Dealer Position
# ----------------------------------------------------------

result = DealerPosition.calculate(

    gamma=gamma,

    delta=delta,

    vanna=vanna,

    charm=charm,

)

# ----------------------------------------------------------
# Report
# ----------------------------------------------------------

print(f"Dealer Bias         : {result.dealer_bias}")
print(f"Dealer Direction    : {result.dealer_direction}")
print(f"Market Condition    : {result.market_condition}")
print(f"Market Stability    : {result.market_stability}")
print(f"Directional Risk    : {result.directional_risk}")

print()

print(f"Institutional Score : {result.institutional_score:.2f}")
print(f"Confidence          : {result.confidence}")

print()

print("Recommendation")
print(result.recommendation)

print()

print("Interpretation")
print(result.interpretation)

print()
print("MISSION COMPLETE")