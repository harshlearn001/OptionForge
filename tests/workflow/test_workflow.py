"""
============================================================
OptionForge
WORKFLOW ENGINE TEST
============================================================
"""

from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.workflow import WorkflowEngine

print("=" * 60)
print("OPTIONFORGE")
print("WORKFLOW TEST")
print("=" * 60)

workflow = WorkflowEngine(
    marketforge_root=r"H:\MarketForge",
)

snapshot = workflow.run("NIFTY")

print()
print("Symbol :", snapshot.symbol)
print("Stage  :", snapshot.stage.name)
print("Option Rows :", snapshot.market_snapshot.option_rows)
print("Future Rows :", snapshot.market_snapshot.future_rows)
print("Spot Rows   :", snapshot.market_snapshot.spot_rows)

print()
print("MISSION COMPLETE")