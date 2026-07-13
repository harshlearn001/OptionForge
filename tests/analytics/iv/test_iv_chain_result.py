import pandas as pd

from optionforge.analytics.iv.iv_chain_result import (
    IVChainResult,
)


def sample():

    chain = pd.DataFrame(

        {

            "STRIKE_PRICE": [

                24900,

                25000,

                25100,

            ],

            "OPT_TYPE": [

                "CE",

                "CE",

                "PE",

            ],

            "IV": [

                0.19,

                0.20,

                0.21,

            ],

        }

    )

    return IVChainResult(

        symbol="NIFTY",

        trade_date=20260714,

        expiry=20260716,

        spot=25012.5,

        chain=chain,

    )


def test_fields():

    result = sample()

    assert result.symbol == "NIFTY"

    assert result.contracts == 3

    assert len(result) == 3

    assert not result.chain.empty


def test_repr():

    result = sample()

    assert "IVChainResult" in repr(result)