"""
============================================================
OptionForge
Market Explosion Risk Demo
============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import MarketExplosionRisk

from optionforge.models import (
    DealerPressureResult,
    InstitutionalSignalResult,
    DealerHedgingFlowResult,
    DealerPositionResult,
)

print("=" * 70)
print("                OPTIONFORGE")
print("          MARKET EXPLOSION RISK")
print("=" * 70)
print()

# ----------------------------------------------------------
# Dealer Pressure
# ----------------------------------------------------------

pressure = DealerPressureResult(
    pressure_score=100.0,
    pressure_level="EXTREME",
    pressure_direction="DOWNSIDE",
    volatility_bias="EXPANDING",
    confidence="★☆☆☆☆",
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
# Calculate
# ----------------------------------------------------------

result = MarketExplosionRisk.calculate(
    pressure=pressure,
    signal=signal,
    hedging=hedging,
    dealer=dealer,
)

# ----------------------------------------------------------
# Report
# ----------------------------------------------------------

print("EXPLOSION RISK")
print("-" * 70)

print(f"Explosion Score      : {result.explosion_score:.2f}")
print(f"Probability          : {result.explosion_probability}")

print()

print("MARKET")
print("-" * 70)

print(f"Market State         : {result.market_state}")
print(f"Expected Behaviour   : {result.expected_behavior}")

print()

print("CONFIDENCE")
print("-" * 70)

print(f"Confidence           : {result.confidence}")

print()

print("RECOMMENDATION")
print("-" * 70)

print(result.recommendation)

print()

print("INTERPRETATION")
print("-" * 70)

print(result.interpretation)

print()
print("=" * 70)
print("MISSION COMPLETE")
print("=" * 70)
