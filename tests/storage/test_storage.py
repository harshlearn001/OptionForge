import sys
from pathlib import Path
from datetime import date

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from optionforge.storage import StorageWriter
from optionforge.storage import StorageReader

print("=" * 60)
print("OPTIONFORGE")
print("STORAGE TEST")
print("=" * 60)

df = pd.DataFrame([
    {
        "SYMBOL":"NIFTY",
        "TRADE_DATE":date(2026,6,27),
        "EXPIRY_DATE":date(2026,7,2),

        "STRIKE_PRICE":25000,
        "OPTION_TYPE":"CE",

        "OPTION_CLOSE":633.98,
        "SPOT_CLOSE":24980.5,

        "OPEN_INTEREST":254000,
        "CHANGE_IN_OI":8200,
        "OPTION_VOLUME":98000,

        "IV":0.20,
        "DELTA":0.54,
        "GAMMA":0.00027,
        "THETA":-4236.48,
        "VEGA":2840.59,

        "INTRINSIC_VALUE":0,
        "TIME_VALUE":633.98,
    }
])

path = StorageWriter.save_daily_chain(
    dataframe=df,
    folder="output/history",
    filename="nifty_20260627.parquet",
)

print("Saved :", path)

loaded = StorageReader.load(path)

print()
print(loaded)

print()
print("MISSION COMPLETE")