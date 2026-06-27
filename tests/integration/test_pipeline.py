"""
OptionForge
tests/test_pipeline.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import pandas as pd

from optionforge.utils.loader import Loader
from optionforge.utils.validator import Validator


def main():

    print("=" * 60)
    print("OPTIONFORGE")
    print("MISSION 003 TEST")
    print("=" * 60)

    # ---------------------------------------------------
    # Create Sample Data
    # ---------------------------------------------------

    sample = pd.DataFrame({

        "TRADE_DATE": ["20260627"],
        "SYMBOL": ["NIFTY"],
        "EXPIRY_DATE": ["20260702"],
        "STRIKE_PRICE": [25000],

        "OPTION_TYPE": ["CE"],

        "SPOT_CLOSE": [24980.50],
        "FUTURE_CLOSE": [25005.20],
        "OPTION_CLOSE": [185.35],

        "OPEN_INTEREST": [254000],
        "CHANGE_IN_OI": [8200],
        "OPTION_VOLUME": [98000]

    })

    Path("sample.csv").write_text(sample.to_csv(index=False))

    # ---------------------------------------------------
    # Loader
    # ---------------------------------------------------

    loader = Loader()

    df = loader.load_option("sample.csv")

    print("\nLoader Success")
    print(df)

    # ---------------------------------------------------
    # Validator
    # ---------------------------------------------------

    Validator.validate(df)

    print("\nValidator Success")

    print("\nMISSION COMPLETE")


if __name__ == "__main__":
    main()