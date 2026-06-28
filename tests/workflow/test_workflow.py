"""
============================================================
OptionForge
WORKFLOW ENGINE TEST
============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.workflow import WorkflowEngine

print("=" * 60)
print("OPTIONFORGE")
print("WORKFLOW TEST")
print("=" * 60)

csv_file = "data/sample_option_chain.csv"

df = WorkflowEngine.run(csv_file)

print()
print(df.head())

print()
print("Rows    :", len(df))
print("Columns :", len(df.columns))

print()
print("MISSION COMPLETE")