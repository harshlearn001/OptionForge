"""
==============================================================
OptionForge
NSE ADAPTER TEST
==============================================================
"""

import sys
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.adapters import NSEAdapter

print("=" * 60)
print("OPTIONFORGE")
print("NSE ADAPTER TEST")
print("=" * 60)

# ---------------------------------------------------------
# Sample NSE Data
# ---------------------------------------------------------

df = pd.DataFrame({
    "SYMBOL": ["NIFTY"],
    "EXPIRY": ["2026-07-02"],
    "STRIKE": [25000],
    "OPTION_TYPE": ["CE"],
    "LTP": [185.25],
    "IV": [20.0],
    "OI": [250000],
    "CHANGE_IN_OI": [12000],
    "VOLUME": [98000],
    "SPOT": [24980],
})

converted = NSEAdapter.convert(df)

print()
print(converted)
print()

print("Rows    :", len(converted))
print("Columns :", len(converted.columns))

print()
print("MISSION COMPLETE")