"""
==============================================================
OptionForge
Spot Adapter Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.adapters.spot_adapter import SpotAdapter

print("=" * 60)
print("OPTIONFORGE")
print("SPOT ADAPTER TEST")
print("=" * 60)

csv_file = r"H:\MarketForge\data\master\Equity_stock_master\RELIANCE.csv"

df = SpotAdapter.convert(csv_file)

print()
print(df.head())

print()
print(df.dtypes)

print()
print(df.columns.tolist())

print()
print("Rows :", len(df))