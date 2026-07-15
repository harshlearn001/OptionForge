"""
============================================================
OptionForge
Institutional Signal Demo
============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import InstitutionalSignal

from optionforge.models import DashboardResult

print("=" * 70)
print("                OPTIONFORGE")
print("          INSTITUTIONAL SIGNAL")
print("=" * 70)
print()

# ----------------------------------------------------------
# Dashboard Result
# ----------------------------------------------------------

dashboard = DashboardResult(
    dealer_bias="SHORT GAMMA",
    dealer_direction="SHORT DELTA",
    gamma_status="BELOW GAMMA FLIP",
    zero_gamma_status="BELOW ZERO GAMMA",
    hedging_flow="SELL FUTURES",
    institutional_score=15.0,
    confidence="★☆☆☆☆",
    market_bias="TREND FOLLOWING",
    risk_level="EXTREME",
    summary="Demo",
)

# ----------------------------------------------------------
# Institutional Signal
# ----------------------------------------------------------

result = InstitutionalSignal.calculate(
    dashboard=dashboard,
)

# ----------------------------------------------------------
# Professional Report
# ----------------------------------------------------------

print("OVERALL SIGNAL")
print("-" * 70)

print(f"Signal             : {result.overall_signal}")
print(f"Strength           : {result.signal_strength:.2f}")

print()

print("MARKET")
print("-" * 70)

print(f"Market Regime      : {result.market_regime}")
print(f"Dealer Regime      : {result.dealer_regime}")
print(f"Volatility         : {result.volatility_outlook}")
print(f"Risk               : {result.risk_level}")

print()

print("TRADING")
print("-" * 70)

print(f"Suggested Action   : {result.action}")
print(f"Confidence         : {result.confidence}")

print()

print("SUMMARY")
print("-" * 70)

print(result.summary)

print()
print("=" * 70)
print("MISSION COMPLETE")
print("=" * 70)
