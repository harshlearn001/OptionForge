"""
==============================================================
OptionForge
Demo - Signal
==============================================================
"""
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.research.signal import Signal

print("=" * 60)
print("OPTIONFORGE")
print("SIGNAL DEMO")
print("=" * 60)

print()

print("BUY   :", Signal.BUY)
print("SELL  :", Signal.SELL)
print("WATCH :", Signal.WATCH)

print()
print("=" * 60)
print("MISSION COMPLETE")
print("=" * 60)