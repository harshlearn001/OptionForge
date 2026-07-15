import sys
from pathlib import Path
from datetime import date

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from optionforge.analytics import OptionChainAnalytics

print("=" * 60)
print("OPTIONFORGE")
print("OPTION CHAIN TEST")
print("=" * 60)

df = pd.DataFrame(
    [
        {
            "SYMBOL": "NIFTY",
            "TRADE_DATE": date(2026, 6, 27),
            "EXPIRY_DATE": date(2026, 7, 2),
            "STRIKE_PRICE": 25000,
            "OPTION_TYPE": "CE",
            "OPTION_CLOSE": 633.98,
            "SPOT_CLOSE": 24980.50,
            "RISK_FREE_RATE": 0.06,
            "TIME_TO_EXPIRY": 30 / 365,
        }
    ]
)

result = OptionChainAnalytics.calculate(df)

print(result)

print()
print("MISSION COMPLETE")
