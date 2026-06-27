import sys
from pathlib import Path
from datetime import date

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from optionforge.models import MarketSnapshot

print("=" * 60)
print("OPTIONFORGE")
print("MARKET SNAPSHOT INTELLIGENCE TEST")
print("=" * 60)

df = pd.DataFrame([

    {
        "STRIKE_PRICE":24000,
        "EXPIRY_DATE":date(2026,6,30),
        "OPTION_TYPE":"CE",
        "OPEN_INTEREST":120000,
        "OPTION_VOLUME":50000,
    },

    {
        "STRIKE_PRICE":24000,
        "EXPIRY_DATE":date(2026,6,30),
        "OPTION_TYPE":"PE",
        "OPEN_INTEREST":150000,
        "OPTION_VOLUME":70000,
    },

    {
        "STRIKE_PRICE":24100,
        "EXPIRY_DATE":date(2026,7,7),
        "OPTION_TYPE":"CE",
        "OPEN_INTEREST":90000,
        "OPTION_VOLUME":35000,
    }

])

snapshot = MarketSnapshot(

    symbol="NIFTY",

    trade_date=date(2026,6,27),

    spot_price=24056,

    future_price=24102,

    option_chain=df,

)

print()

print(snapshot.summary())

print()

print("Nearest Expiry :", snapshot.nearest_expiry())

print("ATM :", snapshot.atm())

print("PCR :", round(snapshot.pcr(),3))

print("Max Call OI :", snapshot.max_call_oi())

print("Max Put OI :", snapshot.max_put_oi())

print()

print("MISSION COMPLETE")