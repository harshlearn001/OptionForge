"""
======================================================================
OPTIONFORGE
OPTION CHAIN ENGINE
======================================================================
"""

import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE))

from optionforge.optionchain import OptionChain

print("=" * 70)
print("OPTIONFORGE")
print("OPTION CHAIN ENGINE")
print("=" * 70)

chain = OptionChain.from_parquet(
    r"H:\MarketForge\data\master\option_master\INDICES\NIFTY.parquet"
)

latest = chain.latest()

print()

print("LATEST SNAPSHOT")
print("-" * 70)

print(latest)

print()

print("Latest Trading Date")
print(latest.latest_date())

print()

print("AVAILABLE EXPIRIES")
print("-" * 70)

exp = latest.expiries()

for i, d in enumerate(exp, start=1):
    print(f"{i:02d}. {d.date()}")

print()

print("TOTAL EXPIRIES :", len(exp))

print()
print("=" * 70)
print("CURRENT WEEKLY")
print("=" * 70)

cw = latest.current_weekly()

print(cw)

print()

print(cw.latest_date())

print()

print(cw.expiries())

print()

print(cw.dataframe().head())

# --------------------------------------------------------

print()
print("=" * 70)
print("NEXT WEEKLY")
print("=" * 70)

nw = latest.next_weekly()

print(nw)

print()

print(nw.expiries())

print()

print(nw.dataframe().head())

# --------------------------------------------------------

print()
print("=" * 70)
print("CURRENT MONTHLY")
print("=" * 70)

cm = latest.current_monthly()

print(cm)

print()

print(cm.expiries())

print()

print(cm.dataframe().head())

print()
print("=" * 70)
print("NEXT MONTHLY")
print("=" * 70)

nm = latest.next_monthly()

print(nm)

print()

print(nm.expiries())

print()

print(nm.dataframe().head())

# -------------------------------------------------------

print()
print("=" * 70)
print("LEAPS")
print("=" * 70)

print(latest.leaps())

# -------------------------------------------------------

print()
print("=" * 70)
print("FAR MONTH")
print("=" * 70)

fm = latest.far_month()

print(fm)

print()

print(fm.expiries())

print()

print(fm.dataframe().head())
