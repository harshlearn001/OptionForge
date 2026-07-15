"""
==============================================================
OptionForge
Gamma Exposure Demo
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import GammaExposure

print("=" * 60)
print("OPTIONFORGE")
print("GAMMA EXPOSURE DEMO")
print("=" * 60)
print()

option_chain = [
    {
        "strike": 25000,
        "option_type": "CE",
        "gamma": 0.0018,
        "open_interest": 150000,
        "lot_size": 75,
    },
    {
        "strike": 25000,
        "option_type": "PE",
        "gamma": 0.0015,
        "open_interest": 120000,
        "lot_size": 75,
    },
    {
        "strike": 25100,
        "option_type": "CE",
        "gamma": 0.0012,
        "open_interest": 80000,
        "lot_size": 75,
    },
    {
        "strike": 24900,
        "option_type": "PE",
        "gamma": 0.0019,
        "open_interest": 140000,
        "lot_size": 75,
    },
]

result = GammaExposure.calculate(
    spot_price=25000,
    option_chain=option_chain,
)

print(f"Call GEX : {result.total_call_gex:,.2f}")
print(f"Put GEX  : {result.total_put_gex:,.2f}")
print(f"Net GEX  : {result.net_gex:,.2f}")
print()

print(f"Largest Positive Strike : {result.largest_positive_strike}")
print(f"Largest Negative Strike : {result.largest_negative_strike}")
print()

print(f"Gamma Regime : {result.market_regime}")
print()

print(result.interpretation)

print()
print("MISSION COMPLETE")
