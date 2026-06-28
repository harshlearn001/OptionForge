"""
==============================================================
OptionForge
Professional Pipeline Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.pipeline import OptionForgePipeline

print("=" * 60)
print("OPTIONFORGE")
print("PIPELINE TEST")
print("=" * 60)

# ---------------------------------------------------------
# CSV Input
# ---------------------------------------------------------

csv_file = "data/sample_option_chain.csv"

df = OptionForgePipeline.run(csv_file)


print()

print(df.head())

print()

print("Rows :", len(df))

print("Columns :", len(df.columns))

print()

print("MISSION COMPLETE")