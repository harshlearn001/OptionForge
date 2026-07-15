"""
============================================================
OptionForge
CONFIG TEST
============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.config.settings import *

print("=" * 60)
print("OPTIONFORGE")
print("CONFIG TEST")
print("=" * 60)

print("Project :", PROJECT_ROOT)
print("Data    :", DATA_FOLDER)
print("Output  :", OUTPUT_FOLDER)
print("Runtime :", RUNTIME_FOLDER)

print()
print("MISSION COMPLETE")
