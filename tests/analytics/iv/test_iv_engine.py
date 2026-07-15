import pandas as pd

from optionforge.analytics.iv.iv_engine import (
    IVEngine,
)


def sample_chain():

    return pd.DataFrame(
        {
            "STRIKE_PRICE": [
                25000,
                25100,
            ],
            "OPT_TYPE": [
                "CE",
                "PE",
            ],
            "CLOSE_PRICE": [
                633.98,
                565.00,
            ],
        }
    )


def test_engine():

    engine = IVEngine()

    result = engine.calculate(
        symbol="NIFTY",
        trade_date=20260714,
        expiry=20260716,
        spot=25000,
        option_chain=sample_chain(),
        time=30 / 365,
        rate=0.06,
    )

    assert result.symbol == "NIFTY"

    assert result.contracts == 2

    assert "IV" in result.chain.columns

    assert "DELTA" in result.chain.columns

    assert "GAMMA" in result.chain.columns


def test_repr():

    engine = IVEngine()

    assert "IVEngine" in repr(engine)
