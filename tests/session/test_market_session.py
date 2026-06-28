"""
============================================================
OptionForge
MARKET SESSION TEST
============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.config.settings import LIVE_FOLDER
from optionforge.session import MarketSession

print("=" * 60)
print("OPTIONFORGE")
print("MARKET SESSION TEST")
print("=" * 60)

csv_file = LIVE_FOLDER / "sample_option_chain.csv"

df = MarketSession.run(csv_file)

print()
print(df.head())

print()
print("Rows    :", len(df))
print("Columns :", len(df.columns))

print()
print("MISSION COMPLETE")