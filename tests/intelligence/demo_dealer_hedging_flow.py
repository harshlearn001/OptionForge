"""
============================================================
OptionForge
Dealer Hedging Flow Demo
============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import DealerHedgingFlow
from optionforge.models import (
    DealerPositionResult,
    GammaFlipResult,
    ZeroGammaResult,
)

print("=" * 60)
print("OPTIONFORGE")
print("DEALER HEDGING FLOW DEMO")
print("=" * 60)
print()

# ----------------------------------------------------------
# Dealer Position
# ----------------------------------------------------------

dealer = DealerPositionResult(

    dealer_bias="SHORT GAMMA",

    dealer_direction="SHORT DELTA",

    market_condition="TRENDING",

    market_stability="LOW",

    directional_risk="VERY HIGH",

    institutional_score=15.0,

    confidence="★☆☆☆☆",

    recommendation="Demo",

    interpretation="Demo",

)

# ----------------------------------------------------------
# Gamma Flip
# ----------------------------------------------------------

gamma_flip = GammaFlipResult(

    gamma_flip=25050.0,

    current_spot=24980.0,

    distance=-70.0,

    flip_status="BELOW GAMMA FLIP",

    dealer_regime="NEGATIVE GAMMA",

    interpretation="Demo",

)

# ----------------------------------------------------------
# Zero Gamma
# ----------------------------------------------------------

zero_gamma = ZeroGammaResult(

    zero_gamma=25050.0,

    current_spot=24980.0,

    distance=-70.0,

    status="BELOW ZERO GAMMA",

    dealer_regime="UNSTABLE",

    interpretation="Demo",

)

# ----------------------------------------------------------
# Dealer Hedging Flow
# ----------------------------------------------------------

result = DealerHedgingFlow.calculate(

    dealer=dealer,

    gamma_flip=gamma_flip,

    zero_gamma=zero_gamma,

)

# ----------------------------------------------------------
# Report
# ----------------------------------------------------------

print(f"Hedging Bias      : {result.hedging_bias}")
print(f"Flow Direction    : {result.flow_direction}")
print(f"Flow Strength     : {result.flow_strength}")
print()

print(f"Volatility Effect : {result.volatility_effect}")
print(f"Market Support    : {result.market_support}")
print(f"Trend Effect      : {result.trend_effect}")
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