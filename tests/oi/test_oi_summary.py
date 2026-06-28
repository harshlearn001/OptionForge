"""
======================================================================
OPTIONFORGE
OI SUMMARY TEST
======================================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.optionchain import OptionChain
from optionforge.oi.oi_summary import OISummary

print("=" * 70)
print("OPTIONFORGE")
print("OI SUMMARY TEST")
print("=" * 70)

# ==========================================================
# Load Latest Current Weekly Chain
# ==========================================================

chain = (
    OptionChain
    .load(
        r"H:\MarketForge\data\master\option_master\INDICES\NIFTY.parquet"
    )
    .latest()
    .current_weekly()
)

print("\nCHAIN")
print("-" * 70)

print(chain)

# ==========================================================
# Summary
# ==========================================================

summary = OISummary(chain.df)

print("\nSUMMARY OBJECT")
print("-" * 70)

print(summary)

print("\nSUMMARY DICTIONARY")
print("-" * 70)

for key, value in summary.to_dict().items():
    print(f"{key:18} : {value}")

# ==========================================================
# Individual Values
# ==========================================================

print("\nINDIVIDUAL VALUES")
print("-" * 70)

print(f"Call OI         : {summary.call_oi:,}")
print(f"Put OI          : {summary.put_oi:,}")
print(f"Total OI        : {summary.total_oi:,}")

print()

print(f"Call Volume     : {summary.call_volume:,}")
print(f"Put Volume      : {summary.put_volume:,}")
print(f"Total Volume    : {summary.total_volume:,}")

print()

print(f"Contracts       : {summary.contracts:,}")
print(f"Trades          : {summary.trades:,}")

print()

print(f"PCR             : {summary.pcr}")

print()

print("=" * 70)
print("OI SUMMARY TEST COMPLETED")
print("=" * 70)