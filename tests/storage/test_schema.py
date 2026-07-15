"""
==============================================================
OptionForge
tests/storage/test_schema.py
--------------------------------------------------------------
Option Chain Schema Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.storage.schema import OptionChainSchema

print("=" * 60)
print("OPTIONFORGE")
print("SCHEMA VALIDATION TEST")
print("=" * 60)

# ---------------------------------------------------------
# Valid Schema
# ---------------------------------------------------------

columns = [
    "SYMBOL",
    "EXPIRY",
    "STRIKE",
    "OPTION_TYPE",
    "LTP",
    "IV",
    "OI",
    "CHANGE_IN_OI",
    "VOLUME",
    "SPOT",
]

valid, missing = OptionChainSchema.validate(columns)

print()

print("VALID SCHEMA")

print(f"Valid   : {valid}")

print(f"Missing : {missing}")

# ---------------------------------------------------------
# Invalid Schema
# ---------------------------------------------------------

bad_columns = [
    "SYMBOL",
    "STRIKE",
    "LTP",
]

valid, missing = OptionChainSchema.validate(bad_columns)

print()

print("INVALID SCHEMA")

print(f"Valid   : {valid}")

print(f"Missing : {missing}")

print()

print("MISSION COMPLETE")
