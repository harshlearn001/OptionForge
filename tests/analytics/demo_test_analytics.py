import sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from optionforge.analytics import OptionAnalytics
from optionforge.models import OptionContract
from optionforge.quant.black_scholes import BlackScholes

print("=" * 60)
print("OPTIONFORGE")
print("ANALYTICS TEST")
print("=" * 60)

spot = 25000
strike = 25000
time = 30 / 365
rate = 0.06
volatility = 0.20

market_price = BlackScholes.call_price(
    spot,
    strike,
    time,
    rate,
    volatility,
)

contract = OptionContract(
    symbol="NIFTY",
    trade_date=date(2026, 6, 27),
    expiry_date=date(2026, 7, 2),
    strike=strike,
    option_type="CE",
    market_price=market_price,
    spot_price=spot,
    risk_free_rate=rate,
    time_to_expiry=time,
)

result = OptionAnalytics.calculate(contract)

print()
print(result)
print()
print("MISSION COMPLETE")
