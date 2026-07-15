"""
==============================================================
OPTIONFORGE
OI BY STRIKE TEST
==============================================================
"""
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from optionforge.optionchain import OptionChain
from optionforge.oi.oi_by_strike import OIByStrike

print("=" * 70)
print("OPTIONFORGE")
print("OI BY STRIKE TEST")
print("=" * 70)

chain = (
    OptionChain
    .load(
        r"H:\MarketForge\data\master\option_master\INDICES\NIFTY.parquet"
    )
    .latest()
    .current_weekly()
)

print()
print("CHAIN INFORMATION")
print("-" * 70)

df = chain.dataframe()

print("Trading Date :", df["trading_date"].iloc[0].date())
print("Expiry Date  :", df["expiry_date"].iloc[0].date())
print("Symbol       :", df["symbol"].iloc[0])
print("Instrument   :", df["instrument"].iloc[0])

print()

table = OIByStrike(chain)

print()
print(table)

print("\nCOLUMNS")
print("-" * 70)
print(table.dataframe().columns.tolist())

print("\nFIRST 20 ROWS")
print("-" * 70)
print(table.dataframe().head(20))

print("\nTOP 10 CALL OI")
print("-" * 70)
print(table.top_call_oi())

print("\nTOP 10 PUT OI")
print("-" * 70)
print(table.top_put_oi())

print("\nTOP 10 TOTAL OI")
print("-" * 70)
print(table.top_total_oi())

print()
print("Rows :", len(table))
print()
print("CHAIN INFORMATION")
print("-" * 70)

df = chain.dataframe()

print("Trading Date :", df["trading_date"].iloc[0].date())
print("Expiry Date  :", df["expiry_date"].iloc[0].date())
print("Symbol       :", df["symbol"].iloc[0])
print("Instrument   :", df["instrument"].iloc[0])

print()