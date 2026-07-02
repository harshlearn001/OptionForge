"""
============================================================
OptionForge
Charm Exposure Demo
============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import CharmExposure

print("=" * 60)
print("OPTIONFORGE")
print("CHARM EXPOSURE DEMO")
print("=" * 60)
print()

option_chain = [

    {
        "strike": 25000,
        "option_type": "CE",
        "charm": 0.11,
        "open_interest": 150000,
        "lot_size": 75,
    },

    {
        "strike": 25000,
        "option_type": "PE",
        "charm": -0.09,
        "open_interest": 120000,
        "lot_size": 75,
    },

    {
        "strike": 25100,
        "option_type": "CE",
        "charm": 0.08,
        "open_interest": 90000,
        "lot_size": 75,
    },

    {
        "strike": 24900,
        "option_type": "PE",
        "charm": -0.13,
        "open_interest": 140000,
        "lot_size": 75,
    },

]

result = CharmExposure.calculate(

    spot_price=25000,

    option_chain=option_chain,

)

print(f"Call Charm : {result.total_call_charm:,.2f}")
print(f"Put Charm  : {result.total_put_charm:,.2f}")
print(f"Net Charm  : {result.net_charm:,.2f}")
print()

print(f"Largest Positive Strike : {result.largest_positive_strike}")
print(f"Largest Negative Strike : {result.largest_negative_strike}")
print()

print(f"Charm Regime : {result.charm_regime}")
print()

print(result.interpretation)

print()
print("MISSION COMPLETE")