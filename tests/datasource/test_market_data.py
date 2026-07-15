"""
==============================================================
OptionForge
tests/datasource/test_market_data.py
--------------------------------------------------------------
Professional Market Data Loader Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

import pandas as pd

from optionforge.datasource import MarketData

print("=" * 60)
print("OPTIONFORGE")
print("MARKET DATA LOADER TEST")
print("=" * 60)

# ---------------------------------------------------------
# Create Sample CSV
# ---------------------------------------------------------

sample = pd.DataFrame(
    {
        "SYMBOL": ["NIFTY"],
        "STRIKE": [25000],
        "OPTION_TYPE": ["CE"],
        "LTP": [185.25],
        "OI": [250000],
    }
)

sample_file = Path("sample_market_data.csv")

sample.to_csv(sample_file, index=False)

# ---------------------------------------------------------
# Load CSV
# ---------------------------------------------------------

df = MarketData.from_csv(sample_file)

print()

print(df)

print()

print(f"Rows Loaded : {len(df)}")

print(f"Columns     : {len(df.columns)}")

print()

print("MISSION COMPLETE")

# ---------------------------------------------------------
# Cleanup
# ---------------------------------------------------------

sample_file.unlink(missing_ok=True)
