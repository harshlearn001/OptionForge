"""
============================================================
OptionForge
Vanna Exposure Demo
============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import VannaExposure

print("=" * 60)
print("OPTIONFORGE")
print("VANNA EXPOSURE DEMO")
print("=" * 60)
print()

option_chain = [

    {
        "strike": 25000,
        "option_type": "CE",
        "vanna": 0.18,
        "open_interest": 150000,
        "lot_size": 75,
    },

    {
        "strike": 25000,
        "option_type": "PE",
        "vanna": -0.15,
        "open_interest": 120000,
        "lot_size": 75,
    },

    {
        "strike": 25100,
        "option_type": "CE",
        "vanna": 0.12,
        "open_interest": 90000,
        "lot_size": 75,
    },

    {
        "strike": 24900,
        "option_type": "PE",
        "vanna": -0.21,
        "open_interest": 140000,
        "lot_size": 75,
    },

]

result = VannaExposure.calculate(

    spot_price=25000,

    option_chain=option_chain,

)

print(f"Call Vanna : {result.total_call_vanna:,.2f}")
print(f"Put Vanna  : {result.total_put_vanna:,.2f}")
print(f"Net Vanna  : {result.net_vanna:,.2f}")
print()

print(f"Largest Positive Strike : {result.largest_positive_strike}")
print(f"Largest Negative Strike : {result.largest_negative_strike}")
print()

print(f"Vanna Regime : {result.vanna_regime}")
print()

print(result.interpretation)

print()
print("MISSION COMPLETE")