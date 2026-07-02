"""
==============================================================
OptionForge
Delta Exposure Demo
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import DeltaExposure

print("=" * 60)
print("OPTIONFORGE")
print("DELTA EXPOSURE DEMO")
print("=" * 60)
print()

option_chain = [

    {
        "strike": 25000,
        "option_type": "CE",
        "delta": 0.55,
        "open_interest": 150000,
        "lot_size": 75,
    },

    {
        "strike": 25000,
        "option_type": "PE",
        "delta": -0.45,
        "open_interest": 120000,
        "lot_size": 75,
    },

    {
        "strike": 25100,
        "option_type": "CE",
        "delta": 0.38,
        "open_interest": 80000,
        "lot_size": 75,
    },

    {
        "strike": 24900,
        "option_type": "PE",
        "delta": -0.62,
        "open_interest": 140000,
        "lot_size": 75,
    },

]

result = DeltaExposure.calculate(

    spot_price=25000,

    option_chain=option_chain,

)

print(f"Call DEX : {result.total_call_dex:,.2f}")
print(f"Put DEX  : {result.total_put_dex:,.2f}")
print(f"Net DEX  : {result.net_dex:,.2f}")
print()

print(f"Largest Positive Strike : {result.largest_positive_strike}")
print(f"Largest Negative Strike : {result.largest_negative_strike}")
print()

print(f"Dealer Position : {result.dealer_position}")
print()

print(result.interpretation)

print()
print("MISSION COMPLETE")