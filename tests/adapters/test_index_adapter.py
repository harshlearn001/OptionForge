"""
==============================================================
OptionForge
INDEX ADAPTER TEST
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.adapters.index_adapter import IndexAdapter

print("=" * 70)
print("OPTIONFORGE")
print("INDEX ADAPTER TEST")
print("=" * 70)

csv_file = r"H:\MarketForge\data\master" r"\Indices_master" r"\NIFTY.csv"

df = IndexAdapter.convert(csv_file)

print("\nBASIC INFORMATION")
print("-" * 70)

print("Rows    :", len(df))
print("Columns :", len(df.columns))

print("\nFIRST 5 ROWS")
print("-" * 70)
print(df.head())

print("\nLAST 5 ROWS")
print("-" * 70)
print(df.tail())

print("\nDATA TYPES")
print("-" * 70)
print(df.dtypes)

print("\nCOLUMN ORDER")
print("-" * 70)

for i, col in enumerate(df.columns, start=1):
    print(f"{i:02d}. {col}")

print("\nDATE RANGE")
print("-" * 70)

print("Minimum :", df["TRADE_DATE"].min())
print("Maximum :", df["TRADE_DATE"].max())

print("\nMISSING VALUES")
print("-" * 70)
print(df.isna().sum())

print("\nDUPLICATE ROWS")
print("-" * 70)
print(df.duplicated().sum())

print("\nNUMERIC SUMMARY")
print("-" * 70)
print(df.describe())

print("\n" + "=" * 70)
print("INDEX ADAPTER VALIDATION COMPLETED")
print("=" * 70)
