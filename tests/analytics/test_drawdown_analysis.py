"""
============================================================
OptionForge
DrawdownAnalysis Tests
============================================================
"""

import pytest

from optionforge.analytics.drawdown_analysis import (
    DrawdownAnalysis,
)
from optionforge.analytics.equity_curve import (
    EquityCurve,
)


def curve():

    return EquityCurve(

        values=(

            100000,

            105000,

            99000,

            110000,

        ),

    )


def analysis():

    return DrawdownAnalysis(

        equity_curve=curve(),

        max_drawdown=5.7,

        current_drawdown=0.0,

        peak_equity=110000,

        lowest_equity=99000,

        recovered=True,

    )


def test_create():

    assert isinstance(

        analysis(),

        DrawdownAnalysis,

    )


def test_max_drawdown():

    assert analysis().max_drawdown == 5.7


def test_current_drawdown():

    assert analysis().current_drawdown == 0.0


def test_peak():

    assert analysis().peak_equity == 110000


def test_lowest():

    assert analysis().lowest_equity == 99000


def test_recovered():

    assert analysis().is_recovered


def test_has_drawdown():

    assert analysis().has_drawdown


@pytest.mark.parametrize(

    "field,value",

    [

        ("max_drawdown", -1),

        ("max_drawdown", 101),

        ("current_drawdown", -1),

        ("current_drawdown", 101),

        ("peak_equity", -100),

        ("lowest_equity", -50),

    ],

)

def test_validation(field, value):

    kwargs = dict(

        equity_curve=curve(),

        max_drawdown=5.7,

        current_drawdown=0.0,

        peak_equity=110000,

        lowest_equity=99000,

        recovered=True,

    )

    kwargs[field] = value

    with pytest.raises(ValueError):

        DrawdownAnalysis(**kwargs)


def test_to_dict():

    data = analysis().to_dict()

    assert data["max_drawdown"] == 5.7

    assert data["peak_equity"] == 110000

    assert data["recovered"] is True


def test_str():

    assert "DrawdownAnalysis" in str(

        analysis(),

    )


def test_repr():

    assert "DrawdownAnalysis" in repr(

        analysis(),

    )