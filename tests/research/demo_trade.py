"""
==============================================================
OptionForge
Trade Demo
==============================================================
"""

import sys
from pathlib import Path
from uuid import uuid4
from datetime import date

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.research.signal import Signal
from optionforge.research.trade import Trade


trade = Trade(
    trade_id=uuid4(),
    strategy_id="OF001",
    strategy_version="1.0.0",
    symbol="RELIANCE",
    signal=Signal.BUY,
    signal_date=date(2026, 7, 3),
    entry_date=date(2026, 7, 6),
    exit_date=date(2026, 7, 7),
    entry_price=1520.50,
    exit_price=1545.20,
    return_pct=1.62,
    holding_days=1,
)

print("=" * 70)
print("OPTIONFORGE")
print("TRADE DEMO")
print("=" * 70)

print(trade)

print("=" * 70)
print("MISSION COMPLETE")
print("=" * 70)