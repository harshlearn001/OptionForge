"""
============================================================
OptionForge
APPLICATION TEST
============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.app import OptionForgeApp

print("=" * 60)
print("OPTIONFORGE")
print("APPLICATION TEST")
print("=" * 60)

OptionForgeApp.run()

print()
print("MISSION COMPLETE")