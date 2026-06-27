import sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from optionforge.models import OptionContract

print("=" * 60)
print("OPTIONFORGE")
print("OPTION CONTRACT TEST")
print("=" * 60)

contract = OptionContract(
    symbol="NIFTY",
    trade_date=date(2026, 6, 27),
    expiry_date=date(2026, 7, 2),
    strike=25000,
    option_type="CE",
    market_price=633.98,
    spot_price=24980.50,
    risk_free_rate=0.06,
    time_to_expiry=30 / 365,
)

print()
print(contract)
print()
print("MISSION COMPLETE")