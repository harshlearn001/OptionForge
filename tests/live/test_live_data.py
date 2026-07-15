"""
============================================================
OptionForge
LIVE DATA TEST
============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.config.settings import LIVE_FOLDER
from optionforge.live import LiveData

print("=" * 60)
print("OPTIONFORGE")
print("LIVE DATA TEST")
print("=" * 60)

df = LiveData.load(LIVE_FOLDER / "sample_option_chain.csv")

print()
print(df.head())

print()
print("Rows    :", len(df))
print("Columns :", len(df.columns))

print()
print("MISSION COMPLETE")
