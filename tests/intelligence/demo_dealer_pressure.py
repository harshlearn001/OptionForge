"""
============================================================
OptionForge
Dealer Pressure Demo
============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import DealerPressure

from optionforge.models import (
    DealerPositionResult,
    DealerHedgingFlowResult,
    InstitutionalSignalResult,
)

print("=" * 70)
print("                OPTIONFORGE")
print("             DEALER PRESSURE")
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
# Institutional Signal
# ----------------------------------------------------------

signal = InstitutionalSignalResult(
    overall_signal="STRONG BEARISH",
    signal_strength=15.0,
    market_regime="TREND FOLLOWING",
    volatility_outlook="EXPANDING",
    dealer_regime="SHORT GAMMA",
    risk_level="EXTREME",
    confidence="★☆☆☆☆",
    action="SELL RALLIES",
    summary="Demo",
)

# ----------------------------------------------------------
# Dealer Pressure
# ----------------------------------------------------------

result = DealerPressure.calculate(
    dealer=dealer,
    hedging=hedging,
    signal=signal,
)

# ----------------------------------------------------------
# Report
# ----------------------------------------------------------

print("PRESSURE")
print("-" * 70)

print(f"Pressure Score      : {result.pressure_score:.2f}")
print(f"Pressure Level      : {result.pressure_level}")

print()

print("MARKET")
print("-" * 70)

print(f"Direction           : {result.pressure_direction}")
print(f"Volatility Bias     : {result.volatility_bias}")

print()

print("CONFIDENCE")
print("-" * 70)

print(f"Confidence          : {result.confidence}")

print()

print("INTERPRETATION")
print("-" * 70)

print(result.interpretation)

print()
print("=" * 70)
print("MISSION COMPLETE")
print("=" * 70)
