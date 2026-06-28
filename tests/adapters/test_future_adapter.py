"""
==============================================================
OptionForge
Professional Future Adapter Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.adapters.future_adapter import FutureAdapter

print("=" * 70)
print("OPTIONFORGE")
print("PROFESSIONAL FUTURE ADAPTER TEST")
print("=" * 70)

csv_file = (
    r"H:\MarketForge\data\master"
    r"\Futures_master_three_expiries"
    r"\FUTSTK\RELIANCE.csv"
)

# ---------------------------------------------------------
# Load
# ---------------------------------------------------------

df = FutureAdapter.convert(csv_file)

# ---------------------------------------------------------
# Basic Information
# ---------------------------------------------------------

print("\nBASIC INFORMATION")
print("-" * 70)

print("Rows    :", len(df))
print("Columns :", len(df.columns))

# ---------------------------------------------------------
# First Rows
# ---------------------------------------------------------

print("\nFIRST 5 ROWS")
print("-" * 70)

print(df.head())

# ---------------------------------------------------------
# Last Rows
# ---------------------------------------------------------

print("\nLAST 5 ROWS")
print("-" * 70)

print(df.tail())

# ---------------------------------------------------------
# Data Types
# ---------------------------------------------------------

print("\nDATA TYPES")
print("-" * 70)

print(df.dtypes)

# ---------------------------------------------------------
# Columns
# ---------------------------------------------------------

print("\nCOLUMN ORDER")
print("-" * 70)

for i, col in enumerate(df.columns, start=1):
    print(f"{i:02d}. {col}")

# ---------------------------------------------------------
# Date Range
# ---------------------------------------------------------

print("\nDATA DATE RANGE")
print("-" * 70)

print("Minimum :", df["TRADE_DATE"].min())
print("Maximum :", df["TRADE_DATE"].max())

# ---------------------------------------------------------
# Expiry Type Summary
# ---------------------------------------------------------

print("\nROWS BY EXPIRY TYPE")
print("-" * 70)

print(df.groupby("EXPIRY_TYPE").size())

# ---------------------------------------------------------
# Date Range Per Expiry Type
# ---------------------------------------------------------

print("\nDATE RANGE BY EXPIRY TYPE")
print("-" * 70)

for expiry_type in sorted(df["EXPIRY_TYPE"].unique()):

    temp = df[df["EXPIRY_TYPE"] == expiry_type]

    print(
        f"{expiry_type:<5}"
        f"  Rows : {len(temp):5d}"
        f"   From : {temp['TRADE_DATE'].min().date()}"
        f"   To : {temp['TRADE_DATE'].max().date()}"
    )

# ---------------------------------------------------------
# Expiry Dates
# ---------------------------------------------------------

print("\nUNIQUE EXPIRY DATES")
print("-" * 70)

for exp in sorted(df["EXPIRY"].unique()):
    print(exp)

# ---------------------------------------------------------
# Latest Trading Day
# ---------------------------------------------------------

print("\nLATEST TRADING DAY")
print("-" * 70)

latest = df["TRADE_DATE"].max()

latest_df = (
    df[df["TRADE_DATE"] == latest]
    .sort_values("EXPIRY")
)

print(latest_df[
    [
        "TRADE_DATE",
        "EXPIRY_TYPE",
        "EXPIRY",
        "OPEN",
        "HIGH",
        "LOW",
        "CLOSE",
        "OI",
        "VOLUME",
    ]
])

# ---------------------------------------------------------
# Missing Values
# ---------------------------------------------------------

print("\nMISSING VALUES")
print("-" * 70)

print(df.isna().sum())

# ---------------------------------------------------------
# Duplicate Rows
# ---------------------------------------------------------

print("\nDUPLICATE ROWS")
print("-" * 70)

print(df.duplicated().sum())

# ---------------------------------------------------------
# Statistics
# ---------------------------------------------------------

print("\nNUMERIC SUMMARY")
print("-" * 70)

print(
    df.describe().T
)

# ---------------------------------------------------------
# Final Result
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("FUTURE ADAPTER VALIDATION COMPLETED")
print("=" * 70)