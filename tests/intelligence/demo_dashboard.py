"""
============================================================
OptionForge
Institutional Dashboard Demo
============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import Dashboard

from optionforge.models import (
    DealerPositionResult,
    GammaFlipResult,
    ZeroGammaResult,
    DealerHedgingFlowResult,
)

print("=" * 70)
print("                OPTIONFORGE")
print("       INSTITUTIONAL DASHBOARD")
print("=" * 70)
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

hedging = DealerHedgingFlowResult(
    hedging_bias="PRO-CYCLICAL",
    flow_direction="SELL FUTURES",
    flow_strength="WEAK",
    volatility_effect="VOLATILITY EXPANSION",
    market_support="UNSUPPORTED",
    trend_effect="TREND ACCELERATION",
    institutional_score=15.0,
    confidence="★☆☆☆☆",
    recommendation="Demo",
    interpretation="Demo",
)

# ----------------------------------------------------------
# Dashboard
# ----------------------------------------------------------

result = Dashboard.calculate(
    dealer=dealer,
    gamma_flip=gamma_flip,
    zero_gamma=zero_gamma,
    hedging=hedging,
)

# ----------------------------------------------------------
# Professional Report
# ----------------------------------------------------------

print("MARKET STRUCTURE")
print("-" * 70)

print(f"Dealer Bias          : {result.dealer_bias}")
print(f"Dealer Direction     : {result.dealer_direction}")

print()

print("DEALER REGIME")
print("-" * 70)

print(f"Gamma Flip           : {result.gamma_status}")
print(f"Zero Gamma           : {result.zero_gamma_status}")

print()

print("FLOW")
print("-" * 70)

print(f"Hedging Flow         : {result.hedging_flow}")

print()

print("RISK")
print("-" * 70)

print(f"Institutional Score  : {result.institutional_score:.2f}")
print(f"Confidence           : {result.confidence}")
print(f"Market Bias          : {result.market_bias}")
print(f"Risk Level           : {result.risk_level}")

print()

print("EXECUTIVE SUMMARY")
print("-" * 70)

print(result.summary)

print()
print("=" * 70)
print("MISSION COMPLETE")
print("=" * 70)
