import pytest

from optionforge.analytics.pcr.pcr_result import (
    InstitutionalPCRResult,
)


def sample():

    return InstitutionalPCRResult(

        symbol="NIFTY",

        trade_date=20201228,

        expiry=20201231,

        spot=13682.50,

        atm_strike=13700,

        major_call_strike=13800,

        major_put_strike=13600,

        call_oi=43102875,

        put_oi=62679450,

        classic_pcr=1.4542,

        weighted_pcr=1.3987,

        institutional_bias="Bullish",

        confidence=87.5,

        contracts=191,

    )


def test_fields():

    result = sample()

    assert result.symbol == "NIFTY"

    assert result.atm_strike == 13700

    assert result.classic_pcr == 1.4542


def test_repr():

    result = sample()

    assert "InstitutionalPCRResult" in repr(result)


def test_frozen():

    result = sample()

    with pytest.raises(Exception):

        result.symbol = "BANKNIFTY"