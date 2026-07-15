"""
============================================================
OptionForge
MARKET SESSION TEST
============================================================
"""

from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.session import MarketSession

print("=" * 60)
print("OPTIONFORGE")
print("MARKET SESSION TEST")
print("=" * 60)

session = MarketSession(
    marketforge_root=r"H:\MarketForge",
)

snapshot = session.run("NIFTY")

print()
print("Symbol :", snapshot.symbol)
print("Stage  :", snapshot.stage.name)
print("Option Rows :", snapshot.market_snapshot.option_rows)
print("Future Rows :", snapshot.market_snapshot.future_rows)
print("Spot Rows   :", snapshot.market_snapshot.spot_rows)

print()
print("MISSION COMPLETE")
